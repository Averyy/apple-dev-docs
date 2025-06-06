# MTKModelIOVertexDescriptorFromMetal(_:)

**Framework**: MetalKit  
**Kind**: func

Returns a partially converted Model I/O vertex descriptor.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MTKModelIOVertexDescriptorFromMetal(_ metalDescriptor: MTLVertexDescriptor) -> MDLVertexDescriptor
```

#### Return Value

A Model I/O vertex descriptor object.

#### Discussion

This function is equivalent to the [`MTKModelIOVertexDescriptorFromMetalWithError`](mtkmodeliovertexdescriptorfrommetalwitherror.md) function, but does not report errors.

## Parameters

- `metalDescriptor`: A Metal vertex descriptor to convert from.

## See Also

- [func MTKMetalVertexDescriptorFromModelIO(MDLVertexDescriptor) -> MTLVertexDescriptor?](mtkmetalvertexdescriptorfrommodelio(_:).md)
  Returns a partially converted Metal vertex descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmodeliovertexdescriptorfrommetal(_:))*