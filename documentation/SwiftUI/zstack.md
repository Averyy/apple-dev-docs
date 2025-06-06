# ZStack

**Framework**: SwiftUI  
**Kind**: struct

A view that overlays its subviews, aligning them in both axes.

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
@frozen
struct ZStack<Content> where Content : View
```

## Mentions

- [Building layouts with stack views](building-layouts-with-stack-views.md)
- [Laying out a simple view](laying-out-a-simple-view.md)
- [Adding a background to your view](adding-a-background-to-your-view.md)
- [Making fine adjustments to a view’s position](making-fine-adjustments-to-a-view-s-position.md)
- [Creating performant scrollable stacks](creating-performant-scrollable-stacks.md)
- [Picking container views for your content](picking-container-views-for-your-content.md)
- [Aligning views within a stack](aligning-views-within-a-stack.md)

#### Overview

The `ZStack` assigns each successive subview a higher z-axis value than the one before it, meaning later subviews appear “on top” of earlier ones.

The following example creates a `ZStack` of 100 x 100 point [`Rectangle`](rectangle.md) views filled with one of six colors, offsetting each successive subview by 10 points so they don’t completely overlap:

```swift
let colors: [Color] =
    [.red, .orange, .yellow, .green, .blue, .purple]

var body: some View {
    ZStack {
        ForEach(0..<colors.count) {
            Rectangle()
                .fill(colors[$0])
                .frame(width: 100, height: 100)
                .offset(x: CGFloat($0) * 10.0,
                        y: CGFloat($0) * 10.0)
        }
    }
}
```

![Six squares of different colors, stacked atop each other, with a 10-point](https://docs-assets.developer.apple.com/published/5ce47ef59a84b346d733bcf2f4a7853e/SwiftUI-ZStack-offset-rectangles%402x.png)

The `ZStack` uses an [`Alignment`](alignment.md) to set the x- and y-axis coordinates of each subview, defaulting to a [`center`](alignment/center.md) alignment. In the following example, the `ZStack` uses a [`bottomLeading`](alignment/bottomleading.md) alignment to lay out two subviews, a red 100 x 50 point rectangle below, and a blue 50 x 100 point rectangle on top. Because of the alignment value, both rectangles share a bottom-left corner with the `ZStack` (in locales where left is the leading side).

```swift
var body: some View {
    ZStack(alignment: .bottomLeading) {
        Rectangle()
            .fill(Color.red)
            .frame(width: 100, height: 50)
        Rectangle()
            .fill(Color.blue)
            .frame(width:50, height: 100)
    }
    .border(Color.green, width: 1)
}
```

![A green 100 by 100 square containing two overlapping rectangles: on the](https://docs-assets.developer.apple.com/published/b18f4156c9780e8200b05194bff17db4/SwiftUI-ZStack-alignment%402x.png)

> **Note**: If you need a version of this stack that conforms to the [`Layout`](layout.md) protocol, like when you want to create a conditional layout using [`AnyLayout`](anylayout.md), use [`ZStackLayout`](zstacklayout.md) instead.

If you need a version of this stack that conforms to the [`Layout`](layout.md) protocol, like when you want to create a conditional layout using [`AnyLayout`](anylayout.md), use [`ZStackLayout`](zstacklayout.md) instead.

## Topics

### Creating a stack
- [init(alignment: Alignment, content: () -> Content)](zstack/init(alignment:content:).md)
  Creates an instance with the given alignment.
### Supporting symbols
- [struct ZStackContent3D](zstackcontent3d.md)
  A type that adds spacing to a [`ZStack`](zstack.md).
### Initializers
- [init<V>(alignment: Alignment, spacing: CGFloat?, content: () -> V)](zstack/init(alignment:spacing:content:).md)
  Creates an instance with the given spacing and alignment.

## Relationships

### Conforms To
- [View](view.md)

## See Also

- [Adding a background to your view](adding-a-background-to-your-view.md)
  Compose a background behind your view and extend it beyond the safe area insets.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/zstack)*