# Conversion Functions

**Framework**: MetalKit

Convert between Metal and Model I/O vertex representations.

## Topics

### Converting Between Model I/O and Metal Vertex Descriptors
- [func MTKMetalVertexDescriptorFromModelIO(MDLVertexDescriptor) -> MTLVertexDescriptor?](mtkmetalvertexdescriptorfrommodelio(_:).md)
  Returns a partially converted Metal vertex descriptor.
- [func MTKModelIOVertexDescriptorFromMetal(MTLVertexDescriptor) -> MDLVertexDescriptor](mtkmodeliovertexdescriptorfrommetal(_:).md)
  Returns a partially converted Model I/O vertex descriptor.
### Converting Between Model I/O and Metal Vertex Formats
- [func MTKMetalVertexFormatFromModelIO(MDLVertexFormat) -> MTLVertexFormat](mtkmetalvertexformatfrommodelio(_:).md)
  Returns a converted Metal vertex format.
- [func MTKModelIOVertexFormatFromMetal(MTLVertexFormat) -> MDLVertexFormat](mtkmodeliovertexformatfrommetal(_:).md)
  Returns a converted Model I/O vertex format.

## See Also

- [class MTKMesh](mtkmesh.md)
  A container for the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKMeshBuffer](mtkmeshbuffer.md)
  A buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKMeshBufferAllocator](mtkmeshbufferallocator.md)
  An interface for allocating a MetalKit buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKSubmesh](mtksubmesh.md)
  A container for the index data of a Model I/O submesh, suitable for use in a Metal app.
- [Model Errors](model-errors.md)
  Learn about errors thrown by model handling methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/conversion-functions)*