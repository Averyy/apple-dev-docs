# init(xStart:xEnd:y:)

**Framework**: Swift Charts  
**Kind**: init

Creates a horizontal rule mark that plots values on its x interval.

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
init<X>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: CGFloat? = nil) where X : Plottable
```

##### Discussion

Use this initializer to create a horizontal rule at x positions from `xStart` to `xEnd` for a single y position:

```swift
Chart(data) {
    RuleMark(
        xStart: .value("Start Date", $0.startDate),
        xEnd: .value("End Date", $0.endDate)
    )
}
```

![Horizontal rule chart with x-axis showing the month in the year 2020 starting with January and ending with December, and with y-axis showing a pollen source: Trees. There are 2 rules. 1 starting in January and going until the end of September and 1 spanning December.](https://docs-assets.developer.apple.com/published/72b85015d5a997aee308bad17bac88e5/LineSegmentMarkSwift.LineSegmentMarkHorizontalSingleLineSegmentChart%402x.png)

See the second code example in [`RuleMark`](rulemark.md) for the setup of the structure that contains the `startDate`, `endDate`, and `source` properties.

## Parameters

- `xStart`: The value plotted with x start.
- `xEnd`: The value plotted with x end.
- `y`: The y position.   If   is  , the rule will be centered vertically by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/rulemark/init(xstart:xend:y:)-6jsoi)*