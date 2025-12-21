# Mesh and object shader resource preparation commands

**Framework**: Metal

Assign resources to mesh and object shaders, including buffers, textures, acceleration structures, sampler states, and function tables.

#### Overview

Mesh shaders share argument tables for each resource type, such as buffers, textures, and sampler states. Object shaders share their own separate argument tables, distinct from mesh shaders and other shader types.

## Topics

### Assigning buffers for object shaders
- [func setObjectBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlrendercommandencoder/setobjectbuffer(_:offset:index:).md)
  Assigns a buffer to an entry in the object shader argument table.
- [func setObjectBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlrendercommandencoder/setobjectbuffers(_:offsets:range:).md)
  Assigns multiple buffers to a range of entries in the object shader argument table.
- [func setObjectBytes(UnsafeRawPointer, length: Int, index: Int)](mtlrendercommandencoder/setobjectbytes(_:length:index:).md)
  Creates a buffer from bytes and assigns it to an entry in the object shader argument table.
- [func setObjectBufferOffset(Int, index: Int)](mtlrendercommandencoder/setobjectbufferoffset(_:index:).md)
  Updates an entry in the object shader argument table with a new location within the entry’s current buffer.
### Assigning textures for object shaders
- [func setObjectTexture((any MTLTexture)?, index: Int)](mtlrendercommandencoder/setobjecttexture(_:index:).md)
  Assigns a texture to an entry in the object shader argument table.
- [func setObjectTextures([(any MTLTexture)?], range: Range<Int>)](mtlrendercommandencoder/setobjecttextures(_:range:).md)
  Assigns multiple textures to a range of entries in the object shader argument table.
### Assigning sampler states for object shaders
- [func setObjectSamplerState((any MTLSamplerState)?, index: Int)](mtlrendercommandencoder/setobjectsamplerstate(_:index:).md)
  Assigns a sampler state to an entry in the object shader argument table.
- [func setObjectSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](mtlrendercommandencoder/setobjectsamplerstate(_:lodminclamp:lodmaxclamp:index:).md)
  Assigns a sampler state and clamp values to an entry in the object shader argument table.
- [func setObjectSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](mtlrendercommandencoder/setobjectsamplerstates(_:range:).md)
  Assigns multiple sampler states to a range of entries in the object shader argument table.
- [func setObjectSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](mtlrendercommandencoder/setobjectsamplerstates(_:lodminclamps:lodmaxclamps:range:).md)
  Assigns multiple sampler states and clamp values to a range of entries in the object shader argument table.
### Assigning buffers for mesh shaders
- [func setMeshBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlrendercommandencoder/setmeshbuffer(_:offset:index:).md)
  Assigns a buffer to an entry in the mesh shader argument table.
- [func setMeshBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlrendercommandencoder/setmeshbuffers(_:offsets:range:).md)
  Assigns multiple buffers to a range of entries in the mesh shader argument table.
- [func setMeshBytes(UnsafeRawPointer, length: Int, index: Int)](mtlrendercommandencoder/setmeshbytes(_:length:index:).md)
  Creates a buffer from bytes and assigns it to an entry in the mesh shader argument table.
- [func setMeshBufferOffset(Int, index: Int)](mtlrendercommandencoder/setmeshbufferoffset(_:index:).md)
  Updates an entry in the mesh shader argument table with a new location within the entry’s current buffer.
### Assigning textures for mesh shaders
- [func setMeshTexture((any MTLTexture)?, index: Int)](mtlrendercommandencoder/setmeshtexture(_:index:).md)
  Assigns a texture to an entry in the mesh shader argument table.
- [func setMeshTextures([(any MTLTexture)?], range: Range<Int>)](mtlrendercommandencoder/setmeshtextures(_:range:).md)
  Assigns multiple textures to a range of entries in the mesh shader argument table.
### Assigning sampler states for mesh shaders
- [func setMeshSamplerState((any MTLSamplerState)?, index: Int)](mtlrendercommandencoder/setmeshsamplerstate(_:index:).md)
  Assigns a sampler state to an entry in the mesh shader argument table.
- [func setMeshSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](mtlrendercommandencoder/setmeshsamplerstate(_:lodminclamp:lodmaxclamp:index:).md)
  Assigns a sampler state and clamp values to an entry in the mesh shader argument table.
- [func setMeshSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](mtlrendercommandencoder/setmeshsamplerstates(_:range:).md)
  Assigns multiple sampler states to a range of entries in the mesh shader argument table.
- [func setMeshSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](mtlrendercommandencoder/setmeshsamplerstates(_:lodminclamps:lodmaxclamps:range:).md)
  Assigns multiple sampler states and clamp values to a range of entries in the mesh shader argument table.

## See Also

- [Vertex shader resource preparation commands](vertex-shader-resource-preparation-commands.md)
  Assign resources to vertex shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Fragment shader resource preparation commands](fragment-shader-resource-preparation-commands.md)
  Assign resources to fragment shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Tile shaders resource preparation commands](tile-shaders-resource-preparation-commands.md)
  Assign resources to tile shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Argument buffer resource preparation commands](argument-buffer-resource-preparation-commands.md)
  Load individual resources and multiple resources within a heap into GPU memory so that they’re available to shaders through argument buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mesh-and-object-shader-resource-preparation-commands)*