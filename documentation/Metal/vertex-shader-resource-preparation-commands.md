# Vertex shader resource preparation commands

**Framework**: Metal

Assign resources to vertex shaders, including buffers, textures, acceleration structures, sampler states, and function tables.

#### Overview

Vertex shaders share argument tables for each resource type, such as buffers, textures, and sampler states. Each shader type has its own argument tables, separate from vertex shaders and other shader types.

## Topics

### Assigning buffers
- [func setVertexBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlrendercommandencoder/setvertexbuffer(_:offset:index:).md)
  Assigns a buffer to an entry in the vertex shader argument table.
- [func setVertexBuffer((any MTLBuffer)?, offset: Int, attributeStride: Int, index: Int)](mtlrendercommandencoder/setvertexbuffer(_:offset:attributestride:index:).md)
- [func setVertexBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlrendercommandencoder/setvertexbuffers(_:offsets:range:).md)
  Assigns multiple buffers to a range of entries in the vertex shader argument table.
- [func setVertexBuffers([(any MTLBuffer)?], offsets: [Int], attributeStrides: [Int], range: Range<Int>)](mtlrendercommandencoder/setvertexbuffers(_:offsets:attributestrides:range:).md)
- [func setVertexBytes(UnsafeRawPointer, length: Int, index: Int)](mtlrendercommandencoder/setvertexbytes(_:length:index:).md)
  Creates a buffer from bytes and assigns it to an entry in the vertex shader argument table.
- [func setVertexBytes(UnsafeRawPointer, length: Int, attributeStride: Int, index: Int)](mtlrendercommandencoder/setvertexbytes(_:length:attributestride:index:).md)
- [func setVertexBufferOffset(Int, index: Int)](mtlrendercommandencoder/setvertexbufferoffset(_:index:).md)
  Updates an entry in the vertex shader argument table with a new location within the entry’s current buffer.
- [func setVertexBufferOffset(offset: Int, attributeStride: Int, index: Int)](mtlrendercommandencoder/setvertexbufferoffset(offset:attributestride:index:).md)
### Assigning textures
- [func setVertexTexture((any MTLTexture)?, index: Int)](mtlrendercommandencoder/setvertextexture(_:index:).md)
  Assigns a texture to an entry in the vertex shader argument table.
- [func setVertexTextures([(any MTLTexture)?], range: Range<Int>)](mtlrendercommandencoder/setvertextextures(_:range:).md)
  Assigns multiple textures to a range of entries in the vertex shader argument table.
### Assigning sampler states
- [func setVertexSamplerState((any MTLSamplerState)?, index: Int)](mtlrendercommandencoder/setvertexsamplerstate(_:index:).md)
  Assigns a sampler state to an entry in the vertex shader argument table.
- [func setVertexSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](mtlrendercommandencoder/setvertexsamplerstate(_:lodminclamp:lodmaxclamp:index:).md)
  Assigns a sampler state and clamp values to an entry in the vertex shader argument table.
- [func setVertexSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](mtlrendercommandencoder/setvertexsamplerstates(_:range:).md)
  Assigns multiple sampler states to a range of entries in the vertex shader argument table.
- [func setVertexSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](mtlrendercommandencoder/setvertexsamplerstates(_:lodminclamps:lodmaxclamps:range:).md)
  Assigns multiple sampler states and clamp values to a range of entries in the vertex shader argument table.
### Assigning acceleration structures
- [func setVertexAccelerationStructure((any MTLAccelerationStructure)?, bufferIndex: Int)](mtlrendercommandencoder/setvertexaccelerationstructure(_:bufferindex:).md)
  Assigns an acceleration structure to an entry in the vertex shader argument table.
### Assigning visible function tables
- [func setVertexVisibleFunctionTable((any MTLVisibleFunctionTable)?, bufferIndex: Int)](mtlrendercommandencoder/setvertexvisiblefunctiontable(_:bufferindex:).md)
  Assigns a visible function table to an entry in the vertex shader argument table.
- [func setVertexVisibleFunctionTables([(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)](mtlrendercommandencoder/setvertexvisiblefunctiontables(_:bufferrange:).md)
  Assigns multiple visible function tables to a range of entries in the vertex shader argument table.
### Assigning intersection function tables
- [func setVertexIntersectionFunctionTable((any MTLIntersectionFunctionTable)?, bufferIndex: Int)](mtlrendercommandencoder/setvertexintersectionfunctiontable(_:bufferindex:).md)
  Assigns an intersection function table to an entry in the vertex shader argument table.
- [func setVertexIntersectionFunctionTables([(any MTLIntersectionFunctionTable)?], bufferRange: Range<Int>)](mtlrendercommandencoder/setvertexintersectionfunctiontables(_:bufferrange:).md)
  Assigns multiple intersection function tables to a range of entries in the vertex shader argument table.

## See Also

- [Mesh and object shader resource preparation commands](mesh-and-object-shader-resource-preparation-commands.md)
  Assign resources to mesh and object shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Fragment shader resource preparation commands](fragment-shader-resource-preparation-commands.md)
  Assign resources to fragment shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Tile shaders resource preparation commands](tile-shaders-resource-preparation-commands.md)
  Assign resources to tile shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Argument buffer resource preparation commands](argument-buffer-resource-preparation-commands.md)
  Load individual resources and multiple resources within a heap into GPU memory so that they’re available to shaders through argument buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/vertex-shader-resource-preparation-commands)*