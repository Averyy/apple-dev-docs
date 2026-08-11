# LowLevelRenderContext Implementations

**Framework**: RealityKit

## Topics

### Instance Properties
- [var device: any MTLDevice](lowlevelrendercontextstandalone/device.md)
  The Metal device that backs this render context.
### Instance Methods
- [func makeArgumentTable(descriptor: LowLevelArgumentTable.Descriptor, buffers: [LowLevelBufferSlice], textures: [LowLevelTextureResource]) throws -> LowLevelArgumentTable](lowlevelrendercontextstandalone/makeargumenttable(descriptor:buffers:textures:).md)
  Creates an argument table that binds the provided buffer slices and textures.
- [func makeBufferResource(descriptor: LowLevelBufferResource.Descriptor) throws -> LowLevelBufferResource](lowlevelrendercontextstandalone/makebufferresource(descriptor:).md)
  Creates a GPU-managed buffer resource from the given descriptor.
- [func makeDefaultGeometryModifier() -> sending LowLevelMaterialResource.GeometryModifier](lowlevelrendercontextstandalone/makedefaultgeometrymodifier.md)
  Returns a pass-through geometry modifier that performs no vertex transformation.
- [func makeGeometryModifier(descriptor:)](lowlevelrendercontextstandalone/makegeometrymodifier(descriptor:).md)
  Synchronous variant of [`makeGeometryModifier(descriptor:)`](lowlevelrendercontextstandalone/makegeometrymodifier(descriptor:).md). Blocks the current thread until compilation completes.
- [func makeGeometryModifier(descriptor: LowLevelMaterialResource.GeometryModifier.Descriptor) async throws -> sending LowLevelMaterialResource.GeometryModifier](lowlevelrendercontextstandalone/makegeometrymodifier(descriptor:)-4p20q.md)
  Asynchronously creates a geometry modifier from a user-authored Metal function described by the given descriptor.
- [func makeGeometryModifier(descriptor: LowLevelMaterialResource.GeometryModifier.Descriptor) throws -> sending LowLevelMaterialResource.GeometryModifier](lowlevelrendercontextstandalone/makegeometrymodifier(descriptor:)-6cl2f.md)
  Synchronous variant of [`makeGeometryModifier(descriptor:)`](lowlevelrendercontextstandalone/makegeometrymodifier(descriptor:)-6cl2f.md). Blocks the current thread until compilation completes.
- [func makeInstanceTransformResource(instanceCapacity: Int) throws -> LowLevelInstanceTransformResource](lowlevelrendercontextstandalone/makeinstancetransformresource(instancecapacity:).md)
  Creates a transform buffer resource for GPU instancing.
- [func makeMaterialResource(descriptor:)](lowlevelrendercontextstandalone/makematerialresource(descriptor:).md)
  Synchronous variant of [`makeMaterialResource(descriptor:)`](lowlevelrendercontextstandalone/makematerialresource(descriptor:).md). Blocks the current thread until compilation completes.
- [func makeMaterialResource(descriptor: LowLevelMaterialResource.Descriptor) throws -> sending LowLevelMaterialResource](lowlevelrendercontextstandalone/makematerialresource(descriptor:)-2qjge.md)
  Synchronous variant of [`makeMaterialResource(descriptor:)`](lowlevelrendercontextstandalone/makematerialresource(descriptor:)-2qjge.md). Blocks the current thread until compilation completes.
- [func makeMaterialResource(descriptor: LowLevelMaterialResource.Descriptor) async throws -> sending LowLevelMaterialResource](lowlevelrendercontextstandalone/makematerialresource(descriptor:)-8pruc.md)
  Asynchronously compiles a material resource from a geometry modifier, surface shader, and lighting function.
- [func makeMeshInstance(meshPart: LowLevelMeshPart, pipeline: LowLevelRenderPipelineState, geometryArguments: LowLevelArgumentTable?, surfaceArguments: LowLevelArgumentTable?, lightingArguments: LowLevelArgumentTable?, transform: simd_float4x4, sortCategory: LowLevelMeshInstance.SortCategory) throws -> LowLevelMeshInstance](lowlevelrendercontextstandalone/makemeshinstance(meshpart:pipeline:geometryarguments:surfacearguments:lightingarguments:transform:sortcategory:).md)
  Creates a drawable mesh instance pairing a mesh part with a compiled pipeline state and optional per-draw argument tables.
- [func makeMeshInstanceArray(renderTargets: LowLevelRenderTarget.DescriptorSet, count: Int) throws -> LowLevelMeshInstanceArray](lowlevelrendercontextstandalone/makemeshinstancearray(rendertargets:count:).md)
  Creates a fixed-capacity ordered collection of mesh instances for the given render targets.
