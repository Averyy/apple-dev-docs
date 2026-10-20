# VectorizedChartContent

**Framework**: Swift Charts  
**Kind**: protocol  
**Role**: Protocol

A generic type that represents content conveyed via a chart.

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
protocol VectorizedChartContent<DataElement> : ChartContent
```

#### Overview

Its primary associated type represents the data element, sometimes called *data point*, *observation* or *aggregate*.

Usually, `DataElement` has properties to determine visual attributes directly, or indirectly by encoding `Plottable` values through a chart scale.

## Topics

### Styling marks
- [func foregroundStyle(KeyPath<Self.DataElement, some ShapeStyle>) -> some VectorizedChartContent<Self.DataElement>
](./vectorizedchartcontent/foregroundstyle%28_%29.md)
  Represents data using a foreground style.
- [func opacity(KeyPath<Self.DataElement, CGFloat>) -> some VectorizedChartContent<Self.DataElement>
](./vectorizedchartcontent/opacity%28_%29.md)
- [func lineStyle(KeyPath<Self.DataElement, StrokeStyle>) -> some VectorizedChartContent<Self.DataElement>
](./vectorizedchartcontent/linestyle%28_%29.md)
  Represents data using line styles.
- [func position(by: PlottableProjection<Self.DataElement, some Plottable>, axis: Axis?, span: MarkDimension) -> some VectorizedChartContent<Self.DataElement>
](./vectorizedchartcontent/position%28by,axis,span%29.md)
### Setting symbol appearance
- [func symbol(by: PlottableProjection<Self.DataElement, some Plottable>) -> some VectorizedChartContent<Self.DataElement>
](./vectorizedchartcontent/symbol%28by%29.md)
  Represents data using different kinds of symbols.
- [func symbolSize(KeyPath<Self.DataElement, CGSize>) -> some VectorizedChartContent<Self.DataElement>
](./vectorizedchartcontent/symbolsize%28_%29-12tl1.md)
  Sets the plotting symbol size for the chart content.
- [func symbolSize(KeyPath<Self.DataElement, CGFloat>) -> some VectorizedChartContent<Self.DataElement>
](./vectorizedchartcontent/symbolsize%28_%29-3nwop.md)
  Sets the plotting symbol size for the chart content according to a perceived area.
### Encoding data into mark characteristics
- [func foregroundStyle(by: PlottableProjection<Self.DataElement, some Plottable>) -> some VectorizedChartContent<Self.DataElement>
](./vectorizedchartcontent/foregroundstyle%28by%29.md)
  Represents data using a foreground style.
- [func lineStyle(by: PlottableProjection<Self.DataElement, some Plottable>) -> some VectorizedChartContent<Self.DataElement>
](./vectorizedchartcontent/linestyle%28by%29.md)
  Represents data using line styles.
- [func symbol(by: PlottableProjection<Self.DataElement, some Plottable>) -> some VectorizedChartContent<Self.DataElement>
](./vectorizedchartcontent/symbol%28by%29.md)
  Represents data using different kinds of symbols.
- [func symbolSize(by: PlottableProjection<Self.DataElement, some Plottable>) -> some VectorizedChartContent<Self.DataElement>
](./vectorizedchartcontent/symbolsize%28by%29.md)
  Represents data using symbol sizes.
### Configuring accessibility
- [func accessibilityHidden(KeyPath<Self.DataElement, Bool>) -> some VectorizedChartContent<Self.DataElement>
](./vectorizedchartcontent/accessibilityhidden%28_%29.md)
  Specifies whether to hide this chart content from system accessibility features.
- [func accessibilityIdentifier(KeyPath<Self.DataElement, String>) -> some VectorizedChartContent<Self.DataElement>
](./vectorizedchartcontent/accessibilityidentifier%28_%29.md)
  Adds an identifier string to the chart content.
- [func accessibilityLabel(KeyPath<Self.DataElement, LocalizedStringKey>) -> some VectorizedChartContent<Self.DataElement>
](./vectorizedchartcontent/accessibilitylabel%28_%29-5r0pw.md)
  Adds a label to the chart content that describes its contents.
- [func accessibilityLabel(KeyPath<Self.DataElement, some StringProtocol>) -> some VectorizedChartContent<Self.DataElement>
](./vectorizedchartcontent/accessibilitylabel%28_%29-8zoay.md)
  Adds a label to the chart content that describes its contents.
- [func accessibilityLabel(KeyPath<Self.DataElement, Text>) -> some VectorizedChartContent<Self.DataElement>
](./vectorizedchartcontent/accessibilitylabel%28_%29-46jbt.md)
  Adds a label to the chart content that describes its contents.
- [func accessibilityValue(KeyPath<Self.DataElement, some StringProtocol>) -> some VectorizedChartContent<Self.DataElement>
](./vectorizedchartcontent/accessibilityvalue%28_%29-2rv8b.md)
  Adds a description of the value that the chart content contains.
- [func accessibilityValue(KeyPath<Self.DataElement, Text>) -> some VectorizedChartContent<Self.DataElement>
](./vectorizedchartcontent/accessibilityvalue%28_%29-pylk.md)
  Adds a description of the value that the chart content contains.
- [func accessibilityValue(KeyPath<Self.DataElement, LocalizedStringKey>) -> some VectorizedChartContent<Self.DataElement>
](./vectorizedchartcontent/accessibilityvalue%28_%29-3dei8.md)
  Adds a description of the value that the chart content contains.
### Supporting types
- [struct PlottableProjection](./plottableprojection.md)
### Associated Types
- [associatedtype DataElement](./vectorizedchartcontent/dataelement.md)

## Relationships

### Inherits From
- [ChartContent](./chartcontent.md)
### Conforming Types
- [AreaPlot](./areaplot.md)
- [BarPlot](./barplot.md)
- [LinePlot](./lineplot.md)
- [PointPlot](./pointplot.md)
- [RectanglePlot](./rectangleplot.md)
- [RulePlot](./ruleplot.md)
- [SectorPlot](./sectorplot.md)
- [VectorizedAreaPlotContent](./vectorizedareaplotcontent.md)
- [VectorizedBarPlotContent](./vectorizedbarplotcontent.md)
- [VectorizedLinePlotContent](./vectorizedlineplotcontent.md)
- [VectorizedPointPlotContent](./vectorizedpointplotcontent.md)
- [VectorizedRectanglePlotContent](./vectorizedrectangleplotcontent.md)
- [VectorizedRulePlotContent](./vectorizedruleplotcontent.md)
- [VectorizedSectorPlotContent](./vectorizedsectorplotcontent.md)

## See Also

### Vectorized plots
- [Creating a data visualization dashboard with Swift Charts](./creating-a-data-visualization-dashboard-with-swift-charts.md)
  Visualize an entire data collection efficiently by instantiating a single vectorized plot in Swift Charts.
- [struct AreaPlot](./areaplot.md)
  Chart content that represents a function or a collection of data using the area of one or more regions.
- [struct LinePlot](./lineplot.md)
  Chart content that represents a function or a collection of data using a sequence of connected line segments.
- [struct PointPlot](./pointplot.md)
  Chart content that represents a collection of data using points.
- [struct RectanglePlot](./rectangleplot.md)
  Chart content that represents a collection of data using rectangles.
- [struct RulePlot](./ruleplot.md)
  Chart content that represents a collection of data using a single horizontal or vertical rule.
- [struct BarPlot](./barplot.md)
  Chart content that represents a collection of data using bars.
- [struct SectorPlot](./sectorplot.md)
  Chart content that represents a collection of data using a sector of a pie or donut chart, which shows how individual categories make up a meaningful total.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/vectorizedchartcontent)*