# MTL4RenderPipelineDescriptor

**Framework**: Metal  
**Kind**: class

Groups together properties to create a render pipeline state object.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class MTL4RenderPipelineDescriptor
```

#### Overview

Compared to [`MTLRenderPipelineDescriptor`](mtlrenderpipelinedescriptor.md), this interface doesn’t offer a mechanism to hint to Metal mutability of vertex and fragment buffers. Additionally, using this descriptor, you don’t specify binary archives.

## Topics

### Instance Properties
- [var alphaToCoverageState: MTL4AlphaToCoverageState](mtl4renderpipelinedescriptor/alphatocoveragestate.md)
  Indicates whether to read and use the alpha channel fragment output of color attachments to compute a sample coverage mask.
- [var alphaToOneState: MTL4AlphaToOneState](mtl4renderpipelinedescriptor/alphatoonestate.md)
  Indicates whether the pipeline forces alpha channel values of color attachments to the largest representable value.
- [var colorAttachmentMappingState: MTL4LogicalToPhysicalColorAttachmentMappingState](mtl4renderpipelinedescriptor/colorattachmentmappingstate.md)
  Configures a logical-to-physical rendering remap state.
- [var colorAttachments: MTL4RenderPipelineColorAttachmentDescriptorArray](mtl4renderpipelinedescriptor/colorattachments.md)
  Accesses an array containing descriptions of the color attachments this pipeline writes to.
- [var fragmentFunctionDescriptor: MTL4FunctionDescriptor?](mtl4renderpipelinedescriptor/fragmentfunctiondescriptor.md)
  Assigns the shader function that this pipeline executes for each fragment.
- [var fragmentStaticLinkingDescriptor: MTL4StaticLinkingDescriptor!](mtl4renderpipelinedescriptor/fragmentstaticlinkingdescriptor.md)
  Provides static linking information for the fragment stage of the render pipeline.
- [var inputPrimitiveTopology: MTLPrimitiveTopologyClass](mtl4renderpipelinedescriptor/inputprimitivetopology.md)
  Assigns type of primitive topology this pipeline renders.
- [var isRasterizationEnabled: Bool](mtl4renderpipelinedescriptor/israsterizationenabled.md)
  Determines whether the pipeline rasterizes primitives.
- [var maxVertexAmplificationCount: Int](mtl4renderpipelinedescriptor/maxvertexamplificationcount.md)
  Determines the maximum value that can you can pass as the pipeline’s amplification count.
- [var rasterSampleCount: Int](mtl4renderpipelinedescriptor/rastersamplecount.md)
  Controls the number of samples this pipeline applies for each fragment.
- [var supportFragmentBinaryLinking: Bool](mtl4renderpipelinedescriptor/supportfragmentbinarylinking.md)
  Indicates whether you can use the pipeline to create new pipelines by adding binary functions to the fragment shader function’s callable functions list.
- [var supportIndirectCommandBuffers: MTL4IndirectCommandBufferSupportState](mtl4renderpipelinedescriptor/supportindirectcommandbuffers.md)
  Indicates whether the pipeline supports indirect command buffers.
- [var supportVertexBinaryLinking: Bool](mtl4renderpipelinedescriptor/supportvertexbinarylinking.md)
  Indicates whether you can use the render pipeline to create new pipelines by adding binary functions to the vertex shader function’s callable functions list.
- [var vertexDescriptor: MTLVertexDescriptor?](mtl4renderpipelinedescriptor/vertexdescriptor.md)
  Configures an optional vertex descriptor for the vertex input.
- [var vertexFunctionDescriptor: MTL4FunctionDescriptor?](mtl4renderpipelinedescriptor/vertexfunctiondescriptor.md)
  Assigns the shader function that this pipeline executes for each vertex.
- [var vertexStaticLinkingDescriptor: MTL4StaticLinkingDescriptor!](mtl4renderpipelinedescriptor/vertexstaticlinkingdescriptor.md)
  Provides static linking information for the vertex stage of the render pipeline.
### Instance Methods
- [func reset()](mtl4renderpipelinedescriptor/reset.md)
  Resets this descriptor to its default state.

## Relationships

### Inherits From
- [MTL4PipelineDescriptor](mtl4pipelinedescriptor.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MTLRenderPipelineState](mtlrenderpipelinestate.md)
  An interface that represents a graphics pipeline configuration for a render pass, which the pass applies to the draw commands you encode.
- [class MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md)
  An argument of options you pass to a GPU device to get a render pipeline state.
- [class MTLRenderPipelineFunctionsDescriptor](mtlrenderpipelinefunctionsdescriptor.md)
  A collection of functions for updating a render pipeline.
- [class MTL4MeshRenderPipelineDescriptor](mtl4meshrenderpipelinedescriptor.md)
  Groups together properties you use to create a mesh render pipeline state object.
- [class MTLMeshRenderPipelineDescriptor](mtlmeshrenderpipelinedescriptor.md)
  An object that configures new render pipeline state objects for mesh shading.
- [class MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md)
  The mutability options for a buffer that a render or compute pipeline uses.
- [class MTLPipelineBufferDescriptorArray](mtlpipelinebufferdescriptorarray.md)
  An array of pipeline buffer descriptors.
- [class MTL4RenderPipelineColorAttachmentDescriptor](mtl4renderpipelinecolorattachmentdescriptor.md)
- [class MTLRenderPipelineColorAttachmentDescriptor](mtlrenderpipelinecolorattachmentdescriptor.md)
  A color render target that specifies the color configuration and color operations for a render pipeline.
- [class MTLRenderPipelineColorAttachmentDescriptorArray](mtlrenderpipelinecolorattachmentdescriptorarray.md)
  An array of render pipeline color attachment descriptor objects.
- [class MTL4TileRenderPipelineDescriptor](mtl4tilerenderpipelinedescriptor.md)
  Groups together properties you use to create a tile render pipeline state object.
- [class MTLTileRenderPipelineDescriptor](mtltilerenderpipelinedescriptor.md)
  An object that configures new render pipeline state objects for tile shading.
- [class MTLTileRenderPipelineColorAttachmentDescriptor](mtltilerenderpipelinecolorattachmentdescriptor.md)
  A description of a tile-shading render pipeline’s color render target.
- [struct MTLPipelineOption](mtlpipelineoption.md)
  Options that determine how Metal prepares the pipeline.
- [class MTL4RenderPipelineBinaryFunctionsDescriptor](mtl4renderpipelinebinaryfunctionsdescriptor.md)
  Allows you to specify additional binary functions to link to each stage of a render pipeline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4renderpipelinedescriptor)*