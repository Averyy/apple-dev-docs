# CapturedRoom.Surface.Edge

**Framework**: RoomPlan  
**Kind**: enum  
**Role**: Enumeration

An object that represents a single edge of a surface.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+

## Declaration

```swift
enum Edge
```

## Overview

Each [`CapturedRoom.Surface`](../surface.md) instance in a captured room’s surface arrays ([`doors`](../doors.md), [`openings`](../openings.md), [`walls`](../walls.md), and [`windows`](../windows.md)) has a set ([`completedEdges`](./completededges.md)) that contains one of each case in this enumeration.

## Topics

### Accessing edge types
- [CapturedRoom.Surface.Edge.top](./edge/top.md)
  An edge that identifies the top of a surface.
- [CapturedRoom.Surface.Edge.bottom](./edge/bottom.md)
  An edge that identifies the bottom of a surface.
- [CapturedRoom.Surface.Edge.left](./edge/left.md)
  An edge that identifies the left side of a surface.
- [CapturedRoom.Surface.Edge.right](./edge/right.md)
  An edge that identifies the right side of a surface.

## Relationships

### Conforms To
- [CaseIterable](../../../Swift/caseiterable.md)
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Shaping a surface
- [var completedEdges: Set<CapturedRoom.Surface.Edge>](./completededges.md)
  An array of edges that outline the surface.
- [var curve: CapturedRoom.Surface.Curve?](./curve-swift.property.md)
  An object that represents the curve of a surface.
- [CapturedRoom.Surface.Curve](./curve-swift.struct.md)
  An object that represents a single curve of a surface.
- [var polygonCorners: [simd_float3]](./polygoncorners.md)
  A 2D polygon that represents nonuniform wall heights and floor shapes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/roomplan/capturedroom/surface/edge)*