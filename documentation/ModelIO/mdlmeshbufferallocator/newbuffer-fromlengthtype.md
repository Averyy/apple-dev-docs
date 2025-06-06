# newBuffer(from:length:type:)

**Framework**: Model I/O  
**Kind**: method  
**Required**: Yes

Creates a new buffer of the specified length in the specified zone.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func newBuffer(from zone: (any MDLMeshBufferZone)?, length: Int, type: MDLMeshBufferType) -> (any MDLMeshBuffer)?
```

#### Return Value

A new memory buffer for mesh data.

#### Discussion

Use this method when making multiple related allocations that should share the same memory pool.

The concrete class implementing this protocol determines the initial contents of the buffer.

## Parameters

- `zone`: A pool of memory for related allocations, as returned by the   method.
- `length`: The size, in bytes, of the buffer to create.
- `type`: Use   to create a buffer for a mesh’s vertex attribute data, or   to create a buffer for a submesh’s index data.

## See Also

- [func newZone(Int) -> any MDLMeshBufferZone](mdlmeshbufferallocator/newzone(_:).md)
  Creates a zone for related memory allocations.
- [func newZoneForBuffers(withSize: [NSNumber], andType: [NSNumber]) -> any MDLMeshBufferZone](mdlmeshbufferallocator/newzoneforbuffers(withsize:andtype:).md)
  Creates a zone large enough to fit the specified group of allocation sizes.
- [func newBuffer(Int, type: MDLMeshBufferType) -> any MDLMeshBuffer](mdlmeshbufferallocator/newbuffer(_:type:).md)
  Creates a new buffer of the specified length.
- [func newBuffer(with: Data, type: MDLMeshBufferType) -> any MDLMeshBuffer](mdlmeshbufferallocator/newbuffer(with:type:).md)
  Creates a new buffer containing the specified data.
- [func newBuffer(from: (any MDLMeshBufferZone)?, data: Data, type: MDLMeshBufferType) -> (any MDLMeshBuffer)?](mdlmeshbufferallocator/newbuffer(from:data:type:).md)
  Creates a new buffer containing the specified data in the specified zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbufferallocator/newbuffer(from:length:type:))*