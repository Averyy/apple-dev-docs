# chartForegroundStyleScale(range:type:)

**Framework**: SwiftUI  
**Kind**: method

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
func chartForegroundStyleScale<Range>(range: Range, type: ScaleType? = nil) -> some View where Range : ScaleRange, Range.VisualValue : ShapeStyle
```

## Parameters

- `range`: The range of foreground styles that correspond to the   scale domain.
- `type`: The scale type.

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
- [func chartForegroundStyleScale(type: ScaleType?) -> some View](view/chartforegroundstylescale(type:).md)
  Configures the foreground style scale for charts.
- [func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some View](view/chartplotstyle(content:).md)
  Configures the plot area of charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartforegroundstylescale(range:type:))*