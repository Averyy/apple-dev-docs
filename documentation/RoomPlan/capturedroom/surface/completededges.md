# completedEdges

**Framework**: RoomPlan  
**Kind**: property  
**Role**: Instance Property

An array of edges that outline the surface.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
var completedEdges: Set<CapturedRoom.Surface.Edge> { get }
```

## See Also

### Shaping a surface
- [CapturedRoom.Surface.Edge](./edge.md)
  An object that represents a single edge of a surface.
- [var curve: CapturedRoom.Surface.Curve?](./curve-swift.property.md)
  An object that represents the curve of a surface.
- [CapturedRoom.Surface.Curve](./curve-swift.struct.md)
  An object that represents a single curve of a surface.
- [var polygonCorners: [simd_float3]](./polygoncorners.md)
  A 2D polygon that represents nonuniform wall heights and floor shapes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/surface/completededges)*