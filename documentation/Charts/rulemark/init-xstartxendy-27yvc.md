# init(xStart:xEnd:y:)

**Framework**: Swift Charts  
**Kind**: init

Creates a horizontal rule mark that plots values on its x interval and on y.

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
init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>) where X : Plottable, Y : Plottable
```

##### Discussion

Use this initializer to create a horizontal rule at x positions from `xStart` to `xEnd` to a y position:

```swift
Chart(data) {
    RuleMark(
        xStart: .value("Start Date", $0.startDate),
        xEnd: .value("End Date", $0.endDate),
        y: .value("Pollen Source", $0.source)
    )
}
```

![Horizontal rule chart with x-axis showing the month in the year 2020 starting with January and ending with December, and with y-axis showing a pollen source: Trees, Grass, and Weeds. There are 4 rules. 2 for Trees 1 starting in January and going until the end of September and 1 spanning December, 1 for Grass starting in March and going until the end of August, and 1 for Weeds starting in April and going until the end of November.](https://docs-assets.developer.apple.com/published/5491601771c8ae97361331c393b3642b/LineSegmentMarkSwift.LineSegmentMarkHorizontalLineSegmentChart%402x.png)

See the second code example in [`RuleMark`](rulemark.md) for the setup of the structure that contains the `startDate`, `endDate`, and `source` properties.

## Parameters

- `xStart`: The value plotted with x start.
- `xEnd`: The value plotted with x end.
- `y`: The value plotted with y.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/rulemark/init(xstart:xend:y:)-27yvc)*