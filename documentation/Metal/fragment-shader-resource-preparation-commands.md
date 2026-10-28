# Fragment shader resource preparation commands

**Framework**: Metal  
**Role**: API Collection

Assign resources to fragment shaders, including buffers, textures, acceleration structures, sampler states, and function tables.

## Overview

Fragment shaders share argument tables for each resource type, such as buffers, textures, and sampler states. Each shader type has its own argument tables, separate from fragment shaders and other shader types.

## Topics

### Assigning buffers
- [func setFragmentBuffer((any MTLBuffer)?, offset: Int, index: Int)](./mtlrendercommandencoder/setfragmentbuffer%28_,offset,index%29.md)
  Assigns a buffer to an entry in the fragment shader argument table.
- [func setFragmentBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](./mtlrendercommandencoder/setfragmentbuffers%28_,offsets,range%29.md)
  Assigns multiple buffers to a range of entries in the fragment shader argument table.
- [func setFragmentBytes(UnsafeRawPointer, length: Int, index: Int)](./mtlrendercommandencoder/setfragmentbytes%28_,length,index%29.md)
  Creates a buffer from bytes and assigns it to an entry in the fragment shader argument table.
- [func setFragmentBufferOffset(Int, index: Int)](./mtlrendercommandencoder/setfragmentbufferoffset%28_,index%29.md)
  Updates an entry in the fragment shader argument table with a new location within the entry’s current buffer.
- [- setFragmentBuffers:offsets:withRange:](./mtlrendercommandencoder/setfragmentbuffers_offsets_withrange_.md)
  Assigns multiple buffers to a range of entries in the fragment shader argument table.
### Assigning textures
- [func setFragmentTexture((any MTLTexture)?, index: Int)](./mtlrendercommandencoder/setfragmenttexture%28_,index%29.md)
  Assigns a texture to an entry in the fragment shader argument table.
- [func setFragmentTextures([(any MTLTexture)?], range: Range<Int>)](./mtlrendercommandencoder/setfragmenttextures%28_,range%29.md)
  Assigns multiple textures to a range of entries in the fragment shader argument table.
- [- setFragmentTextures:withRange:](./mtlrendercommandencoder/setfragmenttextures_withrange_.md)
  Assigns multiple textures to a range of entries in the fragment shader argument table.
### Assigning sampler states
- [func setFragmentSamplerState((any MTLSamplerState)?, index: Int)](./mtlrendercommandencoder/setfragmentsamplerstate%28_,index%29.md)
  Assigns a sampler state to an entry in the fragment shader argument table.
- [func setFragmentSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](./mtlrendercommandencoder/setfragmentsamplerstate%28_,lodminclamp,lodmaxclamp,index%29.md)
  Assigns a sampler state and clamp values to an entry in the fragment shader argument table.
- [func setFragmentSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](./mtlrendercommandencoder/setfragmentsamplerstates%28_,range%29.md)
  Assigns multiple sampler states to a range of entries in the fragment shader argument table.
- [func setFragmentSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](./mtlrendercommandencoder/setfragmentsamplerstates%28_,lodminclamps,lodmaxclamps,range%29.md)
  Assigns multiple sampler states and clamp values to a range of entries in the fragment shader argument table.
- [- setFragmentSamplerStates:withRange:](./mtlrendercommandencoder/setfragmentsamplerstates_withrange_.md)
  Assigns multiple sampler states to a range of entries in the fragment shader argument table.
- [- setFragmentSamplerStates:lodMinClamps:lodMaxClamps:withRange:](./mtlrendercommandencoder/setfragmentsamplerstates_lodminclamps_lodmaxclamps_withrange_.md)
  Assigns multiple sampler states and clamp values to a range of entries in the fragment shader argument table.
### Assigning acceleration structures
- [func setFragmentAccelerationStructure((any MTLAccelerationStructure)?, bufferIndex: Int)](./mtlrendercommandencoder/setfragmentaccelerationstructure%28_,bufferindex%29.md)
  Assigns an acceleration structure to an entry in the fragment shader argument table.
### Assigning visible function tables
- [func setFragmentVisibleFunctionTable((any MTLVisibleFunctionTable)?, bufferIndex: Int)](./mtlrendercommandencoder/setfragmentvisiblefunctiontable%28_,bufferindex%29.md)
  Assigns a visible function table to an entry in the fragment shader argument table.
- [func setFragmentVisibleFunctionTables([(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)](./mtlrendercommandencoder/setfragmentvisiblefunctiontables%28_,bufferrange%29.md)
  Assigns multiple visible function tables to a range of entries in the fragment shader argument table.
- [- setFragmentVisibleFunctionTables:withBufferRange:](./mtlrendercommandencoder/setfragmentvisiblefunctiontables_withbufferrange_.md)
  Assigns multiple visible function tables to a range of entries in the fragment shader argument table.
### Assigning intersection function tables
- [func setFragmentIntersectionFunctionTable((any MTLIntersectionFunctionTable)?, bufferIndex: Int)](./mtlrendercommandencoder/setfragmentintersectionfunctiontable%28_,bufferindex%29.md)
  Assigns an intersection function table to an entry in the fragment shader argument table.
- [func setFragmentIntersectionFunctionTables([(any MTLIntersectionFunctionTable)?], bufferRange: Range<Int>)](./mtlrendercommandencoder/setfragmentintersectionfunctiontables%28_,bufferrange%29.md)
  Assigns multiple intersection function tables to a range of entries in the fragment shader argument table.
- [- setFragmentIntersectionFunctionTables:withBufferRange:](./mtlrendercommandencoder/setfragmentintersectionfunctiontables_withbufferrange_.md)
  Assigns multiple intersection function tables to a range of entries in the fragment shader argument table.

## See Also

### Resource preparation commands
- [Mesh and object shader resource preparation commands](./mesh-and-object-shader-resource-preparation-commands.md)
  Assign resources to mesh and object shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Vertex shader resource preparation commands](./vertex-shader-resource-preparation-commands.md)
  Assign resources to vertex shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Tile shaders resource preparation commands](./tile-shaders-resource-preparation-commands.md)
  Assign resources to tile shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Argument buffer resource preparation commands](./argument-buffer-resource-preparation-commands.md)
  Load individual resources and multiple resources within a heap into GPU memory so that they’re available to shaders through argument buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/fragment-shader-resource-preparation-commands)*