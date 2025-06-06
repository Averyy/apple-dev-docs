# background(ignoresSafeAreaEdges:)

**Framework**: SwiftUI  
**Kind**: method

Sets the view’s background to the default background style.

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
func background(ignoresSafeAreaEdges edges: Edge.Set = .all) -> some View
```

#### Return Value

A view with the [`background`](shapestyle/background.md) shape style drawn behind it.

#### Discussion

This modifier behaves like [`background(_:ignoresSafeAreaEdges:)`](view/background(_:ignoressafeareaedges:).md), except that it always uses the [`background`](shapestyle/background.md) shape style. For example, you can add a background to a [`Label`](label.md):

```swift
ZStack {
    Color.teal
    Label("Flag", systemImage: "flag.fill")
        .padding()
        .background()
}
```

Without the background modifier, the teal color behind the label shows through the label. With the modifier, the label’s text and icon appear backed by a region filled with a color that’s appropriate for light or dark appearance:

![A screenshot of a flag icon and the word flag inside a rectangle; the](https://docs-assets.developer.apple.com/published/8e3ac25578ae088fe9b8c8a1fd739a8b/View-background-7%402x.png)

If you want to specify a [`View`](view.md) or a stack of views as the background, use [`background(alignment:content:)`](view/background(alignment:content:).md) instead. To specify a [`Shape`](shape.md) or [`InsettableShape`](insettableshape.md), use [`background(_:in:fillStyle:)`](view/background(_:in:fillstyle:).md). To configure the background of a presentation, like a sheet, use [`presentationBackground(_:)`](view/presentationbackground(_:).md).

## Parameters

- `edges`: The set of edges for which to ignore safe area insets   when adding the background. The default value is  .   Specify an empty set to respect safe area insets on all edges.

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
- [func background(_:in:fillStyle:)](view/background(_:in:fillstyle:).md)
  Sets the view’s background to an insettable shape filled with a style.
- [func background(in:fillStyle:)](view/background(in:fillstyle:).md)
  Sets the view’s background to an insettable shape filled with the default background style.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/background(ignoressafeareaedges:))*