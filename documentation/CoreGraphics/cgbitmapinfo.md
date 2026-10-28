# CGBitmapInfo

**Framework**: Core Graphics  
**Kind**: struct  
**Role**: Structure

Component information for a bitmap image.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct CGBitmapInfo
```

```c
enum CGBitmapInfo : uint32_t;
```

## Overview

Applications that store pixel data in memory using ARGB format must take care in how they read data. If the code is not written correctly, it’s possible to misread the data which leads to colors or alpha that appear wrong. The byte order constants specify the byte ordering of pixel formats. To specify byte ordering, use a bitwise OR operator to combine the appropriate constant with the `bitmapInfo` parameter.

## Topics

### Constants
- [static var alphaInfoMask: CGBitmapInfo](./cgbitmapinfo/alphainfomask.md)
  The alpha information mask. Use this to extract alpha information that specifies whether a bitmap contains an alpha channel and how the alpha channel is generated.
- [static var floatComponents: CGBitmapInfo](./cgbitmapinfo/floatcomponents.md)
  The components of a bitmap are floating-point values.
- [static var byteOrderMask: CGBitmapInfo](./cgbitmapinfo/byteordermask.md)
  The byte ordering of pixel formats.
- [static var byteOrderDefault: CGBitmapInfo](./cgbitmapinfo/byteorderdefault.md)
  The default byte order.
- [static var byteOrder16Little: CGBitmapInfo](./cgbitmapinfo/byteorder16little.md)
  16-bit, little endian format.
- [static var byteOrder32Little: CGBitmapInfo](./cgbitmapinfo/byteorder32little.md)
  32-bit, little endian format.
- [static var byteOrder16Big: CGBitmapInfo](./cgbitmapinfo/byteorder16big.md)
  16-bit, big endian format.
- [static var byteOrder32Big: CGBitmapInfo](./cgbitmapinfo/byteorder32big.md)
  32-bit, big endian format.
- [static var floatInfoMask: CGBitmapInfo](./cgbitmapinfo/floatinfomask.md)
### Initializers
- [init(rawValue: UInt32)](./cgbitmapinfo/init%28rawvalue%29.md)
- [init(some Sequence<CGBitmapInfo>)](./cgbitmapinfo/init%28_%29.md)
- [init(alpha: CGImageAlphaInfo, component: CGImageComponentInfo, byteOrder: CGImageByteOrderInfo)](./cgbitmapinfo/init%28alpha,component,byteorder%29.md)
- [init(alpha: CGImageAlphaInfo, component: CGImageComponentInfo, byteOrder: CGImageByteOrderInfo, pixelFormat: CGImagePixelFormatInfo)](./cgbitmapinfo/init%28alpha,component,byteorder,pixelformat%29.md)
- [init(arrayLiteral: CGBitmapInfo...)](./cgbitmapinfo/init%28arrayliteral%29.md)
### Instance Properties
- [var alpha: CGImageAlphaInfo](./cgbitmapinfo/alpha.md)
- [var byteOrder: CGImageByteOrderInfo](./cgbitmapinfo/byteorder.md)
- [var component: CGImageComponentInfo](./cgbitmapinfo/component.md)
- [var isEmpty: Bool](./cgbitmapinfo/isempty.md)
- [var pixelFormat: CGImagePixelFormatInfo](./cgbitmapinfo/pixelformat.md)
### Instance Methods
- [func contains(CGBitmapInfo) -> Bool](./cgbitmapinfo/contains%28_%29.md)
- [func formIntersection(CGBitmapInfo)](./cgbitmapinfo/formintersection%28_%29.md)
- [func formSymmetricDifference(CGBitmapInfo)](./cgbitmapinfo/formsymmetricdifference%28_%29.md)
- [func formUnion(CGBitmapInfo)](./cgbitmapinfo/formunion%28_%29.md)
- [func insert(CGBitmapInfo) -> (inserted: Bool, memberAfterInsert: CGBitmapInfo)](./cgbitmapinfo/insert%28_%29.md)
- [func intersection(CGBitmapInfo) -> CGBitmapInfo](./cgbitmapinfo/intersection%28_%29.md)
- [func isDisjoint(with: CGBitmapInfo) -> Bool](./cgbitmapinfo/isdisjoint%28with%29.md)
- [func isSubset(of: CGBitmapInfo) -> Bool](./cgbitmapinfo/issubset%28of%29.md)
- [func isSuperset(of: CGBitmapInfo) -> Bool](./cgbitmapinfo/issuperset%28of%29.md)
- [func remove(CGBitmapInfo) -> CGBitmapInfo?](./cgbitmapinfo/remove%28_%29.md)
- [func subtract(CGBitmapInfo)](./cgbitmapinfo/subtract%28_%29.md)
- [func subtracting(CGBitmapInfo) -> CGBitmapInfo](./cgbitmapinfo/subtracting%28_%29.md)
- [func symmetricDifference(CGBitmapInfo) -> CGBitmapInfo](./cgbitmapinfo/symmetricdifference%28_%29.md)
- [func union(CGBitmapInfo) -> CGBitmapInfo](./cgbitmapinfo/union%28_%29.md)
- [func update(with: CGBitmapInfo) -> CGBitmapInfo?](./cgbitmapinfo/update%28with%29.md)
### Enumeration Cases
- [kCGBitmapAlphaInfoMask](./cgbitmapinfo/kcgbitmapalphainfomask.md)
- [kCGBitmapByteOrderInfoMask](./cgbitmapinfo/kcgbitmapbyteorderinfomask.md)
- [kCGBitmapByteOrderMask](./cgbitmapinfo/kcgbitmapbyteordermask.md)
- [kCGBitmapComponentInfoMask](./cgbitmapinfo/kcgbitmapcomponentinfomask.md)
- [kCGBitmapFloatInfoMask](./cgbitmapinfo/kcgbitmapfloatinfomask.md)
- [kCGBitmapPixelFormatInfoMask](./cgbitmapinfo/kcgbitmappixelformatinfomask.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Examining an image
- [var isMask: Bool](./cgimage/ismask.md)
  Returns whether a bitmap image is an image mask.
- [var width: Int](./cgimage/width.md)
  Returns the width of a bitmap image, in pixels.
- [var height: Int](./cgimage/height.md)
  Returns the height of a bitmap image.
- [var bitsPerComponent: Int](./cgimage/bitspercomponent.md)
  Returns the number of bits allocated for a single color component of a bitmap image.
- [var bitsPerPixel: Int](./cgimage/bitsperpixel.md)
  Returns the number of bits allocated for a single pixel in a bitmap image.
- [var bytesPerRow: Int](./cgimage/bytesperrow.md)
  Returns the number of bytes allocated for a single row of a bitmap image.
- [var colorSpace: CGColorSpace?](./cgimage/colorspace.md)
  Return the color space for a bitmap image.
- [var alphaInfo: CGImageAlphaInfo](./cgimage/alphainfo.md)
  Returns the alpha channel information for a bitmap image.
- [enum CGImageAlphaInfo](./cgimagealphainfo.md)
  Storage options for alpha component data.
- [var dataProvider: CGDataProvider?](./cgimage/dataprovider.md)
  Returns the data provider for a bitmap image or image mask.
- [var decode: UnsafePointer<CGFloat>?](./cgimage/decode.md)
  Returns the decode array for a bitmap image.
- [var shouldInterpolate: Bool](./cgimage/shouldinterpolate.md)
  Returns the interpolation setting for a bitmap image.
- [var renderingIntent: CGColorRenderingIntent](./cgimage/renderingintent.md)
  Returns the rendering intent setting for a bitmap image.
- [var bitmapInfo: CGBitmapInfo](./cgimage/bitmapinfo.md)
  Returns the bitmap information for a bitmap image.
- [var utType: CFString?](./cgimage/uttype.md)
  The Universal Type Identifier for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgbitmapinfo)*