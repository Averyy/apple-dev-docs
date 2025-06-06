# RotatedShape

**Framework**: SwiftUI  
**Kind**: struct

A shape with a rotation transform applied to it.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct RotatedShape<Content> where Content : Shape
```

## Topics

### Creating a rotated shape
- [init(shape: Content, angle: Angle, anchor: UnitPoint)](rotatedshape/init(shape:angle:anchor:).md)
### Getting the shape’s characteristics
- [var anchor: UnitPoint](rotatedshape/anchor.md)
- [var angle: Angle](rotatedshape/angle.md)
- [var shape: Content](rotatedshape/shape.md)
### Supporting types
- [var animatableData: RotatedShape<Content>.AnimatableData](rotatedshape/animatabledata.md)
  The data to animate.

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [Copyable](../Swift/Copyable.md)
- [InsettableShape](insettableshape.md)
- [Sendable](../Swift/Sendable.md)
- [Shape](shape.md)
- [View](view.md)

## See Also

- [struct ScaledShape](scaledshape.md)
  A shape with a scale transform applied to it.
- [struct OffsetShape](offsetshape.md)
  A shape with a translation offset transform applied to it.
- [struct TransformedShape](transformedshape.md)
  A shape with an affine transform applied to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/rotatedshape)*