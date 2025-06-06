# formatCode

**Framework**: Accelerate  
**Kind**: property

The four-character code that encodes the pixel format of the Core Video image format.

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
var formatCode: UInt32 { get }
```

#### Discussion

For example, the following code prints the format code of a [`kCVPixelFormatType_420YpCbCr8Planar`](https://developer.apple.com/documentation/CoreVideo/kCVPixelFormatType_420YpCbCr8Planar) Core Video image format that equals the expected type:

```swift
let cvImageFormat = vImageCVImageFormat.make(
    format: .format420YpCbCr8Planar,
    matrix: kvImage_ARGBToYpCbCrMatrix_ITU_R_709_2.pointee,
    chromaSiting: .center,
    colorSpace: CGColorSpace(name: CGColorSpace.sRGB)!,
    alphaIsOpaqueHint: true)!

// Prints "true".
print(cvImageFormat.formatCode == kCVPixelFormatType_420YpCbCr8Planar)
```

## See Also

- [func vImageCVImageFormat_GetFormatCode(vImageConstCVImageFormat) -> UInt32](vimagecvimageformat_getformatcode(_:).md)
  Returns the four-character code that encodes the pixel format of a Core Video image format.
- [var channelCount: UInt32](vimagecvimageformat/channelcount.md)
  The number of channels, including alpha, for the Core Video image format.
- [var channels: [vImage.BufferType]](vimagecvimageformat/channels.md)
  The channels of the Core Video image format.
- [func channelDescription(bufferType: vImage.BufferType) -> vImageChannelDescription?](vimagecvimageformat/channeldescription(buffertype:).md)
  Returns the range and clamp limits for a specified channel in a Core Video image format.
- [var chromaSiting: vImageCVImageFormat.ChromaSiting?](vimagecvimageformat/chromasiting-swift.property.md)
  The chrominance siting of the Core Video image format.
- [var colorSpace: CGColorSpace?](vimagecvimageformat/colorspace.md)
  The color space of the Core Video image format.
- [var alphaIsOpaqueHint: Bool](vimagecvimageformat/alphaisopaquehint.md)
  The alpha hint of the Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat/formatcode)*