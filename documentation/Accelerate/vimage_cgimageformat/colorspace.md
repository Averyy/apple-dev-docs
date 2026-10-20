# colorSpace

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

A description of the position of the pixel data in the image, relative to a reference XYZ color space.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var colorSpace: Unmanaged<CGColorSpace>!
```

```c
CGColorSpaceRef colorSpace;
```

## See Also

### Instance properties
- [var bitsPerComponent: UInt32](./bitspercomponent.md)
  The number of bits that represents one channel of data in one pixel.
- [var bitsPerPixel: UInt32](./bitsperpixel.md)
  The number of bits that represents one pixel.
- [var bitmapInfo: CGBitmapInfo](./bitmapinfo.md)
  The component information that describes the color channels.
- [var version: UInt32](./version.md)
  The version number.
- [var decode: UnsafePointer<CGFloat>!](./decode.md)
  The decode array for the image.
- [var renderingIntent: CGColorRenderingIntent](./renderingintent.md)
  A rendering intent constant that specifies how Core Graphics handles colors that aren’t within the destination color space gamut.
- [var componentCount: Int](./componentcount.md)
  The number of color and alpha channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat/colorspace)*