# MTLArgumentEncoder

**Framework**: Metal  
**Kind**: protocol

An interface you can use to encode argument data into an argument buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTLArgumentEncoder : NSObjectProtocol
```

## Mentions

- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md)

#### Overview

An [`MTLArgumentEncoder`](mtlargumentencoder.md) instance encodes buffers, textures, samplers, and inlined constant data into an argument buffer. An [`MTLBuffer`](mtlbuffer.md) instance represents the argument buffer that you set as the encoding destination by calling the [`setArgumentBuffer(_:offset:)`](mtlargumentencoder/setargumentbuffer(_:offset:).md) method.

The recommended way to declare an argument buffer is to define its structure in your Metal shading language code. You can assign the argument buffer to a function’s specific buffer index. To create an encoder for this type of argument buffer, call one of the following [`MTLFunction`](mtlfunction.md) methods:

- [`makeArgumentEncoder(bufferIndex:)`](mtlfunction/makeargumentencoder(bufferindex:).md)
- [`makeArgumentEncoder(bufferIndex:reflection:)`](mtlfunction/makeargumentencoder(bufferindex:reflection:).md)

If you construct your shaders dynamically at runtime, you can still construct argument buffers as parameters for the shader. Define each argument separately and then add it to an array of [`MTLArgumentDescriptor`](mtlargumentdescriptor.md) instances. To create an encoder for this type of argument buffer, call the [`makeArgumentEncoder(arguments:)`](mtldevice/makeargumentencoder(arguments:).md) method of the [`MTLDevice`](mtldevice.md) class.

> ❗ **Important**:  A runtime validation error occurs if you create a `MTLArgumentEncoder` instance using structures that don’t reference any other resources and don’t provide any `[[id()]]` annotation on any of their members.

## Topics

### Creating an argument buffer
- [func setArgumentBuffer((any MTLBuffer)?, offset: Int)](mtlargumentencoder/setargumentbuffer(_:offset:).md)
  Specifies the position in a buffer where the encoder writes argument data.
- [func setArgumentBuffer((any MTLBuffer)?, startOffset: Int, arrayElement: Int)](mtlargumentencoder/setargumentbuffer(_:startoffset:arrayelement:).md)
  Specifies an array element within a buffer where the encoder writes argument data.
- [var encodedLength: Int](mtlargumentencoder/encodedlength.md)
  The number of bytes required to store the encoded resources of an argument buffer.
### Encoding buffers
- [func setBuffer((any MTLBuffer)?, offset: Int, index: Int)](mtlargumentencoder/setbuffer(_:offset:index:).md)
  Encodes a reference to a buffer into the argument buffer.
- [func setBuffers([(any MTLBuffer)?], offsets: [Int], range: Range<Int>)](mtlargumentencoder/setbuffers(_:offsets:range:).md)
  Encodes references to an array of buffers into the argument buffer.
### Encoding textures
- [func setTexture((any MTLTexture)?, index: Int)](mtlargumentencoder/settexture(_:index:).md)
  Encodes a reference to a texture into the argument buffer.
- [func setTextures([(any MTLTexture)?], range: Range<Int>)](mtlargumentencoder/settextures(_:range:).md)
  Encodes references to an array of textures into the argument buffer.
### Encoding samplers
- [func setSamplerState((any MTLSamplerState)?, index: Int)](mtlargumentencoder/setsamplerstate(_:index:).md)
  Encodes a sampler into the argument buffer.
- [func setSamplerStates([(any MTLSamplerState)?], range: Range<Int>)](mtlargumentencoder/setsamplerstates(_:range:).md)
  Encodes an array of samplers into the argument buffer.
### Encoding pipeline states
- [func setRenderPipelineState((any MTLRenderPipelineState)?, index: Int)](mtlargumentencoder/setrenderpipelinestate(_:index:).md)
  Encodes a reference to a render pipeline state into the argument buffer.
- [func setRenderPipelineStates([(any MTLRenderPipelineState)?], range: Range<Int>)](mtlargumentencoder/setrenderpipelinestates(_:range:).md)
  Encodes references to an array of render pipeline states into the argument buffer.
- [func setComputePipelineState((any MTLComputePipelineState)?, index: Int)](mtlargumentencoder/setcomputepipelinestate(_:index:).md)
  Encodes a reference to a compute pipeline state into the argument buffer.
- [func setComputePipelineStates(UnsafePointer<(any MTLComputePipelineState)?>, with: NSRange)](mtlargumentencoder/setcomputepipelinestates(_:with:).md)
  Encodes references to an array of compute pipeline states into the argument buffer.
- [func setComputePipelineState((any MTLComputePipelineState)?, at: Int)](mtlargumentencoder/setcomputepipelinestate(_:at:).md)
  Encodes a reference to a compute pipeline state into the argument buffer.
- [func setComputePipelineStates([(any MTLComputePipelineState)?], range: Range<Int>)](mtlargumentencoder/setcomputepipelinestates(_:range:).md)
  Encodes references to an array of compute pipeline states into the argument buffer.
### Encoding inlined constant data
- [func constantData(at: Int) -> UnsafeMutableRawPointer](mtlargumentencoder/constantdata(at:).md)
  Returns a pointer to an inline, constant-data argument within the argument buffer.
### Encoding indirect command buffers
- [func setIndirectCommandBuffer((any MTLIndirectCommandBuffer)?, index: Int)](mtlargumentencoder/setindirectcommandbuffer(_:index:).md)
  Encodes a reference to an indirect command buffer into the argument buffer.
- [func setIndirectCommandBuffers([(any MTLIndirectCommandBuffer)?], range: Range<Int>)](mtlargumentencoder/setindirectcommandbuffers(_:range:).md)
  Encodes an array of indirect command buffers into the argument buffer.
### Encoding acceleration structures
- [func setAccelerationStructure((any MTLAccelerationStructure)?, index: Int)](mtlargumentencoder/setaccelerationstructure(_:index:).md)
  Encodes a reference to an acceleration structure into the argument buffer.
### Encoding function tables
- [func setVisibleFunctionTable((any MTLVisibleFunctionTable)?, index: Int)](mtlargumentencoder/setvisiblefunctiontable(_:index:).md)
  Encodes a reference to a visible-function table into the argument buffer.
- [func setIntersectionFunctionTable((any MTLIntersectionFunctionTable)?, index: Int)](mtlargumentencoder/setintersectionfunctiontable(_:index:).md)
  Encodes a reference to a ray-tracing intersection-function table into the argument buffer.
- [func setIntersectionFunctionTables([(any MTLIntersectionFunctionTable)?], range: Range<Int>)](mtlargumentencoder/setintersectionfunctiontables(_:range:).md)
  Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.
- [func setVisibleFunctionTables([(any MTLVisibleFunctionTable)?], range: Range<Int>)](mtlargumentencoder/setvisiblefunctiontables(_:range:).md)
  Encodes references to an array of ray-tracing intersection-function tables into the argument buffer.
### Creating a nested argument encoder
- [func makeArgumentEncoderForBuffer(atIndex: Int) -> (any MTLArgumentEncoder)?](mtlargumentencoder/makeargumentencoderforbuffer(atindex:).md)
  Creates a new argument encoder for a nested argument buffer.
### Querying alignment
- [var alignment: Int](mtlargumentencoder/alignment.md)
  The alignment, in bytes, required for storing the encoded resources of an argument buffer.
### Identifying the argument encoder
- [var label: String?](mtlargumentencoder/label.md)
  A string that identifies the argument buffer.
- [var device: any MTLDevice](mtlargumentencoder/device.md)
  The device object that created the argument encoder.
### Instance Methods
- [func setDepthStencilState((any MTLDepthStencilState)?, index: Int)](mtlargumentencoder/setdepthstencilstate(_:index:).md)
- [func setDepthStencilStates([(any MTLDepthStencilState)?], range: Range<Int>)](mtlargumentencoder/setdepthstencilstates(_:range:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md)
  Optimize your app’s performance by grouping your resources into argument buffers.
- [Managing groups of resources with argument buffers](managing-groups-of-resources-with-argument-buffers.md)
  Create argument buffers to organize related resources.
- [Tracking the resource residency of argument buffers](tracking-the-resource-residency-of-argument-buffers.md)
  Optimize resource performance within an argument buffer.
- [Indexing argument buffers](indexing-argument-buffers.md)
  Assign resource indices within an argument buffer.
- [Rendering terrain dynamically with argument buffers](rendering-terrain-dynamically-with-argument-buffers.md)
  Use argument buffers to render terrain in real time with a GPU-driven pipeline.
- [Encoding argument buffers on the GPU](encoding-argument-buffers-on-the-gpu.md)
  Use a compute pass to encode an argument buffer and access its arguments in a subsequent render pass.
- [Using argument buffers with resource heaps](using-argument-buffers-with-resource-heaps.md)
  Reduce CPU overhead by using arrays inside argument buffers and combining them with resource heaps.
- [class MTLArgumentDescriptor](mtlargumentdescriptor.md)
  A representation of an argument within an argument buffer.
- [let MTLAttributeStrideStatic: Int](mtlattributestridestatic.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlargumentencoder)*