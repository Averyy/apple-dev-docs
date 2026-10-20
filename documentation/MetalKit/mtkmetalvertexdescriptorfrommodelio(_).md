# MTKMetalVertexDescriptorFromModelIO(_:)

**Framework**: MetalKit  
**Kind**: func  
**Role**: Function

Returns a partially converted Metal vertex descriptor.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MTKMetalVertexDescriptorFromModelIO(_ modelIODescriptor: MDLVertexDescriptor) -> MTLVertexDescriptor?
```

```c
extern MTLVertexDescriptor *MTKMetalVertexDescriptorFromModelIO(MDLVertexDescriptor *modelIODescriptor);
```

#### Return Value

A Metal vertex descriptor object.

#### Discussion

This function is equivalent to the [`MTKMetalVertexDescriptorFromModelIOWithError`](./mtkmetalvertexdescriptorfrommodeliowitherror.md) function, but does not report errors.

## See Also

### Converting Between Model I/O and Metal Vertex Descriptors
- [func MTKModelIOVertexDescriptorFromMetal(MTLVertexDescriptor) -> MDLVertexDescriptor](./mtkmodeliovertexdescriptorfrommetal%28_%29.md)
  Returns a partially converted Model I/O vertex descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmetalvertexdescriptorfrommodelio(_:))*