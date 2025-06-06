# chartScrollTargetBehavior(_:)

**Framework**: SwiftUI  
**Kind**: method

Sets the scroll behavior of the scrollable chart.

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
func chartScrollTargetBehavior(_ behavior: some ChartScrollTargetBehavior) -> some View
```

#### Discussion

Use this method to control how the chart scrolls and aligns when the user finishes scrolling. The example below sets the scroll target behavior to align to the values in the chart. When the user finishes scrolling, the chart will settle to align with the values in the chart.

```swift
Chart(data) {
    BarMark(
        x: .value("x", $0.x),
        y: .value("y", $0.y)
    )
}
.chartScrollableAxes(.vertical)
.chartYVisibleDomain(length: 10)
.chartScrollTargetBehavior(.valueAligned(unit: 1))
```

## Parameters

- `behavior`: The chart scroll target behavior.

## See Also

- [func chartScrollPosition(initialX: some Plottable) -> some View](view/chartscrollposition(initialx:).md)
  Sets the initial scroll position along the x-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.
- [func chartScrollPosition(initialY: some Plottable) -> some View](view/chartscrollposition(initialy:).md)
  Sets the initial scroll position along the y-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.
- [func chartScrollPosition(x: Binding<some Plottable>) -> some View](view/chartscrollposition(x:).md)
  Associates a binding to be updated when the chart scrolls along the x-axis.
- [func chartScrollPosition(y: Binding<some Plottable>) -> some View](view/chartscrollposition(y:).md)
  Associates a binding to be updated when the chart scrolls along the y-axis.
- [func chartScrollableAxes(Axis.Set) -> some View](view/chartscrollableaxes(_:).md)
  Configures the scrollable behavior of charts in this view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartscrolltargetbehavior(_:))*