# CGImageAlphaInfo

**Framework**: Core Graphics  
**Kind**: enum

Storage options for alpha component data.

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
enum CGImageAlphaInfo
```

#### Overview

A [`CGImageAlphaInfo`](cgimagealphainfo.md) constant specifies (1) whether a bitmap contains an alpha channel, (2) where the alpha bits are located in the image data, and (3) whether the alpha value is premultiplied. You can obtain a [`CGImageAlphaInfo`](cgimagealphainfo.md) constant for an image by calling the [`alphaInfo`](cgimage/alphainfo.md) function. (You provide a [`CGBitmapInfo`](cgbitmapinfo.md) constant to the function [`init(width:height:bitsPerComponent:bitsPerPixel:bytesPerRow:space:bitmapInfo:provider:decode:shouldInterpolate:intent:)`](cgimage/init(width:height:bitspercomponent:bitsperpixel:bytesperrow:space:bitmapinfo:provider:decode:shouldinterpolate:intent:).md), part of which is a [`CGImageAlphaInfo`](cgimagealphainfo.md) constant.)

Alpha blending is accomplished by combining the color components of the source image with the color components of the destination image using the linear interpolation formula, where “source” is one color component of one pixel of the new paint and “destination” is one color component of the background image.

Core Graphics supports premultiplied alpha only for images. You should not premultiply any other color values specified in Core Graphics.

## Topics

### Constants
- [CGImageAlphaInfo.first](cgimagealphainfo/first.md)
  The alpha component is stored in the most significant bits of each pixel. For example, non-premultiplied ARGB.
- [CGImageAlphaInfo.last](cgimagealphainfo/last.md)
  The alpha component is stored in the least significant bits of each pixel. For example, non-premultiplied RGBA.
- [CGImageAlphaInfo.none](cgimagealphainfo/none.md)
  There is no alpha channel.
- [CGImageAlphaInfo.noneSkipFirst](cgimagealphainfo/noneskipfirst.md)
  There is no alpha channel. If the total size of the pixel is greater than the space required for the number of color components in the color space, the most significant bits are ignored.
- [CGImageAlphaInfo.alphaOnly](cgimagealphainfo/alphaonly.md)
  There is no color data, only an alpha channel.
- [CGImageAlphaInfo.noneSkipLast](cgimagealphainfo/noneskiplast.md)
  There is no alpha channel.
- [CGImageAlphaInfo.premultipliedFirst](cgimagealphainfo/premultipliedfirst.md)
  The alpha component is stored in the most significant bits of each pixel and the color components have already been multiplied by this alpha value. For example, premultiplied ARGB.
- [CGImageAlphaInfo.premultipliedLast](cgimagealphainfo/premultipliedlast.md)
  The alpha component is stored in the least significant bits of each pixel and the color components have already been multiplied by this alpha value. For example, premultiplied RGBA.
### Initializers
- [init?(rawValue: UInt32)](cgimagealphainfo/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var isMask: Bool](cgimage/ismask.md)
  Returns whether a bitmap image is an image mask.
- [var width: Int](cgimage/width.md)
  Returns the width of a bitmap image, in pixels.
- [var height: Int](cgimage/height.md)
  Returns the height of a bitmap image.
- [var bitsPerComponent: Int](cgimage/bitspercomponent.md)
  Returns the number of bits allocated for a single color component of a bitmap image.
- [var bitsPerPixel: Int](cgimage/bitsperpixel.md)
  Returns the number of bits allocated for a single pixel in a bitmap image.
- [var bytesPerRow: Int](cgimage/bytesperrow.md)
  Returns the number of bytes allocated for a single row of a bitmap image.
- [var colorSpace: CGColorSpace?](cgimage/colorspace.md)
  Return the color space for a bitmap image.
- [var alphaInfo: CGImageAlphaInfo](cgimage/alphainfo.md)
  Returns the alpha channel information for a bitmap image.
- [var dataProvider: CGDataProvider?](cgimage/dataprovider.md)
  Returns the data provider for a bitmap image or image mask.
- [var decode: UnsafePointer<CGFloat>?](cgimage/decode.md)
  Returns the decode array for a bitmap image.
- [var shouldInterpolate: Bool](cgimage/shouldinterpolate.md)
  Returns the interpolation setting for a bitmap image.
- [var renderingIntent: CGColorRenderingIntent](cgimage/renderingintent.md)
  Returns the rendering intent setting for a bitmap image.
- [var bitmapInfo: CGBitmapInfo](cgimage/bitmapinfo.md)
  Returns the bitmap information for a bitmap image.
- [struct CGBitmapInfo](cgbitmapinfo.md)
  Component information for a bitmap image.
- [var utType: CFString?](cgimage/uttype.md)
  The Universal Type Identifier for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgimagealphainfo)*