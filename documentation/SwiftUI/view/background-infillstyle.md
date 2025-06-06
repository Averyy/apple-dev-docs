# background(in:fillStyle:)

**Framework**: SwiftUI  
**Kind**: method

Sets the view’s background to an insettable shape filled with the default background style.

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
func background<S>(in shape: S, fillStyle: FillStyle = FillStyle()) -> some View where S : InsettableShape
```

#### Return Value

A view with the specified insettable shape drawn behind it.

#### Discussion

This modifier behaves like [`background(_:in:fillStyle:)`](view/background(_:in:fillstyle:).md), except that it always uses the [`background`](shapestyle/background.md) shape style to fill the specified insettable shape. For example, you can use a [`RoundedRectangle`](roundedrectangle.md) as a background on a [`Label`](label.md):

```swift
ZStack {
    Color.teal
    Label("Flag", systemImage: "flag.fill")
        .padding()
        .background(in: RoundedRectangle(cornerRadius: 8))
}
```

Without the background modifier, the fill color shows through the label. With the modifier, the label’s text and icon appear backed by a shape filled with a color that’s appropriate for light or dark appearance:

![A screenshot of a flag icon and the word flag inside a rectangle with](https://docs-assets.developer.apple.com/published/bc89a35b3c54aa12cda42b491f420dd6/View-background-9%402x.png)

To create a background with other [`View`](view.md) types — or with a stack of views — use [`background(alignment:content:)`](view/background(alignment:content:).md) instead. To add a [`ShapeStyle`](shapestyle.md) as a background, use [`background(_:ignoresSafeAreaEdges:)`](view/background(_:ignoressafeareaedges:).md).

## Parameters

- `shape`: An instance of a type that conforms to    that SwiftUI draws behind the view using the    shape style.
- `fillStyle`: The   to use when drawing the shape.   The default style uses the nonzero winding number rule and   antialiasing.

## See Also

- [Adding a background to your view](adding-a-background-to-your-view.md)
  Compose a background behind your view and extend it beyond the safe area insets.
- [struct ZStack](zstack.md)
  A view that overlays its subviews, aligning them in both axes.
- [func zIndex(Double) -> some View](view/zindex(_:).md)
  Controls the display order of overlapping views.
- [func background<V>(alignment: Alignment, content: () -> V) -> some View](view/background(alignment:content:).md)
  Layers the views that you specify behind this view.
- [func background<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](view/background(_:ignoressafeareaedges:).md)
  Sets the view’s background to a style.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](view/background(ignoressafeareaedges:).md)
  Sets the view’s background to the default background style.
- [func background(_:in:fillStyle:)](view/background(_:in:fillstyle:).md)
  Sets the view’s background to an insettable shape filled with a style.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](view/overlay(alignment:content:).md)
  Layers the views that you specify in front of this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](view/overlay(_:ignoressafeareaedges:).md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](view/overlay(_:in:fillstyle:).md)
  Layers a shape that you specify in front of this view.
- [var backgroundMaterial: Material?](environmentvalues/backgroundmaterial.md)
  The material underneath the current view.
- [func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some View](view/containerbackground(_:for:).md)
  Sets the container background of the enclosing container using a view.
- [func containerBackground<V>(for: ContainerBackgroundPlacement, alignment: Alignment, content: () -> V) -> some View](view/containerbackground(for:alignment:content:).md)
  Sets the container background of the enclosing container using a view.
- [struct ContainerBackgroundPlacement](containerbackgroundplacement.md)
  The placement of a container background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/background(in:fillstyle:))*