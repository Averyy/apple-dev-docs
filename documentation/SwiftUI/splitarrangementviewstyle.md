# SplitArrangementViewStyle

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

An arrangement view style that places the primary and secondary views side by side along one or more axes.

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
struct SplitArrangementViewStyle
```

## Overview

A split arrangement view keeps its primary and secondary views in separate spaces: next to each other horizontally when someone is holding the device in landscape orientation, or stacked vertically when someone is holding the device in portrait orientation. Here’s how the split arrangement positions the primary and secondary views:

- In landscape orientation, the arrangement view places the primary view in the leading position and the secondary view in the trailing position.
- In portrait orientation, the arrangement view places the primary view in the top position and the secondary view in the bottom position.
- When someone is holding a closed iPhone Duo in landscape orientation, the split arrangement only shows the primary view.

Create a split arrangement view by specifying a primary and secondary view, and add the [`arrangementViewStyle(_:)`](./view/arrangementviewstyle%28_%29.md) modifier with [`split`](./arrangementviewstyle/split.md), as the following example shows:

```swift
ArrangementView {
    NowPlayingView()
} secondary: {
    LyricsView()
}
.arrangementViewStyle(.split)
```

## Adjust layout sizing in a split arrangement

By default, a split arrangement view sizes the primary and secondary views equally when a display has one region. Set a fixed layout size or layout ratio to influence how the arrangement view computes the sizes for each view. In the following example, adding the [`splitArrangementLayoutRatio(_:)`](./view/splitarrangementlayoutratio%28_%29.md) view modifier to `PrimaryContent()` sets a value for a ratio that the arrangement uses to calculate how much of the display’s available space to use for the primary view:

```swift
ArrangementView {
    PrimaryContent()
        .splitArrangementLayoutRatio(0.3)
} secondary: {
    SecondaryContent()
}
```

Use [`splitArrangementLayoutRatio(_:)`](./view/splitarrangementlayoutratio%28_%29.md) or [`splitArrangementLayoutRatio(minHorizontal:idealHorizontal:maxHorizontal:minVertical:idealVertical:maxVertical:)`](./view/splitarrangementlayoutratio%28minhorizontal,idealhorizontal,maxhorizontal,minvertical,idealvertical,maxvertical%29.md) to specify a ratio for a view, or use [`splitArrangementLayoutSize(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:)`](./view/splitarrangementlayoutsize%28minwidth,idealwidth,maxwidth,minheight,idealheight,maxheight%29.md) to specify a size for a view. Use the [`splitArrangementFixedLayoutSize(horizontal:vertical:)`](./view/splitarrangementfixedlayoutsize%28horizontal,vertical%29.md) modifier to have the system calculate the preferred size for the view.

## Limit a split arrangement by orientation

You can limit which axes your split arrangement view supports by specifying the axes for the arrangement view style. The following example shows an arrangement that only splits vertically:

```swift
ArrangementView {
    PrimaryContent()
} secondary: {
    SecondaryContent()
}
.arrangementViewStyle(.split.axes(.vertical))
```

Use [`axes(_:)`](./splitarrangementviewstyle/axes%28_%29.md) to set the axes for a split arrangement style. For axes that you don’t include, the arrangement view only displays the primary view.

## Topics

### Creating a split arrangement view style
- [init()](./splitarrangementviewstyle/init%28%29.md)
  Creates a split arrangement style.
### Specifying split arrangement axes
- [func axes(Axis.Set) -> SplitArrangementViewStyle](./splitarrangementviewstyle/axes%28_%29.md)
  Creates a split arrangement that lays out its views along the axes you provide.

## Relationships

### Conforms To
- [ArrangementViewStyle](./arrangementviewstyle.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/splitarrangementviewstyle)*