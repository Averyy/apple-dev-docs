# Gradient

**Framework**: SwiftUI  
**Kind**: struct

A color gradient represented as an array of color stops, each having a parametric location value.

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
struct Gradient
```

## Mentions

- [Adding a background to your view](adding-a-background-to-your-view.md)

## Topics

### Creating a gradient from colors
- [init(colors: [Color])](gradient/init(colors:).md)
  Creates a gradient from an array of colors.
### Creating a gradient from stops
- [init(stops: [Gradient.Stop])](gradient/init(stops:).md)
  Creates a gradient from an array of color stops.
- [var stops: [Gradient.Stop]](gradient/stops.md)
  The array of color stops.
- [Gradient.Stop](gradient/stop.md)
  One color stop in the gradient.
### Working with color spaces
- [func colorSpace(Gradient.ColorSpace) -> AnyGradient](gradient/colorspace(_:).md)
  Returns a version of the gradient that will use a specified color space for interpolating between its colors.
- [Gradient.ColorSpace](gradient/colorspace.md)
  A method of interpolating between the colors in a gradient.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [ScaleRange](../Charts/ScaleRange.md)
- [Sendable](../Swift/Sendable.md)
- [ShapeStyle](shapestyle.md)

## See Also

- [func border<S>(S, width: CGFloat) -> some View](view/border(_:width:).md)
  Adds a border to this view with the specified style and width.
- [func foregroundStyle<S>(S) -> some View](view/foregroundstyle(_:).md)
  Sets a view’s foreground elements to use a given style.
- [func foregroundStyle<S1, S2>(S1, S2) -> some View](view/foregroundstyle(_:_:).md)
  Sets the primary and secondary levels of the foreground style in the child view.
- [func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View](view/foregroundstyle(_:_:_:).md)
  Sets the primary, secondary, and tertiary levels of the foreground style.
- [func backgroundStyle<S>(S) -> some View](view/backgroundstyle(_:).md)
  Sets the specified style to render backgrounds within the view.
- [var backgroundStyle: AnyShapeStyle?](environmentvalues/backgroundstyle.md)
  An optional style that overrides the default system background style when set.
- [protocol ShapeStyle](shapestyle.md)
  A color or pattern to use when rendering a shape.
- [struct AnyShapeStyle](anyshapestyle.md)
  A type-erased ShapeStyle value.
- [struct MeshGradient](meshgradient.md)
  A two-dimensional gradient defined by a 2D grid of positioned colors.
- [struct AnyGradient](anygradient.md)
  A color gradient.
- [struct ShadowStyle](shadowstyle.md)
  A style to use when rendering shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/gradient)*