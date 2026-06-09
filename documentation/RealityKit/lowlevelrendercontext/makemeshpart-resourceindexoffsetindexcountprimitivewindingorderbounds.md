# makeMeshPart(resource:indexOffset:indexCount:primitive:windingOrder:bounds:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Creates a mesh part that selects a contiguous range of indices from a mesh resource.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func makeMeshPart(resource: LowLevelMeshResource, indexOffset: Int, indexCount: Int, primitive: MTLPrimitiveType, windingOrder: MTLWinding, bounds: BoundingSphereBox) throws -> LowLevelMeshPart
```

#### Return Value

A newly created [`LowLevelMeshPart`](lowlevelmeshpart.md).

#### Discussion

> **Note**: An error if the index range falls outside the resource’s index buffer.

## Parameters

- `resource`: The mesh resource whose index and vertex buffers this part draws from.
- `indexOffset`: The byte offset of the first index within the index buffer.
- `indexCount`: The number of indices to use for this part.
- `primitive`: The geometric primitive type to use when rendering.
- `windingOrder`: The winding order that identifies front-facing polygons.
- `bounds`: The model-space bounding volume for this part.

## See Also

- [func makeMeshResource(descriptor: LowLevelMeshResource.Descriptor) throws -> LowLevelMeshResource](lowlevelrendercontext/makemeshresource(descriptor:).md)
  Creates a mesh resource from the given descriptor.
- [func makeMeshInstance(meshPart: LowLevelMeshPart, pipeline: LowLevelRenderPipelineState, geometryArguments: LowLevelArgumentTable?, surfaceArguments: LowLevelArgumentTable?, lightingArguments: LowLevelArgumentTable?, transform: simd_float4x4, sortCategory: LowLevelMeshInstance.SortCategory) throws -> LowLevelMeshInstance](lowlevelrendercontext/makemeshinstance(meshpart:pipeline:geometryarguments:surfacearguments:lightingarguments:transform:sortcategory:).md)
  Creates a drawable mesh instance pairing a mesh part with a compiled pipeline state and optional per-draw argument tables.
- [func makeMeshInstanceArray(renderTargets: LowLevelRenderTarget.DescriptorSet, count: Int) throws -> LowLevelMeshInstanceArray](lowlevelrendercontext/makemeshinstancearray(rendertargets:count:).md)
  Creates a fixed-capacity ordered collection of mesh instances for the given render targets.
- [func makeInstanceTransformResource(instanceCapacity: Int) throws -> LowLevelInstanceTransformResource](lowlevelrendercontext/makeinstancetransformresource(instancecapacity:).md)
  Creates a transform buffer resource for GPU instancing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontext/makemeshpart(resource:indexoffset:indexcount:primitive:windingorder:bounds:))*