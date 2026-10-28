# makeInstanceTransformResource(instanceCapacity:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a transform buffer resource for GPU instancing.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func makeInstanceTransformResource(instanceCapacity: Int) throws -> LowLevelInstanceTransformResource
```

## Return Value

A newly created [`LowLevelInstanceTransformResource`](../lowlevelinstancetransformresource.md).

## Discussion

The buffer stores up to `instanceCapacity` model-to-local transforms as `float4x4` values. Assign the result to a [`LowLevelMeshInstance`](../lowlevelmeshinstance.md) via [`setInstanceTransforms(_:)`](../lowlevelmeshinstance/setinstancetransforms%28_%29.md) to enable GPU instancing.

> **Throws**: An error if the allocation fails.

## Parameters

- `instanceCapacity`: The maximum number of instances the buffer holds.

## See Also

### Creating meshes
- [func makeMeshResource(descriptor: LowLevelMeshResource.Descriptor) throws -> LowLevelMeshResource](./makemeshresource%28descriptor%29.md)
  Creates a mesh resource from the given descriptor.
- [func makeMeshPart(resource: LowLevelMeshResource, indexOffset: Int, indexCount: Int, primitive: MTLPrimitiveType, windingOrder: MTLWinding, bounds: BoundingSphereBox) throws -> LowLevelMeshPart](./makemeshpart%28resource,indexoffset,indexcount,primitive,windingorder,bounds%29.md)
  Creates a mesh part that selects a contiguous range of indices from a mesh resource.
- [func makeMeshInstance(meshPart: LowLevelMeshPart, pipeline: LowLevelRenderPipelineState, geometryArguments: LowLevelArgumentTable?, surfaceArguments: LowLevelArgumentTable?, lightingArguments: LowLevelArgumentTable?, transform: simd_float4x4, sortCategory: LowLevelMeshInstance.SortCategory) throws -> LowLevelMeshInstance](./makemeshinstance%28meshpart,pipeline,geometryarguments,surfacearguments,lightingarguments,transform,sortcategory%29.md)
  Creates a drawable mesh instance pairing a mesh part with a compiled pipeline state and optional per-draw argument tables.
- [func makeMeshInstanceArray(renderTargets: LowLevelRenderTarget.DescriptorSet, count: Int) throws -> LowLevelMeshInstanceArray](./makemeshinstancearray%28rendertargets,count%29.md)
  Creates a fixed-capacity ordered collection of mesh instances for the given render targets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makeinstancetransformresource(instancecapacity:))*