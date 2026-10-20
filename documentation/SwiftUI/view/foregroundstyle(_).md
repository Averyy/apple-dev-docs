# foregroundStyle(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets a view’s foreground elements to use a given style.

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
func foregroundStyle<S>(_ style: S) -> some View where S : ShapeStyle
```

## Mentions

- [Configuring views](../configuring-views.md)

#### Return Value

A view that uses the given foreground style.

#### Discussion

Use this method to style foreground content like text, shapes, and template images (including symbols):

```swift
HStack {
    Image(systemName: "triangle.fill")
    Text("Hello, world!")
    RoundedRectangle(cornerRadius: 5)
        .frame(width: 40, height: 20)
}
.foregroundStyle(.teal)
```

The example above creates a row of [`teal`](../shapestyle/teal.md) foreground elements:

![A screenshot of a teal triangle, string, and rounded](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-foregroundStyle-1@2x.png)

You can use any style that conforms to the [`ShapeStyle`](../shapestyle.md) protocol, like the [`teal`](../shapestyle/teal.md) color in the example above, or the [`linearGradient(colors:startPoint:endPoint:)`](../shapestyle/lineargradient%28colors,startpoint,endpoint%29.md) gradient shown below:

```swift
Text("Gradient Text")
    .font(.largeTitle)
    .foregroundStyle(
        .linearGradient(
            colors: [.yellow, .blue],
            startPoint: .top,
            endPoint: .bottom
        )
    )
```

![A screenshot of the words Gradient Text, with letters that](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-foregroundStyle-2@2x.png)

> 💡 **Tip**: If you want to fill a single [`Shape`](../shape.md) instance with a style, use the [`fill(style:)`](../shape/fill%28style%29.md) shape modifier instead because it’s more efficient.

SwiftUI creates a context-dependent render for a given style. For example, a [`Color`](../color.md) that you load from an asset catalog can have different light and dark appearances, while some styles also vary by platform.

Hierarchical foreground styles like `ShapeStyle/secondary` don’t impose a style of their own, but instead modify other styles. In particular, they modify the primary level of the current foreground style to the degree given by the hierarchical style’s name. To find the current foreground style to modify, SwiftUI looks for the innermost containing style that you apply with the `foregroundStyle(_:)` or the [`foregroundColor(_:)`](./foregroundcolor%28_%29.md) modifier. If you haven’t specified a style, SwiftUI uses the default foreground style, as in the following example:

```swift
VStack(alignment: .leading) {
    Label("Primary", systemImage: "1.square.fill")
    Label("Secondary", systemImage: "2.square.fill")
        .foregroundStyle(.secondary)
}
```

![A screenshot of two labels with the text primary and secondary.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-foregroundStyle-3@2x.png)

If you add a foreground style on the enclosing [`VStack`](../vstack.md), the hierarchical styling responds accordingly:

```swift
VStack(alignment: .leading) {
    Label("Primary", systemImage: "1.square.fill")
    Label("Secondary", systemImage: "2.square.fill")
        .foregroundStyle(.secondary)
}
.foregroundStyle(.blue)
```

![A screenshot of two labels with the text primary and secondary.](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-foregroundStyle-4@2x.png)

When you apply a custom style to a view, the view disables the vibrancy effect for foreground elements in that view, or in any of its child views, that it would otherwise gain from adding a background material — for example, using the [`background(_:ignoresSafeAreaEdges:)`](./background%28_,ignoressafeareaedges%29.md) modifier. However, hierarchical styles applied to the default foreground don’t disable vibrancy.

## Parameters

- `style`: The color or pattern to use when filling in the foreground elements. To indicate a specific value, use [`Color`](../color.md) or [`image(_:sourceRect:scale:)`](../shapestyle/image%28_,sourcerect,scale%29.md), or one of the gradient types, like [`linearGradient(colors:startPoint:endPoint:)`](../shapestyle/lineargradient%28colors,startpoint,endpoint%29.md). To set a style that’s relative to the containing view’s style, use one of the semantic styles, like [`primary`](../shapestyle/primary.md).

## See Also

### Styling content
- [func border<S>(S, width: CGFloat) -> some View](./border%28_,width%29.md)
  Adds a border to this view with the specified style and width.
- [func foregroundStyle<S1, S2>(S1, S2) -> some View](./foregroundstyle%28_,_%29.md)
  Sets the primary and secondary levels of the foreground style in the child view.
- [func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View](./foregroundstyle%28_,_,_%29.md)
  Sets the primary, secondary, and tertiary levels of the foreground style.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/foregroundstyle(_:))*