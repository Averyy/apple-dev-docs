# RectangleCornerInsets

**Framework**: SwiftUI  
**Kind**: struct

The inset sizes for the corners of a rectangle.

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
@frozen
struct RectangleCornerInsets
```

## Topics

### Initializers
- [init()](rectanglecornerinsets/init.md)
- [init(topLeading: CGSize, topTrailing: CGSize, bottomLeading: CGSize, bottomTrailing: CGSize)](rectanglecornerinsets/init(topleading:toptrailing:bottomleading:bottomtrailing:).md)
### Instance Properties
- [var bottomLeading: CGSize](rectanglecornerinsets/bottomleading.md)
  The size of the bottom-leading corner inset.
- [var bottomTrailing: CGSize](rectanglecornerinsets/bottomtrailing.md)
  The size of the bottom-trailing corner inset.
- [var topLeading: CGSize](rectanglecornerinsets/topleading.md)
  The size of the top-leading corner inset.
- [var topTrailing: CGSize](rectanglecornerinsets/toptrailing.md)
  The size of the top-trailing corner inset.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
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
- [struct RoundedRectangularShapeCorners](roundedrectangularshapecorners.md)
  A type describing the corner styles of a [`RoundedRectangularShape`](roundedrectangularshape.md).
- [struct UnevenRoundedRectangle](unevenroundedrectangle.md)
  A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [struct RectangleCornerRadii](rectanglecornerradii.md)
  Describes the corner radius values of a rounded rectangle with uneven corners.
- [struct ConcentricRectangle](concentricrectangle.md)
  A shape that is replaced by a concentric version of the current container shape. If the container shape is a rectangle derived shape with four corners, this shape could choose to respect corners individually.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/rectanglecornerinsets)*