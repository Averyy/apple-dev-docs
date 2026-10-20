# LowLevelRenderContext Implementations

**Framework**: RealityKit  
**Role**: API Collection

## Topics

### Instance Properties
- [var device: any MTLDevice](./device.md)
  The Metal device that backs this render context.
### Instance Methods
- [func makeArgumentTable(descriptor: LowLevelArgumentTable.Descriptor, buffers: [LowLevelBufferSlice], textures: [LowLevelTextureResource]) throws -> LowLevelArgumentTable](./makeargumenttable%28descriptor,buffers,textures%29.md)
  Creates an argument table that binds the provided buffer slices and textures.
- [func makeBufferResource(descriptor: LowLevelBufferResource.Descriptor) throws -> LowLevelBufferResource](./makebufferresource%28descriptor%29.md)
  Creates a GPU-managed buffer resource from the given descriptor.
- [func makeDefaultGeometryModifier() -> sending LowLevelMaterialResource.GeometryModifier](./makedefaultgeometrymodifier%28%29.md)
  Returns a pass-through geometry modifier that performs no vertex transformation.
- [func makeGeometryModifier(descriptor:)](./makegeometrymodifier%28descriptor%29.md)
  Synchronous variant of [`makeGeometryModifier(descriptor:)`](./makegeometrymodifier%28descriptor%29.md). Blocks the current thread until compilation completes.
- [func makeGeometryModifier(descriptor: LowLevelMaterialResource.GeometryModifier.Descriptor) async throws -> sending LowLevelMaterialResource.GeometryModifier](./makegeometrymodifier%28descriptor%29-4p20q.md)
  Asynchronously creates a geometry modifier from a user-authored Metal function described by the given descriptor.
- [func makeGeometryModifier(descriptor: LowLevelMaterialResource.GeometryModifier.Descriptor) throws -> sending LowLevelMaterialResource.GeometryModifier](./makegeometrymodifier%28descriptor%29-6cl2f.md)
  Synchronous variant of [`makeGeometryModifier(descriptor:)`](./makegeometrymodifier%28descriptor%29-6cl2f.md). Blocks the current thread until compilation completes.
- [func makeInstanceTransformResource(instanceCapacity: Int) throws -> LowLevelInstanceTransformResource](./makeinstancetransformresource%28instancecapacity%29.md)
  Creates a transform buffer resource for GPU instancing.
- [func makeMaterialResource(descriptor:)](./makematerialresource%28descriptor%29.md)
  Synchronous variant of [`makeMaterialResource(descriptor:)`](./makematerialresource%28descriptor%29.md). Blocks the current thread until compilation completes.
- [func makeMaterialResource(descriptor: LowLevelMaterialResource.Descriptor) throws -> sending LowLevelMaterialResource](./makematerialresource%28descriptor%29-2qjge.md)
  Synchronous variant of [`makeMaterialResource(descriptor:)`](./makematerialresource%28descriptor%29-2qjge.md). Blocks the current thread until compilation completes.
- [func makeMaterialResource(descriptor: LowLevelMaterialResource.Descriptor) async throws -> sending LowLevelMaterialResource](./makematerialresource%28descriptor%29-8pruc.md)
  Asynchronously compiles a material resource from a geometry modifier, surface shader, and lighting function.
- [func makeMeshInstance(meshPart: LowLevelMeshPart, pipeline: LowLevelRenderPipelineState, geometryArguments: LowLevelArgumentTable?, surfaceArguments: LowLevelArgumentTable?, lightingArguments: LowLevelArgumentTable?, transform: simd_float4x4, sortCategory: LowLevelMeshInstance.SortCategory) throws -> LowLevelMeshInstance](./makemeshinstance%28meshpart,pipeline,geometryarguments,surfacearguments,lightingarguments,transform,sortcategory%29.md)
  Creates a drawable mesh instance pairing a mesh part with a compiled pipeline state and optional per-draw argument tables.
- [func makeMeshInstanceArray(renderTargets: LowLevelRenderTarget.DescriptorSet, count: Int) throws -> LowLevelMeshInstanceArray](./makemeshinstancearray%28rendertargets,count%29.md)
  Creates a fixed-capacity ordered collection of mesh instances for the given render targets.
