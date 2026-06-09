# setIndexRange(indexOffset:indexCount:)

**Framework**: RealityKit  
**Kind**: method

Updates the first index and index count for this mesh part.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func setIndexRange(indexOffset: Int, indexCount: Int) throws(LowLevelRenderContextError)
```

#### Discussion

Throws [`LowLevelRenderContextError`](lowlevelrendercontexterror.md) if the resulting range falls outside the mesh resource’s index buffer.

> **Note**: [`LowLevelRenderContextError`](lowlevelrendercontexterror.md) if the resulting range falls outside the mesh resource’s index buffer.

## Parameters

- `indexOffset`: The byte offset of the first index within the index buffer.
- `indexCount`: The number of indices to use for this part.

## See Also

- [var primitive: MTLPrimitiveType](lowlevelmeshpart/primitive.md)
  The geometric primitive to use when rendering this part.
- [var windingOrder: MTLWinding](lowlevelmeshpart/windingorder.md)
  The winding order of front-facing polygons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshpart/setindexrange(indexoffset:indexcount:))*