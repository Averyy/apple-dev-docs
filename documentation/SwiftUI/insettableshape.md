# InsettableShape

**Framework**: SwiftUI  
**Kind**: protocol

A shape type that is able to inset itself to produce another shape.

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
protocol InsettableShape : Shape
```

## Topics

### Setting the stroke border characteristics
- [func strokeBorder(_:lineWidth:antialiased:)](insettableshape/strokeborder(_:linewidth:antialiased:).md)
  Returns a view that is the result of filling the `lineWidth`-sized border (aka inner stroke) of `self` with `content`. This is equivalent to insetting `self` by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the line-width.
- [func strokeBorder(lineWidth: CGFloat, antialiased: Bool) -> some View](insettableshape/strokeborder(linewidth:antialiased:).md)
  Returns a view that is the result of filling the `lineWidth`-sized border (aka inner stroke) of `self` with the foreground color. This is equivalent to insetting `self` by `lineWidth / 2` and stroking the resulting shape with `lineWidth` as the line-width.
- [func strokeBorder(_:style:antialiased:)](insettableshape/strokeborder(_:style:antialiased:).md)
  Returns a view that is the result of insetting `self` by `style.lineWidth / 2`, stroking the resulting shape with `style`, and then filling with `content`.
- [func strokeBorder(style: StrokeStyle, antialiased: Bool) -> some View](insettableshape/strokeborder(style:antialiased:).md)
  Returns a view that is the result of insetting `self` by `style.lineWidth / 2`, stroking the resulting shape with `style`, and then filling with the foreground color.
### Setting the inset
- [func inset(by: CGFloat) -> Self.InsetShape](insettableshape/inset(by:).md)
  Returns `self` inset by `amount`.
- [associatedtype InsetShape : InsettableShape](insettableshape/insetshape.md)
  The type of the inset shape.

## Relationships

### Inherits From
- [Animatable](animatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Shape](shape.md)
- [View](view.md)
### Conforming Types
- [ButtonBorderShape](buttonbordershape.md)
- [Capsule](capsule.md)
- [Circle](circle.md)
- [ContainerRelativeShape](containerrelativeshape.md)
- [Ellipse](ellipse.md)
- [OffsetShape](offsetshape.md)
- [Rectangle](rectangle.md)
- [RotatedShape](rotatedshape.md)
- [RoundedRectangle](roundedrectangle.md)
- [UnevenRoundedRectangle](unevenroundedrectangle.md)

## See Also

- [func containerShape<T>(T) -> some View](view/containershape(_:).md)
  Sets the container shape to use for any container relative shape within this view.
- [struct ContainerRelativeShape](containerrelativeshape.md)
  A shape that is replaced by an inset version of the current container shape. If no container shape was defined, is replaced by a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/insettableshape)*