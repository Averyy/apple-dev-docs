# init(x:yStart:yEnd:)

**Framework**: Swift Charts  
**Kind**: init

Creates a vertical rule mark with an x encoding and y interval encoding.

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
init<X, Y>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>) where X : Plottable, Y : Plottable
```

##### Discussion

Use this initializer to create a vertical line at y positions from `yStart` to `yEnd` to an x position:

```swift
Chart(data) {
    RuleMark(
        x: .value("Pollen Source", $0.source),
        yStart: .value("Start Date", $0.startDate),
        yEnd: .value("End Date", $0.endDate)
    )
}
```

![Vertical rule chart with y-axis showing the month in the year 2020 starting with January and ending with December, and with x-axis showing a pollen source: Trees, Grass, and Weeds. There are 4 rules. 2 for Trees 1 starting in January and going until the end of September and 1 spanning December, 1 for Grass starting in March and going until the end of August, and 1 for Weeds starting in April and going until the end of November.](https://docs-assets.developer.apple.com/published/8d9e636deb922381874946adc7aaaae3/LineSegmentMarkSwift.LineSegmentMarkVerticalLineSegmentChart%402x.png)

See [`RuleMark`](rulemark.md) for the setup of the structure that contains the `startDate`, `endDate`, and `source` properties.

## Parameters

- `x`: The value plotted with x.
- `yStart`: The value plotted with y start.
- `yEnd`: The value plotted with y end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/rulemark/init(x:ystart:yend:)-5gy50)*