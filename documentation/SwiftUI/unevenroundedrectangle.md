# UnevenRoundedRectangle

**Framework**: SwiftUI  
**Kind**: struct

A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.

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
struct UnevenRoundedRectangle
```

## Topics

### Creating an uneven rounded rectangle
- [init(cornerRadii: RectangleCornerRadii, style: RoundedCornerStyle)](unevenroundedrectangle/init(cornerradii:style:).md)
  Creates a new rounded rectangle shape with uneven corners.
- [init(topLeadingRadius: CGFloat, bottomLeadingRadius: CGFloat, bottomTrailingRadius: CGFloat, topTrailingRadius: CGFloat, style: RoundedCornerStyle)](unevenroundedrectangle/init(topleadingradius:bottomleadingradius:bottomtrailingradius:toptrailingradius:style:).md)
  Creates a new rounded rectangle shape with uneven corners.
### Getting the shape’s characteristics
- [var cornerRadii: RectangleCornerRadii](unevenroundedrectangle/cornerradii.md)
  The radii of each corner of the rounded rectangle.
- [var style: RoundedCornerStyle](unevenroundedrectangle/style.md)
  The style of corners drawn by the rounded rectangle.
### Supporting types
- [var animatableData: RectangleCornerRadii.AnimatableData](unevenroundedrectangle/animatabledata.md)
  The data to animate.

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [InsettableShape](insettableshape.md)
- [RoundedRectangularShape](roundedrectangularshape.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [Shape](shape.md)
- [View](view.md)

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
- [struct RectangleCornerRadii](rectanglecornerradii.md)
  Describes the corner radius values of a rounded rectangle with uneven corners.
- [struct RectangleCornerInsets](rectanglecornerinsets.md)
  The inset sizes for the corners of a rectangle.
- [struct ConcentricRectangle](concentricrectangle.md)
  A shape whose corners you configure, individually or uniformly, to be squared, rounded, or concentric relative to a container shape’s corners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/unevenroundedrectangle)*