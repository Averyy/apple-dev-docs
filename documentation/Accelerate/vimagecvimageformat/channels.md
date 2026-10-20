# channels

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The channels of the Core Video image format.

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
var channels: [vImage.BufferType] { get }
```

#### Discussion

For example, the following code prints the channels in a [`kCVPixelFormatType_420YpCbCr8Planar`](../../CoreVideo/kcvpixelformattype_420ypcbcr8planar.md) Core Video image format:

```swift
let cvImageFormat = vImageCVImageFormat.make(
    format: .format420YpCbCr8Planar,
    matrix: kvImage_ARGBToYpCbCrMatrix_ITU_R_709_2.pointee,
    chromaSiting: .center,
    colorSpace: CGColorSpace(name: CGColorSpace.sRGB)!,
    alphaIsOpaqueHint: true)!

// Prints "channels [Accelerate.vImage.BufferType.luminance,
//                   Accelerate.vImage.BufferType.Cb,
//                   Accelerate.vImage.BufferType.Cr]".
print("channels \(cvImageFormat.channels)")
```

## See Also

### Related Documentation
- [func vImageCVImageFormat_GetChannelNames(vImageConstCVImageFormat) -> UnsafePointer<vImageBufferTypeCode>!](../vimagecvimageformat_getchannelnames%28_%29.md)
  Returns the names of the channels of a Core Video image format.
### Inspecting a Core Video image format’s properties
- [var channelCount: UInt32](./channelcount.md)
  The number of channels, including alpha, for the Core Video image format.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat/channels)*