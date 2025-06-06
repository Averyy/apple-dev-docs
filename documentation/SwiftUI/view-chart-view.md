# Chart view modifiers

**Framework**: SwiftUI

Configure charts that you declare with Swift Charts.

#### Overview

Use these modifiers to configure a [`Chart`](https://developer.apple.com/documentation/Charts/Chart) view that you add to your SwiftUI app.

## Topics

### Styles
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
- [func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some View](view/chartplotstyle(content:).md)
  Configures the plot area of charts.
### Legends
- [func chartLegend(Visibility) -> some View](view/chartlegend(_:).md)
  Configures the legend for charts.
- [func chartLegend(position: AnnotationPosition, alignment: Alignment?, spacing: CGFloat?) -> some View](view/chartlegend(position:alignment:spacing:).md)
  Configures the legend for charts.
- [func chartLegend<Content>(position: AnnotationPosition, alignment: Alignment?, spacing: CGFloat?, content: () -> Content) -> some View](view/chartlegend(position:alignment:spacing:content:).md)
  Configures the legend for charts.
### Overlays
- [func chartOverlay<V>(alignment: Alignment, content: (ChartProxy) -> V) -> some View](view/chartoverlay(alignment:content:).md)
  Adds an overlay to a view that contains a chart.
### Axes
- [func chartXAxis(Visibility) -> some View](view/chartxaxis(_:).md)
  Sets the visibility of the x axis.
- [func chartXAxis<Content>(content: () -> Content) -> some View](view/chartxaxis(content:).md)
  Configures the x-axis for charts in the view.
- [func chartXAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some View](view/chartxaxisstyle(content:).md)
  Configures the x axis content of charts.
- [func chartYAxis(Visibility) -> some View](view/chartyaxis(_:).md)
  Sets the visibility of the y axis.
- [func chartYAxis<Content>(content: () -> Content) -> some View](view/chartyaxis(content:).md)
  Configures the y-axis for charts in the view.
- [func chartYAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some View](view/chartyaxisstyle(content:).md)
  Configures the y axis content of charts.
### Axis Labels
- [func chartXAxisLabel(_:position:alignment:spacing:)](view/chartxaxislabel(_:position:alignment:spacing:).md)
  Adds x axis label for charts in the view.
- [func chartXAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?, spacing: CGFloat?, content: () -> C) -> some View](view/chartxaxislabel(position:alignment:spacing:content:).md)
  Adds x axis label for charts in the view.
- [func chartYAxisLabel(_:position:alignment:spacing:)](view/chartyaxislabel(_:position:alignment:spacing:).md)
  Adds y axis label for charts in the view.
- [func chartYAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?, spacing: CGFloat?, content: () -> C) -> some View](view/chartyaxislabel(position:alignment:spacing:content:).md)
  Adds y axis label for charts in the view.
### Axis scales
- [func chartXScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](view/chartxscale(domain:range:type:).md)
  Configures the x scale for charts.
- [func chartXScale<Domain>(domain: Domain, type: ScaleType?) -> some View](view/chartxscale(domain:type:).md)
  Configures the x scale for charts.
- [func chartXScale<Range>(range: Range, type: ScaleType?) -> some View](view/chartxscale(range:type:).md)
  Configures the x scale for charts.
- [func chartXScale(type: ScaleType?) -> some View](view/chartxscale(type:).md)
  Configures the x scale for charts.
- [func chartYScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](view/chartyscale(domain:range:type:).md)
  Configures the y scale for charts.
- [func chartYScale<Domain>(domain: Domain, type: ScaleType?) -> some View](view/chartyscale(domain:type:).md)
  Configures the y scale for charts.
- [func chartYScale<Range>(range: Range, type: ScaleType?) -> some View](view/chartyscale(range:type:).md)
  Configures the y scale for charts.
- [func chartYScale(type: ScaleType?) -> some View](view/chartyscale(type:).md)
  Configures the y scale for charts.
### Symbol scales
- [func chartSymbolScale(_:)](view/chartsymbolscale(_:).md)
  Configures the symbol scale for charts.
- [func chartSymbolScale<Domain>(domain: Domain) -> some View](view/chartsymbolscale(domain:).md)
  Configures the symbol style scale for charts.
- [func chartSymbolScale(domain:range:)](view/chartsymbolscale(domain:range:).md)
  Configures the symbol style scale for charts.
- [func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) -> S) -> some View](view/chartsymbolscale(domain:mapping:).md)
  Configures the symbol scale for charts.
- [func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View](view/chartsymbolscale(mapping:).md)
  Configures the symbol scale for charts.
