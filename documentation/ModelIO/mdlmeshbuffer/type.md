# type

**Framework**: Model I/O  
**Kind**: property  
**Required**: Yes

The type of data contained in a buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var type: MDLMeshBufferType { get }
```

#### Discussion

A buffer can contain per-vertex data for one or more vertex attributes of a [`MDLMesh`](mdlmesh.md) object ([`MDLMeshBufferType.vertex`](mdlmeshbuffertype/vertex.md)), or index data for a [`MDLSubmesh`](mdlsubmesh.md) object ([`MDLMeshBufferType.index`](mdlmeshbuffertype/index.md)).

## See Also

- [var allocator: any MDLMeshBufferAllocator](mdlmeshbuffer/allocator.md)
  The allocator object that created the buffer.
- [var zone: any MDLMeshBufferZone](mdlmeshbuffer/zone.md)
  The memory pool from which the buffer was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbuffer/type)*