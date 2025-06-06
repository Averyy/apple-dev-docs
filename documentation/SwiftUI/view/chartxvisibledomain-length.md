# chartXVisibleDomain(length:)

**Framework**: SwiftUI  
**Kind**: method

Sets the length of the visible domain in the X dimension.

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
func chartXVisibleDomain<P>(length: P) -> some View where P : Plottable, P : Numeric
```

#### Discussion

Use this method to control how much of the chart is visible in a scrollable chart. The example below sets the visible portion of the chart to 10 units in the X axis.

```swift
Chart(data) {
    BarMark(
        x: .value("x", $0.x),
        y: .value("y", $0.y)
    )
}
.chartScrollableAxes(.horizontal)
.chartXVisibleDomain(length: 10)
```

## Parameters

- `length`: The length of the visible domain measured in data units.   For categorical data, this should be the number of visible categories.

## See Also

- [func chartYVisibleDomain<P>(length: P) -> some View](view/chartyvisibledomain(length:).md)
  Sets the length of the visible domain in the Y dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartxvisibledomain(length:))*