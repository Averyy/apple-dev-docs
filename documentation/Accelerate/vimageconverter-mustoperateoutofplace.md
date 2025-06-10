# vImageConverter_MustOperateOutOfPlace(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Determines whether a converter is capable of operating in place.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 7.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageConverter_MustOperateOutOfPlace(_ converter: vImageConverter, _ srcs: UnsafePointer<vImage_Buffer>!, _ dests: UnsafePointer<vImage_Buffer>!, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md) if the conversion will work in place, [`kvImageOutOfPlaceOperationRequired`](kvimageoutofplaceoperationrequired.md) if the conversion requires out of place operation; otherwise, one of the error codes described in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

Some conversions work if the source and destination image buffer scanlines start at the same address. Others don’t; for those cases, you need to allocate additional storage to hold the destination buffer.

In-place operation is considered to mean `srcs[i].data = dests[i].data` and `srcs[i].rowBytes = dests[i].rowBytes`. Other styles of partial buffer overlap produce undefined behavior.

## Parameters

- `converter`: The converter to check to determine if it’s capable of operating in place.
- `srcs`: The list of source buffers you plan to use with  . This parameter may be  .
- `dests`: The list of destination buffers you plan to use with  . This parameter may be  .
- `flags`: The flags you’ll pass to  .

## See Also

- [func vImageConverter_GetSourceBufferOrder(vImageConverter) -> UnsafePointer<vImageBufferTypeCode>!](vimageconverter_getsourcebufferorder(_:).md)
  Returns a list of vImage source buffer channel names, specifying the order of planes.
- [func vImageConverter_GetDestinationBufferOrder(vImageConverter) -> UnsafePointer<vImageBufferTypeCode>!](vimageconverter_getdestinationbufferorder(_:).md)
  Returns a list of vImage destination buffer channel names, specifying the order of planes.
- [func vImageConverter_GetNumberOfSourceBuffers(vImageConverter) -> UInt](vimageconverter_getnumberofsourcebuffers(_:).md)
  Returns the number of source buffers consumed by the converter.
- [func vImageConverter_GetNumberOfDestinationBuffers(vImageConverter) -> UInt](vimageconverter_getnumberofdestinationbuffers(_:).md)
  Returns the number of destination buffers written to by the converter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconverter_mustoperateoutofplace(_:_:_:_:))*