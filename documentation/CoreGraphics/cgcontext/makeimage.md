# makeImage()

**Framework**: Core Graphics  
**Kind**: method

Creates and returns a CGImage from the pixel data in a bitmap graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func makeImage() -> CGImage?
```

#### Return Value

A CGImage object that contains a snapshot of the bitmap graphics context or `NULL` if the image is not created.

#### Discussion

The CGImage object returned by this function is created by a copy operation. Subsequent changes to the bitmap graphics context do not affect the contents of the returned image. In some cases the copy operation actually follows copy-on-write semantics, so that the actual physical copy of the bits occur only if the underlying data in the bitmap graphics context is modified. As a consequence, you may want to use the resulting image and release it before you perform additional drawing into the bitmap graphics context. In this way, you can avoid the actual physical copy of the data.

## See Also

- [var bitmapInfo: CGBitmapInfo](cgcontext/bitmapinfo.md)
  Obtains the bitmap information associated with a bitmap graphics context.
- [var alphaInfo: CGImageAlphaInfo](cgcontext/alphainfo.md)
  Returns the alpha information associated with the context, which indicates how a bitmap context handles the alpha component.
- [var bitsPerComponent: Int](cgcontext/bitspercomponent.md)
  Returns the bits per component of a bitmap context.
- [var bitsPerPixel: Int](cgcontext/bitsperpixel.md)
  Returns the bits per pixel of a bitmap context.
- [var bytesPerRow: Int](cgcontext/bytesperrow.md)
  Returns the bytes per row of a bitmap context.
- [var colorSpace: CGColorSpace?](cgcontext/colorspace.md)
  Returns the color space of a bitmap context.
- [var data: UnsafeMutableRawPointer?](cgcontext/data.md)
  Returns a pointer to the image data associated with a bitmap context.
- [var height: Int](cgcontext/height.md)
  Returns the height in pixels of a bitmap context.
- [var width: Int](cgcontext/width.md)
  Returns the width in pixels of a bitmap context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/makeimage())*