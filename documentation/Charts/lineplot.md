# LinePlot

**Framework**: Swift Charts  
**Kind**: struct

Chart content that represents a function or a collection of data using a sequence of connected line segments.

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
struct LinePlot<Content>
```

#### Overview

Use `LinePlot` when you want to visualize data in the same way as with [`LineMark`](linemark.md), but you want to plot a function or visualize an entire data collection with a single plot.

##### Plotting Lines From a Collection

You can initialize and style the plot with simple values or key paths. Add modifiers with `KeyPath` before adding modifiers with simple values.

```swift
Chart {
    LinePlot(
        stocks,
        x: .value("Date", \.date),
        y: .value("Price", \.price),
        series: .value("Asset", \.symbol)
    )
    .foregroundStyle(by: .value("Asset", \.symbol))
}
```

##### Plotting Functions

In addition to providing data points, you can provide a function to a `LinePlot` to plot a function. For example, you can plot the function y = x^2 with:

```swift
Chart {
    LinePlot(x: "x", y: "y") { x in x * x }
}
.chartXScale(-10 ... 10)
.chartYScale(-10 ... 10)
```

You can add multiple function plots in a chart and use different foreground styles to distinguish among them.

```swift
Chart {
    LinePlot(x: "x", y: "y = sin(x)") { sin($0) }
        .foregroundStyle(by: .value("expression", "y=sin(x)"))
        .lineStyle(StrokeStyle(lineWidth: 5, lineCap: .round))
        .opacity(0.8)

    LinePlot(x: "x", y: "y = cos(x)") { cos($0) }
        .foregroundStyle(by: .value("expression", "y=cos(x)")
        .lineStyle(StrokeStyle(lineWidth: 5, lineCap: .round))
        .opacity(0.8)
}
.chartXScale(-10 ... 10)
.chartYScale(-10 ... 10)
```

You can plot a parametric function with the constructor with `x`, `y`, and `t`:

```swift
Chart {
    LinePlot(x: "x", y: "y", t: "t", domain: 0 ... .pi * 2) {
        t in (x: 10 * cos(5 * t) * cos(t), y: 10 * cos(5 * t) * sin(t))
    }
}
.chartXScale(domain: -10 ... 10)
.chartYScale(domain: -10 ... 10)
```

## Topics

### Plotting lines from a collection
- [init<Data>(Data, x: PlottableProjection<LinePlot<Content>.DataElement, some Plottable>, y: PlottableProjection<LinePlot<Content>.DataElement, some Plottable>)](lineplot/init(_:x:y:).md)
- [init<Data>(Data, x: PlottableProjection<LinePlot<Content>.DataElement, some Plottable>, y: PlottableProjection<LinePlot<Content>.DataElement, some Plottable>, series: PlottableProjection<LinePlot<Content>.DataElement, some Plottable>)](lineplot/init(_:x:y:series:).md)
### Supporting types
- [struct VectorizedLinePlotContent](vectorizedlineplotcontent.md)
  An opaque vectorized chart content type.
- [struct FunctionLinePlotContent](functionlineplotcontent.md)
### Initializers
- [init(x: LocalizedStringKey, y: LocalizedStringKey, domain: ClosedRange<Double>?, function: (Double) -> Double)](lineplot/init(x:y:domain:function:)-1135f.md)
  Creates a mark that graphs a function y = f(x).
- [init(x: LocalizedStringResource, y: LocalizedStringResource, domain: ClosedRange<Double>?, function: (Double) -> Double)](lineplot/init(x:y:domain:function:)-17i43.md)
  Creates a mark that graphs a function y = f(x).
- [init<S1, S2>(x: S1, y: S2, domain: ClosedRange<Double>?, function: (Double) -> Double)](lineplot/init(x:y:domain:function:)-6gv5v.md)
  Creates a mark that graphs a function y = f(x).
- [init(x: Text, y: Text, domain: ClosedRange<Double>?, function: (Double) -> Double)](lineplot/init(x:y:domain:function:)-6m9gg.md)
  Creates a mark that graphs a function y = f(x).
- [init<S1, S2, S3>(x: S1, y: S2, t: S3, domain: ClosedRange<Double>, function: (Double) -> (x: Double, y: Double))](lineplot/init(x:y:t:domain:function:)-3mqls.md)
  Creates a mark that graphs a parametric function (x, y) = f(t).
- [init(x: Text, y: Text, t: Text, domain: ClosedRange<Double>, function: (Double) -> (x: Double, y: Double))](lineplot/init(x:y:t:domain:function:)-5c4bo.md)
  Creates a mark that graphs a parametric function (x, y) = f(t).
- [init(x: LocalizedStringResource, y: LocalizedStringResource, t: LocalizedStringResource, domain: ClosedRange<Double>, function: (Double) -> (x: Double, y: Double))](lineplot/init(x:y:t:domain:function:)-610ta.md)
  Creates a mark that graphs a parametric function (x, y) = f(t).
- [init(x: LocalizedStringKey, y: LocalizedStringKey, t: LocalizedStringKey, domain: ClosedRange<Double>, function: (Double) -> (x: Double, y: Double))](lineplot/init(x:y:t:domain:function:)-7bvyi.md)
  Creates a mark that graphs a parametric function (x, y) = f(t).

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

*[View on Apple Developer](https://developer.apple.com/documentation/charts/lineplot)*