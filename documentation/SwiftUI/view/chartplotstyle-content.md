# chartPlotStyle(content:)

**Framework**: SwiftUI  
**Kind**: method

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

- [func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) -> some View](view/chartbackground(alignment:content:).md)
  Adds a background to a view that contains a chart.
- [func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some View](view/chartforegroundstylescale(_:).md)
  Configures the foreground style scale for charts.
- [func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](view/chartforegroundstylescale(domain:range:type:).md)
  Configures the foreground style scale for charts.
- [func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) -> some View](view/chartforegroundstylescale(domain:type:).md)
  Configures the foreground style scale for charts.
- [func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping: (Domain.Element) -> S) -> some View](view/chartforegroundstylescale(domain:mapping:).md)
  Configures the foreground style scale for charts.
- [func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) -> some View](view/chartforegroundstylescale(mapping:).md)
  Configures the foreground style scale for charts.
- [func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some View](view/chartforegroundstylescale(range:type:).md)
  Configures the foreground style scale for charts.
- [func chartForegroundStyleScale(type: ScaleType?) -> some View](view/chartforegroundstylescale(type:).md)
  Configures the foreground style scale for charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartplotstyle(content:))*