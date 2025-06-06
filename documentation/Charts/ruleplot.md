# RulePlot

**Framework**: Swift Charts  
**Kind**: struct

Chart content that represents a collection of data using a single horizontal or vertical rule.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct RulePlot<Content>
```

#### Overview

Use `RulePlot` when you want to visualize data in the same way as with [`RuleMark`](rulemark.md), but you want to visualize an entire data collection with a single plot.

You can initialize and style the plot with simple values or key paths. Add modifiers with `KeyPath` before adding modifiers with simple values.

```swift
Chart {
    RulePlot(
        tasks,
        xStart: .value("Start time", \.startTime),
        xEnd: .value("End time", \.endTime),
        y: .value("Project", \.project)
    )
    .foregroundStyle(by: .value("Status", \.status))
    .opacity(/.opacity)
    .lineStyle(StrokeStyle(lineWidth: 8, lineCap: .round))
}
```

## Topics

### Plotting rules from a collection
- [init<Data>(Data, x: PlottableProjection<RulePlot<Content>.DataElement, some Plottable>, yStart: CGFloat?, yEnd: CGFloat?)](ruleplot/init(_:x:ystart:yend:)-13wts.md)
- [init<Data, Y>(Data, x: KeyPath<RulePlot<Content>.DataElement, CGFloat>, yStart: PlottableProjection<RulePlot<Content>.DataElement, Y>, yEnd: PlottableProjection<RulePlot<Content>.DataElement, Y>)](ruleplot/init(_:x:ystart:yend:)-3fig9.md)
- [init<Data>(Data, x: PlottableProjection<RulePlot<Content>.DataElement, some Plottable>, yStart: KeyPath<RulePlot<Content>.DataElement, CGFloat>, yEnd: KeyPath<RulePlot<Content>.DataElement, CGFloat>)](ruleplot/init(_:x:ystart:yend:)-6ts7e.md)
- [init<Data, Y>(Data, x: CGFloat?, yStart: PlottableProjection<RulePlot<Content>.DataElement, Y>, yEnd: PlottableProjection<RulePlot<Content>.DataElement, Y>)](ruleplot/init(_:x:ystart:yend:)-8b2lx.md)
- [init<Data, Y>(Data, x: PlottableProjection<RulePlot<Content>.DataElement, some Plottable>, yStart: PlottableProjection<RulePlot<Content>.DataElement, Y>, yEnd: PlottableProjection<RulePlot<Content>.DataElement, Y>)](ruleplot/init(_:x:ystart:yend:)-zxo0.md)
- [init<Data>(Data, xStart: KeyPath<RulePlot<Content>.DataElement, CGFloat>, xEnd: KeyPath<RulePlot<Content>.DataElement, CGFloat>, y: PlottableProjection<RulePlot<Content>.DataElement, some Plottable>)](ruleplot/init(_:xstart:xend:y:)-3dsvn.md)
- [init<Data>(Data, xStart: CGFloat?, xEnd: CGFloat?, y: PlottableProjection<RulePlot<Content>.DataElement, some Plottable>)](ruleplot/init(_:xstart:xend:y:)-4yxo8.md)
- [init<Data, X>(Data, xStart: PlottableProjection<RulePlot<Content>.DataElement, X>, xEnd: PlottableProjection<RulePlot<Content>.DataElement, X>, y: KeyPath<RulePlot<Content>.DataElement, CGFloat>)](ruleplot/init(_:xstart:xend:y:)-54gxx.md)
- [init<Data, X>(Data, xStart: PlottableProjection<RulePlot<Content>.DataElement, X>, xEnd: PlottableProjection<RulePlot<Content>.DataElement, X>, y: PlottableProjection<RulePlot<Content>.DataElement, some Plottable>)](ruleplot/init(_:xstart:xend:y:)-8ehr7.md)
- [init<Data, X>(Data, xStart: PlottableProjection<RulePlot<Content>.DataElement, X>, xEnd: PlottableProjection<RulePlot<Content>.DataElement, X>, y: CGFloat?)](ruleplot/init(_:xstart:xend:y:)-hx5a.md)
### Supporting types
- [struct VectorizedRulePlotContent](vectorizedruleplotcontent.md)
  An opaque vectorized chart content type.

## Relationships

### Conforms To
- [ChartContent](chartcontent.md)
- [Copyable](../Swift/Copyable.md)
- [VectorizedChartContent](vectorizedchartcontent.md)

## See Also

- [Creating a data visualization dashboard with Swift Charts](creating-a-data-visualization-dashboard-with-swift-charts.md)
  Visualize an entire data collection efficiently by instantiating a single vectorized plot in Swift Charts.
- [struct AreaPlot](areaplot.md)
  Chart content that represents a function or a collection of data using the area of one or more regions.
- [struct LinePlot](lineplot.md)
  Chart content that represents a function or a collection of data using a sequence of connected line segments.
- [struct PointPlot](pointplot.md)
  Chart content that represents a collection of data using points.
- [struct RectanglePlot](rectangleplot.md)
  Chart content that represents a collection of data using rectangles.
- [struct BarPlot](barplot.md)
  Chart content that represents a collection of data using bars.
- [struct SectorPlot](sectorplot.md)
  Chart content that represents a collection of data using a sector of a pie or donut chart, which shows how individual categories make up a meaningful total.
- [protocol VectorizedChartContent](vectorizedchartcontent.md)
  A generic type that represents content conveyed via a chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/ruleplot)*