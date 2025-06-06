# MeshGradient.BezierPoint

**Framework**: SwiftUI  
**Kind**: struct

One location in a gradient mesh, along with the four Bezier control points surrounding it.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@frozen
struct BezierPoint
```

## Topics

### Initializers
- [init(position: SIMD2<Float>, leadingControlPoint: SIMD2<Float>, topControlPoint: SIMD2<Float>, trailingControlPoint: SIMD2<Float>, bottomControlPoint: SIMD2<Float>)](meshgradient/bezierpoint/init(position:leadingcontrolpoint:topcontrolpoint:trailingcontrolpoint:bottomcontrolpoint:).md)
  Creates a new vertex.
### Instance Properties
- [var bottomControlPoint: SIMD2<Float>](meshgradient/bezierpoint/bottomcontrolpoint.md)
  The Bezier control point of the vertex’s bottom edge.
- [var leadingControlPoint: SIMD2<Float>](meshgradient/bezierpoint/leadingcontrolpoint.md)
  The Bezier control point of the vertex’s leading edge.
- [var position: SIMD2<Float>](meshgradient/bezierpoint/position.md)
  The position of the vertex.
- [var topControlPoint: SIMD2<Float>](meshgradient/bezierpoint/topcontrolpoint.md)
  The Bezier control point of the vertex’s top edge.
- [var trailingControlPoint: SIMD2<Float>](meshgradient/bezierpoint/trailingcontrolpoint.md)
  The Bezier control point of the vertex’s trailing edge.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/meshgradient/bezierpoint)*