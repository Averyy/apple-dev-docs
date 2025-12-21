# Pipeline state creation

**Framework**: Metal

Create pipeline states for render and compute passes, samplers, depth and stencil states, and indirect command buffers.

#### Overview

Use these methods to create instances of various state types for a render or compute pass (see [`Render passes`](render-passes.md) and [`Compute passes`](compute-passes.md), respectively).

You can create multiple [`MTLRenderPipelineState`](mtlrenderpipelinestate.md) instances for a single render pass encoder ([`MTLRenderCommandEncoder`](mtlrendercommandencoder.md)) that each apply to different types of render commands. For example, a single render pass can render primitives with vertices, then meshes, and finish with a tile shader command, each with a different pipeline. To create these pipelines, configure instances of [`MTLRenderPipelineDescriptor`](mtlrenderpipelinedescriptor.md), [`MTLMeshRenderPipelineDescriptor`](mtlmeshrenderpipelinedescriptor.md), and [`MTLTileRenderPipelineDescriptor`](mtltilerenderpipelinedescriptor.md). Then pass those descriptors to the [`makeRenderPipelineState(descriptor:completionHandler:)`](mtldevice/makerenderpipelinestate(descriptor:completionhandler:).md), [`makeRenderPipelineState(descriptor:options:completionHandler:)`](mtldevice/makerenderpipelinestate(descriptor:options:completionhandler:)-1wvya.md) and [`makeRenderPipelineState(tileDescriptor:options:completionHandler:)`](mtldevice/makerenderpipelinestate(tiledescriptor:options:completionhandler:).md) methods (or a counterpart method), respectively.

> ❗ **Important**:  Only create reflection (see [`MTLRenderPipelineReflection`](mtlrenderpipelinereflection.md)) instances if you need them, because each one can require a significant amount of memory.

## Topics

### Creating render pipeline states with vertex shaders
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor) throws -> any MTLRenderPipelineState](mtldevice/makerenderpipelinestate(descriptor:).md)
  Synchronously creates a render pipeline state.
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, completionHandler: ((any MTLRenderPipelineState)?, (any Error)?) -> Void)](mtldevice/makerenderpipelinestate(descriptor:completionhandler:).md)
  Asynchronously creates a render pipeline state.
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption) throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)](mtldevice/makerenderpipelinestate(descriptor:options:)-89vxc.md)
  Synchronously creates a render pipeline state and reflection information in a tuple.
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>?) throws -> any MTLRenderPipelineState](mtldevice/makerenderpipelinestate(descriptor:options:reflection:).md)
  Synchronously creates a render pipeline state and reflection information.
- [func makeRenderPipelineState(descriptor: MTLRenderPipelineDescriptor, options: MTLPipelineOption, completionHandler: ((any MTLRenderPipelineState)?, MTLRenderPipelineReflection?, (any Error)?) -> Void)](mtldevice/makerenderpipelinestate(descriptor:options:completionhandler:)-5gdww.md)
  Asynchronously creates a render pipeline state and reflection information.
### Creating render pipeline states with mesh shaders
- [func makeRenderPipelineState(descriptor: MTLMeshRenderPipelineDescriptor, options: MTLPipelineOption) throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)](mtldevice/makerenderpipelinestate(descriptor:options:)-yrak.md)
  Synchronously creates a mesh render pipeline state and reflection information in a tuple.
- [func makeRenderPipelineState(descriptor: MTLMeshRenderPipelineDescriptor, options: MTLPipelineOption, completionHandler: ((any MTLRenderPipelineState)?, MTLRenderPipelineReflection?, (any Error)?) -> Void)](mtldevice/makerenderpipelinestate(descriptor:options:completionhandler:)-1wvya.md)
  Asynchronously creates a mesh render pipeline state and reflection information.
### Creating tile render pipeline states
- [func makeRenderPipelineState(tileDescriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption) throws -> (any MTLRenderPipelineState, MTLRenderPipelineReflection?)](mtldevice/makerenderpipelinestate(tiledescriptor:options:).md)
  Synchronously creates a tile shader’s render pipeline state and reflection information in a tuple.
