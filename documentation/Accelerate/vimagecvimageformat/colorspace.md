# colorSpace

**Framework**: Accelerate  
**Kind**: property

The color space of the Core Video image format.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
var colorSpace: CGColorSpace? { get set }
```

## See Also

- [func vImageCVImageFormat_GetColorSpace(vImageConstCVImageFormat) -> Unmanaged<CGColorSpace>!](vimagecvimageformat_getcolorspace(_:).md)
  Returns the color space of a Core Video image format.
- [func vImageCVImageFormat_SetColorSpace(vImageCVImageFormat, CGColorSpace!) -> vImage_Error](vimagecvimageformat_setcolorspace(_:_:).md)
  Sets the color space of a Core Video image format.
- [var channelCount: UInt32](vimagecvimageformat/channelcount.md)
  The number of channels, including alpha, for the Core Video image format.
- [var channels: [vImage.BufferType]](vimagecvimageformat/channels.md)
  The channels of the Core Video image format.
- [func channelDescription(bufferType: vImage.BufferType) -> vImageChannelDescription?](vimagecvimageformat/channeldescription(buffertype:).md)
  Returns the range and clamp limits for a specified channel in a Core Video image format.
- [var formatCode: UInt32](vimagecvimageformat/formatcode.md)
  The four-character code that encodes the pixel format of the Core Video image format.
- [var chromaSiting: vImageCVImageFormat.ChromaSiting?](vimagecvimageformat/chromasiting-swift.property.md)
  The chrominance siting of the Core Video image format.
- [var alphaIsOpaqueHint: Bool](vimagecvimageformat/alphaisopaquehint.md)
  The alpha hint of the Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat/colorspace)*