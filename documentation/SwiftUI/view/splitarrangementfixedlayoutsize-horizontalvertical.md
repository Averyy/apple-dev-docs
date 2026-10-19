# splitArrangementFixedLayoutSize(horizontal:vertical:)

**Framework**: SwiftUI  
**Kind**: method

Sets the preferred size constraint for a view in a split arrangement style to the ideal size of the view within its container.

**Availability**:
- iOS 27.1+
- iPadOS 27.1+
- Mac Catalyst 27.1+
- macOS 27.1+
- tvOS 27.1+
- visionOS 27.1+
- watchOS 27.1+

## Declaration

```swift
nonisolated
func splitArrangementFixedLayoutSize(horizontal: Bool = true, vertical: Bool = true) -> some View
```

#### Discussion

Add this modifier to a view in a split style [`ArrangementView`](arrangementview.md), and specify `true` when you want the system to limit the view’s size to the ideal size for that axis, as the following example shows:

```swift
ArrangementView {
    ChartView()
        .splitArrangementFixedLayoutSize(horizontal: true, vertical: false)
} secondary: {
    NewsView()
}
.arrangementViewStyle(.split)
```

Note that the arrangement view may resize the view to a smaller size depending on the view’s priority.

## Parameters

- `horizontal`: A Boolean value that indicates whether to prefer a fixed width for the view in a horizontal split.
- `vertical`: A Boolean value that indicates whether to prefer a fixed height for the view in a vertical split.

## See Also

- [struct ArrangementView](arrangementview.md)
  A view that dynamically lays out a primary and secondary view based on size class, orientation, and reserved regions.
- [func arrangementViewStyle(some ArrangementViewStyle) -> some View](view/arrangementviewstyle(_:).md)
  Sets the style for arrangement views within this view.
- [protocol ArrangementViewStyle](arrangementviewstyle.md)
  A style that indicates how an arrangement view lays out a primary and secondary view.
- [func overlayArrangementEdge(_:)](view/overlayarrangementedge(_:).md)
  The horizontal edge a view in an overlay arrangement aligns to when the arrangement transitions to a landscape orientation.
- [func splitArrangementLayoutRatio(CGFloat?) -> some View](view/splitarrangementlayoutratio(_:).md)
  Sets the preferred size ratio for a view in a split style arrangement view.
- [func splitArrangementLayoutRatio(minHorizontal: CGFloat?, idealHorizontal: CGFloat?, maxHorizontal: CGFloat?, minVertical: CGFloat?, idealVertical: CGFloat?, maxVertical: CGFloat?) -> some View](view/splitarrangementlayoutratio(minhorizontal:idealhorizontal:maxhorizontal:minvertical:idealvertical:maxvertical:).md)
  Sets the size ratio for a view in a split style arrangement view.
- [func splitArrangementLayoutSize(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?) -> some View](view/splitarrangementlayoutsize(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:).md)
  Sets the size constraints for a view in a split style arrangement view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/splitarrangementfixedlayoutsize(horizontal:vertical:))*