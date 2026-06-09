# LowLevelRenderContext

**Framework**: RealityKit  
**Kind**: protocol

An entry point for creating rendering resources and compiling materials.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
protocol LowLevelRenderContext : AnyObject
```

#### Overview

Use a `LowLevelRenderContext` to construct meshes, textures, buffers, argument tables, materials, and pipeline states. These objects are assembled into a [`LowLevelMeshInstanceArray`](lowlevelmeshinstancearray.md) consumed each frame by [`LowLevelRenderer`](lowlevelrenderer.md).

## Topics

### Accessing the render context
- [var device: any MTLDevice](lowlevelrendercontext/device.md)
  The Metal device that backs this render context.
- [var shaderGraph: any LowLevelRenderContextShaderGraph](lowlevelrendercontext/shadergraph.md)
### Creating resources
- [func makeBufferResource(descriptor: LowLevelBufferResource.Descriptor) throws -> LowLevelBufferResource](lowlevelrendercontext/makebufferresource(descriptor:).md)
  Creates a GPU-managed buffer resource from the given descriptor.
- [func makeTextureResource(descriptor: LowLevelTextureResource.Descriptor) throws -> LowLevelTextureResource](lowlevelrendercontext/maketextureresource(descriptor:).md)
  Creates a texture resource from the given descriptor.
- [func makeMaterialResource(descriptor: LowLevelMaterialResource.Descriptor) throws -> sending LowLevelMaterialResource](lowlevelrendercontext/makematerialresource(descriptor:)-8hizx.md)
  Synchronous variant of [`makeMaterialResource(descriptor:)`](lowlevelrendercontext/makematerialresource(descriptor:)-8hizx.md). Blocks the current thread until compilation completes.
- [func makeMaterialResource(descriptor: LowLevelMaterialResource.Descriptor) async throws -> sending LowLevelMaterialResource](lowlevelrendercontext/makematerialresource(descriptor:)-9nufj.md)
  Asynchronously compiles a material resource from a geometry modifier, surface shader, and lighting function.
### Creating meshes
- [func makeMeshResource(descriptor: LowLevelMeshResource.Descriptor) throws -> LowLevelMeshResource](lowlevelrendercontext/makemeshresource(descriptor:).md)
  Creates a mesh resource from the given descriptor.
- [func makeMeshPart(resource: LowLevelMeshResource, indexOffset: Int, indexCount: Int, primitive: MTLPrimitiveType, windingOrder: MTLWinding, bounds: BoundingSphereBox) throws -> LowLevelMeshPart](lowlevelrendercontext/makemeshpart(resource:indexoffset:indexcount:primitive:windingorder:bounds:).md)
  Creates a mesh part that selects a contiguous range of indices from a mesh resource.
- [func makeMeshInstance(meshPart: LowLevelMeshPart, pipeline: LowLevelRenderPipelineState, geometryArguments: LowLevelArgumentTable?, surfaceArguments: LowLevelArgumentTable?, lightingArguments: LowLevelArgumentTable?, transform: simd_float4x4, sortCategory: LowLevelMeshInstance.SortCategory) throws -> LowLevelMeshInstance](lowlevelrendercontext/makemeshinstance(meshpart:pipeline:geometryarguments:surfacearguments:lightingarguments:transform:sortcategory:).md)
  Creates a drawable mesh instance pairing a mesh part with a compiled pipeline state and optional per-draw argument tables.
- [func makeMeshInstanceArray(renderTargets: LowLevelRenderTarget.DescriptorSet, count: Int) throws -> LowLevelMeshInstanceArray](lowlevelrendercontext/makemeshinstancearray(rendertargets:count:).md)
  Creates a fixed-capacity ordered collection of mesh instances for the given render targets.
- [func makeInstanceTransformResource(instanceCapacity: Int) throws -> LowLevelInstanceTransformResource](lowlevelrendercontext/makeinstancetransformresource(instancecapacity:).md)
  Creates a transform buffer resource for GPU instancing.
### Creating pipeline state
- [func makeRenderPipelineState(descriptor: LowLevelRenderPipelineState.Descriptor) throws -> sending LowLevelRenderPipelineState](lowlevelrendercontext/makerenderpipelinestate(descriptor:)-7j32p.md)
  Synchronous variant of [`makeRenderPipelineState(descriptor:)`](lowlevelrendercontext/makerenderpipelinestate(descriptor:)-7j32p.md). Blocks the current thread until compilation completes.
- [func makeRenderPipelineState(descriptor: LowLevelRenderPipelineState.Descriptor) async throws -> sending LowLevelRenderPipelineState](lowlevelrendercontext/makerenderpipelinestate(descriptor:)-55ty6.md)
  Asynchronously compiles a Metal render pipeline state from the given descriptor.
- [func makeArgumentTable(descriptor: LowLevelArgumentTable.Descriptor, buffers: [LowLevelBufferSlice], textures: [LowLevelTextureResource]) throws -> LowLevelArgumentTable](lowlevelrendercontext/makeargumenttable(descriptor:buffers:textures:).md)
  Creates an argument table that binds the provided buffer slices and textures.
### Creating surface shaders
- [func makeSurfaceShader(descriptor: LowLevelMaterialResource.SurfaceShader.Descriptor) throws -> sending LowLevelMaterialResource.SurfaceShader](lowlevelrendercontext/makesurfaceshader(descriptor:)-66tq8.md)
  Synchronous variant of [`makeSurfaceShader(descriptor:)`](lowlevelrendercontext/makesurfaceshader(descriptor:)-66tq8.md). Blocks the current thread until compilation completes.
- [func makeSurfaceShader(descriptor: LowLevelMaterialResource.SurfaceShader.Descriptor) async throws -> sending LowLevelMaterialResource.SurfaceShader](lowlevelrendercontext/makesurfaceshader(descriptor:)-9kdy6.md)
  Asynchronously creates a custom surface shader from a user-authored Metal function descriptor.
- [func makeSimpleSurfaceShader(descriptor: LowLevelMaterialResource.SimpleSurfaceDescriptor) throws -> sending LowLevelMaterialResource.SurfaceShader](lowlevelrendercontext/makesimplesurfaceshader(descriptor:)-74vhb.md)
  Synchronous variant of [`makeSimpleSurfaceShader(descriptor:)`](lowlevelrendercontext/makesimplesurfaceshader(descriptor:)-74vhb.md). Blocks the current thread until compilation completes.
- [func makeSimpleSurfaceShader(descriptor: LowLevelMaterialResource.SimpleSurfaceDescriptor) async throws -> sending LowLevelMaterialResource.SurfaceShader](lowlevelrendercontext/makesimplesurfaceshader(descriptor:)-14ppx.md)
  Asynchronously creates a simple surface shader using a built-in tint color or texture implementation, as described by the given descriptor.
### Creating geometry modifiers
- [func makeGeometryModifier(descriptor: LowLevelMaterialResource.GeometryModifier.Descriptor) throws -> sending LowLevelMaterialResource.GeometryModifier](lowlevelrendercontext/makegeometrymodifier(descriptor:)-307ec.md)
  Synchronous variant of [`makeGeometryModifier(descriptor:)`](lowlevelrendercontext/makegeometrymodifier(descriptor:)-307ec.md). Blocks the current thread until compilation completes.
- [func makeGeometryModifier(descriptor: LowLevelMaterialResource.GeometryModifier.Descriptor) async throws -> sending LowLevelMaterialResource.GeometryModifier](lowlevelrendercontext/makegeometrymodifier(descriptor:)-9tq7q.md)
  Asynchronously creates a geometry modifier from a user-authored Metal function described by the given descriptor.
- [func makeDefaultGeometryModifier() -> sending LowLevelMaterialResource.GeometryModifier](lowlevelrendercontext/makedefaultgeometrymodifier.md)
  Returns a pass-through geometry modifier that performs no vertex transformation.
### Synchronizing command buffers
- [func waitForCommandBuffer(any MTLCommandBuffer)](lowlevelrendercontext/waitforcommandbuffer(_:).md)
  Adds a command buffer that the renderer should wait on before using resources for rendering.
### Instance Properties
- [var lighting: any LowLevelRenderContextLighting](lowlevelrendercontext/lighting.md)
  The lighting function provider for this context.
### Instance Methods
- [func makeGeometryModifier(descriptor:)](lowlevelrendercontext/makegeometrymodifier(descriptor:).md)
  Synchronous variant of [`makeGeometryModifier(descriptor:)`](lowlevelrendercontext/makegeometrymodifier(descriptor:).md). Blocks the current thread until compilation completes.
- [func makeMaterialResource(descriptor:)](lowlevelrendercontext/makematerialresource(descriptor:).md)
  Synchronous variant of [`makeMaterialResource(descriptor:)`](lowlevelrendercontext/makematerialresource(descriptor:).md). Blocks the current thread until compilation completes.
- [func makeRenderPipelineState(descriptor:)](lowlevelrendercontext/makerenderpipelinestate(descriptor:).md)
  Synchronous variant of [`makeRenderPipelineState(descriptor:)`](lowlevelrendercontext/makerenderpipelinestate(descriptor:).md). Blocks the current thread until compilation completes.
- [func makeSimpleSurfaceShader(descriptor:)](lowlevelrendercontext/makesimplesurfaceshader(descriptor:).md)
  Synchronous variant of [`makeSimpleSurfaceShader(descriptor:)`](lowlevelrendercontext/makesimplesurfaceshader(descriptor:).md). Blocks the current thread until compilation completes.
- [func makeSurfaceShader(descriptor:)](lowlevelrendercontext/makesurfaceshader(descriptor:).md)
  Synchronous variant of [`makeSurfaceShader(descriptor:)`](lowlevelrendercontext/makesurfaceshader(descriptor:).md). Blocks the current thread until compilation completes.

## Relationships

### Conforming Types
- [LowLevelRenderContextStandalone](lowlevelrendercontextstandalone.md)

## See Also

- [class LowLevelRenderer](lowlevelrenderer.md)
  A renderer that encodes draw calls for a collection of mesh instances into a Metal command buffer.
- [protocol LowLevelRenderContextLighting](lowlevelrendercontextlighting.md)
  An entry point for creating lighting functions for use in materials.
- [protocol LowLevelRenderContextShaderGraph](lowlevelrendercontextshadergraph.md)
- [class LowLevelRenderContextStandalone](lowlevelrendercontextstandalone.md)
  A standalone Metal-backed render context for creating low-level rendering resources.
- [struct LowLevelRenderContextError](lowlevelrendercontexterror.md)
  An error thrown by render context factory methods when resource creation fails.
- [struct LowLevelRendererError](lowlevelrenderererror.md)
  An error thrown by the renderer during initialization or rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext)*