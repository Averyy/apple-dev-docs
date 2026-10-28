# MTKMetalVertexDescriptorFromModelIOWithError

**Framework**: MetalKit  
**Kind**: func  
**Role**: Function

Returns a partially converted Metal vertex descriptor, reporting any error that occurs.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```c
extern MTLVertexDescriptor *MTKMetalVertexDescriptorFromModelIOWithError(MDLVertexDescriptor *modelIODescriptor, NSError **error);
```

## Return Value

A Metal vertex descriptor object.

## Discussion

This function can only set vertex format, offset, buffer index, and stride information in the resulting [`MTLVertexDescriptor`](../Metal/mtlvertexdescriptor.md) object. The function copies attributes one-for-one, so it is up to you to properly arrange the MDLMutableVertexDescriptor attributes in the correct order so that the resulting [`MTLVertexDescriptor`](../Metal/mtlvertexdescriptor.md) object can properly map mesh data to vertex shader inputs. Layout [`stepFunction`](../Metal/mtlvertexbufferlayoutdescriptor/stepfunction.md) and [`stepRate`](../Metal/mtlvertexbufferlayoutdescriptor/steprate.md) values for the resulting [`MTLVertexDescriptor`](../Metal/mtlvertexdescriptor.md) object must also be set by your application.

## Parameters

- `modelIODescriptor`: A Model I/O vertex descriptor to convert from.
- `error`: A pointer to an [`NSError`](../Foundation/nserror.md) object if an error occurred, or `nil` if conversion succeeded.

## See Also

### Converting Between Model I/O and Metal Vertex Descriptors
- [func MTKMetalVertexDescriptorFromModelIO(MDLVertexDescriptor) -> MTLVertexDescriptor?](./mtkmetalvertexdescriptorfrommodelio%28_%29.md)
  Returns a partially converted Metal vertex descriptor.
- [func MTKModelIOVertexDescriptorFromMetal(MTLVertexDescriptor) -> MDLVertexDescriptor](./mtkmodeliovertexdescriptorfrommetal%28_%29.md)
  Returns a partially converted Model I/O vertex descriptor.
- [MTKModelIOVertexDescriptorFromMetalWithError](./mtkmodeliovertexdescriptorfrommetalwitherror.md)
  Returns a partially converted Model I/O vertex descriptor, reporting any error that occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmetalvertexdescriptorfrommodeliowitherror)*