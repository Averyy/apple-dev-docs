# Low-level rendering

**Framework**: RealityKit

Drive the renderer directly to build custom drawing pipelines, meshes, buffers, and textures when higher-level rendering does not give you the control you need.

#### Overview

These types give you direct access to the rendering pipeline and the GPU resources that feed it, so you can issue your own draw work and manage how scenes get rendered. Use them to define custom render targets, configure pipeline state, and supply geometry, transforms, buffers, and textures that you control at a fine granularity. This is intended for advanced rendering work where the standard material and mesh APIs are too high level for what you need. Reach for these capabilities when you want precise control over how your 3D content is drawn and how its underlying memory is organized.

## Topics

### Render contexts
- [class LowLevelRenderer](lowlevelrenderer.md)
  A renderer that encodes draw calls for a collection of mesh instances into a Metal command buffer.
- [protocol LowLevelRenderContext](lowlevelrendercontext.md)
  An entry point for creating rendering resources and compiling materials.
- [protocol LowLevelRenderContextLighting](lowlevelrendercontextlighting.md)
  The interface for creating lighting functions for use in materials.
- [protocol LowLevelRenderContextShaderGraph](lowlevelrendercontextshadergraph.md)
  The interface for creating Metal shader functions from a ShaderGraph.
- [class LowLevelRenderContextStandalone](lowlevelrendercontextstandalone.md)
  A standalone Metal-backed render context for creating low-level rendering resources.
- [struct LowLevelRenderContextError](lowlevelrendercontexterror.md)
  An error thrown when binding or updating a low-level rendering resource fails.
- [struct LowLevelRendererError](lowlevelrenderererror.md)
  An error thrown when creating or configuring a renderer.
### Pipeline and render targets
- [class LowLevelRenderPipelineState](lowlevelrenderpipelinestate.md)
  A compiled Metal render pipeline state for a specific mesh descriptor, material, and render target configuration.
- [class LowLevelRenderTarget](lowlevelrendertarget.md)
  An object that describes the pixel format configuration for a render pass’s color and depth attachments.
- [class LowLevelArgumentTable](lowlevelargumenttable.md)
  A table of buffer slices and textures bound to a single shader function.
- [struct LowLevelMaterialParameterMapping](lowlevelmaterialparametermapping.md)
  A mapping of named buffer and texture parameters to binding indices for a compiled shader function.
### GPU resources
- [class LowLevelMeshResource](lowlevelmeshresource.md)
  A container for vertex and index data in a custom format.
- [class LowLevelMeshPart](lowlevelmeshpart.md)
  An object that describes a range of primitives to draw from a mesh resource.
- [class LowLevelMeshInstance](lowlevelmeshinstance.md)
  A single drawable object pairing a mesh part with a compiled pipeline state, optional per-draw argument tables, a transform, and a sort category.
- [class LowLevelMeshInstanceArray](lowlevelmeshinstancearray.md)
  A fixed-capacity collection of mesh instances submitted to the renderer.
- [class LowLevelInstanceTransformResource](lowlevelinstancetransformresource.md)
  A GPU-managed buffer that stores an array of per-instance transforms for GPU instancing.
- [class LowLevelBufferResource](lowlevelbufferresource.md)
  A GPU-managed buffer for arbitrary per-draw data such as uniforms and custom parameters.
- [struct LowLevelBufferSlice](lowlevelbufferslice.md)
  A reference to a sub-range of a buffer resource, used to bind a region of a buffer to an argument table slot.
- [class LowLevelTextureResource](lowleveltextureresource.md)
  A container for texture data in a custom format.
- [class LowLevelMaterialResource](lowlevelmaterialresource.md)
  A compiled material composed of three independently-replaceable shader functions.
- [class LowLevelDeviceResource](lowleveldeviceresource.md)
  Encapsulates a GPU device resource created by the application. On visionOS, resources must be allocated in shared memory that can be used by the renderer process. Once a device resource is in use by the renderer, changing its contents is unsafe and undefined.
- [struct BoundingSphereBox](boundingspherebox.md)
  A combined bounding volume consisting of a bounding sphere and an optional axis-aligned bounding box.

## See Also

- [Improving the Performance of a RealityKit App](improving-the-performance-of-a-realitykit-app.md)
  Measure CPU and GPU utilization to find ways to improve your app’s performance.
- [Reducing GPU Utilization in Your RealityKit App](reducing-gpu-utilization-in-your-realitykit-app.md)
  Prevent the GPU from limiting your app’s frame rate by reducing the complexity of your render.
- [Reducing CPU Utilization in Your RealityKit App](reducing-cpu-utilization-in-your-realitykit-app.md)
  Target specific CPU metrics with adjustments to your app and its content.
- [Construct an immersive environment for visionOS](construct-an-immersive-environment-for-visionos.md)
  Build efficient custom worlds for your app.
- [Passing Metal command objects around your application](passing-metal-command-objects-around-your-application.md)
  Build a system that creates and passes Metal command objects to entities dispatching Metal compute shaders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/low-level-rendering)*