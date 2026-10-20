# OffsetShape

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A shape with a translation offset transform applied to it.

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
struct OffsetShape<Content> where Content : Shape
```

## Topics

### Creating an offset shape
- [init(shape: Content, offset: CGSize)](./offsetshape/init%28shape,offset%29.md)
### Getting the shape’s characteristics
- [var offset: CGSize](./offsetshape/offset.md)
- [var shape: Content](./offsetshape/shape.md)
### Supporting types
- [var animatableData: OffsetShape<Content>.AnimatableData](./offsetshape/animatabledata.md)
  The data to animate.

## Relationships

### Conforms To
- [Animatable](./animatable.md)
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [InsettableShape](./insettableshape.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [Shape](./shape.md)
- [View](./view.md)

## See Also

### Transforming a shape
- [struct ScaledShape](./scaledshape.md)
  A shape with a scale transform applied to it.
- [struct RotatedShape](./rotatedshape.md)
  A shape with a rotation transform applied to it.
- [struct TransformedShape](./transformedshape.md)
  A shape with an affine transform applied to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/offsetshape)*