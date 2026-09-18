# ArrangementView

**Framework**: SwiftUI  
**Kind**: struct

A view that arranges primary and secondary content using an adaptive layout that responds to the environment.

**Availability**:
- iOS 27.1+ (Beta)
- iPadOS 27.1+ (Beta)

## Declaration

```swift
nonisolated
struct ArrangementView<Primary, Secondary> where Primary : View, Secondary : View
```

#### Overview

You create an arrangement view with a primary and secondary view. The arrangement view computes a layout for its content based on the context it is presented in, including the available size, size class, and hardware features.

Use the [`arrangementViewStyle(_:)`](view/arrangementviewstyle(_:).md) modifier to choose how the arrangement view lays out its content. The default style is [`AutomaticArrangementViewStyle`](automaticarrangementviewstyle.md), which resolves to a split arrangement. The other built-in styles are [`OverlayArrangementViewStyle`](overlayarrangementviewstyle.md) and [`SplitArrangementViewStyle`](splitarrangementviewstyle.md).

##### Overlay Arrangements

An overlay arrangement layers the primary view on top of the secondary view in z-order. This layout is well-suited for full screen experiences like media players, where playback controls overlay a video surface:

```swift
ArrangementView {
    PlayerControls()
} secondary: {
    VideoPlayer()
}
.arrangementViewStyle(.overlay)
```

When the environment changes, such as when a foldable device is folded, the overlay arrangement can transition its views from a layered layout into a side-by-side layout. Use [`axes(_:)`](overlayarrangementviewstyle/axes(_:).md) to control which axes are supported.

##### Split Arrangements

A split arrangement places the primary and secondary views side by side along one or more axes. Use this layout for experiences that display two distinct pieces of content simultaneously, such as a music player alongside its lyrics:

```swift
ArrangementView {
    NowPlayingView()
} secondary: {
    LyricsView()
}
.arrangementViewStyle(.split)
```

The split arrangement adapts its axis based on the available size and size class. You can constrain which axes the split supports using [`axes(_:)`](splitarrangementviewstyle/axes(_:).md).

## Topics

### Creating an arrangement view
- [init(primary: () -> Primary, secondary: () -> Secondary)](arrangementview/init(primary:secondary:).md)
  Creates an arrangement view with a primary and secondary view.
- [init(ArrangementViewStyleConfiguration)](arrangementview/init(_:).md)
  Creates an arrangement view from a style configuration.
- [struct ArrangementViewStyleConfiguration](arrangementviewstyleconfiguration.md)
  The properties of an arrangement view used to create its custom style.
### Configuring an arrangement view
- [func arrangementViewStyle(some ArrangementViewStyle) -> some View](view/arrangementviewstyle(_:).md)
  Sets the style for arrangement views within this view.

## Relationships

### Conforms To
- [View](view.md)

## See Also

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
- [func splitArrangementLayoutSize(minWidth: CGFloat?, idealWidth: CGFloat?, maxWidth: CGFloat?, minHeight: CGFloat?, idealHeight: CGFloat?, maxHeight: CGFloat?) -> some View](view/splitarrangementlayoutsize(minwidth:idealwidth:maxwidth:minheight:idealheight:maxheight:).md)
  Sets the size constraints for an arrangement view in a split style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/arrangementview)*