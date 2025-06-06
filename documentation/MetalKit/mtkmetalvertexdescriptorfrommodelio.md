# MTKMetalVertexDescriptorFromModelIO(_:)

**Framework**: MetalKit  
**Kind**: func

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

#### Return Value

A Metal vertex descriptor object.

#### Discussion

This function is equivalent to the [`MTKMetalVertexDescriptorFromModelIOWithError`](mtkmetalvertexdescriptorfrommodeliowitherror.md) function, but does not report errors.

## See Also

- [func MTKModelIOVertexDescriptorFromMetal(MTLVertexDescriptor) -> MDLVertexDescriptor](mtkmodeliovertexdescriptorfrommetal(_:).md)
  Returns a partially converted Model I/O vertex descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmetalvertexdescriptorfrommodelio(_:))*