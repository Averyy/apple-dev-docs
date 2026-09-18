# splitArrangementLayoutSize(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:)

**Framework**: SwiftUI  
**Kind**: method

Sets the size constraints for an arrangement view in a split style.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
nonisolated
func splitArrangementLayoutSize(minWidth: CGFloat? = nil, idealWidth: CGFloat? = nil, maxWidth: CGFloat? = nil, minHeight: CGFloat? = nil, idealHeight: CGFloat? = nil, maxHeight: CGFloat? = nil) -> some View
```

#### Discussion

Views with higher `layoutPriority` are sized first using their ideal size, clamped to their min and max values. Width constraints apply to horizontal arrangements, and height constraints apply to vertical arrangements.

```swift
ArrangementView {
    PhotoView()
        .splitArrangementLayoutSize(
            minWidth: 200,
            idealWidth: 320,
            maxWidth: 400)
} secondary: {
    InfoView()
}
.arrangementViewStyle(.split)
```

## Parameters

- `minWidth`: The minimum width for horizontal splits.
- `idealWidth`: The ideal width for horizontal splits.
- `maxWidth`: The maximum width for horizontal splits.
- `minHeight`: The minimum height for vertical splits.
- `idealHeight`: The ideal height for vertical splits.
- `maxHeight`: The maximum height for vertical splits.

## See Also

- [struct ArrangementView](arrangementview.md)
  A view that arranges primary and secondary content using an adaptive layout that responds to the environment.
- [func arrangementViewStyle(some ArrangementViewStyle) -> some View](view/arrangementviewstyle(_:).md)
  Sets the style for arrangement views within this view.
- [protocol ArrangementViewStyle](arrangementviewstyle.md)
  A style that configures an `ArrangementView` with an arrangement.
- [func overlayArrangementEdge(_:)](view/overlayarrangementedge(_:).md)
  The horizontal edge a view in an overlay arrangement occupies when the arrangement transitions to a horizontal layout.
- [func splitArrangementFixedLayoutSize(horizontal: Bool, vertical: Bool) -> some View](view/splitarrangementfixedlayoutsize(horizontal:vertical:).md)
  Sets the preferred size constraint for an arrangement view in a split style to the ideal size of the view within its container. The arrangement view will prefer this size, but may resize to a smaller size depending on the priority of the view.
- [func splitArrangementLayoutRatio(CGFloat?) -> some View](view/splitarrangementlayoutratio(_:).md)
  Sets the preferred size ratio for an arrangement view in a split style. Use this modifier when you want to customize the size of the view compared to its other views in the split layout.
- [func splitArrangementLayoutRatio(minHorizontal: CGFloat?, idealHorizontal: CGFloat?, maxHorizontal: CGFloat?, minVertical: CGFloat?, idealVertical: CGFloat?, maxVertical: CGFloat?) -> some View](view/splitarrangementlayoutratio(minhorizontal:idealhorizontal:maxhorizontal:minvertical:idealvertical:maxvertical:).md)
  Sets the size ratio for an arrangement view in a split style. Use this modifier when you want to customize the size of the view compared to its other views in the split layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/splitarrangementlayoutsize(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:))*