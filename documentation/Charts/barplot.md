# BarPlot

**Framework**: Swift Charts  
**Kind**: struct

Chart content that represents a collection of data using bars.

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
struct BarPlot<Content>
```

#### Overview

Use `BarPlot` when you want to visualize data in the same way as with [`BarMark`](barmark.md), but you want to visualize an entire data collection with a single plot.

You can initialize and style the plot with simple values or key paths. Add modifiers with `KeyPath` before adding modifiers with simple values.

```swift
BarPlot(
    votes,
    x: .value("Party", \.party),
    y: .value("Vote count", \.voteCount)
)
.foregroundStyle(by: \.partyShapeStyle)
.cornerRadius(4)
```

## Topics

### Plotting bars from a collection
- [init<Data>(Data, x: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, y: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, width: MarkDimensions<BarPlot<Content>.DataElement>, height: MarkDimensions<BarPlot<Content>.DataElement>, stacking: MarkStackingMethod)](barplot/init(_:x:y:width:height:stacking:).md)
- [init<Data, Y>(Data, x: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, yStart: PlottableProjection<BarPlot<Content>.DataElement, Y>, yEnd: PlottableProjection<BarPlot<Content>.DataElement, Y>, width: MarkDimensions<BarPlot<Content>.DataElement>)](barplot/init(_:x:ystart:yend:width:).md)
- [init<Data>(Data, x: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, yStart: CGFloat?, yEnd: CGFloat?, width: MarkDimensions<BarPlot<Content>.DataElement>, stacking: MarkStackingMethod)](barplot/init(_:x:ystart:yend:width:stacking:)-2mtih.md)
- [init<Data>(Data, x: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, yStart: KeyPath<BarPlot<Content>.DataElement, CGFloat>, yEnd: KeyPath<BarPlot<Content>.DataElement, CGFloat>, width: MarkDimensions<BarPlot<Content>.DataElement>, stacking: MarkStackingMethod)](barplot/init(_:x:ystart:yend:width:stacking:)-680hw.md)
- [init<Data>(Data, xStart: KeyPath<BarPlot<Content>.DataElement, CGFloat>, xEnd: KeyPath<BarPlot<Content>.DataElement, CGFloat>, y: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, height: MarkDimensions<BarPlot<Content>.DataElement>, stacking: MarkStackingMethod)](barplot/init(_:xstart:xend:y:height:stacking:)-16tou.md)
- [init<Data>(Data, xStart: CGFloat?, xEnd: CGFloat?, y: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, height: MarkDimensions<BarPlot<Content>.DataElement>, stacking: MarkStackingMethod)](barplot/init(_:xstart:xend:y:height:stacking:)-2x0yx.md)
- [init<Data, X>(Data, xStart: PlottableProjection<BarPlot<Content>.DataElement, X>, xEnd: PlottableProjection<BarPlot<Content>.DataElement, X>, y: PlottableProjection<BarPlot<Content>.DataElement, some Plottable>, height: MarkDimensions<BarPlot<Content>.DataElement>)](barplot/init(_:xstart:xend:y:height:).md)
- [init<Data, X>(Data, xStart: PlottableProjection<BarPlot<Content>.DataElement, X>, xEnd: PlottableProjection<BarPlot<Content>.DataElement, X>, yStart: CGFloat?, yEnd: CGFloat?)](barplot/init(_:xstart:xend:ystart:yend:)-48su5.md)
- [init<Data, Y>(Data, xStart: KeyPath<BarPlot<Content>.DataElement, CGFloat>, xEnd: KeyPath<BarPlot<Content>.DataElement, CGFloat>, yStart: PlottableProjection<BarPlot<Content>.DataElement, Y>, yEnd: PlottableProjection<BarPlot<Content>.DataElement, Y>)](barplot/init(_:xstart:xend:ystart:yend:)-862wn.md)
- [init<Data, X>(Data, xStart: PlottableProjection<BarPlot<Content>.DataElement, X>, xEnd: PlottableProjection<BarPlot<Content>.DataElement, X>, yStart: KeyPath<BarPlot<Content>.DataElement, CGFloat>, yEnd: KeyPath<BarPlot<Content>.DataElement, CGFloat>)](barplot/init(_:xstart:xend:ystart:yend:)-mtdv.md)
- [init<Data, Y>(Data, xStart: CGFloat?, xEnd: CGFloat?, yStart: PlottableProjection<BarPlot<Content>.DataElement, Y>, yEnd: PlottableProjection<BarPlot<Content>.DataElement, Y>)](barplot/init(_:xstart:xend:ystart:yend:)-raqh.md)
### Supporting types
- [var body: Self.Body](chartcontent/body-swift.property.md)
  The content and behavior of the chart content.
- [struct VectorizedBarPlotContent](vectorizedbarplotcontent.md)
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
- [struct RulePlot](ruleplot.md)
  Chart content that represents a collection of data using a single horizontal or vertical rule.
- [struct SectorPlot](sectorplot.md)
  Chart content that represents a collection of data using a sector of a pie or donut chart, which shows how individual categories make up a meaningful total.
- [protocol VectorizedChartContent](vectorizedchartcontent.md)
  A generic type that represents content conveyed via a chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/barplot)*