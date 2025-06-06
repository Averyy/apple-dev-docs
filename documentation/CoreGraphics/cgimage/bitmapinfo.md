# bitmapInfo

**Framework**: Core Graphics  
**Kind**: property

Returns the bitmap information for a bitmap image.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var bitmapInfo: CGBitmapInfo { get }
```

#### Discussion

This function returns a constant that specifies:

- The type of bitmap data—floating point or integer. You use the constant [`floatComponents`](cgbitmapinfo/floatcomponents.md) to extract this information.
- Whether an alpha channel is in the data, and if so, how the alpha data is stored. You use the constant [`alphaInfoMask`](cgbitmapinfo/alphainfomask.md) to extract the alpha information. Alpha information is specified as one of the constants listed in [`CGImageAlphaInfo`](cgimagealphainfo.md).

You can extract the alpha information

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
- [struct CGBitmapInfo](cgbitmapinfo.md)
  Component information for a bitmap image.
- [var utType: CFString?](cgimage/uttype.md)
  The Universal Type Identifier for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgimage/bitmapinfo)*