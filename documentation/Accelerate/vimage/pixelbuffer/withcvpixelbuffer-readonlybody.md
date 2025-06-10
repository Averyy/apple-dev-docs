# withCVPixelBuffer(readOnly:body:)

**Framework**: Accelerate  
**Kind**: method

Calls the given closure with a locked 32-bit BGRA Core Video Pixel Buffer.

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
func withCVPixelBuffer(readOnly: Bool, body: (CVPixelBuffer) -> Void)
```

#### Discussion

Use this function to pass a vImage pixel buffer to other frameworks. For example, the following code creates a Core Image [`CIImage`](https://developer.apple.com/documentation/CoreImage/CIImage) instance from a [`CVPixelBuffer`](https://developer.apple.com/documentation/CoreVideo/CVPixelBuffer) that shares its underlying storage with a pixel buffer:

```swift
let src = vImage.PixelBuffer<vImage.Interleaved8x4>(
    size: vImage.Size(width: 64, height: 64))

src.withCVPixelBuffer(readOnly: false) { cvPixelBuffer in

    let ciImage = CIImage(cvImageBuffer: cvPixelBuffer)

    // Core Image workflow using `ciImage`
}
```

## Parameters

- `readOnly`: A Boolean value that specifies whether the function locks the   with the   flag. If the closure doesn’t modify the data, set this parameter to  .
- `body`: A closure with a   parameter that points to the underlying pixel buffer image data.

## See Also

- [func copy(to: vImage.PixelBuffer<Format>)](vimage/pixelbuffer/copy(to:).md)
  Copies the contents of the pixel buffer to another pixel buffer.
- [func copy(to: CVPixelBuffer, cvImageFormat: vImageCVImageFormat, cgImageFormat: vImage_CGImageFormat) throws](vimage/pixelbuffer/copy(to:cvimageformat:cgimageformat:).md)
  Copies the contents of a pixel buffer to a Core Video pixel buffer.
- [func makeCGImage(cgImageFormat: vImage_CGImageFormat) -> CGImage?](vimage/pixelbuffer/makecgimage(cgimageformat:).md)
  Returns a Core Graphics image from the pixel buffer’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/withcvpixelbuffer(readonly:body:))*