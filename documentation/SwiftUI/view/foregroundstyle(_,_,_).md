# foregroundStyle(_:_:_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the primary, secondary, and tertiary levels of the foreground style.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func foregroundStyle<S1, S2, S3>(_ primary: S1, _ secondary: S2, _ tertiary: S3) -> some View where S1 : ShapeStyle, S2 : ShapeStyle, S3 : ShapeStyle
```

## Return Value

A view that uses the given foreground styles.

## Discussion

SwiftUI uses these styles when rendering child views that don’t have an explicit rendering style, like images, text, shapes, and so on.

Symbol images within the view hierarchy use the [`palette`](../symbolrenderingmode/palette.md) rendering mode when you apply this modifier, if you don’t explicitly specify another mode.

## Parameters

- `primary`: The primary color or pattern to use when filling in the foreground elements. To indicate a specific value, use [`Color`](../color.md) or [`image(_:sourceRect:scale:)`](../shapestyle/image%28_,sourcerect,scale%29.md), or one of the gradient types, like [`linearGradient(colors:startPoint:endPoint:)`](../shapestyle/lineargradient%28colors,startpoint,endpoint%29.md). To set a style that’s relative to the containing view’s style, use one of the semantic styles, like [`primary`](../shapestyle/primary.md).
- `secondary`: The secondary color or pattern to use when filling in the foreground elements.
- `tertiary`: The tertiary color or pattern to use when filling in the foreground elements.

## See Also

### Styling content
- [func border<S>(S, width: CGFloat) -> some View](./border%28_,width%29.md)
  Adds a border to this view with the specified style and width.
- [func foregroundStyle<S>(S) -> some View](./foregroundstyle%28_%29.md)
  Sets a view’s foreground elements to use a given style.
- [func foregroundStyle<S1, S2>(S1, S2) -> some View](./foregroundstyle%28_,_%29.md)
  Sets the primary and secondary levels of the foreground style in the child view.
- [func backgroundStyle<S>(S) -> some View](./backgroundstyle%28_%29.md)
  Sets the specified style to render backgrounds within the view.
- [var backgroundStyle: AnyShapeStyle?](../environmentvalues/backgroundstyle.md)
  An optional style that overrides the default system background style when set.
- [protocol ShapeStyle](../shapestyle.md)
  A color or pattern to use when rendering a shape.
- [struct AnyShapeStyle](../anyshapestyle.md)
  A type-erased ShapeStyle value.
- [struct Gradient](../gradient.md)
  A color gradient represented as an array of color stops, each having a parametric location value.
- [struct MeshGradient](../meshgradient.md)
  A two-dimensional gradient defined by a 2D grid of positioned colors.
- [struct AnyGradient](../anygradient.md)
  A color gradient.
- [struct ShadowStyle](../shadowstyle.md)
  A style to use when rendering shadows.
- [struct Glass](../glass.md)
  A structure that defines the configuration of the Liquid Glass material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/foregroundstyle(_:_:_:))*