# CapturedRoom.Surface.Edge

**Framework**: RoomPlan  
**Kind**: enum

An object that represents a single edge of a surface.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum Edge
```

#### Overview

Each [`CapturedRoom.Surface`](capturedroom/surface.md) instance in a captured room’s surface arrays ([`doors`](capturedroom/doors.md), [`openings`](capturedroom/openings.md), [`walls`](capturedroom/walls.md), and [`windows`](capturedroom/windows.md)) has a set ([`completedEdges`](capturedroom/surface/completededges.md)) that contains one of each case in this enumeration.

## Topics

### Accessing edge types
- [CapturedRoom.Surface.Edge.top](capturedroom/surface/edge/top.md)
  An edge that identifies the top of a surface.
- [CapturedRoom.Surface.Edge.bottom](capturedroom/surface/edge/bottom.md)
  An edge that identifies the bottom of a surface.
- [CapturedRoom.Surface.Edge.left](capturedroom/surface/edge/left.md)
  An edge that identifies the left side of a surface.
- [CapturedRoom.Surface.Edge.right](capturedroom/surface/edge/right.md)
  An edge that identifies the right side of a surface.

## Relationships

### Conforms To
- [CaseIterable](../Swift/CaseIterable.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var completedEdges: Set<CapturedRoom.Surface.Edge>](capturedroom/surface/completededges.md)
  An array of edges that outline the surface.
- [var curve: CapturedRoom.Surface.Curve?](capturedroom/surface/curve-swift.property.md)
  An object that represents the curve of a surface.
- [CapturedRoom.Surface.Curve](capturedroom/surface/curve-swift.struct.md)
  An object that represents a single curve of a surface.
- [var polygonCorners: [simd_float3]](capturedroom/surface/polygoncorners.md)
  A 2D polygon that represents nonuniform wall heights and floor shapes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/surface/edge)*