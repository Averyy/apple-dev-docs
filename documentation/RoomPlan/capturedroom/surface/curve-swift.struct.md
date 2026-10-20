# CapturedRoom.Surface.Curve

**Framework**: RoomPlan  
**Kind**: struct  
**Role**: Structure

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

Each [`CapturedRoom.Surface`](../surface.md) instance in a captured room’s surface arrays ([`doors`](../doors.md), [`openings`](../openings.md), [`walls`](../walls.md), and [`windows`](../windows.md)) that models a curved real-world surface contains an optional property ([`curve`](./curve-swift.property.md)) of this type.

## Topics

### Measuring a curve
- [var startAngle: Measurement<UnitAngle>](./curve-swift.struct/startangle.md)
  An angle that begins the curve.
- [var endAngle: Measurement<UnitAngle>](./curve-swift.struct/endangle.md)
  The angle at the end of the curve.
- [var radius: Float](./curve-swift.struct/radius.md)
  The radius of the curve.
### Instance Properties
- [var center: simd_float2](./curve-swift.struct/center.md)
  Center of the curve, in local coordinates. Corresponds to xz center coordinates

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Shaping a surface
- [var completedEdges: Set<CapturedRoom.Surface.Edge>](./completededges.md)
  An array of edges that outline the surface.
- [CapturedRoom.Surface.Edge](./edge.md)
  An object that represents a single edge of a surface.
- [var curve: CapturedRoom.Surface.Curve?](./curve-swift.property.md)
  An object that represents the curve of a surface.
- [var polygonCorners: [simd_float3]](./polygoncorners.md)
  A 2D polygon that represents nonuniform wall heights and floor shapes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/surface/curve-swift.struct)*