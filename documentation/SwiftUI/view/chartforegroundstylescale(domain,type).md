# chartForegroundStyleScale(domain:type:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures the foreground style scale for charts.

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
func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType? = nil) -> some View where Domain : ScaleDomain
```

## Parameters

- `domain`: The possible data values plotted as foreground style in the chart. You can define the domain with a `ClosedRange` for number or `Date` values (e.g., `0 ... 500`), and with an array for categorical values (e.g., `["A", "B", "C"]`)
- `type`: The scale type.

## See Also

### Styles
- [func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) -> some View](./chartbackground%28alignment,content%29.md)
  Adds a background to a view that contains a chart.
- [func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some View](./chartforegroundstylescale%28_%29.md)
  Configures the foreground style scale for charts.
- [func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](./chartforegroundstylescale%28domain,range,type%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartforegroundstylescale(domain:type:))*