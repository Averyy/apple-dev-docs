# Applying vImage operations to video sample buffers

**Framework**: Accelerate

Use the vImage convert-any-to-any functionality to perform real-time image processing of video frames streamed from your device’s camera.

**Availability**:
- macOS 13.3+
- Xcode 14.3+

#### Overview

The vImage library provides the high-level convert-any-to-any [`vImageConverter`](vimageconverter.md) class to convert image data between Core Video and Core Graphics formats. The convert-any-to-any functionality is suited for apps that work across different platforms where [`AVFoundation`](https://developer.apple.comhttps://developer.apple.com/av-foundation/) may provide video frames in different formats.

This sample code app uses [`AVFoundation`](https://developer.apple.comhttps://developer.apple.com/av-foundation/) to access the Mac camera and vImage to convert the camera image to an RGB image that the app displays onscreen.

##### Specify the Pixel Format

To ensure that AVCapture doesn’t have to perform a conversion from the capture format to the output format, the sample code specifies the output format as the camera’s active format. After declaring `videoOutput` as an [`AVCaptureVideoDataOutput`](https://developer.apple.com/documentation/AVFoundation/AVCaptureVideoDataOutput) instance, the following code defines the output pixel format by creating the [`videoSettings`](https://developer.apple.com/documentation/AVFoundation/AVCaptureVideoDataOutput/videoSettings) dictionary:

```swift
pixelFormat = CMFormatDescriptionGetMediaSubType(camera.activeFormat.formatDescription)
videoOutput.videoSettings = [kCVPixelBufferPixelFormatTypeKey as String: pixelFormat]
```

##### Lock the Core Video Pixel Buffer

When the app starts the flow of data through the capture pipeline, [`AVFoundation`](https://developer.apple.comhttps://developer.apple.com/av-foundation/) calls [`captureOutput(_:didOutput:from:)`](https://developer.apple.com/documentation/AVFoundation/AVCaptureVideoDataOutputSampleBufferDelegate/captureOutput(_:didOutput:from:)) for each new video frame. The following code locks the [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/CVPixelBuffer) structure’s underlying memory to make it available exclusively to the vImage conversion function:

```swift
CVPixelBufferLockBaseAddress(
    pixelBuffer,
    CVPixelBufferLockFlags.readOnly)

do {
    try convertVideoFormatToRGB(cvPixelBuffer: pixelBuffer)
} catch {
    fatalError("Unable to perform conversion.")
}

CVPixelBufferUnlockBaseAddress(
    pixelBuffer,
    CVPixelBufferLockFlags.readOnly)
```

##### Create a Core Video to Core Graphics Converter

The vImage convert-any-to-any function requires a converter that describes the source and destination formats. The sample code app converts a Core Video pixel buffer to a Core Graphics image. The code calls the [`make(buffer:)`](vimagecvimageformat/make(buffer:).md) function to derive the source Core Video image format from the [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/CVPixelBuffer). In some cases, the [`vImageCVImageFormat`](vimagecvimageformat.md) instance that the make function returns may have incomplete information. The following code ensures that the format has a color space and chrominance siting information:

```swift
guard let cvImageFormat = vImageCVImageFormat.make(buffer: cvPixelBuffer) else {
    fatalError("Unable to derive Core Video pixel format from buffer.")
}

if cvImageFormat.colorSpace == nil {
    cvImageFormat.colorSpace = CGColorSpaceCreateDeviceRGB()
}

if cvImageFormat.chromaSiting == nil {
    cvImageFormat.chromaSiting = .center
}
```

The sample app specifies a three-channel, 8-bit-per-channel [`vImage_CGImageFormat`](vimage_cgimageformat.md) as the conversion destination format.

```swift
let cgImageFormat = vImage_CGImageFormat(
    bitsPerComponent: 8,
    bitsPerPixel: 8 * 3,
    colorSpace: CGColorSpaceCreateDeviceRGB(),
    bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.none.rawValue))!
```

The [`make(sourceFormat:destinationFormat:flags:)`](vimageconverter/make(sourceformat:destinationformat:flags:)-8iupf.md) type method creates a [`vImageConverter`](vimageconverter.md) instance from the source and destination formats.

```swift
converter = try? vImageConverter.make(sourceFormat: cvImageFormat,
                                      destinationFormat: cgImageFormat)

if converter == nil {
    fatalError("Unable to create Core Video to Core Graphics converter.")
}
```

##### Initialize the Destination Buffer

The destination pixel buffer contains the RGB image after conversion. The code defines it as a three-channel, 8-bit-per-channel [`vImage.PixelBuffer`](vimage/pixelbuffer.md) structure.

```swift
var destinationBuffer: vImage.PixelBuffer<vImage.Interleaved8x3>!
```

The first time that the app calls the conversion function, it runs the following code to initialize the destination pixel buffer with the same dimensions as the Core Video pixel buffer:

```swift
let size = vImage.Size(cvPixelBuffer: cvPixelBuffer)
destinationBuffer = vImage.PixelBuffer<vImage.Interleaved8x3>(size: size)
```

##### Initialize the Source Buffers

Although the sample code app knows that the Core Graphics image format requires only a single buffer at compile time, the camera’s active format defines the number of source buffers and their pixel formats at runtime. Therefore, the code defines the source buffers as an array of [`vImage.DynamicPixelFormat`](vimage/dynamicpixelformat.md) pixel buffers.

```swift
var sourceBuffers: [vImage.PixelBuffer<vImage.DynamicPixelFormat>]!
```

The [`vImageConverter`](vimageconverter.md) provides the [`makeCVToCGPixelBuffers(referencing:)`](vimageconverter/makecvtocgpixelbuffers(referencing:).md) function that returns an array of pixel buffers. These pixel buffers reference the underlying memory of each plane of the Core Video pixel buffer.

```swift
sourceBuffers = try converter.makeCVToCGPixelBuffers(referencing: cvPixelBuffer)
```

##### Convert the Core Video Buffer Contents to a Core Graphics Format Image

The [`convert(from:to:)`](vimageconverter/convert(from:to:)-9s7p7.md) function accepts the source and destination pixel buffers and converts the Core Video pixel buffer’s contents to a Core Graphics image.

```swift
try converter.convert(from: sourceBuffers, to: [destinationBuffer])
```

##### Create an Output Core Graphics Image

Finally, the code calls [`makeCGImage(cgImageFormat:)`](vimage/pixelbuffer/makecgimage(cgimageformat:).md) to create a Core Graphics image that it displays in the user interface.

```swift
let rgbImage = destinationBuffer.makeCGImage(cgImageFormat: cgImageFormat)!
```

## See Also

- [Using vImage pixel buffers to generate video effects](using-vimage-pixel-buffers-to-generate-video-effects.md)
  Render real-time video effects with the vImage Pixel Buffer.
- [Integrating vImage pixel buffers into a Core Image workflow](integrating-vimage-pixel-buffers-into-a-core-image-workflow.md)
  Share image data between Core Video pixel buffers and vImage buffers to integrate vImage operations into a Core Image workflow.
- [Improving the quality of quantized images with dithering](improving-the-quality-of-quantized-images-with-dithering.md)
  Apply dithering to simulate colors that are unavailable in reduced bit depths.
- [Core Video interoperability](core-video-interoperability.md)
  Pass image data between Core Video and vImage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/applying-vimage-operations-to-video-sample-buffers)*