# withCVPixelBuffer(readOnly:body:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Calls the given closure with a locked 32-bit BGRA Core Video Pixel Buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
func withCVPixelBuffer(readOnly: Bool, body: (CVPixelBuffer) -> Void)
```

Available when `Format` is `vImage.Interleaved8x4`.

#### Discussion

Use this function to pass a vImage pixel buffer to other frameworks. For example, the following code creates a Core Image [`CIImage`](../../../CoreImage/ciimage.md) instance from a [`CVPixelBuffer`](../../../CoreVideo/cvpixelbuffer.md) that shares its underlying storage with a pixel buffer:

```swift
let src = vImage.PixelBuffer<vImage.Interleaved8x4>(
    size: vImage.Size(width: 64, height: 64))

src.withCVPixelBuffer(readOnly: false) { cvPixelBuffer in

    let ciImage = CIImage(cvImageBuffer: cvPixelBuffer)

    // Core Image workflow using `ciImage`
}
```

## Parameters

- `readOnly`: A Boolean value that specifies whether the function locks the [`CVPixelBuffer`](../../../CoreVideo/cvpixelbuffer.md) with the [`readOnly`](../../../CoreVideo/cvpixelbufferlockflags/readonly.md) flag. If the closure doesn’t modify the data, set this parameter to `true`.
- `body`: A closure with a [`CVPixelBuffer`](../../../CoreVideo/cvpixelbuffer.md) parameter that points to the underlying pixel buffer image data.

## See Also

### Pixel buffer methods
- [func copy(to: vImage.PixelBuffer<Format>)](./copy%28to%29.md)
  Copies the contents of the pixel buffer to another pixel buffer.
- [func copy(to: CVPixelBuffer, cvImageFormat: vImageCVImageFormat, cgImageFormat: vImage_CGImageFormat) throws](./copy%28to,cvimageformat,cgimageformat%29.md)
  Copies the contents of a pixel buffer to a Core Video pixel buffer.
- [func makeCGImage(cgImageFormat: vImage_CGImageFormat) -> CGImage?](./makecgimage%28cgimageformat%29.md)
  Returns a Core Graphics image from the pixel buffer’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/withcvpixelbuffer(readonly:body:))*