# MeshGradient.BezierPoint

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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
- [init(position: SIMD2<Float>, leadingControlPoint: SIMD2<Float>, topControlPoint: SIMD2<Float>, trailingControlPoint: SIMD2<Float>, bottomControlPoint: SIMD2<Float>)](./bezierpoint/init%28position,leadingcontrolpoint,topcontrolpoint,trailingcontrolpoint,bottomcontrolpoint%29.md)
  Creates a new vertex.
### Instance Properties
- [var bottomControlPoint: SIMD2<Float>](./bezierpoint/bottomcontrolpoint.md)
  The Bezier control point of the vertex’s bottom edge.
- [var leadingControlPoint: SIMD2<Float>](./bezierpoint/leadingcontrolpoint.md)
  The Bezier control point of the vertex’s leading edge.
- [var position: SIMD2<Float>](./bezierpoint/position.md)
  The position of the vertex.
- [var topControlPoint: SIMD2<Float>](./bezierpoint/topcontrolpoint.md)
  The Bezier control point of the vertex’s top edge.
- [var trailingControlPoint: SIMD2<Float>](./bezierpoint/trailingcontrolpoint.md)
  The Bezier control point of the vertex’s trailing edge.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/meshgradient/bezierpoint)*