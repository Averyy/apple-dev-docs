# RectangleCornerRadii

**Framework**: SwiftUI  
**Kind**: struct

Describes the corner radius values of a rounded rectangle with uneven corners.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@frozen
struct RectangleCornerRadii
```

## Topics

### Creating a set of radii
- [init(topLeading: CGFloat, bottomLeading: CGFloat, bottomTrailing: CGFloat, topTrailing: CGFloat)](rectanglecornerradii/init(topleading:bottomleading:bottomtrailing:toptrailing:).md)
  Creates a new set of corner radii for a rounded rectangle with uneven corners.
### Getting values for specific corners
- [var topLeading: CGFloat](rectanglecornerradii/topleading.md)
  The radius of the top-leading corner.
- [var topTrailing: CGFloat](rectanglecornerradii/toptrailing.md)
  The radius of the top-trailing corner.
- [var bottomLeading: CGFloat](rectanglecornerradii/bottomleading.md)
  The radius of the bottom-leading corner.
- [var bottomTrailing: CGFloat](rectanglecornerradii/bottomtrailing.md)
  The radius of the bottom-trailing corner.
### Subscripts
- [subscript(Edge.Corner) -> CGFloat](rectanglecornerradii/subscript(_:).md)
  Returns the corner radius for a certain corner.

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct Rectangle](rectangle.md)
  A rectangular shape aligned inside the frame of the view containing it.
- [struct RoundedRectangle](roundedrectangle.md)
  A rectangular shape with rounded corners, aligned inside the frame of the view containing it.
- [enum RoundedCornerStyle](roundedcornerstyle.md)
  Defines the shape of a rounded rectangle’s corners.
- [protocol RoundedRectangularShape](roundedrectangularshape.md)
  A protocol of [`InsettableShape`](insettableshape.md) that describes a rounded rectangular shape.
- [struct RoundedRectangularShapeCorners](roundedrectangularshapecorners.md)
  A type describing the corner styles of a [`RoundedRectangularShape`](roundedrectangularshape.md).
- [struct UnevenRoundedRectangle](unevenroundedrectangle.md)
  A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [struct RectangleCornerInsets](rectanglecornerinsets.md)
  The inset sizes for the corners of a rectangle.
- [struct ConcentricRectangle](concentricrectangle.md)
  A shape that is replaced by a concentric version of the current container shape. If the container shape is a rectangle derived shape with four corners, this shape could choose to respect corners individually.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/rectanglecornerradii)*