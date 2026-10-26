# Conversion Functions

**Framework**: MetalKit  
**Role**: API Collection

Convert between Metal and Model I/O vertex representations.

## Topics

### Converting Between Model I/O and Metal Vertex Descriptors
- [func MTKMetalVertexDescriptorFromModelIO(MDLVertexDescriptor) -> MTLVertexDescriptor?](./mtkmetalvertexdescriptorfrommodelio%28_%29.md)
  Returns a partially converted Metal vertex descriptor.
- [func MTKModelIOVertexDescriptorFromMetal(MTLVertexDescriptor) -> MDLVertexDescriptor](./mtkmodeliovertexdescriptorfrommetal%28_%29.md)
  Returns a partially converted Model I/O vertex descriptor.
- [MTKMetalVertexDescriptorFromModelIOWithError](./mtkmetalvertexdescriptorfrommodeliowitherror.md)
  Returns a partially converted Metal vertex descriptor, reporting any error that occurs.
- [MTKModelIOVertexDescriptorFromMetalWithError](./mtkmodeliovertexdescriptorfrommetalwitherror.md)
  Returns a partially converted Model I/O vertex descriptor, reporting any error that occurs.
### Converting Between Model I/O and Metal Vertex Formats
- [func MTKMetalVertexFormatFromModelIO(MDLVertexFormat) -> MTLVertexFormat](./mtkmetalvertexformatfrommodelio%28_%29.md)
  Returns a converted Metal vertex format.
- [func MTKModelIOVertexFormatFromMetal(MTLVertexFormat) -> MDLVertexFormat](./mtkmodeliovertexformatfrommetal%28_%29.md)
  Returns a converted Model I/O vertex format.

## See Also

### Model Handling
- [class MTKMesh](./mtkmesh.md)
  A container for the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKMeshBuffer](./mtkmeshbuffer.md)
  A buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKMeshBufferAllocator](./mtkmeshbufferallocator.md)
  An interface for allocating a MetalKit buffer that backs the vertex data of a Model I/O mesh, suitable for use in a Metal app.
- [class MTKSubmesh](./mtksubmesh.md)
  A container for the index data of a Model I/O submesh, suitable for use in a Metal app.
- [Model Errors](./model-errors.md)
  Learn about errors thrown by model handling methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/conversion-functions)*