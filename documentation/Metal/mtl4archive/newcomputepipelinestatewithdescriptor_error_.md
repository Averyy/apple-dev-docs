# newComputePipelineStateWithDescriptor:error:

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Creates a compute pipeline state from the archive with a descriptor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (id<MTLComputePipelineState>) newComputePipelineStateWithDescriptor:(MTL4ComputePipelineDescriptor *) descriptor error:(NSError **) error;
```

## Return Value

A compute pipeline state if the method succeeds, otherwise `nil`.

## Parameters

- `descriptor`: A compute pipeline descriptor.
- `error`: On return, if the method fails, a pointer to an error information instance; otherwise `nil`.

## See Also

### Creating compute pipeline states
- [- newComputePipelineStateWithDescriptor:dynamicLinkingDescriptor:error:](./newcomputepipelinestatewithdescriptor_dynamiclinkingdescriptor_error_.md)
  Creates a compute pipeline state from the archive with a compute descriptor and a dynamic linking descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4archive/newcomputepipelinestatewithdescriptor:error:)*