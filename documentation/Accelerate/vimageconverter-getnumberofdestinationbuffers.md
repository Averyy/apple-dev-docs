# vImageConverter_GetNumberOfDestinationBuffers(_:)

**Framework**: Accelerate  
**Kind**: func

Returns the number of destination buffers written to by the converter.

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
func vImageConverter_GetNumberOfDestinationBuffers(_ converter: vImageConverter) -> UInt
```

#### Return Value

The number of destination buffers.

#### Discussion

This function is for video formats that are planar data formats with data in more than one plane.

## Parameters

- `converter`: A valid converter to query the number of source buffers.

## See Also

- [func vImageConverter_MustOperateOutOfPlace(vImageConverter, UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, vImage_Flags) -> vImage_Error](vimageconverter_mustoperateoutofplace(_:_:_:_:).md)
  Determines whether a converter is capable of operating in place.
- [func vImageConverter_GetSourceBufferOrder(vImageConverter) -> UnsafePointer<vImageBufferTypeCode>!](vimageconverter_getsourcebufferorder(_:).md)
  Returns a list of vImage source buffer channel names, specifying the order of planes.
- [func vImageConverter_GetDestinationBufferOrder(vImageConverter) -> UnsafePointer<vImageBufferTypeCode>!](vimageconverter_getdestinationbufferorder(_:).md)
  Returns a list of vImage destination buffer channel names, specifying the order of planes.
- [func vImageConverter_GetNumberOfSourceBuffers(vImageConverter) -> UInt](vimageconverter_getnumberofsourcebuffers(_:).md)
  Returns the number of source buffers consumed by the converter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconverter_getnumberofdestinationbuffers(_:))*