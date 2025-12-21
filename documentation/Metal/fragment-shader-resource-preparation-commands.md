# Fragment shader resource preparation commands

**Framework**: Metal

Assign resources to fragment shaders, including buffers, textures, acceleration structures, sampler states, and function tables.

#### Overview

Fragment shaders share argument tables for each resource type, such as buffers, textures, and sampler states. Each shader type has its own argument tables, separate from fragment shaders and other shader types.

## Topics

### Assigning buffers
- [func setFragmentBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlrendercommandencoder/setfragmentbuffer(_:offset:index:).md)
  Assigns a buffer to an entry in the fragment shader argument table.
- [func setFragmentBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlrendercommandencoder/setfragmentbuffers(_:offsets:range:).md)
  Assigns multiple buffers to a range of entries in the fragment shader argument table.
- [func setFragmentBytes(UnsafeRawPointer, length: Int, index: Int)](mtlrendercommandencoder/setfragmentbytes(_:length:index:).md)
  Creates a buffer from bytes and assigns it to an entry in the fragment shader argument table.
- [func setFragmentBufferOffset(Int, index: Int)](mtlrendercommandencoder/setfragmentbufferoffset(_:index:).md)
  Updates an entry in the fragment shader argument table with a new location within the entry’s current buffer.
### Assigning textures
- [func setFragmentTexture((any MTLTexture)?, index: Int)](mtlrendercommandencoder/setfragmenttexture(_:index:).md)
  Assigns a texture to an entry in the fragment shader argument table.
- [func setFragmentTextures([(any MTLTexture)?], range: Range<Int>)](mtlrendercommandencoder/setfragmenttextures(_:range:).md)
  Assigns multiple textures to a range of entries in the fragment shader argument table.
### Assigning sampler states
- [func setFragmentSamplerState((any MTLSamplerState)?, index: Int)](mtlrendercommandencoder/setfragmentsamplerstate(_:index:).md)
  Assigns a sampler state to an entry in the fragment shader argument table.
- [func setFragmentSamplerState((any MTLSamplerState)?, lodMinClamp: Float, lodMaxClamp: Float, index: Int)](mtlrendercommandencoder/setfragmentsamplerstate(_:lodminclamp:lodmaxclamp:index:).md)
  Assigns a sampler state and clamp values to an entry in the fragment shader argument table.
- [func setFragmentSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](mtlrendercommandencoder/setfragmentsamplerstates(_:range:).md)
  Assigns multiple sampler states to a range of entries in the fragment shader argument table.
- [func setFragmentSamplerStates([(any MTLSamplerState)?], lodMinClamps: [Float], lodMaxClamps: [Float], range: Range<Int>)](mtlrendercommandencoder/setfragmentsamplerstates(_:lodminclamps:lodmaxclamps:range:).md)
  Assigns multiple sampler states and clamp values to a range of entries in the fragment shader argument table.
### Assigning acceleration structures
- [func setFragmentAccelerationStructure((any MTLAccelerationStructure)?, bufferIndex: Int)](mtlrendercommandencoder/setfragmentaccelerationstructure(_:bufferindex:).md)
  Assigns an acceleration structure to an entry in the fragment shader argument table.
### Assigning visible function tables
- [func setFragmentVisibleFunctionTable((any MTLVisibleFunctionTable)?, bufferIndex: Int)](mtlrendercommandencoder/setfragmentvisiblefunctiontable(_:bufferindex:).md)
  Assigns a visible function table to an entry in the fragment shader argument table.
- [func setFragmentVisibleFunctionTables([(any MTLVisibleFunctionTable)?], bufferRange: Range<Int>)](mtlrendercommandencoder/setfragmentvisiblefunctiontables(_:bufferrange:).md)
  Assigns multiple visible function tables to a range of entries in the fragment shader argument table.
### Assigning intersection function tables
- [func setFragmentIntersectionFunctionTable((any MTLIntersectionFunctionTable)?, bufferIndex: Int)](mtlrendercommandencoder/setfragmentintersectionfunctiontable(_:bufferindex:).md)
  Assigns an intersection function table to an entry in the fragment shader argument table.
- [func setFragmentIntersectionFunctionTables([(any MTLIntersectionFunctionTable)?], bufferRange: Range<Int>)](mtlrendercommandencoder/setfragmentintersectionfunctiontables(_:bufferrange:).md)
  Assigns multiple intersection function tables to a range of entries in the fragment shader argument table.

## See Also

- [Mesh and object shader resource preparation commands](mesh-and-object-shader-resource-preparation-commands.md)
  Assign resources to mesh and object shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Vertex shader resource preparation commands](vertex-shader-resource-preparation-commands.md)
  Assign resources to vertex shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Tile shaders resource preparation commands](tile-shaders-resource-preparation-commands.md)
  Assign resources to tile shaders, including buffers, textures, acceleration structures, sampler states, and function tables.
- [Argument buffer resource preparation commands](argument-buffer-resource-preparation-commands.md)
  Load individual resources and multiple resources within a heap into GPU memory so that they’re available to shaders through argument buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/fragment-shader-resource-preparation-commands)*