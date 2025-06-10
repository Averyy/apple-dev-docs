# frame(width:height:alignment:)

**Framework**: SwiftUI  
**Kind**: method

Positions this view within an invisible frame with the specified size.

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
nonisolated
func frame(width: CGFloat? = nil, height: CGFloat? = nil, alignment: Alignment = .center) -> some View
```

## Mentions

- [Configuring views](configuring-views.md)
- [Laying out a simple view](laying-out-a-simple-view.md)
- [Building layouts with stack views](building-layouts-with-stack-views.md)

#### Return Value

A view with fixed dimensions of `width` and `height`, for the parameters that are non-`nil`.

#### Discussion

Use this method to specify a fixed size for a view’s width, height, or both. If you only specify one of the dimensions, the resulting view assumes this view’s sizing behavior in the other dimension.

For example, the following code lays out an ellipse in a fixed 200 by 100 frame. Because a shape always occupies the space offered to it by the layout system, the first ellipse is 200x100 points. The second ellipse is laid out in a frame with only a fixed height, so it occupies that height, and whatever width the layout system offers to its parent.

```swift
VStack {
    Ellipse()
        .fill(Color.purple)
        .frame(width: 200, height: 100)
    Ellipse()
        .fill(Color.blue)
        .frame(height: 100)
}
```

![A screenshot showing the effect of frame size options: a purple](https://docs-assets.developer.apple.com/published/90f7ac630e92a53baf01d5297639c05d/SwiftUI-View-frame-1%402x.png)

`The alignment` parameter specifies this view’s alignment within the frame.

```swift
Text("Hello world!")
    .frame(width: 200, height: 30, alignment: .topLeading)
    .border(Color.gray)
```

In the example above, the text is positioned at the top, leading corner of the frame. If the text is taller than the frame, its bounds may extend beyond the bottom of the frame’s bounds.

![A screenshot showing the effect of frame size options on a text view](https://docs-assets.developer.apple.com/published/c38bb439a9c5e2632878344997227e8d/SwiftUI-View-frame-2%402x.png)

## Parameters

- `width`: A fixed width for the resulting view. If   is  ,   the resulting view assumes this view’s sizing behavior.
- `height`: A fixed height for the resulting view. If   is  ,   the resulting view assumes this view’s sizing behavior.
- `alignment`: The alignment of this view inside the resulting frame.   Note that most alignment values have no apparent effect when the   size of the frame happens to match that of this view.

## See Also

- [func frame(depth: CGFloat?, alignment: DepthAlignment) -> some View](view/frame(depth:alignment:).md)
  Positions this view within an invisible frame with the specified depth.
- [func frame(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?, alignment: Alignment) -> some View](view/frame(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:alignment:).md)
  Positions this view within an invisible frame having the specified size constraints.
- [func frame(minDepth: CGFloat?, idealDepth: CGFloat?, maxDepth: CGFloat?, alignment: DepthAlignment) -> some View](view/frame(mindepth:idealdepth:maxdepth:alignment:).md)
  Positions this view within an invisible frame having the specified depth constraints.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment) -> some View](view/containerrelativeframe(_:alignment:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, alignment: Alignment, (CGFloat, Axis) -> CGFloat) -> some View](view/containerrelativeframe(_:alignment:_:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func containerRelativeFrame(Axis.Set, count: Int, span: Int, spacing: CGFloat, alignment: Alignment) -> some View](view/containerrelativeframe(_:count:span:spacing:alignment:).md)
  Positions this view within an invisible frame with a size relative to the nearest container.
- [func fixedSize() -> some View](view/fixedsize.md)
  Fixes this view at its ideal size.
- [func fixedSize(horizontal: Bool, vertical: Bool) -> some View](view/fixedsize(horizontal:vertical:).md)
  Fixes this view at its ideal size in the specified dimensions.
- [func layoutPriority(Double) -> some View](view/layoutpriority(_:).md)
  Sets the priority by which a parent layout should apportion space to this child.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/frame(width:height:alignment:))*