# MTKMeshBufferAllocator

**Framework**: MetalKit  
**Kind**: class

An interface for allocating a MetalKit buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class MTKMeshBufferAllocator
```

## Topics

### Initialization
- [init(device: any MTLDevice)](mtkmeshbufferallocator/init(device:).md)
  Initializes a new allocator object.
### Device
- [var device: any MTLDevice](mtkmeshbufferallocator/device.md)
  The device used to create Metal objects.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MDLMeshBufferAllocator](../ModelIO/MDLMeshBufferAllocator.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTKMesh](mtkmesh.md)
  A container for the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKMeshBuffer](mtkmeshbuffer.md)
  A buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKSubmesh](mtksubmesh.md)
  A container for the index data of a Model I/O submesh, suitable for use in a Metal app.
- [Conversion Functions](conversion-functions.md)
  Convert between Metal and Model I/O vertex representations.
- [Model Errors](model-errors.md)
  Learn about errors thrown by model handling methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmeshbufferallocator)*