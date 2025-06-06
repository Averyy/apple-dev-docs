# CGBitmapInfo

**Framework**: Core Graphics  
**Kind**: struct

Component information for a bitmap image.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct CGBitmapInfo
```

#### Overview

Applications that store pixel data in memory using ARGB format must take care in how they read data. If the code is not written correctly, it’s possible to misread the data which leads to colors or alpha that appear wrong. The byte order constants specify the byte ordering of pixel formats. To specify byte ordering, use a bitwise OR operator to combine the appropriate constant with the `bitmapInfo` parameter.

## Topics

### Constants
- [static var alphaInfoMask: CGBitmapInfo](cgbitmapinfo/alphainfomask.md)
  The alpha information mask. Use this to extract alpha information that specifies whether a bitmap contains an alpha channel and how the alpha channel is generated.
- [static var floatComponents: CGBitmapInfo](cgbitmapinfo/floatcomponents.md)
  The components of a bitmap are floating-point values.
- [static var byteOrderMask: CGBitmapInfo](cgbitmapinfo/byteordermask.md)
  The byte ordering of pixel formats.
- [static var byteOrderDefault: CGBitmapInfo](cgbitmapinfo/byteorderdefault.md)
  The default byte order.
- [static var byteOrder16Little: CGBitmapInfo](cgbitmapinfo/byteorder16little.md)
  16-bit, little endian format.
- [static var byteOrder32Little: CGBitmapInfo](cgbitmapinfo/byteorder32little.md)
  32-bit, little endian format.
- [static var byteOrder16Big: CGBitmapInfo](cgbitmapinfo/byteorder16big.md)
  16-bit, big endian format.
- [static var byteOrder32Big: CGBitmapInfo](cgbitmapinfo/byteorder32big.md)
  32-bit, big endian format.
- [static var floatInfoMask: CGBitmapInfo](cgbitmapinfo/floatinfomask.md)
### Initializers
- [init(rawValue: UInt32)](cgbitmapinfo/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

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
- [enum CGImageAlphaInfo](cgimagealphainfo.md)
  Storage options for alpha component data.
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
- [var utType: CFString?](cgimage/uttype.md)
  The Universal Type Identifier for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgbitmapinfo)*