- [func makeMeshPart(resource: LowLevelMeshResource, indexOffset: Int, indexCount: Int, primitive: MTLPrimitiveType, windingOrder: MTLWinding, bounds: BoundingSphereBox) throws -> LowLevelMeshPart](lowlevelrendercontextstandalone/makemeshpart(resource:indexoffset:indexcount:primitive:windingorder:bounds:).md)
  Creates a mesh part that selects a contiguous range of indices from a mesh resource.
- [func makeMeshResource(descriptor: LowLevelMeshResource.Descriptor) throws -> LowLevelMeshResource](lowlevelrendercontextstandalone/makemeshresource(descriptor:).md)
  Creates a mesh resource from the given descriptor.
- [func makeRenderPipelineState(descriptor:)](lowlevelrendercontextstandalone/makerenderpipelinestate(descriptor:).md)
  Synchronous variant of [`makeRenderPipelineState(descriptor:)`](lowlevelrendercontextstandalone/makerenderpipelinestate(descriptor:).md). Blocks the current thread until compilation completes.
- [func makeRenderPipelineState(descriptor: LowLevelRenderPipelineState.Descriptor) throws -> sending LowLevelRenderPipelineState](lowlevelrendercontextstandalone/makerenderpipelinestate(descriptor:)-550yp.md)
  Synchronous variant of [`makeRenderPipelineState(descriptor:)`](lowlevelrendercontextstandalone/makerenderpipelinestate(descriptor:)-550yp.md). Blocks the current thread until compilation completes.
- [func makeRenderPipelineState(descriptor: LowLevelRenderPipelineState.Descriptor) async throws -> sending LowLevelRenderPipelineState](lowlevelrendercontextstandalone/makerenderpipelinestate(descriptor:)-9x6v9.md)
  Asynchronously compiles a Metal render pipeline state from the given descriptor.
- [func makeSimpleSurfaceShader(descriptor:)](lowlevelrendercontextstandalone/makesimplesurfaceshader(descriptor:).md)
  Synchronous variant of [`makeSimpleSurfaceShader(descriptor:)`](lowlevelrendercontextstandalone/makesimplesurfaceshader(descriptor:).md). Blocks the current thread until compilation completes.
- [func makeSimpleSurfaceShader(descriptor: LowLevelMaterialResource.SimpleSurfaceDescriptor) async throws -> sending LowLevelMaterialResource.SurfaceShader](lowlevelrendercontextstandalone/makesimplesurfaceshader(descriptor:)-3f0mt.md)
  Asynchronously creates a simple surface shader using a built-in tint color or texture implementation, as described by the given descriptor.
- [func makeSimpleSurfaceShader(descriptor: LowLevelMaterialResource.SimpleSurfaceDescriptor) throws -> sending LowLevelMaterialResource.SurfaceShader](lowlevelrendercontextstandalone/makesimplesurfaceshader(descriptor:)-6filb.md)
  Synchronous variant of [`makeSimpleSurfaceShader(descriptor:)`](lowlevelrendercontextstandalone/makesimplesurfaceshader(descriptor:)-6filb.md). Blocks the current thread until compilation completes.
- [func makeSurfaceShader(descriptor:)](lowlevelrendercontextstandalone/makesurfaceshader(descriptor:).md)
  Synchronous variant of [`makeSurfaceShader(descriptor:)`](lowlevelrendercontextstandalone/makesurfaceshader(descriptor:).md). Blocks the current thread until compilation completes.
- [func makeSurfaceShader(descriptor: LowLevelMaterialResource.SurfaceShader.Descriptor) throws -> sending LowLevelMaterialResource.SurfaceShader](lowlevelrendercontextstandalone/makesurfaceshader(descriptor:)-35raz.md)
  Synchronous variant of [`makeSurfaceShader(descriptor:)`](lowlevelrendercontextstandalone/makesurfaceshader(descriptor:)-35raz.md). Blocks the current thread until compilation completes.
- [func makeSurfaceShader(descriptor: LowLevelMaterialResource.SurfaceShader.Descriptor) async throws -> sending LowLevelMaterialResource.SurfaceShader](lowlevelrendercontextstandalone/makesurfaceshader(descriptor:)-9hqo9.md)
  Asynchronously creates a custom surface shader from a user-authored Metal function descriptor.
- [func makeTextureResource(descriptor: LowLevelTextureResource.Descriptor) throws -> LowLevelTextureResource](lowlevelrendercontextstandalone/maketextureresource(descriptor:).md)
  Creates a texture resource from the given descriptor.
- [func waitForCommandBuffer(any MTLCommandBuffer)](lowlevelrendercontextstandalone/waitforcommandbuffer(_:).md)
  Adds a command buffer that the renderer should wait on before using resources for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/lowlevelrendercontext-implementations)*