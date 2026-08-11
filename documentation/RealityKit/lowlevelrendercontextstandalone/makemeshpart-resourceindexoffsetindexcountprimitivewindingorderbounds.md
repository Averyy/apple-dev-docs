# makeMeshPart(resource:indexOffset:indexCount:primitive:windingOrder:bounds:)

**Framework**: RealityKit  
**Kind**: method

Creates a mesh part that selects a contiguous range of indices from a mesh resource.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func makeMeshPart(resource: LowLevelMeshResource, indexOffset: Int, indexCount: Int, primitive: MTLPrimitiveType, windingOrder: MTLWinding, bounds: BoundingSphereBox) throws -> LowLevelMeshPart
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/makemeshpart(resource:indexoffset:indexcount:primitive:windingorder:bounds:))*