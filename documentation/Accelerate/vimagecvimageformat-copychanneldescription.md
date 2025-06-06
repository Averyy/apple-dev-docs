# vImageCVImageFormat_CopyChannelDescription(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Copies the channel description for a particular channel type to an image format.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 8.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageCVImageFormat_CopyChannelDescription(_ format: vImageCVImageFormat, _ desc: UnsafePointer<vImageChannelDescription>, _ type: vImageBufferTypeCode) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

## Parameters

- `format`: The   to copy the channel description into.
- `desc`: A pointer to a new   to use for the channel type.
- `type`: The type of the channel that you want to set information about, for example,  .

## See Also

- [func vImageCVImageFormat_GetChannelCount(vImageConstCVImageFormat) -> UInt32](vimagecvimageformat_getchannelcount(_:).md)
  Returns the number of channels, including alpha, for the Core Video image format.
- [func vImageCVImageFormat_GetChannelDescription(vImageConstCVImageFormat, vImageBufferTypeCode) -> UnsafePointer<vImageChannelDescription>!](vimagecvimageformat_getchanneldescription(_:_:).md)
  Returns the channel description for a particular channel type.
- [func vImageCVImageFormat_GetChannelNames(vImageConstCVImageFormat) -> UnsafePointer<vImageBufferTypeCode>!](vimagecvimageformat_getchannelnames(_:).md)
  Returns the names of the channels of a Core Video image format.
- [struct vImageChannelDescription](vimagechanneldescription.md)
  A description of the range and clamp limits for a pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_copychanneldescription(_:_:_:))*