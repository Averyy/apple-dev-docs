# primitive

**Framework**: RealityKit  
**Kind**: property

The geometric primitive to use when rendering this part.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var primitive: MTLPrimitiveType { get }
```

#### Discussion

Corresponds to `MTLPrimitiveType`.

## See Also

- [var windingOrder: MTLWinding](lowlevelmeshpart/windingorder.md)
  The winding order of front-facing polygons.
- [func setIndexRange(indexOffset: Int, indexCount: Int) throws(LowLevelRenderContextError)](lowlevelmeshpart/setindexrange(indexoffset:indexcount:).md)
  Updates the first index and index count for this mesh part.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshpart/primitive)*