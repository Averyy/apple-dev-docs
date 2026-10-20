# decode

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Returns the decode array for a bitmap image.

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
var decode: UnsafePointer<CGFloat>? { get }
```

```c
extern const CGFloat *CGImageGetDecode(CGImageRef image);
```

#### Discussion

For a bitmap image or image mask, for each color component in the source color space, the decode array contains a pair of values denoting the upper and lower limits of a range. When the image is rendered, a linear transform maps the original component value into a relative number, within the designated range, that is appropriate for the destination color space. If remapping of the image’s color values is not allowed, the returned value will be `NULL`.

## See Also

### Examining an image
- [var isMask: Bool](./ismask.md)
  Returns whether a bitmap image is an image mask.
- [var width: Int](./width.md)
  Returns the width of a bitmap image, in pixels.
- [var height: Int](./height.md)
  Returns the height of a bitmap image.
- [var bitsPerComponent: Int](./bitspercomponent.md)
  Returns the number of bits allocated for a single color component of a bitmap image.
- [var bitsPerPixel: Int](./bitsperpixel.md)
  Returns the number of bits allocated for a single pixel in a bitmap image.
- [var bytesPerRow: Int](./bytesperrow.md)
  Returns the number of bytes allocated for a single row of a bitmap image.
- [var colorSpace: CGColorSpace?](./colorspace.md)
  Return the color space for a bitmap image.
- [var alphaInfo: CGImageAlphaInfo](./alphainfo.md)
  Returns the alpha channel information for a bitmap image.
- [enum CGImageAlphaInfo](../cgimagealphainfo.md)
  Storage options for alpha component data.
- [var dataProvider: CGDataProvider?](./dataprovider.md)
  Returns the data provider for a bitmap image or image mask.
- [var shouldInterpolate: Bool](./shouldinterpolate.md)
  Returns the interpolation setting for a bitmap image.
- [var renderingIntent: CGColorRenderingIntent](./renderingintent.md)
  Returns the rendering intent setting for a bitmap image.
- [var bitmapInfo: CGBitmapInfo](./bitmapinfo.md)
  Returns the bitmap information for a bitmap image.
- [struct CGBitmapInfo](../cgbitmapinfo.md)
  Component information for a bitmap image.
- [var utType: CFString?](./uttype.md)
  The Universal Type Identifier for the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgimage/decode)*