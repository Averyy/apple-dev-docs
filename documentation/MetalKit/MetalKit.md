# MetalKit

**Framework**: MetalKit  
**Kind**: module

Build Metal apps quicker and easier using a common set of utility classes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Topics

### View Management
- [class MTKView](mtkview.md)
  A specialized view that creates, configures, and displays Metal objects.
- [protocol MTKViewDelegate](mtkviewdelegate.md)
  Methods for responding to a MetalKit view’s drawing and resizing events.
### Texture Loading
- [class MTKTextureLoader](mtktextureloader.md)
  An object that creates textures from existing data in common image formats.
### Model Handling
- [class MTKMesh](mtkmesh.md)
  A container for the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKMeshBuffer](mtkmeshbuffer.md)
  A buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKMeshBufferAllocator](mtkmeshbufferallocator.md)
  An interface for allocating a MetalKit buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKSubmesh](mtksubmesh.md)
  A container for the index data of a Model I/O submesh, suitable for use in a Metal app.
- [Conversion Functions](conversion-functions.md)
  Convert between Metal and Model I/O vertex representations.
- [Model Errors](model-errors.md)
  Learn about errors thrown by model handling methods.
### Reference
- [MetalKit Functions](metalkit-functions.md)
  The MetalKit framework defines helper functions that are used to efficiently interface with the Metal and Model I/O frameworks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MetalKit)*