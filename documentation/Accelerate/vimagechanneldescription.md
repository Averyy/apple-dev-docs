# vImageChannelDescription

**Framework**: Accelerate  
**Kind**: struct

A description of the range and clamp limits for a pixel format.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct vImageChannelDescription
```

#### Overview

A [`vImageChannelDescription`](vimagechanneldescription.md) structure describes the range and clamp limits for each channel in a Core Video image format. The [`min`](vimagechanneldescription/min.md) and [`max`](vimagechanneldescription/max.md) properties define the clamping limits, and functions clamp values to [`min`](vimagechanneldescription/min.md)…[`max`](vimagechanneldescription/max.md). The [`zero`](vimagechanneldescription/zero.md) and [`full`](vimagechanneldescription/full.md) values specify the normal range and bias for a format, and encode `0.0` and `1.0`, respectively (`0.0` and `0.5` for chrominance).

## Topics

### Creating a channel description
- [init(min: CGFloat, zero: CGFloat, full: CGFloat, max: CGFloat)](vimagechanneldescription/init(min:zero:full:max:).md)
  Returns a structure that describes the range and clamp limits for a pixel format.
- [init()](vimagechanneldescription/init.md)
  Returns an empty structure that describes the range and clamp limits for a pixel format.
### Instance properties
- [var min: CGFloat](vimagechanneldescription/min.md)
  The minimum encoded value.
- [var zero: CGFloat](vimagechanneldescription/zero.md)
  The encoding for the value zero.
- [var full: CGFloat](vimagechanneldescription/full.md)
  The encoding for the value one.
- [var max: CGFloat](vimagechanneldescription/max.md)
  The maximum encoded value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func vImageCVImageFormat_GetChannelCount(vImageConstCVImageFormat) -> UInt32](vimagecvimageformat_getchannelcount(_:).md)
  Returns the number of channels, including alpha, for the Core Video image format.
- [func vImageCVImageFormat_GetChannelDescription(vImageConstCVImageFormat, vImageBufferTypeCode) -> UnsafePointer<vImageChannelDescription>!](vimagecvimageformat_getchanneldescription(_:_:).md)
  Returns the channel description for a particular channel type.
- [func vImageCVImageFormat_CopyChannelDescription(vImageCVImageFormat, UnsafePointer<vImageChannelDescription>, vImageBufferTypeCode) -> vImage_Error](vimagecvimageformat_copychanneldescription(_:_:_:).md)
  Copies the channel description for a particular channel type to an image format.
- [func vImageCVImageFormat_GetChannelNames(vImageConstCVImageFormat) -> UnsafePointer<vImageBufferTypeCode>!](vimagecvimageformat_getchannelnames(_:).md)
  Returns the names of the channels of a Core Video image format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagechanneldescription)*