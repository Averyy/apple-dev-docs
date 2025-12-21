# RoundedRectangularShape

**Framework**: SwiftUI  
**Kind**: protocol

A protocol of [`InsettableShape`](insettableshape.md) that describes a rounded rectangular shape.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
protocol RoundedRectangularShape : InsettableShape
```

#### Overview

Conform your [`InsettableShape`](insettableshape.md) type to [`RoundedRectangularShape`](roundedrectangularshape.md) when your shape is a rounded rectangular with four corners and you want to expose information about the corners. For example, a custom triangle [`Shape`](shape.md) is not fit for such conformance, while a custom rectangle [`Shape`](shape.md) could benefit from providing the implementation, especially when the shape is used as a container shape in [`containerShape(_:)`](view/containershape(_:)-3br47.md) to achieve concentricity.

System shapes like [`Rectangle`](rectangle.md), [`RoundedRectangle`](roundedrectangle.md), [`UnevenRoundedRectangle`](unevenroundedrectangle.md), [`Capsule`](capsule.md), and [`Circle`](circle.md) already provide default implementation for this protocol.

## Topics

### Instance Methods
- [func corners(in: CGSize?) -> Self.Corners?](roundedrectangularshape/corners(in:).md)
  Resolved corners given a size. If the corner style of a shape is size-dependent, read the provided size and return values accordingly. This function could be called with a nil size when the size hasn’t been determined. In that case, return the best approximated value. For example, for a capsule shape, its corner radius is determined by the size. If size is not available, return `.fixed(.infinity)` to indicate that the corner should be as round as it could be.
### Type Aliases
- [RoundedRectangularShape.Corners](roundedrectangularshape/corners.md)

## Relationships

### Inherits From
- [Animatable](animatable.md)
- [InsettableShape](insettableshape.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Shape](shape.md)
- [View](view.md)
### Conforming Types
- [Capsule](capsule.md)
- [Circle](circle.md)
- [Rectangle](rectangle.md)
- [RoundedRectangle](roundedrectangle.md)
- [UnevenRoundedRectangle](unevenroundedrectangle.md)

## See Also

- [struct Rectangle](rectangle.md)
  A rectangular shape aligned inside the frame of the view containing it.
- [struct RoundedRectangle](roundedrectangle.md)
  A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [enum RoundedCornerStyle](roundedcornerstyle.md)
  Defines the shape of a rounded rectangle’s corners.
- [struct RoundedRectangularShapeCorners](roundedrectangularshapecorners.md)
  A type describing the corner styles of a [`RoundedRectangularShape`](roundedrectangularshape.md).
- [struct UnevenRoundedRectangle](unevenroundedrectangle.md)
  A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [struct RectangleCornerRadii](rectanglecornerradii.md)
  Describes the corner radius values of a rounded rectangle with uneven corners.
- [struct RectangleCornerInsets](rectanglecornerinsets.md)
  The inset sizes for the corners of a rectangle.
- [struct ConcentricRectangle](concentricrectangle.md)
  A shape that is replaced by a concentric version of the current container shape. If the container shape is a rectangle derived shape with four corners, this shape could choose to respect corners individually.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/roundedrectangularshape)*