# ArrangementViewStyle

**Framework**: SwiftUI  
**Kind**: protocol  
**Role**: Protocol

A style that indicates how an arrangement view lays out a primary and secondary view.

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
@MainActor
@preconcurrency protocol ArrangementViewStyle
```

## Overview

Set an arrangement view style with the [`arrangementViewStyle(_:)`](./view/arrangementviewstyle%28_%29.md) view modifier on an [`ArrangementView`](./arrangementview.md), as the following example shows:

```swift
ArrangementView {
    PlayerControls()
} secondary: {
    VideoPlayer()
}
.arrangementViewStyle(.overlay) 
```

## Topics

### Getting arrangement view styles
- [static var automatic: AutomaticArrangementViewStyle](./arrangementviewstyle/automatic.md)
  The default arrangement view style.
- [struct AutomaticArrangementViewStyle](./automaticarrangementviewstyle.md)
  The default arrangement view style.
- [static var overlay: OverlayArrangementViewStyle](./arrangementviewstyle/overlay.md)
  A style that layers the primary view over the secondary view, or places the views side by side on a folded display.
- [struct OverlayArrangementViewStyle](./overlayarrangementviewstyle.md)
  A style that layers the primary view over the secondary view, or places the views side by side on a folded display.
- [static var split: SplitArrangementViewStyle](./arrangementviewstyle/split.md)
  An arrangement view style that places the primary and secondary views side by side along one or more axes.
- [struct SplitArrangementViewStyle](./splitarrangementviewstyle.md)
  An arrangement view style that places the primary and secondary views side by side along one or more axes.
### Creating a view using an arrangement view style
- [func makeBody(configuration: Self.Configuration) -> Self.Body](./arrangementviewstyle/makebody%28configuration%29.md)
  Creates a view for the arrangement view style from the configuration.
- [associatedtype Body : View](./arrangementviewstyle/body.md)
- [ArrangementViewStyle.Configuration](./arrangementviewstyle/configuration.md)
  The configuration the style uses to create the arrangement view.

## Relationships

### Conforming Types
- [AutomaticArrangementViewStyle](./automaticarrangementviewstyle.md)
- [OverlayArrangementViewStyle](./overlayarrangementviewstyle.md)
- [SplitArrangementViewStyle](./splitarrangementviewstyle.md)

## See Also

### Dynamically arranging a primary and secondary view
- [struct ArrangementView](./arrangementview.md)
  A view that dynamically lays out a primary and secondary view based on size class, orientation, and reserved regions.
- [func arrangementViewStyle(some ArrangementViewStyle) -> some View](./view/arrangementviewstyle%28_%29.md)
  Sets the style for arrangement views within this view.
- [func overlayArrangementEdge(_:)](./view/overlayarrangementedge%28_%29.md)
  The horizontal edge a view in an overlay arrangement aligns to when the arrangement transitions to a landscape orientation.
- [func splitArrangementFixedLayoutSize(horizontal: Bool, vertical: Bool) -> some View](./view/splitarrangementfixedlayoutsize%28horizontal,vertical%29.md)
  Sets the preferred size constraint for a view in a split arrangement style to the ideal size of the view within its container.
- [func splitArrangementLayoutRatio(CGFloat?) -> some View](./view/splitarrangementlayoutratio%28_%29.md)
  Sets the preferred size ratio for a view in a split style arrangement view.
- [func splitArrangementLayoutRatio(minHorizontal: CGFloat?, idealHorizontal: CGFloat?, maxHorizontal: CGFloat?, minVertical: CGFloat?, idealVertical: CGFloat?, maxVertical: CGFloat?) -> some View](./view/splitarrangementlayoutratio%28minhorizontal,idealhorizontal,maxhorizontal,minvertical,idealvertical,maxvertical%29.md)
  Sets the size ratio for a view in a split style arrangement view.
- [func splitArrangementLayoutSize(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?) -> some View](./view/splitarrangementlayoutsize%28minwidth,idealwidth,maxwidth,minheight,idealheight,maxheight%29.md)
  Sets the size constraints for a view in a split style arrangement view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/arrangementviewstyle)*