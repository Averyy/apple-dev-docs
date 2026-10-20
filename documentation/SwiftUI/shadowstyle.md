# ShadowStyle

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A style to use when rendering shadows.

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
struct ShadowStyle
```

## Topics

### Getting shadow styles
- [static func drop(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> ShadowStyle](./shadowstyle/drop%28color,radius,x,y%29.md)
  Creates a custom drop shadow style.
- [static func inner(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> ShadowStyle](./shadowstyle/inner%28color,radius,x,y%29.md)
  Creates a custom inner shadow style.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Styling content
- [func border<S>(S, width: CGFloat) -> some View](./view/border%28_,width%29.md)
  Adds a border to this view with the specified style and width.
- [func foregroundStyle<S>(S) -> some View](./view/foregroundstyle%28_%29.md)
  Sets a view’s foreground elements to use a given style.
- [func foregroundStyle<S1, S2>(S1, S2) -> some View](./view/foregroundstyle%28_,_%29.md)
  Sets the primary and secondary levels of the foreground style in the child view.
- [func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View](./view/foregroundstyle%28_,_,_%29.md)
  Sets the primary, secondary, and tertiary levels of the foreground style.
- [func backgroundStyle<S>(S) -> some View](./view/backgroundstyle%28_%29.md)
  Sets the specified style to render backgrounds within the view.
- [var backgroundStyle: AnyShapeStyle?](./environmentvalues/backgroundstyle.md)
  An optional style that overrides the default system background style when set.
- [protocol ShapeStyle](./shapestyle.md)
  A color or pattern to use when rendering a shape.
- [struct AnyShapeStyle](./anyshapestyle.md)
  A type-erased ShapeStyle value.
- [struct Gradient](./gradient.md)
  A color gradient represented as an array of color stops, each having a parametric location value.
- [struct MeshGradient](./meshgradient.md)
  A two-dimensional gradient defined by a 2D grid of positioned colors.
- [struct AnyGradient](./anygradient.md)
  A color gradient.
- [struct Glass](./glass.md)
  A structure that defines the configuration of the Liquid Glass material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shadowstyle)*