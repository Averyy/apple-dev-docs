# Tile shaders resource preparation commands

**Framework**: Metal

Assign resources to tile shaders, including buffers, textures, acceleration structures, sampler states, and function tables.

#### Overview

Tile shaders share argument tables for each resource type, such as buffers, textures, and sampler states. Each shader type has its own argument tables, separate from tile shaders and other shader types.

## Topics

### Assigning buffers
- [func setTileBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlrendercommandencoder/settilebuffer(_:offset:index:).md)
  Assigns a buffer to an entry in the tile shader argument table.
- [func setTileBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlrendercommandencoder/settilebuffers(_:offsets:range:).md)
  Assigns multiple buffers to a range of entries in the tile shader argument table.
- [func setTileBytes(UnsafeRawPointer, length: Int, index: Int)](mtlrendercommandencoder/settilebytes(_:length:index:).md)
  Creates a buffer from bytes and assigns it to an entry in the tile shader argument table.
- [func setTileBufferOffset(Int, index: Int)](mtlrendercommandencoder/settilebufferoffset(_:index:).md)
  Updates an entry in the tile shader argument table with a new location within the entry’s current buffer.
### Assigning textures
- [func setTileTexture((any MTLTexture)?, index: Int)](mtlrendercommandencoder/settiletexture(_:index:).md)
  Assigns a texture to an entry in the tile shader argument table.
- [func setTileTextures([(any MTLTexture)?], range: Range<Int>)](mtlrendercommandencoder/settiletextures(_:range:).md)
  Assigns multiple textures to a range of entries in the tile shader argument table.
### Assigning sampler states
- [func setTileSamplerState((any MTLSamplerState)?, index: Int)](mtlrendercommandencoder/settilesamplerstate(_:index:).md)
  Assigns a sampler state to an entry in the tile shader argument table.
- [func setTileSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](mtlrendercommandencoder/settilesamplerstate(_:lodminclamp:lodmaxclamp:index:).md)
  Assigns a sampler state and clamp values to an entry in the tile shader argument table.
- [func setTileSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](mtlrendercommandencoder/settilesamplerstates(_:range:).md)
  Assigns multiple sampler states to a range of entries in the tile shader argument table.
- [func setTileSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](mtlrendercommandencoder/settilesamplerstates(_:lodminclamps:lodmaxclamps:range:).md)
  Assigns multiple sampler states and clamp values to a range of entries in the tile shader argument table.
### Assigning acceleration structures
- [func setTileAccelerationStructure((any MTLAccelerationStructure)?, bufferIndex: Int)](mtlrendercommandencoder/settileaccelerationstructure(_:bufferindex:).md)
  Assigns an acceleration structure to an entry in the tile shader argument table.
### Assigning visible function tables
- [func setTileVisibleFunctionTable((any MTLVisibleFunctionTable)?, bufferIndex: Int)](mtlrendercommandencoder/settilevisiblefunctiontable(_:bufferindex:).md)
  Assigns a visible function table to an entry in the tile shader argument table.
- [func setTileVisibleFunctionTables([(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)](mtlrendercommandencoder/settilevisiblefunctiontables(_:bufferrange:).md)
  Assigns multiple visible function tables to a range of entries in the tile shader argument table.
### Assigning intersection function tables
- [func setTileIntersectionFunctionTable((any MTLIntersectionFunctionTable)?, bufferIndex: Int)](mtlrendercommandencoder/settileintersectionfunctiontable(_:bufferindex:).md)
  Assigns an intersection function table to an entry in the tile shader argument table.
- [func setTileIntersectionFunctionTables([(any MTLIntersectionFunctionTable)?], bufferRange: Range<Int>)](mtlrendercommandencoder/settileintersectionfunctiontables(_:bufferrange:).md)
  Assigns multiple intersection function tables to a range of entries in the tile shader argument table.

## See Also

- [Mesh and object shader resource preparation commands](mesh-and-object-shader-resource-preparation-commands.md)
  Assign resources to mesh and object shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Vertex shader resource preparation commands](vertex-shader-resource-preparation-commands.md)
  Assign resources to vertex shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Fragment shader resource preparation commands](fragment-shader-resource-preparation-commands.md)
  Assign resources to fragment shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Argument buffer resource preparation commands](argument-buffer-resource-preparation-commands.md)
  Load individual resources and multiple resources within a heap into GPU memory so that they’re available to shaders through argument buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/tile-shaders-resource-preparation-commands)*