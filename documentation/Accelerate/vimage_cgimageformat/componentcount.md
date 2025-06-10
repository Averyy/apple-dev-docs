# componentCount

**Framework**: Accelerate  
**Kind**: property

The number of color and alpha channels.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
var componentCount: Int { get }
```

## See Also

- [var bitsPerComponent: UInt32](vimage_cgimageformat/bitspercomponent.md)
  The number of bits that represents one channel of data in one pixel.
- [var bitsPerPixel: UInt32](vimage_cgimageformat/bitsperpixel.md)
  The number of bits that represents one pixel.
- [var colorSpace: Unmanaged<CGColorSpace>!](vimage_cgimageformat/colorspace.md)
  A description of the position of the pixel data in the image, relative to a reference XYZ color space.
- [var bitmapInfo: CGBitmapInfo](vimage_cgimageformat/bitmapinfo.md)
  The component information that describes the color channels.
- [var version: UInt32](vimage_cgimageformat/version.md)
  The version number.
- [var decode: UnsafePointer<CGFloat>!](vimage_cgimageformat/decode.md)
  The decode array for the image.
- [var renderingIntent: CGColorRenderingIntent](vimage_cgimageformat/renderingintent.md)
  A rendering intent constant that specifies how Core Graphics handles colors that aren’t within the destination color space gamut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat/componentcount)*