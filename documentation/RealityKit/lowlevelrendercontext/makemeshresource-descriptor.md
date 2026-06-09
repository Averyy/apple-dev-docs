# makeMeshResource(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Creates a mesh resource from the given descriptor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func makeMeshResource(descriptor: LowLevelMeshResource.Descriptor) throws -> LowLevelMeshResource
```

#### Return Value

A newly created [`LowLevelMeshResource`](lowlevelmeshresource.md).

#### Discussion

> **Note**: An error if the descriptor is invalid or if the underlying GPU allocation fails.

## Parameters

- `descriptor`: The vertex and index buffer layout to allocate.

## See Also

- [func makeMeshPart(resource: LowLevelMeshResource, indexOffset: Int, indexCount: Int, primitive: MTLPrimitiveType, windingOrder: MTLWinding, bounds: BoundingSphereBox) throws -> LowLevelMeshPart](lowlevelrendercontext/makemeshpart(resource:indexoffset:indexcount:primitive:windingorder:bounds:).md)
  Creates a mesh part that selects a contiguous range of indices from a mesh resource.
- [func makeMeshInstance(meshPart: LowLevelMeshPart, pipeline: LowLevelRenderPipelineState, geometryArguments: LowLevelArgumentTable?, surfaceArguments: LowLevelArgumentTable?, lightingArguments: LowLevelArgumentTable?, transform: simd_float4x4, sortCategory: LowLevelMeshInstance.SortCategory) throws -> LowLevelMeshInstance](lowlevelrendercontext/makemeshinstance(meshpart:pipeline:geometryarguments:surfacearguments:lightingarguments:transform:sortcategory:).md)
  Creates a drawable mesh instance pairing a mesh part with a compiled pipeline state and optional per-draw argument tables.
- [func makeMeshInstanceArray(renderTargets: LowLevelRenderTarget.DescriptorSet, count: Int) throws -> LowLevelMeshInstanceArray](lowlevelrendercontext/makemeshinstancearray(rendertargets:count:).md)
  Creates a fixed-capacity ordered collection of mesh instances for the given render targets.
- [func makeInstanceTransformResource(instanceCapacity: Int) throws -> LowLevelInstanceTransformResource](lowlevelrendercontext/makeinstancetransformresource(instancecapacity:).md)
  Creates a transform buffer resource for GPU instancing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makemeshresource(descriptor:))*