# type

**Framework**: MetalKit  
**Kind**: property

The type of data contained in the originating Model I/O buffer.

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

A [`MDLMeshBuffer`](https://developer.apple.com/documentation/ModelIO/MDLMeshBuffer) object can contain Model I/O mesh vertex data or submesh index data.

## See Also

- [var allocator: MTKMeshBufferAllocator](mtkmeshbuffer/allocator.md)
  The allocator object used to create this mesh buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmeshbuffer/type)*