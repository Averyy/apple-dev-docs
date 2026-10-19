# OverlayArrangementViewStyle

**Framework**: SwiftUI  
**Kind**: struct

A style that layers the primary view over the secondary view, or places the views side by side on a folded display.

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
struct OverlayArrangementViewStyle
```

#### Overview

An overlay arrangement view places a primary view and a secondary view in a stacked arrangement when the device has a flat display, or next to each other horizontally when someone is holding a folded device in landscape orientation or above and below each other when someone is holding a folded device in portrait orientation. Here’s how the overlay arrangement positions the primary and secondary views:

- In a stacked overlay arrangement, the arrangement view places the primary view above the secondary view in the z-axis.
- When someone holds a folded iPhone Duo in landscape orientation, the arrangement view places the secondary view in the leading position and the primary view in the trailing position.
- When someone holds a folded iPhone Duo in portrait orientation, the arrangement view places the secondary view in the top position and the primary view in the bottom position.

Create an overlay arrangement view by specifying a primary and secondary view, and add the [`arrangementViewStyle(_:)`](view/arrangementviewstyle(_:).md) modifier with [`overlay`](arrangementviewstyle/overlay.md), as the following example shows:

```swift
ArrangementView {
    PlayerControls()
} secondary: {
    VideoPlayer()
}
.arrangementViewStyle(.overlay) 
```

#### Limit an Overlay Arrangement By Orientation

You can limit which axes your overlay arrangement view supports by specifying the axes for the arrangement view style. The following example shows an arrangement that only functions vertically:

```swift
ArrangementView {
    PrimaryContent()
} secondary: {
    SecondaryContent()
}
.arrangementViewStyle(.overlay.axes(.vertical))
```

Use [`axes(_:)`](overlayarrangementviewstyle/axes(_:).md) to set the axes for an overlay arrangement style. For axes that you don’t include, the arrangement view only displays the primary view.

#### Customize a Folded Layout

Add the horizontal [`overlayArrangementEdge(_:)`](view/overlayarrangementedge(_:)-8slwf.md) or vertical [`overlayArrangementEdge(_:)`](view/overlayarrangementedge(_:)-4tjwn.md) view modifier to adjust how the overlay arrangement positions the primary and secondary views on a folded iPhone Duo. The following example shows a modifier that causes the primary view to appear in the leading position instead of the trailing position when someone holds a folded iPhone Duo in landscape orientation:

```swift
ArrangementView {
    PlayerControls()
        .overlayArrangementEdge(.leading)
} secondary: {
    VideoPlayer()
}
.arrangementViewStyle(.overlay) 
```

## Topics

### Creating an overlay arrangement view style
- [init()](overlayarrangementviewstyle/init.md)
  Creates an overlay arrangement style.
### Specifying overlay arrangement axes
- [func axes(Axis.Set) -> OverlayArrangementViewStyle](overlayarrangementviewstyle/axes(_:).md)
  Creates an overlay arrangement that lays out its views along the axes you provide.

## Relationships

### Conforms To
- [ArrangementViewStyle](arrangementviewstyle.md)

## See Also

- [static var automatic: AutomaticArrangementViewStyle](arrangementviewstyle/automatic.md)
  The default arrangement view style.
- [struct AutomaticArrangementViewStyle](automaticarrangementviewstyle.md)
  The default arrangement view style.
- [static var overlay: OverlayArrangementViewStyle](arrangementviewstyle/overlay.md)
  A style that layers the primary view over the secondary view, or places the views side by side on a folded display.
- [static var split: SplitArrangementViewStyle](arrangementviewstyle/split.md)
  An arrangement view style that places the primary and secondary views side by side along one or more axes.
- [struct SplitArrangementViewStyle](splitarrangementviewstyle.md)
  An arrangement view style that places the primary and secondary views side by side along one or more axes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/overlayarrangementviewstyle)*