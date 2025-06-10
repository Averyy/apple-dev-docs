# MDLMeshBufferType

**Framework**: Model I/O  
**Kind**: enum

Options for the content of a mesh buffer, used by the [`type`](mdlmeshbuffer/type.md) property and by [`MDLMeshBufferAllocator`](mdlmeshbufferallocator.md) methods for creating buffers.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
enum MDLMeshBufferType
```

## Topics

### Constants
- [MDLMeshBufferType.vertex](mdlmeshbuffertype/vertex.md)
  The buffer contains per-vertex data for one or more vertex attributes of a [`MDLMesh`](mdlmesh.md) object.
- [MDLMeshBufferType.index](mdlmeshbuffertype/index.md)
  The buffer contains index data for a [`MDLSubmesh`](mdlsubmesh.md) object.
### Enumeration Cases
- [MDLMeshBufferType.custom](mdlmeshbuffertype/custom.md)
### Initializers
- [init?(rawValue: UInt)](mdlmeshbuffertype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbuffertype)*