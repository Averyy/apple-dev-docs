# vImageConverter_GetNumberOfSourceBuffers(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns the number of source buffers consumed by the converter.

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
func vImageConverter_GetNumberOfSourceBuffers(_ converter: vImageConverter) -> UInt
```

```c
unsigned long vImageConverter_GetNumberOfSourceBuffers(vImageConverterRef const converter);
```

#### Return Value

The number of source buffers.

#### Discussion

This function is for video formats that are planar data formats with data in more than one plane.

## Parameters

- `converter`: A valid converter to query the number of source buffers.

## See Also

### Querying a converter’s properties
- [func vImageConverter_MustOperateOutOfPlace(vImageConverter, UnsafePointer<vImage_Buffer>!, UnsafePointer<vImage_Buffer>!, vImage_Flags) -> vImage_Error](./vimageconverter_mustoperateoutofplace%28_,_,_,_%29.md)
  Determines whether a converter is capable of operating in place.
- [func vImageConverter_GetSourceBufferOrder(vImageConverter) -> UnsafePointer<vImageBufferTypeCode>!](./vimageconverter_getsourcebufferorder%28_%29.md)
  Returns a list of vImage source buffer channel names, specifying the order of planes.
- [func vImageConverter_GetDestinationBufferOrder(vImageConverter) -> UnsafePointer<vImageBufferTypeCode>!](./vimageconverter_getdestinationbufferorder%28_%29.md)
  Returns a list of vImage destination buffer channel names, specifying the order of planes.
- [func vImageConverter_GetNumberOfDestinationBuffers(vImageConverter) -> UInt](./vimageconverter_getnumberofdestinationbuffers%28_%29.md)
  Returns the number of destination buffers written to by the converter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconverter_getnumberofsourcebuffers(_:))*