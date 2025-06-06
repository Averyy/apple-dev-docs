# vImageCVImageFormat_GetChannelCount(_:)

**Framework**: Accelerate  
**Kind**: func

Returns the number of channels, including alpha, for the Core Video image format.

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
func vImageCVImageFormat_GetChannelCount(_ format: vImageConstCVImageFormat) -> UInt32
```

#### Return Value

The number of channels.

#### Discussion

This function returns the number of interleaved or planar channels.

The functions that create Core Video image formats, such as [`vImageCVImageFormat_CreateWithCVPixelBuffer(_:)`](vimagecvimageformat_createwithcvpixelbuffer(_:).md), return a [`vImageCVImageFormat`](vimagecvimageformat.md). The following code shows how you create a [`vImageConstCVImageFormat`](vimageconstcvimageformat.md) representation of a [`vImageCVImageFormat`](vimagecvimageformat.md) instance to pass to [`vImageCVImageFormat_GetChannelCount(_:)`](vimagecvimageformat_getchannelcount(_:).md):

```swift
let channelCount = withUnsafeBytes(of: cvImageFormat) { bytes in
    let format = bytes.assumingMemoryBound(
        to: vImageConstCVImageFormat.self).first!
    
    return vImageCVImageFormat_GetChannelCount(format)
}
```

## Parameters

- `format`: The Core Video image format to query.

## See Also

- [var channelCount: UInt32](vimagecvimageformat/channelcount.md)
  The number of channels, including alpha, for the Core Video image format.
- [func vImageCVImageFormat_GetChannelDescription(vImageConstCVImageFormat, vImageBufferTypeCode) -> UnsafePointer<vImageChannelDescription>!](vimagecvimageformat_getchanneldescription(_:_:).md)
  Returns the channel description for a particular channel type.
- [func vImageCVImageFormat_CopyChannelDescription(vImageCVImageFormat, UnsafePointer<vImageChannelDescription>, vImageBufferTypeCode) -> vImage_Error](vimagecvimageformat_copychanneldescription(_:_:_:).md)
  Copies the channel description for a particular channel type to an image format.
- [func vImageCVImageFormat_GetChannelNames(vImageConstCVImageFormat) -> UnsafePointer<vImageBufferTypeCode>!](vimagecvimageformat_getchannelnames(_:).md)
  Returns the names of the channels of a Core Video image format.
- [struct vImageChannelDescription](vimagechanneldescription.md)
  A description of the range and clamp limits for a pixel format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagecvimageformat_getchannelcount(_:))*