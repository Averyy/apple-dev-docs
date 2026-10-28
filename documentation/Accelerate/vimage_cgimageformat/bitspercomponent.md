# bitsPerComponent

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The number of bits that represents one channel of data in one pixel.

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
var bitsPerComponent: UInt32
```

```c
uint32_t bitsPerComponent;
```

## Discussion

For ARGB8888, this is 8. Expected values are 1, 2, 4, 5, 8, 10, 12, 16, or 32.

## See Also

### Instance properties
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
- [var componentCount: Int](./componentcount.md)
  The number of color and alpha channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat/bitspercomponent)*