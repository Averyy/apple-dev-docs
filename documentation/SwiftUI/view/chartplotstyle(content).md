# chartPlotStyle(content:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Configures the plot area of charts.

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
func chartPlotStyle<Content>(@ViewBuilder content: @escaping (ChartPlotContent) -> Content) -> some View where Content : View
```

#### Discussion

Use this modifier to configure the size or aspect ratio of the plot area of charts.

For example:

```swift
Chart(data: data) {
    BarMark(x: .value("Category", $0.category))
}
.chartPlotStyle { content in
    content.frame(width: 100, height: 100)
}
```

## Parameters

- `content`: A closure that returns the content of the plot area.

## See Also

### Styles
- [func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) -> some View](./chartbackground%28alignment,content%29.md)
  Adds a background to a view that contains a chart.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartplotstyle(content:))*