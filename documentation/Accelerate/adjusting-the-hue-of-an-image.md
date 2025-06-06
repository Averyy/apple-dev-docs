# Adjusting the hue of an image

**Framework**: Accelerate

Convert an image to L*a*b* color space and apply hue adjustment.

**Availability**:
- macOS 13.0+
- Xcode 14.0+

#### Overview

This sample code project allows you to adjust the hue of an image by treating the chrominance information as 2D coordinates, and transforming those values with a rotation matrix. You can convert an RGB image — with its pixels represented as red, green, and blue values — to L*a*b*, where luminance and chrominance are stored discretely. The  in L*a*b* refers to the lightness, and the  and  refer to the red-green and blue-yellow values, respectively.

The image below shows an approximation of an L*a*b* color chart. The  value transitions horizontally (left to right) from negative, through zero, to positive, and the  value transitions vertically (bottom to top) from negative, through zero, to positive. Because this sample code focuses on color rather than lightness, the image doesn’t consider L*.

![A graphic containing vertical and horizontal gradients. The gradient colors transition from green on the left to red on the right, and from yellow at the top to blue at the bottom.](https://docs-assets.developer.apple.com/published/8b5229283b3e0e9790f3ad28ee2bb7e2/lab-color-chart_2x.png)

The sample uses the vImage Any-to-Any converter to convert the source image’s color space to L*a*b*. The code converts the interleaved L*a*b* image data to multiple-plane image data that it passes to a matrix multiply operation to apply the hue adjustment.

The following image shows four photographs, from left to right, with a hue adjustment of -90º, 0º (an unchanged hue), 90º, and 180º:

![Four photographs of a flower with different hue adjustments.](https://docs-assets.developer.apple.com/published/b3598292b9795848665392d30103feb1/hueAdjust_2x.png)

##### Create the Lab Image Format

To create the image format for the L*a*b* color space, the sample app uses the [`genericLab`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace/genericLab) system-defined [`CGColorSpace`](https://developer.apple.com/documentation/CoreGraphics/CGColorSpace).

```swift
var labImageFormat = vImage_CGImageFormat(
    bitsPerComponent: 8,
    bitsPerPixel: 8 * 3,
    colorSpace: CGColorSpace(name: CGColorSpace.genericLab)!,
    bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.none.rawValue),
    renderingIntent: .defaultIntent)!
```

On return, `labImageFormat` describes the interleaved L*a*b* pixels over which this sample works. The first channel in each pixel is the lightness, and the second and third channels are the  and , respectively.

##### Generate the Pixel Buffer and Image Format From the Source Image

The converter that the sample uses to convert the source pixels to L*a*b* color space requires two [`vImage_CGImageFormat`](vimage_cgimageformat.md) structures that describe the source and destination images. The sample uses the [`makeDynamicPixelBufferAndCGImageFormat(cgImage:)`](vimage/pixelbuffer/makedynamicpixelbufferandcgimageformat(cgimage:).md) method to create a dynamic pixel buffer and image format structure from the source Core Graphics image.

```swift
let source = try vImage.PixelBuffer
    .makeDynamicPixelBufferAndCGImageFormat(cgImage: sourceCGImage)
```

On return, `source.cgImageFormat` contains the image format of the source image, and `source.pixelBuffer` is a pixel buffer that contains the source image data.

##### Create the Source Image Color Space to Lab Converter

The sample app uses the source and L*a*b* image formats to create a [`vImageConverter`](vimageconverter.md) instance to convert between the two color spaces.

```swift
let rgbToLab = try vImageConverter.make(sourceFormat: source.cgImageFormat,
                                        destinationFormat: labImageFormat)
```

For more information about vImage’s convert-any-to-any functionality, see [`Building a basic image conversion workflow`](building-a-basic-image-conversion-workflow.md).

##### Convert the Source Image to Lab

The sample creates a pixel buffer that’s the same size as the source image.

```swift
labInterleavedSource = vImage.PixelBuffer<vImage.Interleaved8x3>(size: size)
```

The converter’s [`convert(from:to:)`](vimageconverter/convert(from:to:)-9s7p7.md) function performs the conversion.

```swift
try rgbToLab.convert(from: source.pixelBuffer,
                     to: labInterleavedSource)
```

On return, the `labInterleavedSource` contains the L*a*b* representation of the source image.

##### Convert the Interleaved Lab Buffer to Planar Buffers

The function the sample app uses to apply the hue adjustment, [`multiply(by:divisor:preBias:postBias:destination:)`](vimage/pixelbuffer/multiply(by:divisor:prebias:postbias:destination:)-7jo6v.md), operates on a multiple-plane pixel buffer. To convert the interleaved L*a*b* buffer to planar buffers, the app creates a [`vImage.Planar8x3`](vimage/planar8x3.md) pixel buffer.

```swift
labPlanarDestination = vImage.PixelBuffer<vImage.Planar8x3>(size: size)
```

It then calls [`deinterleave(destination:)`](vimage/pixelbuffer/deinterleave(destination:)-hrhz.md) to populate the planar buffers with the contents of the interleaved buffer.

```swift
labInterleavedSource.deinterleave(destination: labPlanarDestination)
```

For more information about working with planar buffers, see [`Optimizing image-processing performance`](optimizing-image-processing-performance.md).

##### Apply the Hue Adjustment

The app adjusts the hue of an image by rotating a two-element vector, described by  and . For more information about working with rotation matrices, see [`Working with Matrices`](working-with-matrices.md).

The following visualizes a sample color (marked ) rotated by -90º (marked ) and 45º (marked ):

![A graphic showing a color rotated by minus 90 degrees and by 45 degrees. The background contains vertical and horizontal gradients. The colors transition from green on the left to red on the right, and from yellow at the top to blue at the bottom. The original color is light yellow. The color that is rotated minus 90 degrees is light green, and the color that is rotated 45 degrees is light red. ](https://docs-assets.developer.apple.com/published/057803bef57b84075891b0e92e7f3688/ColorRotate_2x.png)

The following code generates the rotation matrix based on `hueAngle`:

```swift
let divisor: Int = 0x1000

let rotationMatrix = [
    1, 0,             0,
    0, cos(hueAngle), -sin(hueAngle),
    0, sin(hueAngle),  cos(hueAngle)
].map {
    return Int($0 * Float(divisor))
}
```

The `preBias` and `postBias` values effectively shift the  and  values from `0...255` to `-128...127`, so the rotation is centered where  and  are zero.

```swift
let preBias = [Int](repeating: -128, count: 3)
let postBias = [Int](repeating: 128 * divisor, count: 3)
```

The [`multiply(by:divisor:preBias:postBias:destination:)`](vimage/pixelbuffer/multiply(by:divisor:prebias:postbias:destination:)-7jo6v.md) function multiplies each pixel in the source buffer by the matrix and writes the result to the destination buffers. The code performs the matrix multiplication in-place, so the source and destination point to the same buffers.

The following code performs the matrix multiply operation:

```swift
labPlanarDestination.multiply(
    by: rotationMatrix,
    divisor: divisor,
    preBias: preBias,
    postBias: postBias,
    destination: labPlanarDestination)
```

On return, `labPlanarDestination` contains the hue-adjusted  and  channels.

##### Display the Image

Finally, the sample code converts the hue-adjusted planar buffer back to an interleaved buffer.

```swift
labPlanarDestination.interleave(destination: labInterleavedDestination)
```

The SwiftUI [`Image`](https://developer.apple.com/documentation/SwiftUI/Image) view supports the L*a*b* color space. The following code creates a Core Graphics image from the interleaved pixel buffer and passes it to the published `outputImage` property that the app displays on the screen:

```swift
if let result = labInterleavedDestination
    .makeCGImage(cgImageFormat: labImageFormat) {
    
    DispatchQueue.main.async {
        self.outputImage = result
    }
}
```

## See Also

- [Adjusting the brightness and contrast of an image](adjusting-the-brightness-and-contrast-of-an-image.md)
  Use a gamma function to apply a linear or exponential curve.
- [Adjusting saturation and applying tone mapping](adjusting-saturation-and-applying-tone-mapping.md)
  Convert an RGB image to discrete luminance and chrominance channels, and apply color and contrast treatments.
- [Applying tone curve adjustments to images](applying-tone-curve-adjustments-to-images.md)
  Use the vImage library’s polynomial transform to apply tone curve adjustments to images.
- [Specifying histograms with vImage](specifying-histograms-with-vimage.md)
  Calculate the histogram of one image, and apply it to a second image.
- [Enhancing image contrast with histogram manipulation](enhancing-image-contrast-with-histogram-manipulation.md)
  Enhance and adjust the contrast of an image with histogram equalization and contrast stretching.
- [Histogram](histogram.md)
  Calculate or manipulate an image’s histogram.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/adjusting-the-hue-of-an-image)*