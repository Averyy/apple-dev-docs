# init(x:yStart:yEnd:)

**Framework**: Swift Charts  
**Kind**: init

Creates a vertical rule mark with a fixed x position and y interval encoding.

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
init<Y>(x: CGFloat? = nil, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>) where Y : Plottable
```

##### Discussion

Use this initializer to create a vertical rule at y positions from `yStart` to `yEnd` for a single x position:

```swift
Chart(data) {
    RuleMark(
        yStart: .value("Start Date", $0.startDate),
        yEnd: .value("End Date", $0.endDate)
    )
}
```

![Vertical rule chart with y-axis showing the month in the year 2020 starting with January and ending with December, and with x-axis showing a pollen source: Trees. There are 2 rules. 1 starting in January and going until the end of September and 1 spanning December.](https://docs-assets.developer.apple.com/published/31d074cac1397acb76198b06c2b6bd65/LineSegmentMarkSwift.LineSegmentMarkVerticalSingleLineSegmentChart%402x.png)

See [`RuleMark`](rulemark.md) for the setup of the structure containing the `startDate`, `endDate`, and `source` properties.

## Parameters

- `x`: The x position.   If   is  , the rule will be centered horizontally by default.
- `yStart`: The value plotted with y start.
- `yEnd`: The value plotted with y end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/rulemark/init(x:ystart:yend:)-8iusl)*