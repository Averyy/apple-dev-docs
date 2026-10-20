# MDLMeshBufferType

**Framework**: Model I/O  
**Kind**: enum  
**Role**: Enumeration

Options for the content of a mesh buffer, used by the [`type`](./mdlmeshbuffer/type.md) property and by [`MDLMeshBufferAllocator`](./mdlmeshbufferallocator.md) methods for creating buffers.

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

```c
enum MDLMeshBufferType : NSUInteger;
```

## Topics

### Constants
- [MDLMeshBufferType.vertex](./mdlmeshbuffertype/vertex.md)
  The buffer contains per-vertex data for one or more vertex attributes of a [`MDLMesh`](./mdlmesh.md) object.
- [MDLMeshBufferType.index](./mdlmeshbuffertype/index.md)
  The buffer contains index data for a [`MDLSubmesh`](./mdlsubmesh.md) object.
### Enumeration Cases
- [MDLMeshBufferType.custom](./mdlmeshbuffertype/custom.md)
### Initializers
- [init?(rawValue: UInt)](./mdlmeshbuffertype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbuffertype)*