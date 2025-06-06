# PointPlot

**Framework**: Swift Charts  
**Kind**: struct

Chart content that represents a collection of data using points.

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
struct PointPlot<Content>
```

#### Overview

Use `PointPlot` when you want to visualize data in the same way as with [`PointMark`](pointmark.md), but you want to visualize an entire data collection with a single plot.

You can initialize and style the plot with simple values or key paths. Add modifiers with `KeyPath` before adding modifiers with simple values.

```swift
Chart {
    PointPlot(
        flightDelays,
        x: .value("Flight Distance", \.distance),
        y: .value("Flight Delay", \.delay)
    )
    .foregroundStyle(by: .value("Airline", \.airline))
    .opacity(\.opacity)
    .symbolSize(by: .value("Capacity", \.passengerCount))
    .symbol(.circle)
}
```

## Topics

### Plotting points from a collection
- [init<Data>(Data, x: KeyPath<Data.Element, CGFloat>, y: PlottableProjection<PointPlot<Content>.DataElement, some Plottable>)](pointplot/init(_:x:y:)-1a9af.md)
- [init<Data>(Data, x: CGFloat?, y: PlottableProjection<PointPlot<Content>.DataElement, some Plottable>)](pointplot/init(_:x:y:)-1p6px.md)
- [init<Data>(Data, x: PlottableProjection<PointPlot<Content>.DataElement, some Plottable>, y: CGFloat?)](pointplot/init(_:x:y:)-72pm2.md)
- [init<Data>(Data, x: PlottableProjection<PointPlot<Content>.DataElement, some Plottable>, y: PlottableProjection<PointPlot<Content>.DataElement, some Plottable>)](pointplot/init(_:x:y:)-7frpp.md)
- [init<Data>(Data, x: PlottableProjection<PointPlot<Content>.DataElement, some Plottable>, y: KeyPath<PointPlot<Content>.DataElement, CGFloat>)](pointplot/init(_:x:y:)-9p3yg.md)
### Supporting types
- [struct VectorizedPointPlotContent](vectorizedpointplotcontent.md)
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
- [struct RectanglePlot](rectangleplot.md)
  Chart content that represents a collection of data using rectangles.
- [struct RulePlot](ruleplot.md)
  Chart content that represents a collection of data using a single horizontal or vertical rule.
- [struct BarPlot](barplot.md)
  Chart content that represents a collection of data using bars.
- [struct SectorPlot](sectorplot.md)
  Chart content that represents a collection of data using a sector of a pie or donut chart, which shows how individual categories make up a meaningful total.
- [protocol VectorizedChartContent](vectorizedchartcontent.md)
  A generic type that represents content conveyed via a chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/pointplot)*