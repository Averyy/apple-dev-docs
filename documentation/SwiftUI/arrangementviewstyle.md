# ArrangementViewStyle

**Framework**: SwiftUI  
**Kind**: protocol

A style that configures an `ArrangementView` with an arrangement.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency protocol ArrangementViewStyle
```

## Topics

### Getting arrangement view styles
- [static var automatic: AutomaticArrangementViewStyle](arrangementviewstyle/automatic.md)
  The default arrangement view style.
- [static var overlay: OverlayArrangementViewStyle](arrangementviewstyle/overlay.md)
  An arrangement view style that layers the primary view over the secondary view in z-order.
- [static var split: SplitArrangementViewStyle](arrangementviewstyle/split.md)
  An arrangement view style that places the primary and secondary views side by side along one or more axes.
### Creating a view using an arrangement view style
- [func makeBody(configuration: Self.Configuration) -> Self.Body](arrangementviewstyle/makebody(configuration:).md)
  Creates a view for the arrangement view style from the configuration.
- [associatedtype Body : View](arrangementviewstyle/body.md)
- [ArrangementViewStyle.Configuration](arrangementviewstyle/configuration.md)
  The configuration used to create the arrangement view style.
### Supporting Types
- [struct AutomaticArrangementViewStyle](automaticarrangementviewstyle.md)
  The default arrangement view style.
- [struct OverlayArrangementViewStyle](overlayarrangementviewstyle.md)
  An arrangement view style which overlays views.
- [struct SplitArrangementViewStyle](splitarrangementviewstyle.md)
  An arrangement view style which splits views.

## Relationships

### Conforming Types
- [AutomaticArrangementViewStyle](automaticarrangementviewstyle.md)
- [OverlayArrangementViewStyle](overlayarrangementviewstyle.md)
- [SplitArrangementViewStyle](splitarrangementviewstyle.md)

## See Also

- [struct ArrangementView](arrangementview.md)
  A view that arranges primary and secondary content using an adaptive layout that responds to the environment.
- [func arrangementViewStyle(some ArrangementViewStyle) -> some View](view/arrangementviewstyle(_:).md)
  Sets the style for arrangement views within this view.
- [func overlayArrangementEdge(_:)](view/overlayarrangementedge(_:).md)
  The horizontal edge a view in an overlay arrangement occupies when the arrangement transitions to a horizontal layout.
- [func splitArrangementFixedLayoutSize(horizontal: Bool, vertical: Bool) -> some View](view/splitarrangementfixedlayoutsize(horizontal:vertical:).md)
  Sets the preferred size constraint for an arrangement view in a split style to the ideal size of the view within its container. The arrangement view will prefer this size, but may resize to a smaller size depending on the priority of the view.
- [func splitArrangementLayoutRatio(CGFloat?) -> some View](view/splitarrangementlayoutratio(_:).md)
  Sets the preferred size ratio for an arrangement view in a split style. Use this modifier when you want to customize the size of the view compared to its other views in the split layout.
- [func splitArrangementLayoutRatio(minHorizontal: CGFloat?, idealHorizontal: CGFloat?, maxHorizontal: CGFloat?, minVertical: CGFloat?, idealVertical: CGFloat?, maxVertical: CGFloat?) -> some View](view/splitarrangementlayoutratio(minhorizontal:idealhorizontal:maxhorizontal:minvertical:idealvertical:maxvertical:).md)
  Sets the size ratio for an arrangement view in a split style. Use this modifier when you want to customize the size of the view compared to its other views in the split layout.
- [func splitArrangementLayoutSize(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?) -> some View](view/splitarrangementlayoutsize(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:).md)
  Sets the size constraints for an arrangement view in a split style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/arrangementviewstyle)*