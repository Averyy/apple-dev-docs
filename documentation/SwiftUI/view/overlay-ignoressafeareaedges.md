# overlay(_:ignoresSafeAreaEdges:)

**Framework**: SwiftUI  
**Kind**: method

Layers the specified style in front of this view.

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
func overlay<S>(_ style: S, ignoresSafeAreaEdges edges: Edge.Set = .all) -> some View where S : ShapeStyle
```

#### Return Value

A view with the specified style drawn in front of it.

#### Discussion

Use this modifier to layer a type that conforms to the [`ShapeStyle`](shapestyle.md) protocol, like a [`Color`](color.md), [`Material`](material.md), or [`HierarchicalShapeStyle`](hierarchicalshapestyle.md), in front of a view. For example, you can overlay the [`ultraThinMaterial`](shapestyle/ultrathinmaterial.md) over a [`Circle`](circle.md):

```swift
struct CoveredCircle: View {
    var body: some View {
        Circle()
            .frame(width: 300, height: 200)
            .overlay(.ultraThinMaterial)
    }
}
```

SwiftUI anchors the style to the view’s bounds. For the example above, the overlay fills the entirety of the circle’s frame (which happens to be wider than the circle is tall):

![A screenshot of a circle showing through a rectangle that imposes](https://docs-assets.developer.apple.com/published/ad8d81eac6822374f7b9a42224523ba6/View-overlay-5%402x.png)

SwiftUI also limits the style’s extent to the view’s container-relative shape. You can see this effect if you constrain the `CoveredCircle` view with a [`containerShape(_:)`](view/containershape(_:).md) modifier:

```swift
CoveredCircle()
    .containerShape(RoundedRectangle(cornerRadius: 30))
```

The overlay takes on the specified container shape:

![A screenshot of a circle showing through a rounded rectangle that](https://docs-assets.developer.apple.com/published/79c6ec70d1f649f4c2eac46aa9cba166/View-overlay-6%402x.png)

By default, the overlay ignores safe area insets on all edges, but you can provide a specific set of edges to ignore, or an empty set to respect safe area insets on all edges:

```swift
Rectangle()
    .overlay(
        .secondary,
        ignoresSafeAreaEdges: []) // Ignore no safe area insets.
```

If you want to specify a [`View`](view.md) or a stack of views as the overlay rather than a style, use [`overlay(alignment:content:)`](view/overlay(alignment:content:).md) instead. If you want to specify a [`Shape`](shape.md), use [`overlay(_:in:fillStyle:)`](view/overlay(_:in:fillstyle:).md).

## Parameters

- `style`: An instance of a type that conforms to   that   SwiftUI layers in front of the modified view.
- `edges`: The set of edges for which to ignore safe area insets   when adding the overlay. The default value is  .   Specify an empty set to respect safe area insets on all edges.

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
- [func background(in:fillStyle:)](view/background(in:fillstyle:).md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](view/overlay(alignment:content:).md)
  Layers the views that you specify in front of this view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/overlay(_:ignoressafeareaedges:))*