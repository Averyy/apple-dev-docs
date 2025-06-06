# RuleMark

**Framework**: Swift Charts  
**Kind**: struct

Chart content that represents data using a single horizontal or vertical rule.

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
@MainActor
@preconcurrency struct RuleMark
```

#### Overview

You can use `RuleMark` to plot a horizontal or vertical rule in your chart.

##### Show Range with Rule Marks

To create a horizontal line at a `y` position from `xStart` to `xEnd` you use the `init(xStart:xEnd:y:)` or `init(xStart:xEnd:y:)`.  To create a vertical line at an `x` position from `yStart` to `yEnd` you use `init(x:yStart:yEnd:)` or `init(x:yStart:yEnd:)`. The example below uses the `Pollen` structure and the `init(xStart:xEnd:y:)` to map horizontal lines that span from the value of the `startDate` to the value of the `endDate`  for x positions to a pollen `source` property’s y position:

```swift
struct Pollen {
    var source: String
    var startDate: Date
    var endDate: Date

    init(startMonth: Int, numMonths: Int, source: String) {
        self.source = source
        let calendar = Calendar.autoupdatingCurrent
        self.startDate = calendar.date(from: DateComponents(year: 2020, month: startMonth, day: 1))!
        self.endDate = calendar.date(byAdding: .month, value: numMonths, to: startDate)!
    }
}

var data: [Pollen] = [
    Pollen(startMonth: 1, numMonths: 9, source: "Trees"),
    Pollen(startMonth: 12, numMonths: 1, source: "Trees"),
    Pollen(startMonth: 3, numMonths: 8, source: "Grass"),
    Pollen(startMonth: 4, numMonths: 8, source: "Weeds")
]

var body: some View {
    Chart(data) {
        RuleMark(
            xStart: .value("Start Date", $0.startDate),
            xEnd: .value("End Date", $0.endDate),
            y: .value("Pollen Source", $0.source)
        )
    }
}
```

![Horizontal rule chart with x-axis showing the month in the year 2020 starting with January and ending with December, and with y-axis showing a pollen source: Trees, Grass, and Weeds. There are 4 rules. 2 for Trees 1 starting in January and going until the end of September and 1 spanning December, 1 for Grass starting in March and going until the end of August, and 1 for Weeds starting in April and going until the end of November.](https://docs-assets.developer.apple.com/published/5491601771c8ae97361331c393b3642b/LineSegmentMarkSwift.LineSegmentMarkHorizontalLineSegmentChart%402x.png)

##### Annotate a Chart with Rule Mark

You can annotate a chart with horizontal or vertically spanning rules. This allows viewers to easily compare values over a range to a constant value.  Use the[`init(xStart:xEnd:y:)`](rulemark/init(xstart:xend:y:)-444cp.md) initializer to represent a constant `y` value or [`init(x:yStart:yEnd:)`](rulemark/init(x:ystart:yend:)-6zemd.md) for a constant `x` value. To span the plotting area of a chart with a line, omit the optional start and end parameters and plot a constant value.  The example below results in a line that spans the chart horizontally at the y position of 9000:

```swift
struct DepartmentProfit {
    var department: String
    var profit: Double
}

var data: [DepartmentProfit] = [
    DepartmentProfit(department: "Production", profit: 15000),
    DepartmentProfit(department: "Marketing", profit: 8000),
    DepartmentProfit(department: "Finance", profit: 10000)
]

var body: some View {
    Chart
        ForEach(data) {
            BarMark(
                x: .value("Department", $0.department),
                y: .value("Profit", $0.profit)
            )
        }
        RuleMark(y: .value("Break Even Threshold", 9000))
            .foregroundStyle(.red)
    }
}
```

![Vertical bar chart with x-axis showing department categories Production, Marketing, Finance, and R&D, and with y-axis ranging from 0 to 15000. There are 3 bars: Production 15000, Marketing 8000, Finance 10000. A rule mark at 9000 shows the break even threshold.](https://docs-assets.developer.apple.com/published/7e451f6fe310c4757a2b567b44b30323/LineSegmentMarkSwift.LineSegmentMarkBarChartWithHorizontalLineSegmentMark%402x.png)

## Topics

### Initializers
- [init<X, Y>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>)](rulemark/init(x:ystart:yend:)-5gy50.md)
  Creates a vertical rule mark with an x encoding and y interval encoding.
- [init<X>(x: PlottableValue<X>, yStart: CGFloat?, yEnd: CGFloat?)](rulemark/init(x:ystart:yend:)-6zemd.md)
  Creates a vertical rule mark with value plotted with x.
- [init<Y>(x: CGFloat?, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>)](rulemark/init(x:ystart:yend:)-8iusl.md)
  Creates a vertical rule mark with a fixed x position and y interval encoding.
- [init<X, Y>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: PlottableValue<Y>)](rulemark/init(xstart:xend:y:)-27yvc.md)
  Creates a horizontal rule mark that plots values on its x interval and on y.
- [init<Y>(xStart: CGFloat?, xEnd: CGFloat?, y: PlottableValue<Y>)](rulemark/init(xstart:xend:y:)-444cp.md)
  Creates a horizontal rule mark that plots a value on y.
- [init<X>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: CGFloat?)](rulemark/init(xstart:xend:y:)-6jsoi.md)
  Creates a horizontal rule mark that plots values on its x interval.

## Relationships

### Conforms To
- [ChartContent](chartcontent.md)
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AreaMark](areamark.md)
  Chart content that represents data using the area of one or more regions.
- [struct LineMark](linemark.md)
  Chart content that represents data using a sequence of connected line segments.
- [struct PointMark](pointmark.md)
  Chart content that represents data using points.
- [struct RectangleMark](rectanglemark.md)
  Chart content that represents data using rectangles.
- [struct BarMark](barmark.md)
  Chart content that represents data using bars.
- [struct SectorMark](sectormark.md)
  A sector of a pie or donut chart, which shows how individual categories make up a meaningful total.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/rulemark)*