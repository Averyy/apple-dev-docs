# overlay(alignment:content:)

**Framework**: SwiftUI  
**Kind**: method

Layers the views that you specify in front of this view.

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
func overlay<V>(alignment: Alignment = .center, @ViewBuilder content: () -> V) -> some View where V : View
```

#### Return Value

A view that uses the specified content as a foreground.

#### Discussion

Use this modifier to place one or more views in front of another view. For example, you can place a group of stars on a [`RoundedRectangle`](roundedrectangle.md):

```swift
RoundedRectangle(cornerRadius: 8)
    .frame(width: 200, height: 100)
    .overlay(alignment: .topLeading) { Star(color: .red) }
    .overlay(alignment: .topTrailing) { Star(color: .yellow) }
    .overlay(alignment: .bottomLeading) { Star(color: .green) }
    .overlay(alignment: .bottomTrailing) { Star(color: .blue) }
```

The example above assumes that you’ve defined a `Star` view with a parameterized color:

```swift
struct Star: View {
    var color = Color.yellow

    var body: some View {
        Image(systemName: "star.fill")
            .foregroundStyle(color)
    }
}
```

By setting different `alignment` values for each modifier, you make the stars appear in different places on the rectangle:

![A screenshot of a rounded rectangle with a star in each corner. The](https://docs-assets.developer.apple.com/published/0e35601a7bf9406b5995a8203e6eea9a/View-overlay-2%402x.png)

If you specify more than one view in the `content` closure, the modifier collects all of the views in the closure into an implicit [`ZStack`](zstack.md), taking them in order from back to front. For example, you can place a star and a [`Circle`](circle.md) on a field of [`blue`](shapestyle/blue.md):

```swift
Color.blue
    .frame(width: 200, height: 200)
    .overlay {
        Circle()
            .frame(width: 100, height: 100)
        Star()
    }
```

Both the overlay modifier and the implicit [`ZStack`](zstack.md) composed from the overlay content — the circle and the star — use a default [`center`](alignment/center.md) alignment. The star appears centered on the circle, and both appear as a composite view centered in front of the square:

![A screenshot of a star centered on a circle, which is](https://docs-assets.developer.apple.com/published/636dc94ec79008e94db2b7b0f7bca91f/View-overlay-3%402x.png)

If you specify an alignment for the overlay, it applies to the implicit stack rather than to the individual views in the closure. You can see this if you add the [`bottom`](alignment/bottom.md) alignment:

```swift
Color.blue
    .frame(width: 200, height: 200)
    .overlay(alignment: .bottom) {
        Circle()
            .frame(width: 100, height: 100)
        Star()
    }
```

The circle and the star move down as a unit to align the stack’s bottom edge with the bottom edge of the square, while the star remains centered on the circle:

![A screenshot of a star centered on a circle, which is on a square.](https://docs-assets.developer.apple.com/published/04f713a3a16278b631260f43368cd385/View-overlay-3a%402x.png)

To control the placement of individual items inside the `content` closure, either use a different overlay modifier for each item, as the earlier example of stars in the corners of a rectangle demonstrates, or add an explicit [`ZStack`](zstack.md) inside the content closure with its own alignment:

```swift
Color.blue
    .frame(width: 200, height: 200)
    .overlay(alignment: .bottom) {
        ZStack(alignment: .bottom) {
            Circle()
                .frame(width: 100, height: 100)
            Star()
        }
    }
```

The stack alignment ensures that the star’s bottom edge aligns with the circle’s, while the overlay aligns the composite view with the square:

![A screenshot of a star, a circle, and a square with all their](https://docs-assets.developer.apple.com/published/e6b247cd2ef7a62a8b69f351ca17ae55/View-overlay-4%402x.png)

You can achieve layering without an overlay modifier by putting both the modified view and the overlay content into a [`ZStack`](zstack.md). This can produce a simpler view hierarchy, but changes the layout priority that SwiftUI applies to the views. Use the overlay modifier when you want the modified view to dominate the layout.

If you want to specify a [`ShapeStyle`](shapestyle.md) like a [`Color`](color.md) or a [`Material`](material.md) as the overlay, use [`overlay(_:ignoresSafeAreaEdges:)`](view/overlay(_:ignoressafeareaedges:).md) instead. To specify a [`Shape`](shape.md), use [`overlay(_:in:fillStyle:)`](view/overlay(_:in:fillstyle:).md).

## Parameters

- `alignment`: The alignment that the modifier uses to position the   implicit   that groups the foreground views. The default   is  .
- `content`: A   that you use to declare the views to   draw in front of this view, stacked in the order that you list them.   The last view that you list appears at the front of the stack.

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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/overlay(alignment:content:))*