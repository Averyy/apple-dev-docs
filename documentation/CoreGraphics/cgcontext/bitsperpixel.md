# bitsPerPixel

**Framework**: Core Graphics  
**Kind**: property

Returns the bits per pixel of a bitmap context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var bitsPerPixel: Int { get }
```

## See Also

- [var bitmapInfo: CGBitmapInfo](cgcontext/bitmapinfo.md)
  Obtains the bitmap information associated with a bitmap graphics context.
- [var alphaInfo: CGImageAlphaInfo](cgcontext/alphainfo.md)
  Returns the alpha information associated with the context, which indicates how a bitmap context handles the alpha component.
- [var bitsPerComponent: Int](cgcontext/bitspercomponent.md)
  Returns the bits per component of a bitmap context.
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
- [func makeImage() -> CGImage?](cgcontext/makeimage.md)
  Creates and returns a CGImage from the pixel data in a bitmap graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/bitsperpixel)*