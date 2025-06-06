# RectanglePlot

**Framework**: Swift Charts  
**Kind**: struct

Chart content that represents a collection of data using rectangles.

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
struct RectanglePlot<Content>
```

#### Overview

Use `RectanglePlot` when you want to visualize data in the same way as with [`RectangleMark`](rectanglemark.md), but you want to visualize an entire data collection with a single plot.

You can initialize and style the plot with simple values or key paths. Add modifiers with `KeyPath` before adding modifiers with simple values.

```swift
Chart {
    RectanglePlot(
        tasks,
        x: .value("Time", \.startTime, \.endTime),
        y: .value("Project", \.project)
    )
    .foregroundStyle(by: .value("Status", \.status))
    .cornerRadius(4)
}
```

## Topics

### Plotting rectangles from a collection
- [init<Data>(Data, x: PlottableProjection<RectanglePlot<Content>.DataElement, some Plottable>, y: PlottableProjection<RectanglePlot<Content>.DataElement, some Plottable>, width: MarkDimensions<RectanglePlot<Content>.DataElement>, height: MarkDimensions<RectanglePlot<Content>.DataElement>)](rectangleplot/init(_:x:y:width:height:).md)
- [init<Data, Y>(Data, x: PlottableProjection<RectanglePlot<Content>.DataElement, some Plottable>, yStart: PlottableProjection<RectanglePlot<Content>.DataElement, Y>, yEnd: PlottableProjection<RectanglePlot<Content>.DataElement, Y>, width: MarkDimensions<RectanglePlot<Content>.DataElement>)](rectangleplot/init(_:x:ystart:yend:width:)-93op1.md)
- [init<Data>(Data, x: PlottableProjection<RectanglePlot<Content>.DataElement, some Plottable>, yStart: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, yEnd: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, width: MarkDimensions<RectanglePlot<Content>.DataElement>)](rectangleplot/init(_:x:ystart:yend:width:)-nnvk.md)
- [init<Data>(Data, x: PlottableProjection<RectanglePlot<Content>.DataElement, some Plottable>, yStart: CGFloat?, yEnd: CGFloat?, width: MarkDimensions<RectanglePlot<Content>.DataElement>)](rectangleplot/init(_:x:ystart:yend:width:)-12u1b.md)
- [init<Data>(Data, xStart: CGFloat?, xEnd: CGFloat?, y: PlottableProjection<RectanglePlot<Content>.DataElement, some Plottable>, height: MarkDimensions<RectanglePlot<Content>.DataElement>)](rectangleplot/init(_:xstart:xend:y:height:)-51nra.md)
- [init<Data>(Data, xStart: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, xEnd: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, y: PlottableProjection<RectanglePlot<Content>.DataElement, some Plottable>, height: MarkDimensions<RectanglePlot<Content>.DataElement>)](rectangleplot/init(_:xstart:xend:y:height:)-8s17v.md)
- [init<Data, X>(Data, xStart: PlottableProjection<RectanglePlot<Content>.DataElement, X>, xEnd: PlottableProjection<RectanglePlot<Content>.DataElement, X>, y: PlottableProjection<RectanglePlot<Content>.DataElement, some Plottable>, height: MarkDimensions<RectanglePlot<Content>.DataElement>)](rectangleplot/init(_:xstart:xend:y:height:)-15ish.md)
- [init<Data, X>(Data, xStart: PlottableProjection<RectanglePlot<Content>.DataElement, X>, xEnd: PlottableProjection<RectanglePlot<Content>.DataElement, X>, yStart: CGFloat?, yEnd: CGFloat?)](rectangleplot/init(_:xstart:xend:ystart:yend:)-46wi0.md)
- [init<Data, X, Y>(Data, xStart: PlottableProjection<RectanglePlot<Content>.DataElement, X>, xEnd: PlottableProjection<RectanglePlot<Content>.DataElement, X>, yStart: PlottableProjection<RectanglePlot<Content>.DataElement, Y>, yEnd: PlottableProjection<RectanglePlot<Content>.DataElement, Y>)](rectangleplot/init(_:xstart:xend:ystart:yend:)-4g377.md)
- [init<Data, Y>(Data, xStart: CGFloat?, xEnd: CGFloat?, yStart: PlottableProjection<RectanglePlot<Content>.DataElement, Y>, yEnd: PlottableProjection<RectanglePlot<Content>.DataElement, Y>)](rectangleplot/init(_:xstart:xend:ystart:yend:)-6d8yb.md)
- [init<Data, X>(Data, xStart: PlottableProjection<RectanglePlot<Content>.DataElement, X>, xEnd: PlottableProjection<RectanglePlot<Content>.DataElement, X>, yStart: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, yEnd: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>)](rectangleplot/init(_:xstart:xend:ystart:yend:)-6uuk4.md)
- [init<Data, Y>(Data, xStart: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, xEnd: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, yStart: PlottableProjection<RectanglePlot<Content>.DataElement, Y>, yEnd: PlottableProjection<RectanglePlot<Content>.DataElement, Y>)](rectangleplot/init(_:xstart:xend:ystart:yend:)-741lz.md)
- [init<Data>(Data, xStart: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, xEnd: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, yStart: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>, yEnd: KeyPath<RectanglePlot<Content>.DataElement, CGFloat>)](rectangleplot/init(_:xstart:xend:ystart:yend:)-ir9o.md)
### Supporting types
- [struct VectorizedRectanglePlotContent](vectorizedrectangleplotcontent.md)
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
- [struct RulePlot](ruleplot.md)
  Chart content that represents a collection of data using a single horizontal or vertical rule.
- [struct BarPlot](barplot.md)
  Chart content that represents a collection of data using bars.
- [struct SectorPlot](sectorplot.md)
  Chart content that represents a collection of data using a sector of a pie or donut chart, which shows how individual categories make up a meaningful total.
- [protocol VectorizedChartContent](vectorizedchartcontent.md)
  A generic type that represents content conveyed via a chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/rectangleplot)*