- [func chartSymbolScale(range:)](view/chartsymbolscale(range:).md)
  Configures the symbol style scale for charts.
### Symbol size scales
- [func chartSymbolSizeScale<DataValue>(KeyValuePairs<DataValue, CGFloat>) -> some View](view/chartsymbolsizescale(_:).md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](view/chartsymbolsizescale(domain:range:type:).md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<Domain>(domain: Domain, type: ScaleType?) -> some View](view/chartsymbolsizescale(domain:type:).md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<Domain>(domain: Domain, mapping: (Domain.Element) -> CGFloat) -> some View](view/chartsymbolsizescale(domain:mapping:).md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<DataValue>(mapping: (DataValue) -> CGFloat) -> some View](view/chartsymbolsizescale(mapping:).md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<Range>(range: Range, type: ScaleType?) -> some View](view/chartsymbolsizescale(range:type:).md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale(type: ScaleType?) -> some View](view/chartsymbolsizescale(type:).md)
  Configures the symbol size scale for charts.
### Line style scales
- [func chartLineStyleScale<DataValue>(KeyValuePairs<DataValue, StrokeStyle>) -> some View](view/chartlinestylescale(_:).md)
  Configures the line style scale for charts.
- [func chartLineStyleScale<Domain>(domain: Domain) -> some View](view/chartlinestylescale(domain:).md)
  Configures the line style scale for charts.
- [func chartLineStyleScale<Domain, Range>(domain: Domain, range: Range) -> some View](view/chartlinestylescale(domain:range:).md)
  Configures the line style scale for charts.
- [func chartLineStyleScale<Range>(range: Range) -> some View](view/chartlinestylescale(range:).md)
  Configures the line style scale for charts.
- [func chartLineStyleScale<Domain>(domain: Domain, mapping: (Domain.Element) -> StrokeStyle) -> some View](view/chartlinestylescale(domain:mapping:).md)
  Configures the line style scale for charts.
- [func chartLineStyleScale<DataValue>(mapping: (DataValue) -> StrokeStyle) -> some View](view/chartlinestylescale(mapping:).md)
  Configures the line style scale for charts.
### Scrolling
- [func chartScrollPosition(initialX: some Plottable) -> some View](view/chartscrollposition(initialx:).md)
  Sets the initial scroll position along the x-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.
- [func chartScrollPosition(initialY: some Plottable) -> some View](view/chartscrollposition(initialy:).md)
  Sets the initial scroll position along the y-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.
- [func chartScrollPosition(x: Binding<some Plottable>) -> some View](view/chartscrollposition(x:).md)
  Associates a binding to be updated when the chart scrolls along the x-axis.
- [func chartScrollPosition(y: Binding<some Plottable>) -> some View](view/chartscrollposition(y:).md)
  Associates a binding to be updated when the chart scrolls along the y-axis.
- [func chartScrollTargetBehavior(some ChartScrollTargetBehavior) -> some View](view/chartscrolltargetbehavior(_:).md)
  Sets the scroll behavior of the scrollable chart.
- [func chartScrollableAxes(Axis.Set) -> some View](view/chartscrollableaxes(_:).md)
  Configures the scrollable behavior of charts in this view.
### Selection
- [func chartXSelection<P>(range: Binding<ClosedRange<P>?>) -> some View](view/chartxselection(range:).md)
- [func chartXSelection<P>(value: Binding<P?>) -> some View](view/chartxselection(value:).md)
- [func chartYSelection<P>(range: Binding<ClosedRange<P>?>) -> some View](view/chartyselection(range:).md)
- [func chartYSelection<P>(value: Binding<P?>) -> some View](view/chartyselection(value:).md)
- [func chartAngleSelection<P>(value: Binding<P?>) -> some View](view/chartangleselection(value:).md)
### Visible domain
- [func chartXVisibleDomain<P>(length: P) -> some View](view/chartxvisibledomain(length:).md)
  Sets the length of the visible domain in the X dimension.
- [func chartYVisibleDomain<P>(length: P) -> some View](view/chartyvisibledomain(length:).md)
  Sets the length of the visible domain in the Y dimension.
### Interaction
- [func chartGesture((ChartProxy) -> some Gesture) -> some View](view/chartgesture(_:).md)

## See Also

- [Accessibility modifiers](view-accessibility.md)
  Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Appearance modifiers](view-appearance.md)
  Configure a view’s foreground and background styles, controls, and visibility.
- [Text and symbol modifiers](view-text-and-symbols.md)
  Manage the rendering, selection, and entry of text in your view.
- [Auxiliary view modifiers](view-auxiliary-views.md)
  Add and configure supporting views, like toolbars and context menus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-chart-view)*