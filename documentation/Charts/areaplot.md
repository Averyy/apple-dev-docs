# AreaPlot

**Framework**: Swift Charts  
**Kind**: struct

Chart content that represents a function or a collection of data using the area of one or more regions.

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
struct AreaPlot<Content>
```

#### Overview

Use `AreaPlot` when you want to visualize data in the same way as with [`AreaMark`](areamark.md), but you want to plot a function or visualize an entire data collection with a single plot.

##### Plotting Areas From a Collection

You can initialize and style the plot with simple values or key paths. Add modifiers with `KeyPath` before adding modifiers with simple values.

```swift
Chart {
    AreaPlot(
        portfolioElements,
        x: .value("Date", \.date),
        y: .value("Asset value", \.assetValue),
        series: .value("Asset", \.asset),
        stacking: .standard
    )
    .foregroundStyle(by: .value("Asset", \.asset))
}
```

##### Plotting Functions

In addition to providing data points, you can provide a function to an `AreaPlot` to plot a function. For example, you can plot the area between y = x and y = x^2 - 1 with:

```swift
Chart {
    AreaPlot(x: "x", yStart: "x", yEnd: "x^2 - 1") { x in (yStart: x, yEnd: x * x - 1) }
}
.chartXScale(domain: -2 ... 2)
.chartYScale(domain: -4 ... 4)
```

You can also provide a single function to an `AreaPlot`. In this case it will plot the area between zero and the given function.

```swift
Chart {
    AreaPlot(x: "x", y: "x^2 - 1") { x in x * x - 1 }
}
.chartXScale(domain: -2 ... 2)
.chartYScale(domain: -4 ... 4)
```

## Topics

### Plotting areas from a collection
- [init<Data>(Data, x: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, y: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, stacking: MarkStackingMethod)](areaplot/init(_:x:y:stacking:).md)
- [init<Data>(Data, x: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, y: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, series: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, stacking: MarkStackingMethod)](areaplot/init(_:x:y:series:stacking:).md)
- [init<Data, X>(Data, xStart: PlottableProjection<AreaPlot<Content>.DataElement, X>, xEnd: PlottableProjection<AreaPlot<Content>.DataElement, X>, y: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>)](areaplot/init(_:xstart:xend:y:).md)
- [init<Data, X>(Data, xStart: PlottableProjection<AreaPlot<Content>.DataElement, X>, xEnd: PlottableProjection<AreaPlot<Content>.DataElement, X>, y: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, series: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>)](areaplot/init(_:xstart:xend:y:series:).md)
- [init<Data, Y>(Data, x: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, yStart: PlottableProjection<AreaPlot<Content>.DataElement, Y>, yEnd: PlottableProjection<AreaPlot<Content>.DataElement, Y>)](areaplot/init(_:x:ystart:yend:).md)
- [init<Data, Y>(Data, x: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>, yStart: PlottableProjection<AreaPlot<Content>.DataElement, Y>, yEnd: PlottableProjection<AreaPlot<Content>.DataElement, Y>, series: PlottableProjection<AreaPlot<Content>.DataElement, some Plottable>)](areaplot/init(_:x:ystart:yend:series:).md)
### Supporting types
- [struct VectorizedAreaPlotContent](vectorizedareaplotcontent.md)
  An opaque vectorized chart content type.
- [struct FunctionAreaPlotContent](functionareaplotcontent.md)
### Initializers
- [init(x: LocalizedStringResource, y: LocalizedStringResource, domain: ClosedRange<Double>?, function: (Double) -> Double)](areaplot/init(x:y:domain:function:)-1jmpp.md)
  Creates a mark that fills the area between zero and the given function.
- [init(x: Text, y: Text, domain: ClosedRange<Double>?, function: (Double) -> Double)](areaplot/init(x:y:domain:function:)-2fab1.md)
  Creates a mark that fills the area between zero and the given function.
- [init<S1, S2>(x: S1, y: S2, domain: ClosedRange<Double>?, function: (Double) -> Double)](areaplot/init(x:y:domain:function:)-39eit.md)
  Creates a mark that fills the area between zero and the given function.
- [init(x: LocalizedStringKey, y: LocalizedStringKey, domain: ClosedRange<Double>?, function: (Double) -> Double)](areaplot/init(x:y:domain:function:)-etud.md)
  Creates a mark that fills the area between zero and the given function.
- [init<S1, S2, S3>(x: S1, yStart: S2, yEnd: S3, domain: ClosedRange<Double>?, function: (Double) -> (yStart: Double, yEnd: Double))](areaplot/init(x:ystart:yend:domain:function:)-23gxe.md)
  Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).
- [init(x: LocalizedStringKey, yStart: LocalizedStringKey, yEnd: LocalizedStringKey, domain: ClosedRange<Double>?, function: (Double) -> (yStart: Double, yEnd: Double))](areaplot/init(x:ystart:yend:domain:function:)-5akqm.md)
  Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).
- [init(x: LocalizedStringResource, yStart: LocalizedStringResource, yEnd: LocalizedStringResource, domain: ClosedRange<Double>?, function: (Double) -> (yStart: Double, yEnd: Double))](areaplot/init(x:ystart:yend:domain:function:)-9gui6.md)
  Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).
- [init(x: Text, yStart: Text, yEnd: Text, domain: ClosedRange<Double>?, function: (Double) -> (yStart: Double, yEnd: Double))](areaplot/init(x:ystart:yend:domain:function:)-etcn.md)
  Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).

## Relationships

### Conforms To
- [ChartContent](chartcontent.md)
- [Copyable](../Swift/Copyable.md)
- [VectorizedChartContent](vectorizedchartcontent.md)

## See Also

- [Creating a data visualization dashboard with Swift Charts](creating-a-data-visualization-dashboard-with-swift-charts.md)
  Visualize an entire data collection efficiently by instantiating a single vectorized plot in Swift Charts.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/areaplot)*