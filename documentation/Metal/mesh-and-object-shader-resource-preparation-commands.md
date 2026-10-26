# Mesh and object shader resource preparation commands

**Framework**: Metal  
**Role**: API Collection

Assign resources to mesh and object shaders, including buffers, textures, acceleration structures, sampler states, and function tables.

#### Overview

Mesh shaders share argument tables for each resource type, such as buffers, textures, and sampler states. Object shaders share their own separate argument tables, distinct from mesh shaders and other shader types.

## Topics

### Assigning buffers for object shaders
- [func setObjectBuffer((any MTLBuffer)?, offset: Int, index: Int)](./mtlrendercommandencoder/setobjectbuffer%28_,offset,index%29.md)
  Assigns a buffer to an entry in the object shader argument table.
- [func setObjectBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](./mtlrendercommandencoder/setobjectbuffers%28_,offsets,range%29.md)
  Assigns multiple buffers to a range of entries in the object shader argument table.
- [func setObjectBytes(UnsafeRawPointer, length: Int, index: Int)](./mtlrendercommandencoder/setobjectbytes%28_,length,index%29.md)
  Creates a buffer from bytes and assigns it to an entry in the object shader argument table.
- [func setObjectBufferOffset(Int, index: Int)](./mtlrendercommandencoder/setobjectbufferoffset%28_,index%29.md)
  Updates an entry in the object shader argument table with a new location within the entry’s current buffer.
- [- setObjectBuffers:offsets:withRange:](./mtlrendercommandencoder/setobjectbuffers_offsets_withrange_.md)
  Encodes a command that assigns multiple buffers to a range of entries in the object shader argument table.
### Assigning textures for object shaders
- [func setObjectTexture((any MTLTexture)?, index: Int)](./mtlrendercommandencoder/setobjecttexture%28_,index%29.md)
  Assigns a texture to an entry in the object shader argument table.
- [func setObjectTextures([(any MTLTexture)?], range: Range<Int>)](./mtlrendercommandencoder/setobjecttextures%28_,range%29.md)
  Assigns multiple textures to a range of entries in the object shader argument table.
- [- setObjectTextures:withRange:](./mtlrendercommandencoder/setobjecttextures_withrange_.md)
  Assigns multiple textures to a range of entries in the object shader argument table.
### Assigning sampler states for object shaders
- [func setObjectSamplerState((any MTLSamplerState)?, index: Int)](./mtlrendercommandencoder/setobjectsamplerstate%28_,index%29.md)
  Assigns a sampler state to an entry in the object shader argument table.
- [func setObjectSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](./mtlrendercommandencoder/setobjectsamplerstate%28_,lodminclamp,lodmaxclamp,index%29.md)
  Assigns a sampler state and clamp values to an entry in the object shader argument table.
- [func setObjectSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](./mtlrendercommandencoder/setobjectsamplerstates%28_,range%29.md)
  Assigns multiple sampler states to a range of entries in the object shader argument table.
- [func setObjectSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](./mtlrendercommandencoder/setobjectsamplerstates%28_,lodminclamps,lodmaxclamps,range%29.md)
  Assigns multiple sampler states and clamp values to a range of entries in the object shader argument table.
- [- setObjectSamplerStates:withRange:](./mtlrendercommandencoder/setobjectsamplerstates_withrange_.md)
  Assigns multiple sampler states to a range of entries in the object shader argument table.
- [- setObjectSamplerStates:lodMinClamps:lodMaxClamps:withRange:](./mtlrendercommandencoder/setobjectsamplerstates_lodminclamps_lodmaxclamps_withrange_.md)
  Assigns multiple sampler states and clamp values to a range of entries in the object shader argument table.
### Assigning buffers for mesh shaders
- [func setMeshBuffer((any MTLBuffer)?, offset: Int, index: Int)](./mtlrendercommandencoder/setmeshbuffer%28_,offset,index%29.md)
  Assigns a buffer to an entry in the mesh shader argument table.
- [func setMeshBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](./mtlrendercommandencoder/setmeshbuffers%28_,offsets,range%29.md)
  Assigns multiple buffers to a range of entries in the mesh shader argument table.
- [func setMeshBytes(UnsafeRawPointer, length: Int, index: Int)](./mtlrendercommandencoder/setmeshbytes%28_,length,index%29.md)
  Creates a buffer from bytes and assigns it to an entry in the mesh shader argument table.
- [func setMeshBufferOffset(Int, index: Int)](./mtlrendercommandencoder/setmeshbufferoffset%28_,index%29.md)
  Updates an entry in the mesh shader argument table with a new location within the entry’s current buffer.
- [- setMeshBuffers:offsets:withRange:](./mtlrendercommandencoder/setmeshbuffers_offsets_withrange_.md)
  Assigns multiple buffers to a range of entries in the mesh shader argument table.
### Assigning textures for mesh shaders
- [func setMeshTexture((any MTLTexture)?, index: Int)](./mtlrendercommandencoder/setmeshtexture%28_,index%29.md)
  Assigns a texture to an entry in the mesh shader argument table.
- [func setMeshTextures([(any MTLTexture)?], range: Range<Int>)](./mtlrendercommandencoder/setmeshtextures%28_,range%29.md)
  Assigns multiple textures to a range of entries in the mesh shader argument table.
- [- setMeshTextures:withRange:](./mtlrendercommandencoder/setmeshtextures_withrange_.md)
  Assigns multiple textures to a range of entries in the mesh shader argument table.
### Assigning sampler states for mesh shaders
- [func setMeshSamplerState((any MTLSamplerState)?, index: Int)](./mtlrendercommandencoder/setmeshsamplerstate%28_,index%29.md)
  Assigns a sampler state to an entry in the mesh shader argument table.
- [func setMeshSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](./mtlrendercommandencoder/setmeshsamplerstate%28_,lodminclamp,lodmaxclamp,index%29.md)
  Assigns a sampler state and clamp values to an entry in the mesh shader argument table.
- [func setMeshSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](./mtlrendercommandencoder/setmeshsamplerstates%28_,range%29.md)
  Assigns multiple sampler states to a range of entries in the mesh shader argument table.
- [func setMeshSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](./mtlrendercommandencoder/setmeshsamplerstates%28_,lodminclamps,lodmaxclamps,range%29.md)
  Assigns multiple sampler states and clamp values to a range of entries in the mesh shader argument table.
- [- setMeshSamplerStates:withRange:](./mtlrendercommandencoder/setmeshsamplerstates_withrange_.md)
  Assigns multiple sampler states to a range of entries in the mesh shader argument table.
- [- setMeshSamplerStates:lodMinClamps:lodMaxClamps:withRange:](./mtlrendercommandencoder/setmeshsamplerstates_lodminclamps_lodmaxclamps_withrange_.md)
  Assigns multiple sampler states and clamp values to a range of entries in the mesh shader argument table.

## See Also

### Resource preparation commands
- [Vertex shader resource preparation commands](./vertex-shader-resource-preparation-commands.md)
  Assign resources to vertex shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Fragment shader resource preparation commands](./fragment-shader-resource-preparation-commands.md)
  Assign resources to fragment shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Tile shaders resource preparation commands](./tile-shaders-resource-preparation-commands.md)
  Assign resources to tile shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Argument buffer resource preparation commands](./argument-buffer-resource-preparation-commands.md)
  Load individual resources and multiple resources within a heap into GPU memory so that they’re available to shaders through argument buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mesh-and-object-shader-resource-preparation-commands)*