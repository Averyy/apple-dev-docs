# newZone(_:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a zone for related memory allocations.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func newZone(_ capacity: Int) -> any MDLMeshBufferZone
```

```objc
- (id<MDLMeshBufferZone>) newZone:(NSUInteger) capacity;
```

## Return Value

A new memory zone.

## Discussion

Objects implementing the [`MDLMeshBufferZone`](../mdlmeshbufferzone.md) protocol describe a logical pool of memory for allocation of related buffers. The actual class of buffer zone objects vended by an allocator may be private.

## Parameters

- `capacity`: The capacity of the zone to be created.

## See Also

### Allocating Mesh Buffers
- [func newZoneForBuffers(withSize: [NSNumber], andType: [NSNumber]) -> any MDLMeshBufferZone](./newzoneforbuffers%28withsize,andtype%29.md)
  Creates a zone large enough to fit the specified group of allocation sizes.
- [func newBuffer(Int, type: MDLMeshBufferType) -> any MDLMeshBuffer](./newbuffer%28_,type%29.md)
  Creates a new buffer of the specified length.
- [func newBuffer(from: (any MDLMeshBufferZone)?, length: Int, type: MDLMeshBufferType) -> (any MDLMeshBuffer)?](./newbuffer%28from,length,type%29.md)
  Creates a new buffer of the specified length in the specified zone.
- [func newBuffer(with: Data, type: MDLMeshBufferType) -> any MDLMeshBuffer](./newbuffer%28with,type%29.md)
  Creates a new buffer containing the specified data.
- [func newBuffer(from: (any MDLMeshBufferZone)?, data: Data, type: MDLMeshBufferType) -> (any MDLMeshBuffer)?](./newbuffer%28from,data,type%29.md)
  Creates a new buffer containing the specified data in the specified zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbufferallocator/newzone(_:))*