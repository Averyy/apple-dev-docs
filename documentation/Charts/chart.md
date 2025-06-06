# Chart

**Framework**: Swift Charts  
**Kind**: struct

A SwiftUI view that displays a chart.

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
@preconcurrency struct Chart<Content> where Content : ChartContent
```

## Mentions

- [Creating a chart using Swift Charts](creating-a-chart-using-swift-charts.md)

#### Overview

To create a chart, instantiate a `Chart` structure with marks that display the properties of your data. For example, suppose you have an array of `ValuePerCategory` structures that define data points composed of a `category` and a `value`:

```swift
struct ValuePerCategory {
    var category: String
    var value: Double
}

let data: [ValuePerCategory] = [
    .init(category: "A", value: 5),
    .init(category: "B", value: 9),
    .init(category: "C", value: 7)
]
```

You can use [`BarMark`](barmark.md) inside a chart to represent the `category` property as different bars in the chart and the `value` property as the y value for each bar:

```swift
Chart(data, id: \.category) { item in
    BarMark(
        x: .value("Category", item.category),
        y: .value("Value", item.value)
    )
}
```

This chart initializer behaves a lot like a SwiftUI [`ForEach`](https://developer.apple.com/documentation/SwiftUI/ForEach), creating a mark — in this case, a bar — for each of the values in the `data` array:

![A bar chart with three categories A, B, and C on the x-axis and a range of 0 to 10 on the y-axis. A bar appears in each category. All the bars are the same color. The first has a value of 5. The second has a value of 9. The third has a value of 7.](https://docs-assets.developer.apple.com/published/e8d88794fa77f18d67e494cac557a292/chart-1-macOS%402x.png)

##### Controlling Data Series Inside a Chart

You can compose more sophisticated charts by providing more than one series of marks to the chart. For example, suppose you have profit data for two companies:

```swift
struct ProfitOverTime {
    var date: Date
    var profit: Double
}

let departmentAProfit: [ProfitOverTime] = <#Profit array A#>
let departmentBProfit: [ProfitOverTime] = <#Profit array B#>
```

The following chart creates two different series of [`LineMark`](linemark.md) instances with different colors to represent the data for each company. In effect, it moves the `ForEach` construct from the chart’s initializer into the body of the chart, enabling you to represent multiple different series:

```swift
Chart {
    ForEach(departmentAProfit, id: \.date) { item in
        LineMark(
            x: .value("Date", item.date),
            y: .value("Profit A", item.profit),
            series: .value("Company", "A")
        )
        .foregroundStyle(.blue)
    }
    ForEach(departmentBProfit, id: \.date) { item in
        LineMark(
            x: .value("Date", item.date),
            y: .value("Profit B", item.profit),
            series: .value("Company", "B")
        )
        .foregroundStyle(.green)
    }
    RuleMark(
        y: .value("Threshold", 400)
    )
    .foregroundStyle(.red)
}
```

You indicate which series a line mark belongs to by specifying its `series` input parameter. The above chart also uses a [`RuleMark`](rulemark.md) to produce a horizontal line segment that displays a constant threshold value across the width of the chart:

![A line chart with three lines. Dates appear on the x-axis, spanning one full month, and company profit appears on the y-axis in the range of 0 to 750. Two of the lines trend upward from left to right, with occasional downward movement. The third line is purely horizontal at the level of 400.](https://docs-assets.developer.apple.com/published/689db8aa648e1884570bed622d3af3a1/chart-2-macOS%402x.png)

## Topics

### Creating a chart
- [init(content: () -> Content)](chart/init(content:).md)
  Creates a chart composed of any number of data series and individual marks.
- [init<Data, C>(Data, content: (Data.Element) -> C)](chart/init(_:content:).md)
  Creates a chart composed of a series of identifiable marks.
- [init<Data, ID, C>(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) -> C)](chart/init(_:id:content:).md)
  Creates a chart composed of a series of marks.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [View](../SwiftUI/View.md)

## See Also

- [Creating a chart using Swift Charts](creating-a-chart-using-swift-charts.md)
  Make a chart by combining chart building blocks in SwiftUI.
- [Visualizing your app’s data](visualizing_your_app_s_data.md)
  Build complex and interactive charts using Swift Charts.
- [protocol ChartContent](chartcontent.md)
  A type that represents the content that you draw on a chart.
- [struct ChartContentBuilder](chartcontentbuilder.md)
  A result builder that you use to compose the contents of a chart.
- [struct Plot](plot.md)
  A mechanism for grouping chart contents into a single entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chart)*