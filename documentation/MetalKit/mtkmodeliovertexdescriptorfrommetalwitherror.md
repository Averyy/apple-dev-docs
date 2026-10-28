# MTKModelIOVertexDescriptorFromMetalWithError

**Framework**: MetalKit  
**Kind**: func  
**Role**: Function

Returns a partially converted Model I/O vertex descriptor, reporting any error that occurs.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```c
extern MDLVertexDescriptor *MTKModelIOVertexDescriptorFromMetalWithError(MTLVertexDescriptor *metalDescriptor, NSError **error);
```

## Return Value

A Model I/O vertex descriptor object.

## Discussion

This function can only set vertex format, offset, buffer index, and stride information in the resulting MDLMutableVertexDescriptor object. It does not add any semantic information such as attribute names. Names must be set in the returned MDLMutableVertexDescriptor object before it can be applied to a Model I/O mesh.

## Parameters

- `metalDescriptor`: A Metal vertex descriptor to convert from.
- `error`: A pointer to an [`NSError`](../Foundation/nserror.md) object if an error occurred, or `nil` if conversion succeeded.

## See Also

### Converting Between Model I/O and Metal Vertex Descriptors
- [func MTKMetalVertexDescriptorFromModelIO(MDLVertexDescriptor) -> MTLVertexDescriptor?](./mtkmetalvertexdescriptorfrommodelio%28_%29.md)
  Returns a partially converted Metal vertex descriptor.
- [MTKMetalVertexDescriptorFromModelIOWithError](./mtkmetalvertexdescriptorfrommodeliowitherror.md)
  Returns a partially converted Metal vertex descriptor, reporting any error that occurs.
- [func MTKModelIOVertexDescriptorFromMetal(MTLVertexDescriptor) -> MDLVertexDescriptor](./mtkmodeliovertexdescriptorfrommetal%28_%29.md)
  Returns a partially converted Model I/O vertex descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmodeliovertexdescriptorfrommetalwitherror)*