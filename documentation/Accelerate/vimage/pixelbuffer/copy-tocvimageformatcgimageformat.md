# copy(to:cvImageFormat:cgImageFormat:)

**Framework**: Accelerate  
**Kind**: method

Copies the contents of a pixel buffer to a Core Video pixel buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func copy(to cvPixelBuffer: CVPixelBuffer, cvImageFormat: vImageCVImageFormat, cgImageFormat: vImage_CGImageFormat) throws
```

#### Discussion

The destination Core Video pixel buffer must be nonplanar and be the same size as the source buffer.

The following code shows how to incorporate a vImage pixel buffer into a [`CIImageProcessorKernel`](https://developer.apple.com/documentation/CoreImage/CIImageProcessorKernel) instance. The code calls [`copy(to:cvImageFormat:cgImageFormat:)`](vimage/pixelbuffer/copy(to:cvimageformat:cgimageformat:).md) to write the result of a contast stretch operation to the processor kernel’s output.

```swift
class ContrastStretchImageProcessorKernel: CIImageProcessorKernel {
    
    static var cgImageFormat = vImage_CGImageFormat(
        bitsPerComponent: 8,
        bitsPerPixel: 32,
        colorSpace: CGColorSpaceCreateDeviceRGB(),
        bitmapInfo: CGBitmapInfo(rawValue: CGImageAlphaInfo.noneSkipLast.rawValue),
        renderingIntent: .defaultIntent)!
    
    static let cvImageFormat = vImageCVImageFormat.make(
        format: .format32BGRA,
        colorSpace: CGColorSpaceCreateDeviceRGB(),
        alphaIsOpaqueHint: true)!

    override class var outputFormat: CIFormat {
        return CIFormat.BGRA8
    }
    
    override class func formatForInput(at input: Int32) -> CIFormat {
        return CIFormat.BGRA8
    }
    
    override class func process(with inputs: [CIImageProcessorInput]?,
                                arguments: [String: Any]?,
                                output: CIImageProcessorOutput) throws {
        
        guard
            let input = inputs?.first,
            let inputPixelBuffer = input.pixelBuffer,
            let outputPixelBuffer = output.pixelBuffer else {
                return
            }
   
        let buffer = try vImage.PixelBuffer(copying: inputPixelBuffer,
                                            cvImageFormat: cvImageFormat,
                                            cgImageFormat: &cgImageFormat,
                                            pixelFormat: vImage.Interleaved8x4.self)
        
        buffer.contrastStretch(destination: buffer)
        
        try buffer.copy(to: outputPixelBuffer,
                        cvImageFormat: cvImageFormat,
                        cgImageFormat: cgImageFormat)
    }
}
```

## Parameters

- `cvPixelBuffer`: The destination Core Video pixel buffer.
- `cvImageFormat`: A   that specifies the pixel format of the destination buffer.
- `cgImageFormat`: The Core Graphics format of the source buffer.

## See Also

- [func copy(to: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/copy(to:).md)
  Copies the contents of the pixel buffer to another pixel buffer.
- [func makeCGImage(cgImageFormat: vImage_CGImageFormat) -> CGImage?](vimage/pixelbuffer/makecgimage(cgimageformat:).md)
  Returns a Core Graphics image from the pixel buffer’s contents.
- [func withCVPixelBuffer(readOnly: Bool, body: (CVPixelBuffer) -> Void)](vimage/pixelbuffer/withcvpixelbuffer(readonly:body:).md)
  Calls the given closure with a locked 32-bit BGRA Core Video Pixel Buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/copy(to:cvimageformat:cgimageformat:))*