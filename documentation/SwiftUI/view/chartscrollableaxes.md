# chartScrollableAxes(_:)

**Framework**: SwiftUI  
**Kind**: method

Configures the scrollable behavior of charts in this view.

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
func chartScrollableAxes(_ axes: Axis.Set) -> some View
```

#### Discussion

Use this method to make a chart scrollable. Below is an example that makes a chart scrollable along the horizontal axis.

```swift
Chart(data) {
    BarMark(
        x: .value("x", $0.x),
        y: .value("y", $0.y)
    )
}
.chartScrollableAxes(.horizontal)
```

> **Note**: When scrolling is enabled along an axis, a default portion of the chart will be made visible. You can use the `chartXVisibleDomain` or `chartYVisibleDomain` modifiers to configure the visible domain.

When scrolling is enabled along an axis, a default portion of the chart will be made visible. You can use the `chartXVisibleDomain` or `chartYVisibleDomain` modifiers to configure the visible domain.

## Parameters

- `axes`: The set of axes to enable scrolling.

## See Also

- [func chartScrollPosition(initialX: some Plottable) -> some View](view/chartscrollposition(initialx:).md)
  Sets the initial scroll position along the x-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.
- [func chartScrollPosition(initialY: some Plottable) -> some View](view/chartscrollposition(initialy:).md)
  Sets the initial scroll position along the y-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.
- [func chartScrollPosition(x: Binding<some Plottable>) -> some View](view/chartscrollposition(x:).md)
  Associates a binding to be updated when the chart scrolls along the x-axis.
- [func chartScrollPosition(y: Binding<some Plottable>) -> some View](view/chartscrollposition(y:).md)
  Associates a binding to be updated when the chart scrolls along the y-axis.
- [func chartScrollTargetBehavior(some ChartScrollTargetBehavior) -> some View](view/chartscrolltargetbehavior(_:).md)
  Sets the scroll behavior of the scrollable chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartscrollableaxes(_:))*