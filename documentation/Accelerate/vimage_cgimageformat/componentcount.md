# componentCount

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The number of color and alpha channels.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
var componentCount: Int { get }
```

## See Also

### Instance properties
- [var bitsPerComponent: UInt32](./bitspercomponent.md)
  The number of bits that represents one channel of data in one pixel.
- [var bitsPerPixel: UInt32](./bitsperpixel.md)
  The number of bits that represents one pixel.
- [var colorSpace: Unmanaged<CGColorSpace>!](./colorspace.md)
  A description of the position of the pixel data in the image, relative to a reference XYZ color space.
- [var bitmapInfo: CGBitmapInfo](./bitmapinfo.md)
  The component information that describes the color channels.
- [var version: UInt32](./version.md)
  The version number.
- [var decode: UnsafePointer<CGFloat>!](./decode.md)
  The decode array for the image.
- [var renderingIntent: CGColorRenderingIntent](./renderingintent.md)
  A rendering intent constant that specifies how Core Graphics handles colors that aren’t within the destination color space gamut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat/componentcount)*