# overlayArrangementEdge(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

The horizontal edge a view in an overlay arrangement aligns to when the arrangement transitions to a landscape orientation.

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
func overlayArrangementEdge(_ edge: HorizontalEdge?) -> some View
```

**Other overloads**:

```swift
nonisolated
func overlayArrangementEdge(_ edge: VerticalEdge?) -> some View
```

## Discussion

Use this modifier to anchor the given view when its overlay layout transitions into a landscape orientation. For example, to move the view to the trailing side of the arrangement view, use the [`HorizontalEdge.trailing`](../horizontaledge/trailing.md) edge.

```swift
var body: some View {
    ArrangementView {
        ControlsView()
            .overlayArrangementEdge(.trailing)
    } secondary: {
        ContentView()
    }
}
```

## Parameters

- `edge`: The horizontal edge against which the arrangement aligns the view.

## See Also

### Dynamically arranging a primary and secondary view
- [struct ArrangementView](../arrangementview.md)
  A view that dynamically lays out a primary and secondary view based on size class, orientation, and reserved regions.
- [func arrangementViewStyle(some ArrangementViewStyle) -> some View](./arrangementviewstyle%28_%29.md)
  Sets the style for arrangement views within this view.
- [protocol ArrangementViewStyle](../arrangementviewstyle.md)
  A style that indicates how an arrangement view lays out a primary and secondary view.
- [func splitArrangementFixedLayoutSize(horizontal: Bool, vertical: Bool) -> some View](./splitarrangementfixedlayoutsize%28horizontal,vertical%29.md)
  Sets the preferred size constraint for a view in a split arrangement style to the ideal size of the view within its container.
- [func splitArrangementLayoutRatio(CGFloat?) -> some View](./splitarrangementlayoutratio%28_%29.md)
  Sets the preferred size ratio for a view in a split style arrangement view.
- [func splitArrangementLayoutRatio(minHorizontal: CGFloat?, idealHorizontal: CGFloat?, maxHorizontal: CGFloat?, minVertical: CGFloat?, idealVertical: CGFloat?, maxVertical: CGFloat?) -> some View](./splitarrangementlayoutratio%28minhorizontal,idealhorizontal,maxhorizontal,minvertical,idealvertical,maxvertical%29.md)
  Sets the size ratio for a view in a split style arrangement view.
- [func splitArrangementLayoutSize(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?) -> some View](./splitarrangementlayoutsize%28minwidth,idealwidth,maxwidth,minheight,idealheight,maxheight%29.md)
  Sets the size constraints for a view in a split style arrangement view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/overlayarrangementedge(_:))*