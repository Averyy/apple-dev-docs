# chartBackground(alignment:content:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds a background to a view that contains a chart.

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
nonisolated
func chartBackground<V>(alignment: Alignment = .center, @ViewBuilder content: @escaping (ChartProxy) -> V) -> some View where V : View
```

#### Discussion

You can use this modifier to define a background view as a function of the chart in the view. You can access the chart with the `ChartProxy` object passed into the closure.

> **Note**: If `self` contains more than one chart, the chart proxy will refer to the first chart.

## Parameters

- `alignment`: The alignment of the content.
- `content`: The content of the background.

## See Also

### Styles
- [func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some View](./chartforegroundstylescale%28_%29.md)
  Configures the foreground style scale for charts.
- [func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](./chartforegroundstylescale%28domain,range,type%29.md)
  Configures the foreground style scale for charts.
- [func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) -> some View](./chartforegroundstylescale%28domain,type%29.md)
  Configures the foreground style scale for charts.
- [func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping: (Domain.Element) -> S) -> some View](./chartforegroundstylescale%28domain,mapping%29.md)
  Configures the foreground style scale for charts.
- [func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) -> some View](./chartforegroundstylescale%28mapping%29.md)
  Configures the foreground style scale for charts.
- [func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some View](./chartforegroundstylescale%28range,type%29.md)
  Configures the foreground style scale for charts.
- [func chartForegroundStyleScale(type: ScaleType?) -> some View](./chartforegroundstylescale%28type%29.md)
  Configures the foreground style scale for charts.
- [func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some View](./chartplotstyle%28content%29.md)
  Configures the plot area of charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartbackground(alignment:content:))*