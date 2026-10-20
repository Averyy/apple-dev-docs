# newBuffer(from:length:type:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (id<MDLMeshBuffer>) newBufferFromZone:(id<MDLMeshBufferZone>) zone length:(NSUInteger) length type:(MDLMeshBufferType) type;
```

#### Return Value

A new memory buffer for mesh data.

#### Discussion

Use this method when making multiple related allocations that should share the same memory pool.

The concrete class implementing this protocol determines the initial contents of the buffer.

## Parameters

- `zone`: A pool of memory for related allocations, as returned by the [`newZone(_:)`](./newzone%28_%29.md) method.
- `length`: The size, in bytes, of the buffer to create.
- `type`: Use [`MDLMeshBufferType.vertex`](../mdlmeshbuffertype/vertex.md) to create a buffer for a mesh’s vertex attribute data, or [`MDLMeshBufferType.index`](../mdlmeshbuffertype/index.md) to create a buffer for a submesh’s index data.

## See Also

### Allocating Mesh Buffers
- [func newZone(Int) -> any MDLMeshBufferZone](./newzone%28_%29.md)
  Creates a zone for related memory allocations.
- [func newZoneForBuffers(withSize: [NSNumber], andType: [NSNumber]) -> any MDLMeshBufferZone](./newzoneforbuffers%28withsize,andtype%29.md)
  Creates a zone large enough to fit the specified group of allocation sizes.
- [func newBuffer(Int, type: MDLMeshBufferType) -> any MDLMeshBuffer](./newbuffer%28_,type%29.md)
  Creates a new buffer of the specified length.
- [func newBuffer(with: Data, type: MDLMeshBufferType) -> any MDLMeshBuffer](./newbuffer%28with,type%29.md)
  Creates a new buffer containing the specified data.
- [func newBuffer(from: (any MDLMeshBufferZone)?, data: Data, type: MDLMeshBufferType) -> (any MDLMeshBuffer)?](./newbuffer%28from,data,type%29.md)
  Creates a new buffer containing the specified data in the specified zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbufferallocator/newbuffer(from:length:type:))*