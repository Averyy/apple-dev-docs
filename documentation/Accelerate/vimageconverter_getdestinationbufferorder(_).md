# vImageConverter_GetDestinationBufferOrder(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns a list of vImage destination buffer channel names, specifying the order of planes.

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
func vImageConverter_GetDestinationBufferOrder(_ converter: vImageConverter) -> UnsafePointer<vImageBufferTypeCode>!
```

```c
const vImageBufferTypeCode *vImageConverter_GetDestinationBufferOrder(vImageConverterRef converter);
```

#### Return Value

An array of buffer type codes (see [vImage Buffer Type Codes](./api-1399056-vimage-buffer-type-codes.md)) that ends with [`kvImageBufferTypeCode_EndOfList`](./kvimagebuffertypecode_endoflist.md).

#### Discussion

This function describes the identity of each buffer passed in the `dests` parameters of [`vImageConvert_AnyToAny(_:_:_:_:_:)`](./vimageconvert_anytoany%28_,_,_,_,_%29.md), so you can order the buffers correctly. It’s provided for informational purposes, to help you configure image processing pipelines to vImage that aren’t supported through more direct means.

## Parameters

- `converter`: A valid [`vImageConverter`](./vimageconverter.md) instance to query the destination buffer channel names and order of planes.

## See Also

### Querying a converter’s properties
- [func vImageConverter_MustOperateOutOfPlace(vImageConverter, UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, vImage_Flags) -> vImage_Error](./vimageconverter_mustoperateoutofplace%28_,_,_,_%29.md)
  Determines whether a converter is capable of operating in place.
- [func vImageConverter_GetSourceBufferOrder(vImageConverter) -> UnsafePointer<vImageBufferTypeCode>!](./vimageconverter_getsourcebufferorder%28_%29.md)
  Returns a list of vImage source buffer channel names, specifying the order of planes.
- [func vImageConverter_GetNumberOfSourceBuffers(vImageConverter) -> UInt](./vimageconverter_getnumberofsourcebuffers%28_%29.md)
  Returns the number of source buffers consumed by the converter.
- [func vImageConverter_GetNumberOfDestinationBuffers(vImageConverter) -> UInt](./vimageconverter_getnumberofdestinationbuffers%28_%29.md)
  Returns the number of destination buffers written to by the converter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconverter_getdestinationbufferorder(_:))*