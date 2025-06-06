# zone

**Framework**: Model I/O  
**Kind**: property  
**Required**: Yes

The memory pool from which the buffer was created.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var zone: any MDLMeshBufferZone { get }
```

#### Discussion

Use the [`newBuffer(from:data:type:)`](mdlmeshbufferallocator/newbuffer(from:data:type:).md) or [`newBuffer(from:length:type:)`](mdlmeshbufferallocator/newbuffer(from:length:type:).md) method of an allocator to reserve memory in a shared pool for multiple related buffers.

## See Also

- [var allocator: any MDLMeshBufferAllocator](mdlmeshbuffer/allocator.md)
  The allocator object that created the buffer.
- [var type: MDLMeshBufferType](mdlmeshbuffer/type.md)
  The type of data contained in a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbuffer/zone)*