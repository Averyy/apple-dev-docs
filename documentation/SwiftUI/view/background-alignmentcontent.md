# background(alignment:content:)

**Framework**: SwiftUI  
**Kind**: method

Layers the views that you specify behind this view.

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
func background<V>(alignment: Alignment = .center, @ViewBuilder content: () -> V) -> some View where V : View
```

#### Return Value

A view that uses the specified content as a background.

#### Discussion

Use this modifier to place one or more views behind another view. For example, you can place a collection of stars beind a [`Text`](text.md) view:

```swift
Text("ABCDEF")
    .background(alignment: .leading) { Star(color: .red) }
    .background(alignment: .center) { Star(color: .green) }
    .background(alignment: .trailing) { Star(color: .blue) }
```

The example above assumes that you’ve defined a `Star` view with a parameterized color:

```swift
struct Star: View {
    var color: Color

    var body: some View {
        Image(systemName: "star.fill")
            .foregroundStyle(color)
    }
}
```

By setting different `alignment` values for each modifier, you make the stars appear in different places behind the text:

![A screenshot of the letters A, B, C, D, E, and F written in front of](https://docs-assets.developer.apple.com/published/301a90b5111a107b80cf175a2a867a4a/View-background-2%402x.png)

If you specify more than one view in the `content` closure, the modifier collects all of the views in the closure into an implicit [`ZStack`](zstack.md), taking them in order from back to front. For example, you can layer a vertical bar behind a circle, with both of those behind a horizontal bar:

```swift
Color.blue
    .frame(width: 200, height: 10) // Creates a horizontal bar.
    .background {
        Color.green
            .frame(width: 10, height: 100) // Creates a vertical bar.
        Circle()
            .frame(width: 50, height: 50)
    }
```

Both the background modifier and the implicit [`ZStack`](zstack.md) composed from the background content — the circle and the vertical bar — use a default [`center`](alignment/center.md) alignment. The vertical bar appears centered behind the circle, and both appear as a composite view centered behind the horizontal bar:

![A screenshot of a circle with a horizontal blue bar layered on top](https://docs-assets.developer.apple.com/published/6e671ae0d8386497562685d261b7f44d/View-background-3%402x.png)

If you specify an alignment for the background, it applies to the implicit stack rather than to the individual views in the closure. You can see this if you add the [`leading`](alignment/leading.md) alignment:

```swift
Color.blue
    .frame(width: 200, height: 10)
    .background(alignment: .leading) {
        Color.green
            .frame(width: 10, height: 100)
        Circle()
            .frame(width: 50, height: 50)
    }
```

The vertical bar and the circle move as a unit to align the stack with the leading edge of the horizontal bar, while the vertical bar remains centered on the circle:

![A screenshot of a horizontal blue bar in front of a circle, which](https://docs-assets.developer.apple.com/published/53abc674b550ce27c3b30be982117a10/View-background-3a%402x.png)

To control the placement of individual items inside the `content` closure, either use a different background modifier for each item, as the earlier example of stars under text demonstrates, or add an explicit [`ZStack`](zstack.md) inside the content closure with its own alignment:

```swift
Color.blue
    .frame(width: 200, height: 10)
    .background(alignment: .leading) {
        ZStack(alignment: .leading) {
            Color.green
                .frame(width: 10, height: 100)
            Circle()
                .frame(width: 50, height: 50)
        }
    }
```

The stack alignment ensures that the circle’s leading edge aligns with the vertical bar’s, while the background modifier aligns the composite view with the horizontal bar:

![A screenshot of a horizontal blue bar in front of a circle, which](https://docs-assets.developer.apple.com/published/4f44c3882d3f69c1330a7ce92f62b200/View-background-4%402x.png)

You can achieve layering without a background modifier by putting both the modified view and the background content into a [`ZStack`](zstack.md). This produces a simpler view hierarchy, but it changes the layout priority that SwiftUI applies to the views. Use the background modifier when you want the modified view to dominate the layout.

If you want to specify a [`ShapeStyle`](shapestyle.md) like a [`HierarchicalShapeStyle`](hierarchicalshapestyle.md) or a [`Material`](material.md) as the background, use [`background(_:ignoresSafeAreaEdges:)`](view/background(_:ignoressafeareaedges:).md) instead. To specify a [`Shape`](shape.md) or [`InsettableShape`](insettableshape.md), use [`background(_:in:fillStyle:)`](view/background(_:in:fillstyle:).md). To configure the background of a presentation, like a sheet, use [`presentationBackground(alignment:content:)`](view/presentationbackground(alignment:content:).md).

## Parameters

- `alignment`: The alignment that the modifier uses to position the   implicit   that groups the background views. The default   is  .
- `content`: A   that you use to declare the views to draw   behind this view, stacked in a cascading order from bottom to top.   The last view that you list appears at the front of the stack.

## See Also

- [Adding a background to your view](adding-a-background-to-your-view.md)
  Compose a background behind your view and extend it beyond the safe area insets.
- [struct ZStack](zstack.md)
  A view that overlays its subviews, aligning them in both axes.
- [func zIndex(Double) -> some View](view/zindex(_:).md)
  Controls the display order of overlapping views.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/background(alignment:content:))*