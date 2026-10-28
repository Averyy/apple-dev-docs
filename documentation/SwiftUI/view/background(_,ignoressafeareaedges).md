# background(_:ignoresSafeAreaEdges:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the view’s background to a style.

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
func background<S>(_ style: S, ignoresSafeAreaEdges edges: Edge.Set = .all) -> some View where S : ShapeStyle
```

## Return Value

A view with the specified style drawn behind it.

## Discussion

Use this modifier to place a type that conforms to the [`ShapeStyle`](../shapestyle.md) protocol — like a [`Color`](../color.md), [`Material`](../material.md), or [`HierarchicalShapeStyle`](../hierarchicalshapestyle.md) — behind a view. For example, you can add the [`regularMaterial`](../shapestyle/regularmaterial.md) behind a [`Label`](../label.md):

```swift
struct FlagLabel: View {
    var body: some View {
        Label("Flag", systemImage: "flag.fill")
            .padding()
            .background(.regularMaterial)
    }
}
```

SwiftUI anchors the style to the view’s bounds. For the example above, the background fills the entirety of the label’s frame, which includes the padding:

![A screenshot of a flag symbol and the word flag layered over a](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-background-5@2x.png)

SwiftUI limits the background style’s extent to the modified view’s container-relative shape. You can see this effect if you constrain the `FlagLabel` view with a [`containerShape(_:)`](./containershape%28_%29.md) modifier:

```swift
FlagLabel()
    .containerShape(RoundedRectangle(cornerRadius: 16))
```

The background takes on the specified container shape:

![A screenshot of a flag symbol and the word flag layered over a](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/View-background-6@2x.png)

By default, the background ignores safe area insets on all edges, but you can provide a specific set of edges to ignore, or an empty set to respect safe area insets on all edges:

```swift
Rectangle()
    .background(
        .regularMaterial,
        ignoresSafeAreaEdges: []) // Ignore no safe area insets.
```

If you want to specify a [`View`](../view.md) or a stack of views as the background, use [`background(alignment:content:)`](./background%28alignment,content%29.md) instead. To specify a [`Shape`](../shape.md) or [`InsettableShape`](../insettableshape.md), use [`background(_:in:fillStyle:)`](./background%28_,in,fillstyle%29.md) . To configure the background of a presentation, like a sheet, use [`presentationBackground(_:)`](./presentationbackground%28_%29.md).

## Parameters

- `style`: An instance of a type that conforms to [`ShapeStyle`](../shapestyle.md) that SwiftUI draws behind the modified view.
- `edges`: The set of edges for which to ignore safe area insets when adding the background. The default value is [`all`](../edge/set/all.md). Specify an empty set to respect safe area insets on all edges.

## See Also

### Layering views
- [Adding a background to your view](../adding-a-background-to-your-view.md)
  Compose a background behind your view and extend it beyond the safe area insets.
- [struct ZStack](../zstack.md)
  A view that overlays its subviews, aligning them in both axes.
- [func zIndex(Double) -> some View](./zindex%28_%29.md)
  Controls the display order of overlapping views.
- [func background<V>(alignment: Alignment, content: () -> V) -> some View](./background%28alignment,content%29.md)
  Layers the views that you specify behind this view.
- [func background(ignoresSafeAreaEdges: Edge.Set) -> some View](./background%28ignoressafeareaedges%29.md)
  Sets the view’s background to the default background style.
- [func background(_:in:fillStyle:)](./background%28_,in,fillstyle%29.md)
  Sets the view’s background to an insettable shape filled with a style.
- [func background(in:fillStyle:)](./background%28in,fillstyle%29.md)
  Sets the view’s background to an insettable shape filled with the default background style.
- [func overlay<V>(alignment: Alignment, content: () -> V) -> some View](./overlay%28alignment,content%29.md)
  Layers the views that you specify in front of this view.
- [func overlay<S>(S, ignoresSafeAreaEdges: Edge.Set) -> some View](./overlay%28_,ignoressafeareaedges%29.md)
  Layers the specified style in front of this view.
- [func overlay<S, T>(S, in: T, fillStyle: FillStyle) -> some View](./overlay%28_,in,fillstyle%29.md)
  Layers a shape that you specify in front of this view.
- [var backgroundMaterial: Material?](../environmentvalues/backgroundmaterial.md)
  The material underneath the current view.
- [func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some View](./containerbackground%28_,for%29.md)
  Sets the container background of the enclosing container using a view.
- [func containerBackground<V>(for: ContainerBackgroundPlacement, alignment: Alignment, content: () -> V) -> some View](./containerbackground%28for,alignment,content%29.md)
  Sets the container background of the enclosing container using a view.
- [struct ContainerBackgroundPlacement](../containerbackgroundplacement.md)
  The placement of a container background.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/background(_:ignoressafeareaedges:))*