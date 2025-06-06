# allocator

**Framework**: MetalKit  
**Kind**: property

The allocator object used to create this mesh buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var allocator: MTKMeshBufferAllocator { get }
```

#### Discussion

The allocator uses Model I/O for copy and re-layout operations, such as when a new vertex descriptor is applied to an existing vertex buffer.

## See Also

- [var type: MDLMeshBufferType](mtkmeshbuffer/type.md)
  The type of data contained in the originating Model I/O buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmeshbuffer/allocator)*