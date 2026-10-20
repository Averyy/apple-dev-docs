# newZoneForBuffers(withSize:andType:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a zone large enough to fit the specified group of allocation sizes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func newZoneForBuffers(withSize sizes: [NSNumber], andType types: [NSNumber]) -> any MDLMeshBufferZone
```

```objc
- (id<MDLMeshBufferZone>) newZoneForBuffersWithSize:(NSArray<NSNumber *> *) sizes andType:(NSArray<NSNumber *> *) types;
```

#### Return Value

A new memory zone.

#### Discussion

Objects implementing the [`MDLMeshBufferZone`](../mdlmeshbufferzone.md) protocol describe a logical pool of memory for allocation of related buffers. The actual class of buffer zone objects vended by an allocator may be private.

This method creates a zone with enough capacity to allocate buffers with the sizes and types specified, taking into account any alignment restrictions necessary to use these buffers.

## Parameters

- `sizes`: An array of integers, each the length in bytes of an allocation to be made later.
- `types`: An array of integers, each the [`MDLMeshBufferType`](../mdlmeshbuffertype.md) value corresponding to an allocation described in the `sizes` array.

## See Also

### Allocating Mesh Buffers
- [func newZone(Int) -> any MDLMeshBufferZone](./newzone%28_%29.md)
  Creates a zone for related memory allocations.
- [func newBuffer(Int, type: MDLMeshBufferType) -> any MDLMeshBuffer](./newbuffer%28_,type%29.md)
  Creates a new buffer of the specified length.
- [func newBuffer(from: (any MDLMeshBufferZone)?, length: Int, type: MDLMeshBufferType) -> (any MDLMeshBuffer)?](./newbuffer%28from,length,type%29.md)
  Creates a new buffer of the specified length in the specified zone.
- [func newBuffer(with: Data, type: MDLMeshBufferType) -> any MDLMeshBuffer](./newbuffer%28with,type%29.md)
  Creates a new buffer containing the specified data.
- [func newBuffer(from: (any MDLMeshBufferZone)?, data: Data, type: MDLMeshBufferType) -> (any MDLMeshBuffer)?](./newbuffer%28from,data,type%29.md)
  Creates a new buffer containing the specified data in the specified zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbufferallocator/newzoneforbuffers(withsize:andtype:))*