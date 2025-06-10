# backgroundStyle(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the specified style to render backgrounds within the view.

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
nonisolated
func backgroundStyle<S>(_ style: S) -> some View where S : ShapeStyle
```

#### Discussion

The following example uses this modifier to set the [`backgroundStyle`](environmentvalues/backgroundstyle.md) environment value to a [`blue`](shapestyle/blue.md) color that includes a subtle [`gradient`](color/gradient.md). SwiftUI fills the [`Circle`](circle.md) shape that acts as a background element with this style:

```swift
Image(systemName: "swift")
    .padding()
    .background(in: Circle())
    .backgroundStyle(.blue.gradient)
```

![An image of the Swift logo inside a circle that’s blue with a slight](https://docs-assets.developer.apple.com/published/4b3325ab8b030bb73b60cd8cfe326695/View-backgroundStyle-1-iOS%402x.png)

To restore the default background style, set the [`backgroundStyle`](environmentvalues/backgroundstyle.md) environment value to `nil` using the [`environment(_:_:)`](view/environment(_:_:).md) modifer:

```swift
.environment(\.backgroundStyle, nil)
```

## See Also

- [func border<S>(S, width: CGFloat) -> some View](view/border(_:width:).md)
  Adds a border to this view with the specified style and width.
- [func foregroundStyle<S>(S) -> some View](view/foregroundstyle(_:).md)
  Sets a view’s foreground elements to use a given style.
- [func foregroundStyle<S1, S2>(S1, S2) -> some View](view/foregroundstyle(_:_:).md)
  Sets the primary and secondary levels of the foreground style in the child view.
- [func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View](view/foregroundstyle(_:_:_:).md)
  Sets the primary, secondary, and tertiary levels of the foreground style.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/backgroundstyle(_:))*