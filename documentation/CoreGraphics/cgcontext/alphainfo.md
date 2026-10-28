# alphaInfo

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Returns the alpha information associated with the context, which indicates how a bitmap context handles the alpha component.

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
var alphaInfo: CGImageAlphaInfo { get }
```

```c
extern CGImageAlphaInfo CGBitmapContextGetAlphaInfo(CGContextRef context);
```

## Discussion

Every bitmap context contains an attribute that specifies whether the bitmap contains an alpha component, and how it is generated. The alpha component determines the opacity of a pixel when it is drawn.

## See Also

### Managing a Bitmap Graphics Context
- [var bitmapInfo: CGBitmapInfo](./bitmapinfo.md)
  Obtains the bitmap information associated with a bitmap graphics context.
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
- [var height: Int](./height.md)
  Returns the height in pixels of a bitmap context.
- [var width: Int](./width.md)
  Returns the width in pixels of a bitmap context.
- [func makeImage() -> CGImage?](./makeimage%28%29.md)
  Creates and returns a CGImage from the pixel data in a bitmap graphics context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/alphainfo)*