- [func makeMeshPart(resource: LowLevelMeshResource, indexOffset: Int, indexCount: Int, primitive: MTLPrimitiveType, windingOrder: MTLWinding, bounds: BoundingSphereBox) throws -> LowLevelMeshPart](./makemeshpart%28resource,indexoffset,indexcount,primitive,windingorder,bounds%29.md)
  Creates a mesh part that selects a contiguous range of indices from a mesh resource.
- [func makeMeshResource(descriptor: LowLevelMeshResource.Descriptor) throws -> LowLevelMeshResource](./makemeshresource%28descriptor%29.md)
  Creates a mesh resource from the given descriptor.
- [func makeRenderPipelineState(descriptor:)](./makerenderpipelinestate%28descriptor%29.md)
  Synchronous variant of [`makeRenderPipelineState(descriptor:)`](./makerenderpipelinestate%28descriptor%29.md). Blocks the current thread until compilation completes.
- [func makeRenderPipelineState(descriptor: LowLevelRenderPipelineState.Descriptor) throws -> sending LowLevelRenderPipelineState](./makerenderpipelinestate%28descriptor%29-550yp.md)
  Synchronous variant of [`makeRenderPipelineState(descriptor:)`](./makerenderpipelinestate%28descriptor%29-550yp.md). Blocks the current thread until compilation completes.
- [func makeRenderPipelineState(descriptor: LowLevelRenderPipelineState.Descriptor) async throws -> sending LowLevelRenderPipelineState](./makerenderpipelinestate%28descriptor%29-9x6v9.md)
  Asynchronously compiles a Metal render pipeline state from the given descriptor.
- [func makeSimpleSurfaceShader(descriptor:)](./makesimplesurfaceshader%28descriptor%29.md)
  Synchronous variant of [`makeSimpleSurfaceShader(descriptor:)`](./makesimplesurfaceshader%28descriptor%29.md). Blocks the current thread until compilation completes.
- [func makeSimpleSurfaceShader(descriptor: LowLevelMaterialResource.SimpleSurfaceDescriptor) async throws -> sending LowLevelMaterialResource.SurfaceShader](./makesimplesurfaceshader%28descriptor%29-3f0mt.md)
  Asynchronously creates a simple surface shader using a built-in tint color or texture implementation, as described by the given descriptor.
- [func makeSimpleSurfaceShader(descriptor: LowLevelMaterialResource.SimpleSurfaceDescriptor) throws -> sending LowLevelMaterialResource.SurfaceShader](./makesimplesurfaceshader%28descriptor%29-6filb.md)
  Synchronous variant of [`makeSimpleSurfaceShader(descriptor:)`](./makesimplesurfaceshader%28descriptor%29-6filb.md). Blocks the current thread until compilation completes.
- [func makeSurfaceShader(descriptor:)](./makesurfaceshader%28descriptor%29.md)
  Synchronous variant of [`makeSurfaceShader(descriptor:)`](./makesurfaceshader%28descriptor%29.md). Blocks the current thread until compilation completes.
- [func makeSurfaceShader(descriptor: LowLevelMaterialResource.SurfaceShader.Descriptor) throws -> sending LowLevelMaterialResource.SurfaceShader](./makesurfaceshader%28descriptor%29-35raz.md)
  Synchronous variant of [`makeSurfaceShader(descriptor:)`](./makesurfaceshader%28descriptor%29-35raz.md). Blocks the current thread until compilation completes.
- [func makeSurfaceShader(descriptor: LowLevelMaterialResource.SurfaceShader.Descriptor) async throws -> sending LowLevelMaterialResource.SurfaceShader](./makesurfaceshader%28descriptor%29-9hqo9.md)
  Asynchronously creates a custom surface shader from a user-authored Metal function descriptor.
- [func makeTextureResource(descriptor: LowLevelTextureResource.Descriptor) throws -> LowLevelTextureResource](./maketextureresource%28descriptor%29.md)
  Creates a texture resource from the given descriptor.
- [func waitForCommandBuffer(any MTLCommandBuffer)](./waitforcommandbuffer%28_%29.md)
  Adds a command buffer that the renderer should wait on before using resources for rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/lowlevelrendercontext-implementations)*