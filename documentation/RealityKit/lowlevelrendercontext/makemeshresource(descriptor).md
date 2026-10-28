# makeMeshResource(descriptor:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a mesh resource from the given descriptor.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func makeMeshResource(descriptor: LowLevelMeshResource.Descriptor) throws -> LowLevelMeshResource
```

## Return Value

A newly created [`LowLevelMeshResource`](../lowlevelmeshresource.md).

## Discussion

> **Throws**: An error if the descriptor is invalid or if the underlying GPU allocation fails.

## Parameters

- `descriptor`: The vertex and index buffer layout to allocate.

## See Also

### Creating meshes
- [func makeMeshPart(resource: LowLevelMeshResource, indexOffset: Int, indexCount: Int, primitive: MTLPrimitiveType, windingOrder: MTLWinding, bounds: BoundingSphereBox) throws -> LowLevelMeshPart](./makemeshpart%28resource,indexoffset,indexcount,primitive,windingorder,bounds%29.md)
  Creates a mesh part that selects a contiguous range of indices from a mesh resource.
- [func makeMeshInstance(meshPart: LowLevelMeshPart, pipeline: LowLevelRenderPipelineState, geometryArguments: LowLevelArgumentTable?, surfaceArguments: LowLevelArgumentTable?, lightingArguments: LowLevelArgumentTable?, transform: simd_float4x4, sortCategory: LowLevelMeshInstance.SortCategory) throws -> LowLevelMeshInstance](./makemeshinstance%28meshpart,pipeline,geometryarguments,surfacearguments,lightingarguments,transform,sortcategory%29.md)
  Creates a drawable mesh instance pairing a mesh part with a compiled pipeline state and optional per-draw argument tables.
- [func makeMeshInstanceArray(renderTargets: LowLevelRenderTarget.DescriptorSet, count: Int) throws -> LowLevelMeshInstanceArray](./makemeshinstancearray%28rendertargets,count%29.md)
  Creates a fixed-capacity ordered collection of mesh instances for the given render targets.
- [func makeInstanceTransformResource(instanceCapacity: Int) throws -> LowLevelInstanceTransformResource](./makeinstancetransformresource%28instancecapacity%29.md)
  Creates a transform buffer resource for GPU instancing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makemeshresource(descriptor:))*