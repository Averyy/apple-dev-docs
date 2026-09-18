# splitArrangementFixedLayoutSize(horizontal:vertical:)

**Framework**: SwiftUI  
**Kind**: method

Sets the preferred size constraint for an arrangement view in a split style to the ideal size of the view within its container. The arrangement view will prefer this size, but may resize to a smaller size depending on the priority of the view.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
nonisolated
func splitArrangementFixedLayoutSize(horizontal: Bool = true, vertical: Bool = true) -> some View
```

#### Discussion

```swift
ArrangementView {
    ChartView()
        .splitArrangementFixedLayoutSize(horizontal: true, vertical: false)
} secondary: {
    NewsView()
}
.arrangementViewStyle(.split)
```

## Parameters

- `horizontal`: Whether to prefer a fixed width for the view in a horizontal split.
- `vertical`: Whether to prefer a fixed height for the view in a vertical split.

## See Also

- [struct ArrangementView](arrangementview.md)
  A view that arranges primary and secondary content using an adaptive layout that responds to the environment.
- [func arrangementViewStyle(some ArrangementViewStyle) -> some View](view/arrangementviewstyle(_:).md)
  Sets the style for arrangement views within this view.
- [protocol ArrangementViewStyle](arrangementviewstyle.md)
  A style that configures an `ArrangementView` with an arrangement.
- [func overlayArrangementEdge(_:)](view/overlayarrangementedge(_:).md)
  The horizontal edge a view in an overlay arrangement occupies when the arrangement transitions to a horizontal layout.
- [func splitArrangementLayoutRatio(CGFloat?) -> some View](view/splitarrangementlayoutratio(_:).md)
  Sets the preferred size ratio for an arrangement view in a split style. Use this modifier when you want to customize the size of the view compared to its other views in the split layout.
- [func splitArrangementLayoutRatio(minHorizontal: CGFloat?, idealHorizontal: CGFloat?, maxHorizontal: CGFloat?, minVertical: CGFloat?, idealVertical: CGFloat?, maxVertical: CGFloat?) -> some View](view/splitarrangementlayoutratio(minhorizontal:idealhorizontal:maxhorizontal:minvertical:idealvertical:maxvertical:).md)
  Sets the size ratio for an arrangement view in a split style. Use this modifier when you want to customize the size of the view compared to its other views in the split layout.
- [func splitArrangementLayoutSize(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?) -> some View](view/splitarrangementlayoutsize(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:).md)
  Sets the size constraints for an arrangement view in a split style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/splitarrangementfixedlayoutsize(horizontal:vertical:))*