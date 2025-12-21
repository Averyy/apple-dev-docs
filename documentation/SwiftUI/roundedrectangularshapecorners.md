# RoundedRectangularShapeCorners

**Framework**: SwiftUI  
**Kind**: struct

A type describing the corner styles of a [`RoundedRectangularShape`](roundedrectangularshape.md).

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
struct RoundedRectangularShapeCorners
```

## Topics

### Initializers
- [init(all: Edge.Corner.Style)](roundedrectangularshapecorners/init(all:).md)
  Create corner styles with all corner having the same style.
- [init(topLeading: Edge.Corner.Style, topTrailing: Edge.Corner.Style, bottomLeading: Edge.Corner.Style, bottomTrailing: Edge.Corner.Style)](roundedrectangularshapecorners/init(topleading:toptrailing:bottomleading:bottomtrailing:).md)
  Create corner styles with per-corner styles.
### Instance Properties
- [var bottomLeading: Edge.Corner.Style](roundedrectangularshapecorners/bottomleading.md)
  The bottom leading corner style.
- [var bottomTrailing: Edge.Corner.Style](roundedrectangularshapecorners/bottomtrailing.md)
  The bottom trailing corner style
- [var topLeading: Edge.Corner.Style](roundedrectangularshapecorners/topleading.md)
  The top leading corner style.
- [var topTrailing: Edge.Corner.Style](roundedrectangularshapecorners/toptrailing.md)
  The top trailing corner style.
### Subscripts
- [subscript(Edge.Corner) -> Edge.Corner.Style](roundedrectangularshapecorners/subscript(_:).md)
  Returns the corner style for a provided corner.
### Type Properties
- [static var concentric: RoundedRectangularShapeCorners](roundedrectangularshapecorners/concentric.md)
  Corner styles will be concentric with its container, varying the radius as needed in all four corners.
### Type Methods
- [static func concentric(minimum: Edge.Corner.Style?) -> RoundedRectangularShapeCorners](roundedrectangularshapecorners/concentric(minimum:).md)
  Corner styles will be concentric with its container, varying the radius as needed in all four corners but never going below zero, or the provided minimum corner style, if provided.
- [static func fixed(CGFloat) -> RoundedRectangularShapeCorners](roundedrectangularshapecorners/fixed(_:).md)
  Corner styles with fixed radius in all four corners.

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
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
- [struct UnevenRoundedRectangle](unevenroundedrectangle.md)
  A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [struct RectangleCornerRadii](rectanglecornerradii.md)
  Describes the corner radius values of a rounded rectangle with uneven corners.
- [struct RectangleCornerInsets](rectanglecornerinsets.md)
  The inset sizes for the corners of a rectangle.
- [struct ConcentricRectangle](concentricrectangle.md)
  A shape that is replaced by a concentric version of the current container shape. If the container shape is a rectangle derived shape with four corners, this shape could choose to respect corners individually.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/roundedrectangularshapecorners)*