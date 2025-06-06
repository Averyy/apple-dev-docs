# init(x:y:)

**Framework**: Swift Charts  
**Kind**: init

Creates a line mark.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>) where X : Plottable, Y : Plottable
```

##### Discussion

Use this initializer to create a chart with a single line.

```swift
Chart(sunshineData) {
    LineMark(
        x: .value("Month", $0.date),
        y: .value("Hours of Sunshine", $0.hoursOfSunshine)
    )
}
```

![Line chart with date on x-axis and hours of sunshine on y-axis. One line showing 12 points representing hours of sunshine in a month 1 74, 2 99, 3 154, 4 201, 5 247, 6 234, 7 304, 8 248, 9 197, 10 122, 11 77, 12 62.](https://docs-assets.developer.apple.com/published/f5d223bb9ca48efff7a8b1d5772443a5/LineMarkSwift.LineMarkLineChart%402x.png)

## Parameters

- `x`: The value plotted with x.
- `y`: The value plotted with y.

## See Also

- [init<X, Y, S>(x: PlottableValue<X>, y: PlottableValue<Y>, series: PlottableValue<S>)](linemark/init(x:y:series:).md)
  Creates a separate line for each unique value of series.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/linemark/init(x:y:))*