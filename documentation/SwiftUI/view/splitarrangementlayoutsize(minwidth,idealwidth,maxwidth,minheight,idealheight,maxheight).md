# splitArrangementLayoutSize(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Sets the size constraints for a view in a split style arrangement view.

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
func splitArrangementLayoutSize(minWidth: CGFloat? = nil, idealWidth: CGFloat? = nil, maxWidth: CGFloat? = nil, minHeight: CGFloat? = nil, idealHeight: CGFloat? = nil, maxHeight: CGFloat? = nil) -> some View
```

#### Discussion

Use this modifier to specify the size of a view in a split arrangement, as the following example shows:

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

The arrangement sizes the view with higher `layoutPriority` using its ideal size, clamped to the minimum and maximum values. The arrangement applies width constraints to horizontal arrangement layouts, and height constraints to vertical arrangement layouts.

## Parameters

- `minWidth`: A float value that specifies the minimum width in points for a horizontal split arrangement.
- `idealWidth`: A float value that specifies the ideal width in points for a horizontal split arrangement.
- `maxWidth`: A float value that specifies the maximum width in points for a horizontal split arrangement.
- `minHeight`: A float value that specifies the minimum height in points for a vertical split arrangement.
- `idealHeight`: A float value that specifies the ideal height in points for a vertical split arrangement.
- `maxHeight`: A float value that specifies the maximum height in points for a vertical split arrangement.

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
- [func splitArrangementLayoutRatio(minHorizontal: CGFloat?, idealHorizontal: CGFloat?, maxHorizontal: CGFloat?, minVertical: CGFloat?, idealVertical: CGFloat?, maxVertical: CGFloat?) -> some View](./splitarrangementlayoutratio%28minhorizontal,idealhorizontal,maxhorizontal,minvertical,idealvertical,maxvertical%29.md)
  Sets the size ratio for a view in a split style arrangement view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/splitarrangementlayoutsize(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:))*