# MTKMeshBuffer

**Framework**: MetalKit  
**Kind**: class  
**Role**: Class

A buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MTKMeshBuffer
```

```objc
@interface MTKMeshBuffer : NSObject
```

## Topics

### Originating Objects
- [var allocator: MTKMeshBufferAllocator](./mtkmeshbuffer/allocator.md)
  The allocator object used to create this mesh buffer.
- [var type: MDLMeshBufferType](./mtkmeshbuffer/type.md)
  The type of data contained in the originating Model I/O buffer.
### Metal Buffer Properties
- [var buffer: any MTLBuffer](./mtkmeshbuffer/buffer.md)
  The Metal buffer backing all vertex and index data.
- [var length: Int](./mtkmeshbuffer/length.md)
  The logical size of the Metal buffer, in bytes.
- [var offset: Int](./mtkmeshbuffer/offset.md)
  The byte offset of the data within the Metal buffer.
### Instance Methods
- [func zone() -> (any MDLMeshBufferZone)?](./mtkmeshbuffer/zone%28%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MDLMeshBuffer](../ModelIO/mdlmeshbuffer.md)
- [MDLNamed](../ModelIO/mdlnamed.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Model Handling
- [class MTKMesh](./mtkmesh.md)
  A container for the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKMeshBufferAllocator](./mtkmeshbufferallocator.md)
  An interface for allocating a MetalKit buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKSubmesh](./mtksubmesh.md)
  A container for the index data of a Model I/O submesh, suitable for use in a Metal app.
- [Conversion Functions](./conversion-functions.md)
  Convert between Metal and Model I/O vertex representations.
- [Model Errors](./model-errors.md)
  Learn about errors thrown by model handling methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmeshbuffer)*