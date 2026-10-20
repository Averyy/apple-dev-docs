# colorSpace

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The color space of the Core Video image format.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
var colorSpace: CGColorSpace? { get set }
```

## See Also

### Related Documentation
- [func vImageCVImageFormat_GetColorSpace(vImageConstCVImageFormat) -> Unmanaged<CGColorSpace>!](../vimagecvimageformat_getcolorspace%28_%29.md)
  Returns the color space of a Core Video image format.
- [func vImageCVImageFormat_SetColorSpace(vImageCVImageFormat, CGColorSpace!) -> vImage_Error](../vimagecvimageformat_setcolorspace%28_,_%29.md)
  Sets the color space of a Core Video image format.
### Inspecting a Core Video image format’s properties
- [var channelCount: UInt32](./channelcount.md)
  The number of channels, including alpha, for the Core Video image format.
- [var channels: [vImage.BufferType]](./channels.md)
  The channels of the Core Video image format.
- [func channelDescription(bufferType: vImage.BufferType) -> vImageChannelDescription?](./channeldescription%28buffertype%29.md)
  Returns the range and clamp limits for a specified channel in a Core Video image format.
- [var formatCode: UInt32](./formatcode.md)
  The four-character code that encodes the pixel format of the Core Video image format.
- [var chromaSiting: vImageCVImageFormat.ChromaSiting?](./chromasiting-swift.property.md)
  The chrominance siting of the Core Video image format.
- [var alphaIsOpaqueHint: Bool](./alphaisopaquehint.md)
  The alpha hint of the Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat/colorspace)*