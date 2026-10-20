# channelCount

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The number of channels, including alpha, for the Core Video image format.

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
var channelCount: UInt32 { get }
```

#### Discussion

For example, the following code prints the number of channels in a [`kCVPixelFormatType_420YpCbCr8Planar`](../../CoreVideo/kcvpixelformattype_420ypcbcr8planar.md) Core Video image format:

```swift
let cvImageFormat = vImageCVImageFormat.make(
    format: .format420YpCbCr8Planar,
    matrix: kvImage_ARGBToYpCbCrMatrix_ITU_R_709_2.pointee,
    chromaSiting: .center,
    colorSpace: CGColorSpace(name: CGColorSpace.sRGB)!,
    alphaIsOpaqueHint: true)!

// Prints "channelCount: 3".
print("channelCount: \(cvImageFormat.channelCount)")
```

## See Also

### Related Documentation
- [func vImageCVImageFormat_GetChannelCount(vImageConstCVImageFormat) -> UInt32](../vimagecvimageformat_getchannelcount%28_%29.md)
  Returns the number of channels, including alpha, for the Core Video image format.
### Inspecting a Core Video image format’s properties
- [var channels: [vImage.BufferType]](./channels.md)
  The channels of the Core Video image format.
- [func channelDescription(bufferType: vImage.BufferType) -> vImageChannelDescription?](./channeldescription%28buffertype%29.md)
  Returns the range and clamp limits for a specified channel in a Core Video image format.
- [var formatCode: UInt32](./formatcode.md)
  The four-character code that encodes the pixel format of the Core Video image format.
- [var chromaSiting: vImageCVImageFormat.ChromaSiting?](./chromasiting-swift.property.md)
  The chrominance siting of the Core Video image format.
- [var colorSpace: CGColorSpace?](./colorspace.md)
  The color space of the Core Video image format.
- [var alphaIsOpaqueHint: Bool](./alphaisopaquehint.md)
  The alpha hint of the Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat/channelcount)*