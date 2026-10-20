# height

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Returns the height in pixels of a bitmap context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var height: Int { get }
```

```c
extern size_t CGBitmapContextGetHeight(CGContextRef context);
```

## See Also

### Managing a Bitmap Graphics Context
- [var bitmapInfo: CGBitmapInfo](./bitmapinfo.md)
  Obtains the bitmap information associated with a bitmap graphics context.
- [var alphaInfo: CGImageAlphaInfo](./alphainfo.md)
  Returns the alpha information associated with the context, which indicates how a bitmap context handles the alpha component.
- [var bitsPerComponent: Int](./bitspercomponent.md)
  Returns the bits per component of a bitmap context.
- [var bitsPerPixel: Int](./bitsperpixel.md)
  Returns the bits per pixel of a bitmap context.
- [var bytesPerRow: Int](./bytesperrow.md)
  Returns the bytes per row of a bitmap context.
- [var colorSpace: CGColorSpace?](./colorspace.md)
  Returns the color space of a bitmap context.
- [var data: UnsafeMutableRawPointer?](./data.md)
  Returns a pointer to the image data associated with a bitmap context.
- [var width: Int](./width.md)
  Returns the width in pixels of a bitmap context.
- [func makeImage() -> CGImage?](./makeimage%28%29.md)
  Creates and returns a CGImage from the pixel data in a bitmap graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/height)*