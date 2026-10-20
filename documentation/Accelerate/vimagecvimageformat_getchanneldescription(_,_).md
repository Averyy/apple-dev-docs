# vImageCVImageFormat_GetChannelDescription(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns the channel description for a particular channel type.

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
func vImageCVImageFormat_GetChannelDescription(_ format: vImageConstCVImageFormat, _ type: vImageBufferTypeCode) -> UnsafePointer<vImageChannelDescription>!
```

```c
const vImageChannelDescription *vImageCVImageFormat_GetChannelDescription(vImageConstCVImageFormatRef format, vImageBufferTypeCode type);
```

#### Return Value

A pointer to a [`vImageChannelDescription`](./vimagechanneldescription.md) structure that contains the channel description.

#### Discussion

The functions that create Core Video image formats, such as [`vImageCVImageFormat_CreateWithCVPixelBuffer(_:)`](./vimagecvimageformat_createwithcvpixelbuffer%28_%29.md), return a [`vImageCVImageFormat`](./vimagecvimageformat.md). The following code shows how you create a [`vImageConstCVImageFormat`](./vimageconstcvimageformat.md) representation of a [`vImageCVImageFormat`](./vimagecvimageformat.md) instance to pass to [`vImageCVImageFormat_GetChannelDescription(_:_:)`](./vimagecvimageformat_getchanneldescription%28_,_%29.md):

**Swift**:

```swift
let channelDescription = withUnsafeBytes(of: cvImageFormat) { bytes in
    let format = bytes.assumingMemoryBound(
        to: vImageConstCVImageFormat.self).first!
    
    return vImageCVImageFormat_GetChannelDescription(format,
                                                     vImageBufferTypeCode(kvImageBufferTypeCode_Luminance))
}
```

**Objective-C**:

```objc
vImageConstCVImageFormatRef constFormat = cvImageFormat;

const vImageChannelDescription *channelDescription =
    vImageCVImageFormat_GetChannelDescription(constFormat,
                                              (vImageBufferTypeCode)kvImageBufferTypeCode_Luminance);
```

## Parameters

- `format`: The Core Video image format to query.
- `type`: The type of the channel that you want information about. For example, [`kvImageBufferTypeCode_Luminance`](./kvimagebuffertypecode_luminance.md).

## See Also

### Related Documentation
- [func channelDescription(bufferType: vImage.BufferType) -> vImageChannelDescription?](./vimagecvimageformat/channeldescription%28buffertype%29.md)
  Returns the range and clamp limits for a specified channel in a Core Video image format.
### Querying and setting channel information
- [func vImageCVImageFormat_GetChannelCount(vImageConstCVImageFormat) -> UInt32](./vimagecvimageformat_getchannelcount%28_%29.md)
  Returns the number of channels, including alpha, for the Core Video image format.
- [func vImageCVImageFormat_CopyChannelDescription(vImageCVImageFormat, UnsafePointer<vImageChannelDescription>, vImageBufferTypeCode) -> vImage_Error](./vimagecvimageformat_copychanneldescription%28_,_,_%29.md)
  Copies the channel description for a particular channel type to an image format.
- [func vImageCVImageFormat_GetChannelNames(vImageConstCVImageFormat) -> UnsafePointer<vImageBufferTypeCode>!](./vimagecvimageformat_getchannelnames%28_%29.md)
  Returns the names of the channels of a Core Video image format.
- [struct vImageChannelDescription](./vimagechanneldescription.md)
  A description of the range and clamp limits for a pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_getchanneldescription(_:_:))*