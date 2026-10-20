# setIndexRange(indexOffset:indexCount:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Updates the first index and index count for this mesh part.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func setIndexRange(indexOffset: Int, indexCount: Int) throws(LowLevelRenderContextError)
```

#### Discussion

> **Throws**: [`LowLevelRenderContextError`](../lowlevelrendercontexterror.md) if the resulting range falls outside the mesh resource’s index buffer.

## Parameters

- `indexOffset`: The byte offset of the first index within the index buffer.
- `indexCount`: The number of indices to use for this part.

## See Also

### Configuring the geometry
- [var primitive: MTLPrimitiveType](./primitive.md)
  The geometric primitive to use when rendering this part.
- [var windingOrder: MTLWinding](./windingorder.md)
  The winding order of front-facing polygons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshpart/setindexrange(indexoffset:indexcount:))*