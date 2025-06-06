# chartScrollPosition(y:)

**Framework**: SwiftUI  
**Kind**: method

Associates a binding to be updated when the chart scrolls along the y-axis.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func chartScrollPosition(y: Binding<some Plottable>) -> some View
```

## See Also

- [func chartScrollPosition(initialX: some Plottable) -> some View](view/chartscrollposition(initialx:).md)
  Sets the initial scroll position along the x-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.
- [func chartScrollPosition(initialY: some Plottable) -> some View](view/chartscrollposition(initialy:).md)
  Sets the initial scroll position along the y-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.
- [func chartScrollPosition(x: Binding<some Plottable>) -> some View](view/chartscrollposition(x:).md)
  Associates a binding to be updated when the chart scrolls along the x-axis.
- [func chartScrollTargetBehavior(some ChartScrollTargetBehavior) -> some View](view/chartscrolltargetbehavior(_:).md)
  Sets the scroll behavior of the scrollable chart.
- [func chartScrollableAxes(Axis.Set) -> some View](view/chartscrollableaxes(_:).md)
  Configures the scrollable behavior of charts in this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartscrollposition(y:))*