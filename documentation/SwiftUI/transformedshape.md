# TransformedShape

**Framework**: SwiftUI  
**Kind**: struct

A shape with an affine transform applied to it.

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
struct TransformedShape<Content> where Content : Shape
```

## Topics

### Creating a transformed shape
- [init(shape: Content, transform: CGAffineTransform)](transformedshape/init(shape:transform:).md)
### Getting the shape’s characteristics
- [var shape: Content](transformedshape/shape.md)
- [var transform: CGAffineTransform](transformedshape/transform.md)

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Shape](shape.md)
- [View](view.md)

## See Also

- [struct ScaledShape](scaledshape.md)
  A shape with a scale transform applied to it.
- [struct RotatedShape](rotatedshape.md)
  A shape with a rotation transform applied to it.
- [struct OffsetShape](offsetshape.md)
  A shape with a translation offset transform applied to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/transformedshape)*