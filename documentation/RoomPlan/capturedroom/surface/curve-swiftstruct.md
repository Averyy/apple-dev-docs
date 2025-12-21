# CapturedRoom.Surface.Curve

**Framework**: RoomPlan  
**Kind**: struct

An object that represents a single curve of a surface.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
struct Curve
```

#### Overview

Each [`CapturedRoom.Surface`](capturedroom/surface.md) instance in a captured room’s surface arrays ([`doors`](capturedroom/doors.md), [`openings`](capturedroom/openings.md), [`walls`](capturedroom/walls.md), and [`windows`](capturedroom/windows.md)) that models a curved real-world surface contains an optional property ([`curve`](capturedroom/surface/curve-swift.property.md)) of this type.

## Topics

### Measuring a curve
- [var startAngle: Measurement<UnitAngle>](capturedroom/surface/curve-swift.struct/startangle.md)
  An angle that begins the curve.
- [var endAngle: Measurement<UnitAngle>](capturedroom/surface/curve-swift.struct/endangle.md)
  The angle at the end of the curve.
- [var radius: Float](capturedroom/surface/curve-swift.struct/radius.md)
  The radius of the curve.
### Instance Properties
- [var center: simd_float2](capturedroom/surface/curve-swift.struct/center.md)
  Center of the curve, in local coordinates. Corresponds to xz center coordinates

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var completedEdges: Set<CapturedRoom.Surface.Edge>](capturedroom/surface/completededges.md)
  An array of edges that outline the surface.
- [CapturedRoom.Surface.Edge](capturedroom/surface/edge.md)
  An object that represents a single edge of a surface.
- [var curve: CapturedRoom.Surface.Curve?](capturedroom/surface/curve-swift.property.md)
  An object that represents the curve of a surface.
- [var polygonCorners: [simd_float3]](capturedroom/surface/polygoncorners.md)
  A 2D polygon that represents nonuniform wall heights and floor shapes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/surface/curve-swift.struct)*