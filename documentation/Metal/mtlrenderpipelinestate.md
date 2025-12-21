# MTLRenderPipelineState

**Framework**: Metal  
**Kind**: protocol

An interface that represents a graphics pipeline configuration for a render pass, which the pass applies to the draw commands you encode.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
protocol MTLRenderPipelineState : MTLAllocation, Sendable
```

## Mentions

- [Improving CPU performance by using argument buffers](improving-cpu-performance-by-using-argument-buffers.md)
- [Improving rendering performance with vertex amplification](improving-rendering-performance-with-vertex-amplification.md)

#### Overview

The [`MTLRenderPipelineState`](mtlrenderpipelinestate.md) protocol is an interface that represents a specific configuration for the graphics-rendering pipeline, including which shaders it uses. Use a pipeline state to configure a render pass by calling the [`setRenderPipelineState(_:)`](mtlrendercommandencoder/setrenderpipelinestate(_:).md) method of an [`MTLRenderCommandEncoder`](mtlrendercommandencoder.md) instance.

To create a pipeline state, call the appropriate [`MTLDevice`](mtldevice.md) method (see [`Pipeline state creation`](pipeline-state-creation.md)). You typically make pipeline states at a noncritical time, like when the app first launches. This is because graphics drivers may need time to evaluate and build each pipeline state. However, you can quickly use and reuse each pipeline state throughout your app’s lifetime.

## Topics

### Identifying a pipeline state
- [var device: any MTLDevice](mtlrenderpipelinestate/device.md)
  The device instance that creates the pipeline state.
- [var label: String?](mtlrenderpipelinestate/label.md)
  A string that helps you identify the render pipeline state during debugging.
- [var gpuResourceID: MTLResourceID](mtlrenderpipelinestate/gpuresourceid.md)
  An unique identifier that represents the pipeline state, which you can add to an argument buffer.
### Checking object shader memory requirements
- [var maxTotalThreadsPerObjectThreadgroup: Int](mtlrenderpipelinestate/maxtotalthreadsperobjectthreadgroup.md)
  The largest number of threads the pipeline state can have in a single object shader threadgroup.
- [var objectThreadExecutionWidth: Int](mtlrenderpipelinestate/objectthreadexecutionwidth.md)
  The number of threads the render pass applies to a SIMD group for an object shader.
### Checking mesh shader memory requirements
- [var maxTotalThreadsPerMeshThreadgroup: Int](mtlrenderpipelinestate/maxtotalthreadspermeshthreadgroup.md)
  The largest number of threads the pipeline state can have in a single mesh shader threadgroup.
- [var maxTotalThreadgroupsPerMeshGrid: Int](mtlrenderpipelinestate/maxtotalthreadgroupspermeshgrid.md)
  The largest number of threadgroups the pipeline state can have in a single mesh shader grid.
- [var meshThreadExecutionWidth: Int](mtlrenderpipelinestate/meshthreadexecutionwidth.md)
  The number of threads the render pass applies to a SIMD group for a mesh shader.
### Checking tile shader memory requirements
- [var maxTotalThreadsPerThreadgroup: Int](mtlrenderpipelinestate/maxtotalthreadsperthreadgroup.md)
  The largest number of threads the pipeline state can have in a single tile shader threadgroup.
- [var threadgroupSizeMatchesTileSize: Bool](mtlrenderpipelinestate/threadgroupsizematchestilesize.md)
  A Boolean value that indicates whether the pipeline state needs a threadgroup’s size to equal a tile’s size.
- [var imageblockSampleLength: Int](mtlrenderpipelinestate/imageblocksamplelength.md)
  The memory size, in byes, of the render pipeline’s imageblock for a single sample.
- [func imageblockMemoryLength(forDimensions: MTLSize) -> Int](mtlrenderpipelinestate/imageblockmemorylength(fordimensions:).md)
  Returns the length of an imageblock’s memory for the specified imageblock dimensions.
### Checking feature support
- [var supportIndirectCommandBuffers: Bool](mtlrenderpipelinestate/supportindirectcommandbuffers.md)
  A Boolean value that indicates whether the render pipeline supports encoding commands into an indirect command buffer.
### Checking shader validation
- [var shaderValidation: MTLShaderValidation](mtlrenderpipelinestate/shadervalidation.md)
  The current state of shader validation for the pipeline.
### Creating function handles and tables
- [func functionHandle(function: any MTLFunction, stage: MTLRenderStages) -> (any MTLFunctionHandle)?](mtlrenderpipelinestate/functionhandle(function:stage:)-7uvul.md)
  Creates a function handle for a shader.
- [func makeVisibleFunctionTable(descriptor: MTLVisibleFunctionTableDescriptor, stage: MTLRenderStages) -> (any MTLVisibleFunctionTable)?](mtlrenderpipelinestate/makevisiblefunctiontable(descriptor:stage:).md)
  Creates a new visible function table.
- [func makeIntersectionFunctionTable(descriptor: MTLIntersectionFunctionTableDescriptor, stage: MTLRenderStages) -> (any MTLIntersectionFunctionTable)?](mtlrenderpipelinestate/makeintersectionfunctiontable(descriptor:stage:).md)
  Creates a new intersection function table.
### Creating modified clones of the render pipeline
- [func makeRenderPipelineState(additionalBinaryFunctions: MTLRenderPipelineFunctionsDescriptor) throws -> any MTLRenderPipelineState](mtlrenderpipelinestate/makerenderpipelinestate(additionalbinaryfunctions:)-84te1.md)
  Creates a new pipeline state that’s a copy of the current pipeline state with additional shaders.
### Instance Properties
- [var reflection: MTLRenderPipelineReflection?](mtlrenderpipelinestate/reflection.md)
  Obtains a reflection object for this render pipeline.
- [var requiredThreadsPerMeshThreadgroup: MTLSize](mtlrenderpipelinestate/requiredthreadspermeshthreadgroup.md)
- [var requiredThreadsPerObjectThreadgroup: MTLSize](mtlrenderpipelinestate/requiredthreadsperobjectthreadgroup.md)
- [var requiredThreadsPerTileThreadgroup: MTLSize](mtlrenderpipelinestate/requiredthreadspertilethreadgroup.md)
### Instance Methods
- [func functionHandle(function: any MTL4BinaryFunction, stage: MTLRenderStages) -> (any MTLFunctionHandle)?](mtlrenderpipelinestate/functionhandle(function:stage:)-1pgxo.md)
  Obtains the function handle for a specific function this pipeline state links at the binary level.
- [func functionHandle(withName: String, stage: MTLRenderStages) -> (any MTLFunctionHandle)?](mtlrenderpipelinestate/functionhandle(withname:stage:).md)
  Obtains a function handle for the a specific function this pipeline links at the Metal IR level.
- [func makeRenderPipelineDescriptorForSpecialization() -> MTL4PipelineDescriptor](mtlrenderpipelinestate/makerenderpipelinedescriptorforspecialization.md)
  Creates a render pipeline descriptor from this pipeline that you can use for pipeline specialization.
- [func makeRenderPipelineState(additionalBinaryFunctions: MTL4RenderPipelineBinaryFunctionsDescriptor) throws -> any MTLRenderPipelineState](mtlrenderpipelinestate/makerenderpipelinestate(additionalbinaryfunctions:)-49r1w.md)
  Creates a new render pipeline state by adding binary functions to each stage of this pipeline state.

## Relationships

### Inherits From
- [MTLAllocation](mtlallocation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class MTL4RenderPipelineDescriptor](mtl4renderpipelinedescriptor.md)
  Groups together properties to create a render pipeline state object.
- [class MTLRenderPipelineDescriptor](mtlrenderpipelinedescriptor.md)
  An argument of options you pass to a GPU device to get a render pipeline state.
- [class MTLRenderPipelineFunctionsDescriptor](mtlrenderpipelinefunctionsdescriptor.md)
  A collection of functions for updating a render pipeline.
- [class MTL4MeshRenderPipelineDescriptor](mtl4meshrenderpipelinedescriptor.md)
  Groups together properties you use to create a mesh render pipeline state object.
- [class MTLMeshRenderPipelineDescriptor](mtlmeshrenderpipelinedescriptor.md)
  An object that configures new render pipeline state objects for mesh shading.
- [class MTLPipelineBufferDescriptor](mtlpipelinebufferdescriptor.md)
  The mutability options for a buffer that a render or compute pipeline uses.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate)*