# splitArrangementLayoutRatio(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the preferred size ratio for an arrangement view in a split style. Use this modifier when you want to customize the size of the view compared to its other views in the split layout.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
nonisolated
func splitArrangementLayoutRatio(_ ratio: CGFloat?) -> some View
```

#### Discussion

The view with the highest `layoutPriority` will be sized first using its ratio. When a ratio is used on a view that would be greater than the remaining size of the arrangement view container, the remaining size will be used. When a ratio of a view would result in the views of the container not filling its total size, the highest priority view will fill the remaining size of the container.

```swift
ArrangementView {
    ConversationView()
        .splitArrangementLayoutRatio(0.3)
} secondary: {
    PhotosView()
}
.arrangementViewStyle(.split.axes(.horizontal))
```

## Parameters

- `ratio`: The ratio the view uses for its preferred size.

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
- [func splitArrangementLayoutRatio(minHorizontal: CGFloat?, idealHorizontal: CGFloat?, maxHorizontal: CGFloat?, minVertical: CGFloat?, idealVertical: CGFloat?, maxVertical: CGFloat?) -> some View](view/splitarrangementlayoutratio(minhorizontal:idealhorizontal:maxhorizontal:minvertical:idealvertical:maxvertical:).md)
  Sets the size ratio for an arrangement view in a split style. Use this modifier when you want to customize the size of the view compared to its other views in the split layout.
- [func splitArrangementLayoutSize(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?) -> some View](view/splitarrangementlayoutsize(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:).md)
  Sets the size constraints for an arrangement view in a split style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/splitarrangementlayoutratio(_:))*