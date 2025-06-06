# AnyGradient

**Framework**: SwiftUI  
**Kind**: struct

A color gradient.

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
struct AnyGradient
```

#### Overview

When used as a [`ShapeStyle`](shapestyle.md), this type draws a linear gradient with start-point [0.5, 0] and end-point [0.5, 1].

## Topics

### Creating a gradient
- [init(Gradient)](anygradient/init(_:).md)
  Creates a new instance from the specified gradient.
### Working with color spaces
- [func colorSpace(Gradient.ColorSpace) -> AnyGradient](anygradient/colorspace(_:).md)
  Returns a version of the gradient that will use a specified color space for interpolating between its colors.

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
- [struct Gradient](gradient.md)
  A color gradient represented as an array of color stops, each having a parametric location value.
- [struct MeshGradient](meshgradient.md)
  A two-dimensional gradient defined by a 2D grid of positioned colors.
- [struct ShadowStyle](shadowstyle.md)
  A style to use when rendering shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anygradient)*