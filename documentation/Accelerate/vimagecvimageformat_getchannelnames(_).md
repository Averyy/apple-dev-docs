# vImageCVImageFormat_GetChannelNames(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns the names of the channels of a Core Video image format.

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
func vImageCVImageFormat_GetChannelNames(_ format: vImageConstCVImageFormat) -> UnsafePointer<vImageBufferTypeCode>!
```

```c
const vImageBufferTypeCode *vImageCVImageFormat_GetChannelNames(vImageConstCVImageFormatRef format);
```

#### Return Value

A pointer to an array that contains the [`vImageBufferTypeCode`](./vimagebuffertypecode.md) elements that correspond to the names of the channels in the image.

#### Discussion

The functions that create Core Video image formats, such as [`vImageCVImageFormat_CreateWithCVPixelBuffer(_:)`](./vimagecvimageformat_createwithcvpixelbuffer%28_%29.md), return a [`vImageCVImageFormat`](./vimagecvimageformat.md). The following code shows how you create a [`vImageConstCVImageFormat`](./vimageconstcvimageformat.md) representation of a [`vImageCVImageFormat`](./vimagecvimageformat.md) instance to pass to [`vImageCVImageFormat_GetChannelNames(_:)`](./vimagecvimageformat_getchannelnames%28_%29.md):

**Swift**:

```swift
let channelNames = withUnsafeBytes(of: cvImageFormat) { bytes in
    let format = bytes.assumingMemoryBound(
        to: vImageConstCVImageFormat.self).first!
    
    return vImageCVImageFormat_GetChannelNames(format)
}
```

**Objective-C**:

```objc
vImageConstCVImageFormatRef constFormat = cvImageFormat;

const vImageBufferTypeCode *channelNames =
    vImageCVImageFormat_GetChannelNames(constFormat);
```

## Parameters

- `format`: The Core Video image format to query.

## See Also

### Related Documentation
- [var channels: [vImage.BufferType]](./vimagecvimageformat/channels.md)
  The channels of the Core Video image format.
### Querying and setting channel information
- [func vImageCVImageFormat_GetChannelCount(vImageConstCVImageFormat) -> UInt32](./vimagecvimageformat_getchannelcount%28_%29.md)
  Returns the number of channels, including alpha, for the Core Video image format.
- [func vImageCVImageFormat_GetChannelDescription(vImageConstCVImageFormat, vImageBufferTypeCode) -> UnsafePointer<vImageChannelDescription>!](./vimagecvimageformat_getchanneldescription%28_,_%29.md)
  Returns the channel description for a particular channel type.
- [func vImageCVImageFormat_CopyChannelDescription(vImageCVImageFormat, UnsafePointer<vImageChannelDescription>, vImageBufferTypeCode) -> vImage_Error](./vimagecvimageformat_copychanneldescription%28_,_,_%29.md)
  Copies the channel description for a particular channel type to an image format.
- [struct vImageChannelDescription](./vimagechanneldescription.md)
  A description of the range and clamp limits for a pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_getchannelnames(_:))*