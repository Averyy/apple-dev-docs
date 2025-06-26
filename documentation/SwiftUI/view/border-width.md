# border(_:width:)

**Framework**: SwiftUI  
**Kind**: method

Adds a border to this view with the specified style and width.

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
nonisolated
func border<S>(_ content: S, width: CGFloat = 1) -> some View where S : ShapeStyle
```

## Mentions

- [Configuring views](configuring-views.md)
- [Inspecting view layout](inspecting-view-layout.md)

#### Return Value

A view that adds a border with the specified style and width to this view.

#### Discussion

Use this modifier to draw a border of a specified width around the view’s frame. By default, the border appears inside the bounds of this view. For example, you can add a four-point wide border covers the text:

```swift
Text("Purple border inside the view bounds.")
    .border(Color.purple, width: 4)
```

![A screenshot showing the text Purple border inside the view bounds.](https://docs-assets.developer.apple.com/published/bbfa1b5948bba764b28577b4339f2155/View-border-1%402x.png)

To place a border around the outside of this view, apply padding of the same width before adding the border:

```swift
Text("Purple border outside the view bounds.")
    .padding(4)
    .border(Color.purple, width: 4)
```

![A screenshot showing the text Purple border outside the view bounds.](https://docs-assets.developer.apple.com/published/4c8091d3872d2d209592ace9b523b9d7/View-border-2%402x.png)

## Parameters

- `content`: A value that conforms to the   protocol,   like a   or  , that SwiftUI   uses to fill the border.
- `width`: The thickness of the border. The default is 1 pixel.

## See Also

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
- [struct AnyGradient](anygradient.md)
  A color gradient.
- [struct ShadowStyle](shadowstyle.md)
  A style to use when rendering shadows.
- [struct Glass](glass.md)
  A structure that defines the configuration of the Liquid Glass material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/border(_:width:))*