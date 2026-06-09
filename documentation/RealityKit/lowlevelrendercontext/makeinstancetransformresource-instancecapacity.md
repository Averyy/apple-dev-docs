# makeInstanceTransformResource(instanceCapacity:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Creates a transform buffer resource for GPU instancing.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func makeInstanceTransformResource(instanceCapacity: Int) throws -> LowLevelInstanceTransformResource
```

#### Return Value

A newly created [`LowLevelInstanceTransformResource`](lowlevelinstancetransformresource.md).

#### Discussion

The buffer stores up to `instanceCapacity` model-to-local transforms as `float4x4` values. Assign the result to a [`LowLevelMeshInstance`](lowlevelmeshinstance.md) via [`setInstanceTransforms(_:)`](lowlevelmeshinstance/setinstancetransforms(_:).md) to enable GPU instancing.

> **Note**: An error if the allocation fails.

## Parameters

- `instanceCapacity`: The maximum number of instances the buffer holds.

## See Also

- [func makeMeshResource(descriptor: LowLevelMeshResource.Descriptor) throws -> LowLevelMeshResource](lowlevelrendercontext/makemeshresource(descriptor:).md)
  Creates a mesh resource from the given descriptor.
- [func makeMeshPart(resource: LowLevelMeshResource, indexOffset: Int, indexCount: Int, primitive: MTLPrimitiveType, windingOrder: MTLWinding, bounds: BoundingSphereBox) throws -> LowLevelMeshPart](lowlevelrendercontext/makemeshpart(resource:indexoffset:indexcount:primitive:windingorder:bounds:).md)
  Creates a mesh part that selects a contiguous range of indices from a mesh resource.
- [func makeMeshInstance(meshPart: LowLevelMeshPart, pipeline: LowLevelRenderPipelineState, geometryArguments: LowLevelArgumentTable?, surfaceArguments: LowLevelArgumentTable?, lightingArguments: LowLevelArgumentTable?, transform: simd_float4x4, sortCategory: LowLevelMeshInstance.SortCategory) throws -> LowLevelMeshInstance](lowlevelrendercontext/makemeshinstance(meshpart:pipeline:geometryarguments:surfacearguments:lightingarguments:transform:sortcategory:).md)
  Creates a drawable mesh instance pairing a mesh part with a compiled pipeline state and optional per-draw argument tables.
- [func makeMeshInstanceArray(renderTargets: LowLevelRenderTarget.DescriptorSet, count: Int) throws -> LowLevelMeshInstanceArray](lowlevelrendercontext/makemeshinstancearray(rendertargets:count:).md)
  Creates a fixed-capacity ordered collection of mesh instances for the given render targets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makeinstancetransformresource(instancecapacity:))*