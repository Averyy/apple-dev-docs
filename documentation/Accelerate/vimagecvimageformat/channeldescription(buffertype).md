# channelDescription(bufferType:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Returns the range and clamp limits for a specified channel in a Core Video image format.

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
func channelDescription(bufferType: vImage.BufferType) -> vImageChannelDescription?
```

#### Return Value

A [`vImageChannelDescription`](../vimagechanneldescription.md) structure that describes the range and clamp limits for the specified channel.

#### Discussion

Use this function to return the [`vImageChannelDescription`](../vimagechanneldescription.md) description for a specified channel in a Core Video format.

For example, the following code prints the description of each channel in a [`kCVPixelFormatType_420YpCbCr8Planar`](../../CoreVideo/kcvpixelformattype_420ypcbcr8planar.md) Core Video image format:

```swift
let cvImageFormat = vImageCVImageFormat.make(
    format: .format420YpCbCr8Planar,
    matrix: kvImage_ARGBToYpCbCrMatrix_ITU_R_709_2.pointee,
    chromaSiting: .center,
    colorSpace: CGColorSpace(name: CGColorSpace.sRGB)!,
    alphaIsOpaqueHint: true)!

// Prints:
//    luminance   vImageChannelDescription(min: 0.0, zero: 16.0, full: 235.0, max: 255.0)
//    Cb          vImageChannelDescription(min: 0.0, zero: 128.0, full: 240.0, max: 255.0)
//    Cr          vImageChannelDescription(min: 0.0, zero: 128.0, full: 240.0, max: 255.0)
for channel in cvImageFormat.channels {
    let desc = cvImageFormat.channelDescription(bufferType: channel)!
    print("\(channel) \t\t \(desc)")
}
```

## Parameters

- `bufferType`: The source buffer type.

## See Also

### Related Documentation
- [func vImageCVImageFormat_CopyChannelDescription(vImageCVImageFormat, UnsafePointer<vImageChannelDescription>, vImageBufferTypeCode) -> vImage_Error](../vimagecvimageformat_copychanneldescription%28_,_,_%29.md)
  Copies the channel description for a particular channel type to an image format.
### Inspecting a Core Video image format’s properties
- [var channelCount: UInt32](./channelcount.md)
  The number of channels, including alpha, for the Core Video image format.
- [var channels: [vImage.BufferType]](./channels.md)
  The channels of the Core Video image format.
- [var formatCode: UInt32](./formatcode.md)
  The four-character code that encodes the pixel format of the Core Video image format.
- [var chromaSiting: vImageCVImageFormat.ChromaSiting?](./chromasiting-swift.property.md)
  The chrominance siting of the Core Video image format.
- [var colorSpace: CGColorSpace?](./colorspace.md)
  The color space of the Core Video image format.
- [var alphaIsOpaqueHint: Bool](./alphaisopaquehint.md)
  The alpha hint of the Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat/channeldescription(buffertype:))*