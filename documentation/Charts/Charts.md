# Swift Charts

**Framework**: Swift Charts  
**Kind**: module

Construct and customize charts on every Apple platform.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

#### Overview

Swift Charts is a powerful and concise SwiftUI framework you can use to transform your data into informative visualizations. With Swift Charts, you can build effective and customizable charts with minimal code. This framework provides marks, scales, axes, and legends as building blocks that you can combine to develop a broad range of data-driven charts.

![A graphic showing three charts built with Swift Charts: a line chart, a bar chart, and a scatter plot.](https://docs-assets.developer.apple.com/published/39f0be0768748aef1d94764a618561a0/FrameworkOverview%402x.png)

There are many ways you can use Swift Charts to communicate patterns or trends in your data. You can create a variety of charts including line charts, bar charts, and scatter plots as shown above. When you create a chart using this framework, it automatically generates scales and axes that fit your data.

Swift Charts supports localization and accessibility features. You can also override default behavior to customize your charts by using chart modifiers. For example, you can create a dynamic experience by adding animations to your charts.

## Topics

### Essentials
- [Swift Charts updates](../Updates/SwiftCharts.md)
  Learn about important changes to Swift Charts.
### Charts
- [Creating a chart using Swift Charts](creating-a-chart-using-swift-charts.md)
  Make a chart by combining chart building blocks in SwiftUI.
- [Visualizing your app’s data](visualizing_your_app_s_data.md)
  Build complex and interactive charts using Swift Charts.
- [struct Chart](chart.md)
  A SwiftUI view that displays a chart.
- [protocol ChartContent](chartcontent.md)
  A type that represents the content that you draw on a chart.
- [struct ChartContentBuilder](chartcontentbuilder.md)
  A result builder that you use to compose the contents of a chart.
- [struct Plot](plot.md)
  A mechanism for grouping chart contents into a single entity.
### Marks
- [struct AreaMark](areamark.md)
  Chart content that represents data using the area of one or more regions.
- [struct LineMark](linemark.md)
  Chart content that represents data using a sequence of connected line segments.
- [struct PointMark](pointmark.md)
  Chart content that represents data using points.
- [struct RectangleMark](rectanglemark.md)
  Chart content that represents data using rectangles.
- [struct RuleMark](rulemark.md)
  Chart content that represents data using a single horizontal or vertical rule.
- [struct BarMark](barmark.md)
  Chart content that represents data using bars.
- [struct SectorMark](sectormark.md)
  A sector of a pie or donut chart, which shows how individual categories make up a meaningful total.
### Vectorized plots
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
- [struct SectorPlot](sectorplot.md)
  Chart content that represents a collection of data using a sector of a pie or donut chart, which shows how individual categories make up a meaningful total.
- [protocol VectorizedChartContent](vectorizedchartcontent.md)
  A generic type that represents content conveyed via a chart.
### Mark configuration
- [struct MarkStackingMethod](markstackingmethod.md)
  The ways in which you can stack marks in a chart.
- [struct MarkDimension](markdimension.md)
  An individual dimension representing a mark’s width or height.
- [struct InterpolationMethod](interpolationmethod.md)
  The ways in which line or area marks interpolate their data.
- [struct BasicChartSymbolShape](basicchartsymbolshape.md)
  A basic chart symbol shape.
- [protocol ChartSymbolShape](chartsymbolshape.md)
  A type that can act as a shape for the marks that you add to a chart.
- [struct AnyChartSymbolShape](anychartsymbolshape.md)
  A type-erased plotting shape.
### Labeled data
- [struct PlottableValue](plottablevalue.md)
  Labeled data that you plot in a chart using marks.
- [protocol Plottable](plottable.md)
  A type that can serve as data to plot in a chart.
### Scales
- [protocol ScaleRange](scalerange.md)
  A type that you can use to configure the range of a chart.
- [protocol PositionScaleRange](positionscalerange.md)
  A type that configures the x-axis and y-axis values.
- [struct PlotDimensionScaleRange](plotdimensionscalerange.md)
  A range that represents the plot area’s width or height.
- [protocol ScaleDomain](scaledomain.md)
  A type that you can use to configure the domain of a chart.
- [struct AutomaticScaleDomain](automaticscaledomain.md)
  A domain that the chart infers from its data.
- [struct ScaleType](scaletype.md)
  The ways you can scale the domain or range of a plot.
### Axes
- [Customizing axes in Swift Charts](customizing-axes-in-swift-charts.md)
  Improve the clarity of your chart by configuring the appearance of its axes.
- [struct ChartAxisContent](chartaxiscontent.md)
  A view that represents a chart’s axis.
- [protocol AxisContent](axiscontent.md)
  A type that represents the elements you use to build a chart’s axes.
- [struct AxisMarks](axismarks.md)
  A group of visual marks that a chart draws to indicate the composition of a chart’s axes.
- [struct AnyAxisContent](anyaxiscontent.md)
  A type-erased element of a chart’s axis.
- [struct AxisContentBuilder](axiscontentbuilder.md)
  A result builder that constructs axis content.
### Axis marks
- [protocol AxisMark](axismark.md)
  A type that serves as the basic building block for the elements of an axis.
- [struct AxisTick](axistick.md)
  A mark that a chart draws on an axis to indicate a reference point along that axis.
- [struct AxisGridLine](axisgridline.md)
  A line that a chart draws across its plot area to indicate a reference point along a particular axis.
- [struct AxisValueLabel](axisvaluelabel.md)
  A label that describes the value for an axis mark.
- [struct AxisValue](axisvalue.md)
  A value for an axis mark.
- [struct AnyAxisMark](anyaxismark.md)
  A type-erased axis mark.
- [struct AxisMarkBuilder](axismarkbuilder.md)
  A result builder that constructs axis marks and overrides default marks.
### Annotations
- [struct AnnotationContext](annotationcontext.md)
  Information about an item that you add an annotation to.
- [struct AnnotationPosition](annotationposition.md)
  The position of an annotation.
- [struct AnnotationOverflowResolution](annotationoverflowresolution.md)
### Data bins
- [struct NumberBins](numberbins.md)
  A collection of bins for a chart that plots data against numbers.
- [struct DateBins](datebins.md)
  A collection of bins for a chart that plots data against dates.
- [struct ChartBinRange](chartbinrange.md)
  The range of data that a single bin of a chart represents.
### Chart management
- [struct ChartPlotContent](chartplotcontent.md)
  A view that represents a chart’s plot area.
- [struct ChartProxy](chartproxy.md)
  A proxy that you use to access the scales and plot area of a chart.
### Scrolling
- [protocol ChartScrollTargetBehavior](chartscrolltargetbehavior.md)
  A type that configures the scroll behavior of charts.
- [struct ChartScrollTargetBehaviorContext](chartscrolltargetbehaviorcontext.md)
  Contextual information that you can use to determine how to best adjust how charts scroll.
### Protocols
- [protocol AGChartsDecider](agchartsdecider.md)
- [protocol Chart3DContent](chart3dcontent.md)
- [protocol Chart3DSurfaceStyle](chart3dsurfacestyle.md)
- [protocol Chart3DSymbolShape](chart3dsymbolshape.md)
  A type that can act as a shape for the marks that you add to a chart.
### Structures
- [struct AnyChart3DSymbolShape](anychart3dsymbolshape.md)
  A type-erased plotting shape.
- [struct BasicChart3DSurfaceStyle](basicchart3dsurfacestyle.md)
- [struct BasicChart3DSymbolShape](basicchart3dsymbolshape.md)
  A basic chart symbol shape.
- [struct Chart3D](chart3d.md)
- [struct Chart3DCameraPose](chart3dcamerapose.md)
- [struct Chart3DCameraProjection](chart3dcameraprojection.md)
- [struct Chart3DContentBuilder](chart3dcontentbuilder.md)
- [struct Chart3DPose](chart3dpose.md)
- [struct Chart3DRenderingStyle](chart3drenderingstyle.md)
- [struct SurfacePlot](surfaceplot.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Charts)*