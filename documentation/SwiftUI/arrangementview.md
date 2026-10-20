# ArrangementView

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A view that dynamically lays out a primary and secondary view based on size class, orientation, and reserved regions.

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
struct ArrangementView<Primary, Secondary> where Primary : View, Secondary : View
```

#### Overview

Use an arrangement view to lay out two related content views differently depending on the current size classes, orientation, and status of reserved regions such as the fold on iPhone Duo. The arrangement view helps you improve how your app handles a folded display in addition to a flat display.

Because an arrangement view is a container that lays out other views, avoid adding an arrangement view inside another container such as a scroll view, navigation split view, grid, or other container view that lays out other views. Also avoid placing some container views inside an arrangement view, such as a navigation split view or tab view.

When iPhone Duo is fully open or closed, people interact with the flat display like other iPhone and iPad models. An arrangement view is useful when:

- You want to place two views next to each other horizontally when someone is holding a device in landscape orientation or above and below each other when someone is holding a device in portrait orientation, without having to write conditional logic to switch between horizontal and vertical stacks.
- You want to automatically adjust how much space two views take when someone folds the display.
- You want to layer one view over another view on a flat display, and place the views next to each other when the device is folded. This arrangement works well when there’s a clear foreground and background relationship between your views, such as a view for video playback and a view with playback controls.

Arrangement views offer two distinct styles: split and overlay. You specify the split arrangement view style to indicate that the views lay out next to each other, either horizontally or vertically. You specify the overlay style to indicate that the views layer over each other on a flat display and next to each other on a folded display.

For more information on designing your app to use an arrangement view, see [Designing for iPhone Duo](https://developer.apple.com/design/human-interface-guidelines/designing-for-iphone-duo).

#### Configure an overlay arrangement view

An overlay arrangement view places a primary view and a secondary view in a stacked arrangement when the device has a flat display, or next to each other horizontally when someone is holding a folded device in landscape orientation or above and below each other when someone is holding a folded device in portrait orientation. Here’s how the overlay arrangement positions the primary and secondary views:

- In a stacked overlay arrangement, the arrangement view places the primary view above the secondary view in the z-axis.
- When someone holds a folded iPhone Duo in landscape orientation, the arrangement view places the secondary view in the leading position and the primary view in the trailing position.
- When someone holds a folded iPhone Duo in portrait orientation, the arrangement view places the secondary view in the top position and the primary view in the bottom position.

Create an overlay arrangement view by specifying a primary and secondary view, and add the [`arrangementViewStyle(_:)`](./view/arrangementviewstyle%28_%29.md) modifier with [`overlay`](./arrangementviewstyle/overlay.md), as the following example shows:

```swift
ArrangementView {
    PlayerControls()
} secondary: {
    VideoPlayer()
}
.arrangementViewStyle(.overlay) 
```

For more information on configuring layout for a folded iPhone Duo in an overlay arrangement, see [Customize a folded layout](./overlayarrangementviewstyle.md#Customize-a-folded-layout).

#### Configure a split arrangement view

Unlike an overlay arrangement, which typically layers its two views and only separates them when the device folds, a split arrangement view always keeps its primary and secondary views in separate spaces: next to each other horizontally when someone is holding the device in landscape orientation, or stacked vertically when someone is holding the device in portrait orientation. Here’s how the split arrangement positions the primary and secondary views:

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

For more information on adjusting view sizes in a split arrangement, see [Adjust layout sizing in a split arrangement](./splitarrangementviewstyle.md#Adjust-layout-sizing-in-a-split-arrangement).

#### Limit an arrangement by orientation

You can limit which axes your split or overlay arrangement view supports by specifying the axes for the arrangement view style. The following example shows an arrangement that only splits vertically:

```swift
ArrangementView {
    PrimaryContent()
} secondary: {
    SecondaryContent()
}
.arrangementViewStyle(.split.axes(.vertical))
```

Use [`axes(_:)`](./splitarrangementviewstyle/axes%28_%29.md) to set the axes for a split style, or [`axes(_:)`](./overlayarrangementviewstyle/axes%28_%29.md) to set the axes for an overlay style.

## Topics

### Creating an arrangement view
- [init(primary: () -> Primary, secondary: () -> Secondary)](./arrangementview/init%28primary,secondary%29.md)
  Creates an arrangement view with a primary and secondary view.
- [init(ArrangementViewStyleConfiguration)](./arrangementview/init%28_%29.md)
  Creates an arrangement view from a style configuration.
- [struct ArrangementViewStyleConfiguration](./arrangementviewstyleconfiguration.md)
  The properties of an arrangement view you provide to create a custom style.
### Configuring an arrangement view
- [func arrangementViewStyle(some ArrangementViewStyle) -> some View](./view/arrangementviewstyle%28_%29.md)
  Sets the style for arrangement views within this view.

## Relationships

### Conforms To
- [View](./view.md)

## See Also

### Dynamically arranging a primary and secondary view
- [func arrangementViewStyle(some ArrangementViewStyle) -> some View](./view/arrangementviewstyle%28_%29.md)
  Sets the style for arrangement views within this view.
- [protocol ArrangementViewStyle](./arrangementviewstyle.md)
  A style that indicates how an arrangement view lays out a primary and secondary view.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/arrangementview)*