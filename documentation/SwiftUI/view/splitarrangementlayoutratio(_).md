# splitArrangementLayoutRatio(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the preferred size ratio for a view in a split style arrangement view.

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
func splitArrangementLayoutRatio(_ ratio: CGFloat?) -> some View
```

#### Discussion

Use this modifier when you want to customize the size of the view compared to the other view in the split layout, as the following example shows:

```swift
ArrangementView {
    ConversationView()
        .splitArrangementLayoutRatio(0.3)
} secondary: {
    PhotosView()
}
.arrangementViewStyle(.split.axes(.horizontal))
```

The arrangement sizes the view with the highest `layoutPriority` using its ratio. When a view has a ratio that would be greater than the remaining size of the arrangement view container, the arrangement uses the remaining size instead. When a view’s ratio prevents filling the container’s total size with both views, the arrangement increases the size of the highest priority view.

## Parameters

- `ratio`: A float value between zero and one that indicates the ratio the view uses for its preferred size.

## See Also

- [struct ArrangementView](arrangementview.md)
  A view that dynamically lays out a primary and secondary view based on size class, orientation, and reserved regions.
- [func arrangementViewStyle(some ArrangementViewStyle) -> some View](view/arrangementviewstyle(_:).md)
  Sets the style for arrangement views within this view.
- [protocol ArrangementViewStyle](arrangementviewstyle.md)
  A style that indicates how an arrangement view lays out a primary and secondary view.
- [func overlayArrangementEdge(_:)](view/overlayarrangementedge(_:).md)
  The horizontal edge a view in an overlay arrangement aligns to when the arrangement transitions to a landscape orientation.
- [func splitArrangementFixedLayoutSize(horizontal: Bool, vertical: Bool) -> some View](view/splitarrangementfixedlayoutsize(horizontal:vertical:).md)
  Sets the preferred size constraint for a view in a split arrangement style to the ideal size of the view within its container.
- [func splitArrangementLayoutRatio(minHorizontal: CGFloat?, idealHorizontal: CGFloat?, maxHorizontal: CGFloat?, minVertical: CGFloat?, idealVertical: CGFloat?, maxVertical: CGFloat?) -> some View](view/splitarrangementlayoutratio(minhorizontal:idealhorizontal:maxhorizontal:minvertical:idealvertical:maxvertical:).md)
  Sets the size ratio for a view in a split style arrangement view.
- [func splitArrangementLayoutSize(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?) -> some View](view/splitarrangementlayoutsize(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:).md)
  Sets the size constraints for a view in a split style arrangement view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/splitarrangementlayoutratio(_:))*