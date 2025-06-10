# Converting chroma-subsampled images

**Framework**: Accelerate

Create vImage buffers with the correct dimensions to convert to and from images with subsampled chroma information.

#### Overview

When you work with video data, you often work with images represented by separate luminance (Y) and chrominance (CbCr) information at different resolutions. The vImage library provides functionality to convert images in this format to an interleaved RGB format, which simplifies applying some image-processing operations.

Alternatively, other image transformations, such as adjusting saturation, require that you convert an RGB image to YCbCr. Reducing the resolution of the chrominance information can also improve the performance of your app because you’re only processing half or a quarter of the number of pixels.

 describes the encoding that compresses image data by reducing the resolution of the chrominance information. Chroma subsampling relies on the fact that human vision is less sensitive to color than luminance.

The code in this article uses the 4:2:0 subsampling scheme, which means there’s one Cb and one Cr pixel for every four luminance pixels. That is, each chrominance channel is half of the width and half of the height of the luminance channel. For example, 4:2:0 subsampling represents a 4 x 2 image with a 4 x 2 luminance channel and two 2 x 1 chrominance channels:

![A diagram showing source RGB pixels converted to discrete luminance and chrominance pixels arranged as two-times-two tiles.](https://docs-assets.developer.apple.com/published/fc95d53c190aa0f91c8411fcd7bbf01a/media-4264983%402x.png)

The images below show the 4:2:0 subsampling scheme applied to a photograph. The  luminance channel has the same resolution as the original image. However, the  and  chrominance channels have a lower resolution. For each 2 x 2 square of pixels in the luminance channel, the chrominance channels only contain a single pixel. Therefore, the chrominance channels are a quarter of the size of the luminance channel.

![A diagram that shows the sizes and content of the two chrominance channels and single luminance channel of a YpCbCr image compared to an RGB image of the same subject. On the left are the three YpCbCr channels and on the right in the single, interleaved RGB image.](https://docs-assets.developer.apple.com/published/696306b4d1602091ebaca151924bab5d/media-3866875%402x.png)

##### Define the Core Video and Core Graphics Image Formats

If you’re working with [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/cvpixelbuffer-q2e) objects, the vImage library provides the [`vImageCVImageFormat_CreateWithCVPixelBuffer(_:)`](vimagecvimageformat_createwithcvpixelbuffer(_:).md) and [`make(buffer:)`](vimagecvimageformat/make(buffer:).md) functions that generate a [`vImageCVImageFormat`](vimagecvimageformat.md) structure from a Core Video pixel buffer. However, the code in this article defines a [`vImageCVImageFormat.Format.format420YpCbCr8PlanarFullRange`](vimagecvimageformat/format/format420ypcbcr8planarfullrange.md) Core Video image format that describes the YpCbCr image. The code below also defines an 8-bit-per-channel RGB Core Graphics image format:

```swift
var cgImageFormat = vImage_CGImageFormat(
    bitsPerComponent: 8,
    bitsPerPixel: 8 * 3,
    colorSpace: CGColorSpaceCreateDeviceRGB(),
    bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.none.rawValue))!

let cvImageFormat = vImageCVImageFormat.make(
    format: .format420YpCbCr8PlanarFullRange,
    matrix: kvImage_ARGBToYpCbCrMatrix_ITU_R_601_4.pointee,
    chromaSiting: .center,
    colorSpace: CGColorSpaceCreateDeviceRGB(),
    alphaIsOpaqueHint: true)!
```

##### Perform the Core Graphics to Core Video Conversion

Use the Core Video and Core Graphics image format descriptions to create an any-to-any [`vImageConverter`](vimageconverter.md) instance that converts from Core Graphics to Core Video image format.

```swift
let cgToCvConverter = try vImageConverter.make(sourceFormat: cgImageFormat,
                                               destinationFormat: cvImageFormat)
```

The converter provides the [`destinationBufferCount`](vimageconverter/destinationbuffercount.md) property that you use to generate the correct number of destination buffers. Although the chrominance size is a quarter of the luminance sizes, declare the sizes of all three pixel buffers as the source image size.

```swift
let ypCbCr8PlanarBuffers = (0 ..< cgToCvConverter.destinationBufferCount).map { _ in
    vImage.PixelBuffer<vImage.Planar8>(size: rgbSourceBuffer.size)
}
```

> ❗ **Important**:  The source and destination vlmage buffers that you pass to an any-to-any conversion must all share the same dimensions.

In the code below, `rgbSourceBuffer` is a [`vImage.PixelBuffer`](vimage/pixelbuffer.md) with a format of [`vImage.Interleaved8x3`](vimage/interleaved8x3.md) (that matches the [`vImage_CGImageFormat`](vimage_cgimageformat.md) structure above) which contains a source image. Call the [`convert(from:to:)`](vimageconverter/convert(from:to:)-587gc.md) method to populate the destination buffers.

```swift
try cgToCvConverter.convert(from: [rgbSourceBuffer],
                            to: ypCbCr8PlanarBuffers)
```

On return, the three pixel buffers in the `ypCbCr8PlanarBuffers` array contain the luminance and two chrominance channels. The image below shows the luminance channel (left), the Cb channel (middle), and the Cr channel (right):

![Three grayscale images of the different planes of the YpCrCb representation of a photograph of a flower. The first image contains the luminance information. The second and third images contain the chrominance information and are scaled that the only fill the top-left quarter of the image.](https://docs-assets.developer.apple.com/published/05210844d773d099f3ddea68afb37de1/media-4264989%402x.png)

##### Apply an Operation to the Subsampled Chrominance Channels

Although the two chrominance channels are the same size as the full-sized luminance channel, they only contain a quarter of the data. If you’re applying an image-processing operation to the Cb and Cr channels, use the [`withUnsafeRegionOfInterest(_:_:)`](vimage/pixelbuffer/withunsaferegionofinterest(_:_:).md) method. This ensures that you’re not processing unused pixels. The code below reduces the saturation of the image using the technique discussed in [`Adjusting saturation and applying tone mapping`](adjusting-saturation-and-applying-tone-mapping.md):

```swift
let saturation = Float(0.25)
let preBias = -128
let divisor = 0x1000
let postBias = 128 * divisor
let factor = Int(saturation * Float(divisor))

// Define a region of interest that's a quarter of the area of the
// luminance channel.
let roi = CGRect(x: 0, y: 0,
                 width: ypCbCr8PlanarBuffers[0].width / 2,
                 height: ypCbCr8PlanarBuffers[0].height / 2)

// Indices 1 and 2 refer to the Cb and Cr buffers, respectively.
for index in [1, 2] {
    ypCbCr8PlanarBuffers[index].withUnsafeRegionOfInterest(roi) { buffer in
        buffer.multiply(by: factor,
                        divisor: divisor,
                        preBias: preBias,
                        postBias: postBias,
                        destination: buffer)
    }
}
```

For more information about limiting the effect of vImage operations to rectangular regions of interest, see [`Applying vImage operations to regions of interest`](applying-vimage-operations-to-regions-of-interest.md).

##### Perform the Core Video to Core Graphics Conversion

To convert the YpCbCr buffers to an RGB buffer, create a converter with the Core Video image format as the source and the Core Graphics image format as the destination. Call the [`convert(from:to:)`](vimageconverter/convert(from:to:)-587gc.md) method as above, but specify the `ypCbCr8PlanarBuffers` array as the source and an 8-bit-per-channel interleaved buffer as the destination.

```swift
let cvToCgConverter = try vImageConverter.make(sourceFormat: cvImageFormat,
                                               destinationFormat: cgImageFormat)

let rgbDestinationBuffer = vImage.PixelBuffer<vImage.Interleaved8x3>(
    size: ypCbCr8PlanarBuffers.first!.size)

try cvToCgConverter.convert(from: ypCbCr8PlanarBuffers,
                            to: [rgbDestinationBuffer])
```

On return, `rgbDestinationBuffer` contains the desaturated version (right) of the original image (left).

![A side-by-side comparison of the original photograph of a flower and the desaturated version of the same photograph.](https://docs-assets.developer.apple.com/published/1df1b26d502a07d2261f0ac6c69daf84/media-4264990%402x.png)

## See Also

- [Building a basic image conversion workflow](building-a-basic-image-conversion-workflow.md)
  Learn the fundamentals of the convert-any-to-any function by converting a CMYK image to an RGB image.
- [Functions that perform any-to-any conversion](functions-that-perform-any-to-any-conversion.md)
  Convert between Core Video or Core Graphics image data of arbitrary color spaces and bit depths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/converting-chroma-subsampled-images)*