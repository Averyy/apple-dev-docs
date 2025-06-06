# background(alignment:content:)

**Framework**: Assignables  
**Kind**: method

Layers the views that you specify behind this view.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func background<V>(alignment: Alignment = .center, @ViewBuilder content: () -> V) -> some View where V : View
```

#### Return Value

A view that uses the specified content as a background.

#### Discussion

Use this modifier to place one or more views behind another view. For example, you can place a collection of stars beind a `Text` view:

```None
Text("ABCDEF")
    .background(alignment: .leading) { Star(color: .red) }
    .background(alignment: .center) { Star(color: .green) }
    .background(alignment: .trailing) { Star(color: .blue) }
```

The example above assumes that you’ve defined a `Star` view with a parameterized color:

```None
struct Star: View {
    var color: Color

    var body: some View {
        Image(systemName: "star.fill")
            .foregroundStyle(color)
    }
}
```

By setting different `alignment` values for each modifier, you make the stars appear in different places behind the text:

If you specify more than one view in the `content` closure, the modifier collects all of the views in the closure into an implicit `ZStack`, taking them in order from back to front. For example, you can layer a vertical bar behind a circle, with both of those behind a horizontal bar:

```None
Color.blue
    .frame(width: 200, height: 10) // Creates a horizontal bar.
    .background {
        Color.green
            .frame(width: 10, height: 100) // Creates a vertical bar.
        Circle()
            .frame(width: 50, height: 50)
    }
```

Both the background modifier and the implicit `ZStack` composed from the background content — the circle and the vertical bar — use a default `Alignment/center` alignment. The vertical bar appears centered behind the circle, and both appear as a composite view centered behind the horizontal bar:

If you specify an alignment for the background, it applies to the implicit stack rather than to the individual views in the closure. You can see this if you add the `Alignment/leading` alignment:

```None
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

To control the placement of individual items inside the `content` closure, either use a different background modifier for each item, as the earlier example of stars under text demonstrates, or add an explicit `ZStack` inside the content closure with its own alignment:

```None
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

You can achieve layering without a background modifier by putting both the modified view and the background content into a `ZStack`. This produces a simpler view hierarchy, but it changes the layout priority that SwiftUI applies to the views. Use the background modifier when you want the modified view to dominate the layout.

If you want to specify a `ShapeStyle` like a `HierarchicalShapeStyle` or a `Material` as the background, use `View/background(_:ignoresSafeAreaEdges:)` instead. To specify a `Shape` or `InsettableShape`, use `View/background(_:in:fillStyle:)`. To configure the background of a presentation, like a sheet, use `View/presentationBackground(alignment:content:)`.

## Parameters

- `alignment`: The alignment that the modifier uses to position the   implicit   that groups the background views. The default   is  .
- `content`: A   that you use to declare the views to draw   behind this view, stacked in a cascading order from bottom to top.   The last view that you list appears at the front of the stack.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/background(alignment:content:))*