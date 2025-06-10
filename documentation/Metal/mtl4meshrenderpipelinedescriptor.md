# MTL4MeshRenderPipelineDescriptor

**Framework**: Metal  
**Kind**: class

Groups together properties you use to create a mesh render pipeline state object.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class MTL4MeshRenderPipelineDescriptor
```

#### Overview

Compared to [`MTLMeshRenderPipelineDescriptor`](mtlmeshrenderpipelinedescriptor.md), this interface doesn’t offer a mechanism to hint to Metal mutability of object, mesh, or fragment buffers. Additionally, when you use this descriptor, you don’t specify binary archives.

## Topics

### Instance Properties
- [var alphaToCoverageState: MTL4AlphaToCoverageState](mtl4meshrenderpipelinedescriptor/alphatocoveragestate.md)
  Indicates whether to read and use the alpha channel fragment output of color attachments to compute a sample coverage mask.
- [var alphaToOneState: MTL4AlphaToOneState](mtl4meshrenderpipelinedescriptor/alphatoonestate.md)
  Indicates whether the pipeline forces alpha channel values of color attachments to the largest representable value.
- [var colorAttachmentMappingState: MTL4LogicalToPhysicalColorAttachmentMappingState](mtl4meshrenderpipelinedescriptor/colorattachmentmappingstate.md)
  Sets the logical-to-physical rendering remap state.
- [var colorAttachments: MTL4RenderPipelineColorAttachmentDescriptorArray](mtl4meshrenderpipelinedescriptor/colorattachments.md)
  Accesses an array containing descriptions of the color attachments this pipeline writes to.
- [var fragmentFunctionDescriptor: MTL4FunctionDescriptor?](mtl4meshrenderpipelinedescriptor/fragmentfunctiondescriptor.md)
  Assigns a function descriptor representing the function this pipeline executes for each fragment.
- [var fragmentStaticLinkingDescriptor: MTL4StaticLinkingDescriptor!](mtl4meshrenderpipelinedescriptor/fragmentstaticlinkingdescriptor.md)
  Provides static linking information for the fragment stage of the render pipeline.
- [var isRasterizationEnabled: Bool](mtl4meshrenderpipelinedescriptor/israsterizationenabled.md)
  Determines whether the pipeline rasterizes primitives.
- [var maxTotalThreadgroupsPerMeshGrid: Int](mtl4meshrenderpipelinedescriptor/maxtotalthreadgroupspermeshgrid.md)
  Controls the largest number of threads the pipeline state can execute when the object stage of a mesh render pipeline you create from this descriptor dispatches its mesh stage.
- [var maxTotalThreadsPerMeshThreadgroup: Int](mtl4meshrenderpipelinedescriptor/maxtotalthreadspermeshthreadgroup.md)
  Controls the largest number of threads the pipeline state can execute in a single mesh shader threadgroup dispatch.
- [var maxTotalThreadsPerObjectThreadgroup: Int](mtl4meshrenderpipelinedescriptor/maxtotalthreadsperobjectthreadgroup.md)
  Controls the largest number of threads the pipeline state can execute in a single object shader threadgroup dispatch.
- [var maxVertexAmplificationCount: Int](mtl4meshrenderpipelinedescriptor/maxvertexamplificationcount.md)
  Determines the maximum value that can you can pass as the pipeline’s amplification count.
- [var meshFunctionDescriptor: MTL4FunctionDescriptor?](mtl4meshrenderpipelinedescriptor/meshfunctiondescriptor.md)
  Assigns a function descriptor representing the function this pipeline executes for each primitive in the mesh shader stage.
- [var meshStaticLinkingDescriptor: MTL4StaticLinkingDescriptor!](mtl4meshrenderpipelinedescriptor/meshstaticlinkingdescriptor.md)
  Provides static linking information for the mesh stage of the render pipeline.
- [var meshThreadgroupSizeIsMultipleOfThreadExecutionWidth: Bool](mtl4meshrenderpipelinedescriptor/meshthreadgroupsizeismultipleofthreadexecutionwidth.md)
  Provides a guarantee to Metal regarding the number of threadgroup threads for the mesh stage of a pipeline you create from this descriptor.
- [var objectFunctionDescriptor: MTL4FunctionDescriptor?](mtl4meshrenderpipelinedescriptor/objectfunctiondescriptor.md)
  Assigns a function descriptor representing the function this pipeline executes for each  in the object shader stage.
- [var objectStaticLinkingDescriptor: MTL4StaticLinkingDescriptor!](mtl4meshrenderpipelinedescriptor/objectstaticlinkingdescriptor.md)
  Provides static linking information for the object stage of the render pipeline.
- [var objectThreadgroupSizeIsMultipleOfThreadExecutionWidth: Bool](mtl4meshrenderpipelinedescriptor/objectthreadgroupsizeismultipleofthreadexecutionwidth.md)
  Provides a guarantee to Metal regarding the number of threadgroup threads for the object stage of a pipeline you create from this descriptor.
- [var payloadMemoryLength: Int](mtl4meshrenderpipelinedescriptor/payloadmemorylength.md)
  Reserves storage for the object-to-mesh stage payload.
- [var rasterSampleCount: Int](mtl4meshrenderpipelinedescriptor/rastersamplecount.md)
  Sets number of samples this pipeline applies for each fragment.
- [var requiredThreadsPerMeshThreadgroup: MTLSize](mtl4meshrenderpipelinedescriptor/requiredthreadspermeshthreadgroup.md)
  Controls the required number of mesh threads-per-threadgroup when drawing with a mesh shader pipeline you create from this descriptor.
- [var requiredThreadsPerObjectThreadgroup: MTLSize](mtl4meshrenderpipelinedescriptor/requiredthreadsperobjectthreadgroup.md)
  Controls the required number of object threads-per-threadgroup when drawing with a mesh shader pipeline you create from this descriptor.
- [var supportFragmentBinaryLinking: Bool](mtl4meshrenderpipelinedescriptor/supportfragmentbinarylinking.md)
  Indicates whether you can use the render pipeline to create new pipelines by adding binary functions to the fragment shader function’s callable functions list.
- [var supportIndirectCommandBuffers: MTL4IndirectCommandBufferSupportState](mtl4meshrenderpipelinedescriptor/supportindirectcommandbuffers.md)
  Indicates whether the pipeline supports indirect command buffers.
- [var supportMeshBinaryLinking: Bool](mtl4meshrenderpipelinedescriptor/supportmeshbinarylinking.md)
  Indicates whether you can use the render pipeline to create new pipelines by adding binary functions to the mesh shader function’s callable functions list.
- [var supportObjectBinaryLinking: Bool](mtl4meshrenderpipelinedescriptor/supportobjectbinarylinking.md)
  Indicates whether you can use the render pipeline to create new pipelines by adding binary functions to the object shader function’s callable functions list.
### Instance Methods
- [func reset()](mtl4meshrenderpipelinedescriptor/reset.md)
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
- [class MTL4RenderPipelineDescriptor](mtl4renderpipelinedescriptor.md)
  Groups together properties to create a render pipeline state object.
- [class MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md)
  An argument of options you pass to a GPU device to get a render pipeline state.
- [class MTLRenderPipelineFunctionsDescriptor](mtlrenderpipelinefunctionsdescriptor.md)
  A collection of functions for updating a render pipeline.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor)*