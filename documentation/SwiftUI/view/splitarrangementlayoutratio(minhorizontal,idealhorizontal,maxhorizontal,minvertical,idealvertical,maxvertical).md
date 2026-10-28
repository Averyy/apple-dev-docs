# splitArrangementLayoutRatio(minHorizontal:idealHorizontal:maxHorizontal:minVertical:idealVertical:maxVertical:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the size ratio for a view in a split style arrangement view.

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
func splitArrangementLayoutRatio(minHorizontal: CGFloat? = nil, idealHorizontal: CGFloat? = nil, maxHorizontal: CGFloat? = nil, minVertical: CGFloat? = nil, idealVertical: CGFloat? = nil, maxVertical: CGFloat? = nil) -> some View
```

## Discussion

Use this modifier when you want to customize the size of a view compared to the other view in the split arrangement, as the following example shows:

```swift
ArrangementView {
    NumpadView()
        .splitArrangementLayoutRatio(
            minHorizontal: 0.2,
            idealHorizontal: 0.3,
            maxHorizontal: 0.5,
            idealVertical: 0.4)
} secondary: {
    HistoryView()
}
.arrangementViewStyle(.split)
```

## Parameters

- `minHorizontal`: A float value between zero and one that indicates the minimum ratio for a horizontal split arrangement.
- `idealHorizontal`: A float value between zero and one that indicates the ideal ratio for a horizontal split arrangement.
- `maxHorizontal`: A float value between zero and one that indicates the maximum ratio for a horizontal split arrangement.
- `minVertical`: A float value between zero and one that indicates the minimum ratio for a vertical split arrangement.
- `idealVertical`: A float value between zero and one that indicates the ideal ratio for a vertical split arrangement.
- `maxVertical`: A float value between zero and one that indicates the maximum ratio for a vertical split arrangement.

## See Also

### Dynamically arranging a primary and secondary view
- [struct ArrangementView](../arrangementview.md)
  A view that dynamically lays out a primary and secondary view based on size class, orientation, and reserved regions.
- [func arrangementViewStyle(some ArrangementViewStyle) -> some View](./arrangementviewstyle%28_%29.md)
  Sets the style for arrangement views within this view.
- [protocol ArrangementViewStyle](../arrangementviewstyle.md)
  A style that indicates how an arrangement view lays out a primary and secondary view.
- [func overlayArrangementEdge(_:)](./overlayarrangementedge%28_%29.md)
  The horizontal edge a view in an overlay arrangement aligns to when the arrangement transitions to a landscape orientation.
- [func splitArrangementFixedLayoutSize(horizontal: Bool, vertical: Bool) -> some View](./splitarrangementfixedlayoutsize%28horizontal,vertical%29.md)
  Sets the preferred size constraint for a view in a split arrangement style to the ideal size of the view within its container.
- [func splitArrangementLayoutRatio(CGFloat?) -> some View](./splitarrangementlayoutratio%28_%29.md)
  Sets the preferred size ratio for a view in a split style arrangement view.
- [func splitArrangementLayoutSize(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?) -> some View](./splitarrangementlayoutsize%28minwidth,idealwidth,maxwidth,minheight,idealheight,maxheight%29.md)
  Sets the size constraints for a view in a split style arrangement view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/splitarrangementlayoutratio(minhorizontal:idealhorizontal:maxhorizontal:minvertical:idealvertical:maxvertical:))*