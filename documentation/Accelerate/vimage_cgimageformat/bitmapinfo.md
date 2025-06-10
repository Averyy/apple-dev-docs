# bitmapInfo

**Framework**: Accelerate  
**Kind**: property

The component information that describes the color channels.

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
var bitmapInfo: CGBitmapInfo
```

## Mentions

- [Building a Basic Image-Processing Workflow](building-a-basic-image-processing-workflow.md)

#### Discussion

For example, ARGB8888 is [`CGImageAlphaInfo.first`](https://developer.apple.com/documentation/CoreGraphics/CGImageAlphaInfo/first) `|` [`byteOrderDefault`](https://developer.apple.com/documentation/CoreGraphics/CGBitmapInfo/byteOrderDefault), and BGRA8888 is [`CGImageAlphaInfo.first`](https://developer.apple.com/documentation/CoreGraphics/CGImageAlphaInfo/first) `|` [`byteOrder32Little`](https://developer.apple.com/documentation/CoreGraphics/CGBitmapInfo/byteOrder32Little).

## See Also

- [var bitsPerComponent: UInt32](vimage_cgimageformat/bitspercomponent.md)
  The number of bits that represents one channel of data in one pixel.
- [var bitsPerPixel: UInt32](vimage_cgimageformat/bitsperpixel.md)
  The number of bits that represents one pixel.
- [var colorSpace: Unmanaged<CGColorSpace>!](vimage_cgimageformat/colorspace.md)
  A description of the position of the pixel data in the image, relative to a reference XYZ color space.
- [var version: UInt32](vimage_cgimageformat/version.md)
  The version number.
- [var decode: UnsafePointer<CGFloat>!](vimage_cgimageformat/decode.md)
  The decode array for the image.
- [var renderingIntent: CGColorRenderingIntent](vimage_cgimageformat/renderingintent.md)
  A rendering intent constant that specifies how Core Graphics handles colors that aren’t within the destination color space gamut.
- [var componentCount: Int](vimage_cgimageformat/componentcount.md)
  The number of color and alpha channels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_cgimageformat/bitmapinfo)*