# bitsPerPixel

**Framework**: Accelerate  
**Kind**: property

The number of bits that represents one pixel.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var bitsPerPixel: UInt32
```

#### Discussion

For ARGB8888, this is 32.

The number of color components derives from the color space, and the number of alpha components (zero or one) derives from the [`bitmapInfo`](vimage_cgimageformat/bitmapinfo.md).

## See Also

- [var bitsPerComponent: UInt32](vimage_cgimageformat/bitspercomponent.md)
  The number of bits that represents one channel of data in one pixel.
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
- [var componentCount: Int](vimage_cgimageformat/componentcount.md)
  The number of color and alpha channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat/bitsperpixel)*