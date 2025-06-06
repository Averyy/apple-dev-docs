# SectorPlot

**Framework**: Swift Charts  
**Kind**: struct

Chart content that represents a collection of data using a sector of a pie or donut chart, which shows how individual categories make up a meaningful total.

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
struct SectorPlot<Content>
```

#### Overview

Use `SectorPlot` when you want to visualize data in the same way as with [`SectorMark`](sectormark.md), but you want to visualize an entire data collection with a single plot.

You can initialize and style the plot with simple values or key paths. Add modifiers with `KeyPath` before adding modifiers with simple values.

```swift
SectorPlot(
    votes,
    angle: .value("Vote count", \.voteCount),
    angularInset: 1
)
.foregroundStyle(by: .value("Party", \.party))
.cornerRadius(4)
```

## Topics

### Plotting sectors from a collection
- [init<Data>(Data, angle: PlottableProjection<SectorPlot<Content>.DataElement, some Plottable>, innerRadius: MarkDimensions<SectorPlot<Content>.DataElement>, outerRadius: MarkDimensions<SectorPlot<Content>.DataElement>, angularInset: CGFloat?)](sectorplot/init(_:angle:innerradius:outerradius:angularinset:)-1ed01.md)
- [init<Data>(Data, angle: PlottableProjection<SectorPlot<Content>.DataElement, some Plottable>, innerRadius: MarkDimensions<SectorPlot<Content>.DataElement>, outerRadius: MarkDimensions<SectorPlot<Content>.DataElement>, angularInset: KeyPath<SectorPlot<Content>.DataElement, CGFloat>)](sectorplot/init(_:angle:innerradius:outerradius:angularinset:)-9pmo7.md)
### Supporting types
- [struct VectorizedSectorPlotContent](vectorizedsectorplotcontent.md)
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
- [struct BarPlot](barplot.md)
  Chart content that represents a collection of data using bars.
- [protocol VectorizedChartContent](vectorizedchartcontent.md)
  A generic type that represents content conveyed via a chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/sectorplot)*