- [func makeRenderPipelineState(tileDescriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedRenderPipelineReflection?>?) throws -> any MTLRenderPipelineState](mtldevice/makerenderpipelinestate(tiledescriptor:options:reflection:).md)
  Synchronously creates a tile shader’s render pipeline state and reflection information.
- [func makeRenderPipelineState(tileDescriptor: MTLTileRenderPipelineDescriptor, options: MTLPipelineOption, completionHandler: ((any MTLRenderPipelineState)?, MTLRenderPipelineReflection?, (any Error)?) -> Void)](mtldevice/makerenderpipelinestate(tiledescriptor:options:completionhandler:).md)
  Asynchronously creates a tile shader’s render pipeline state and reflection information.
### Creating compute pipeline states
- [func makeComputePipelineState(descriptor: MTLComputePipelineDescriptor, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>?) throws -> any MTLComputePipelineState](mtldevice/makecomputepipelinestate(descriptor:options:reflection:).md)
  Synchronously creates a compute pipeline state and reflection information.
- [func makeComputePipelineState(descriptor: MTLComputePipelineDescriptor, options: MTLPipelineOption, completionHandler: ((any MTLComputePipelineState)?, MTLComputePipelineReflection?, (any Error)?) -> Void)](mtldevice/makecomputepipelinestate(descriptor:options:completionhandler:).md)
  Asynchronously creates a compute pipeline state and reflection information.
- [func makeComputePipelineState(function: any MTLFunction) throws -> any MTLComputePipelineState](mtldevice/makecomputepipelinestate(function:).md)
  Synchronously creates a compute pipeline state with a function instance.
- [func makeComputePipelineState(function: any MTLFunction, completionHandler: ((any MTLComputePipelineState)?, (any Error)?) -> Void)](mtldevice/makecomputepipelinestate(function:completionhandler:).md)
  Asynchronously creates a compute pipeline state with a function instance.
- [func makeComputePipelineState(function: any MTLFunction, options: MTLPipelineOption, reflection: AutoreleasingUnsafeMutablePointer<MTLAutoreleasedComputePipelineReflection?>?) throws -> any MTLComputePipelineState](mtldevice/makecomputepipelinestate(function:options:reflection:).md)
  Synchronously creates a compute pipeline state and reflection with a function instance.
- [func makeComputePipelineState(function: any MTLFunction, options: MTLPipelineOption, completionHandler: ((any MTLComputePipelineState)?, MTLComputePipelineReflection?, (any Error)?) -> Void)](mtldevice/makecomputepipelinestate(function:options:completionhandler:).md)
  Asynchronously creates a compute pipeline state and reflection with a function instance.
### Creating depth and stencil states
- [func makeDepthStencilState(descriptor: MTLDepthStencilDescriptor) -> (any MTLDepthStencilState)?](mtldevice/makedepthstencilstate(descriptor:).md)
  Creates a depth-stencil state instance.
### Supporting types
- [typealias MTLNewRenderPipelineStateCompletionHandler](mtlnewrenderpipelinestatecompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a render pipeline.
- [typealias MTLNewRenderPipelineStateWithReflectionCompletionHandler](mtlnewrenderpipelinestatewithreflectioncompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a render pipeline and reflection information.
- [typealias MTLNewComputePipelineStateCompletionHandler](mtlnewcomputepipelinestatecompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a compute pipeline.
- [typealias MTLNewComputePipelineStateWithReflectionCompletionHandler](mtlnewcomputepipelinestatewithreflectioncompletionhandler.md)
  A completion handler signature a method calls when it finishes creating a compute pipeline and reflection information.

## See Also

- [Device inspection](device-inspection.md)
  Locate and identify a GPU and the features it supports, and sample its counters.
- [Work submission](work-submission.md)
  Create queues that submit work to the GPU or load assets into GPU resources, and indirect command buffers that group your frequent commands together.
- [Resource creation](resource-creation.md)
  Load assets with input/output queues and make various resource instances, such as buffers, textures, acceleration structures, and memory heaps.
- [Shader library and archive creation](shader-library-and-archive-creation.md)
  Create static and dynamic shader libraries, and binary shader archives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/pipeline-state-creation)*