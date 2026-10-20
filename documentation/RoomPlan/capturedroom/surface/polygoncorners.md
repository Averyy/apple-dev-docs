# polygonCorners

**Framework**: RoomPlan  
**Kind**: property  
**Role**: Instance Property

A 2D polygon that represents nonuniform wall heights and floor shapes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
var polygonCorners: [simd_float3] { get }
```

#### Discussion

This property’s triplet type describes the polygon in local plane coordinates.

## See Also

### Shaping a surface
- [var completedEdges: Set<CapturedRoom.Surface.Edge>](./completededges.md)
  An array of edges that outline the surface.
- [CapturedRoom.Surface.Edge](./edge.md)
  An object that represents a single edge of a surface.
- [var curve: CapturedRoom.Surface.Curve?](./curve-swift.property.md)
  An object that represents the curve of a surface.
- [CapturedRoom.Surface.Curve](./curve-swift.struct.md)
  An object that represents a single curve of a surface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/surface/polygoncorners)*