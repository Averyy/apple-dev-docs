# RoundedRectangle

**Framework**: SwiftUI  
**Kind**: struct

A rectangular shape with rounded corners, aligned inside the frame of the view containing it.

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
struct RoundedRectangle
```

## Topics

### Creating a rounded rectangle
- [init(cornerRadius: CGFloat, style: RoundedCornerStyle)](roundedrectangle/init(cornerradius:style:).md)
  Creates a new rounded rectangle shape.
- [init(cornerSize: CGSize, style: RoundedCornerStyle)](roundedrectangle/init(cornersize:style:).md)
  Creates a new rounded rectangle shape.
### Getting the shape’s characteristics
- [var cornerSize: CGSize](roundedrectangle/cornersize.md)
  The width and height of the rounded rectangle’s corners.
- [var style: RoundedCornerStyle](roundedrectangle/style.md)
  The style of corners drawn by the rounded rectangle.
### Supporting types
- [var animatableData: CGSize.AnimatableData](roundedrectangle/animatabledata.md)
  The data to animate.

## Relationships

### Conforms To
- [Animatable](animatable.md)
- [Copyable](../Swift/Copyable.md)
- [InsettableShape](insettableshape.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Shape](shape.md)
- [View](view.md)

## See Also

- [struct Rectangle](rectangle.md)
  A rectangular shape aligned inside the frame of the view containing it.
- [enum RoundedCornerStyle](roundedcornerstyle.md)
  Defines the shape of a rounded rectangle’s corners.
- [struct UnevenRoundedRectangle](unevenroundedrectangle.md)
  A rectangular shape with rounded corners with different values, aligned inside the frame of the view containing it.
- [struct RectangleCornerRadii](rectanglecornerradii.md)
  Describes the corner radius values of a rounded rectangle with uneven corners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/roundedrectangle)*