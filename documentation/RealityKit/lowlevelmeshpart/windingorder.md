# windingOrder

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The winding order of front-facing polygons.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final var windingOrder: MTLWinding { get set }
```

## Discussion

Corresponds to `MTLWinding`.

## See Also

### Configuring the geometry
- [var primitive: MTLPrimitiveType](./primitive.md)
  The geometric primitive to use when rendering this part.
- [func setIndexRange(indexOffset: Int, indexCount: Int) throws(LowLevelRenderContextError)](./setindexrange%28indexoffset,indexcount%29.md)
  Updates the first index and index count for this mesh part.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmeshpart/windingorder)*