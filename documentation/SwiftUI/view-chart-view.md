# Chart view modifiers

**Framework**: SwiftUI  
**Role**: API Collection

Configure charts that you declare with Swift Charts.

## Overview

Use these modifiers to configure a [`Chart`](../Charts/chart.md) view that you add to your SwiftUI app.

## Topics

### Styles
- [func chartBackground<V>(alignment: Alignment, content: (ChartProxy) -> V) -> some View](./view/chartbackground%28alignment,content%29.md)
  Adds a background to a view that contains a chart.
- [func chartForegroundStyleScale<DataValue, S>(KeyValuePairs<DataValue, S>) -> some View](./view/chartforegroundstylescale%28_%29.md)
  Configures the foreground style scale for charts.
- [func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](./view/chartforegroundstylescale%28domain,range,type%29.md)
  Configures the foreground style scale for charts.
- [func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType?) -> some View](./view/chartforegroundstylescale%28domain,type%29.md)
  Configures the foreground style scale for charts.
- [func chartForegroundStyleScale<Domain, S>(domain: Domain, mapping: (Domain.Element) -> S) -> some View](./view/chartforegroundstylescale%28domain,mapping%29.md)
  Configures the foreground style scale for charts.
- [func chartForegroundStyleScale<DataValue, S>(mapping: (DataValue) -> S) -> some View](./view/chartforegroundstylescale%28mapping%29.md)
  Configures the foreground style scale for charts.
- [func chartForegroundStyleScale<Range>(range: Range, type: ScaleType?) -> some View](./view/chartforegroundstylescale%28range,type%29.md)
  Configures the foreground style scale for charts.
- [func chartForegroundStyleScale(type: ScaleType?) -> some View](./view/chartforegroundstylescale%28type%29.md)
  Configures the foreground style scale for charts.
- [func chartPlotStyle<Content>(content: (ChartPlotContent) -> Content) -> some View](./view/chartplotstyle%28content%29.md)
  Configures the plot area of charts.
### 3D configuration
- [func chart3DCameraProjection(Chart3DCameraProjection) -> some View](./view/chart3dcameraprojection%28_%29.md)
- [func chart3DPose(_:)](./view/chart3dpose%28_%29.md)
  Associates a binding to be updated when the 3D chart’s pose is changed by an interaction.
- [func chart3DRenderingStyle(Chart3DRenderingStyle) -> some View](./view/chart3drenderingstyle%28_%29.md)
### Legends
- [func chartLegend(Visibility) -> some View](./view/chartlegend%28_%29.md)
  Configures the legend for charts.
- [func chartLegend(position: AnnotationPosition, alignment: Alignment?, spacing: CGFloat?) -> some View](./view/chartlegend%28position,alignment,spacing%29.md)
  Configures the legend for charts.
- [func chartLegend<Content>(position: AnnotationPosition, alignment: Alignment?, spacing: CGFloat?, content: () -> Content) -> some View](./view/chartlegend%28position,alignment,spacing,content%29.md)
  Configures the legend for charts.
### Overlays
- [func chartOverlay<V>(alignment: Alignment, content: (ChartProxy) -> V) -> some View](./view/chartoverlay%28alignment,content%29.md)
  Adds an overlay to a view that contains a chart.
### Axes
- [func chartXAxis(Visibility) -> some View](./view/chartxaxis%28_%29.md)
  Sets the visibility of the x axis.
- [func chartXAxis<Content>(content: () -> Content) -> some View](./view/chartxaxis%28content%29.md)
  Configures the x-axis for charts in the view.
- [func chartXAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some View](./view/chartxaxisstyle%28content%29.md)
  Configures the x axis content of charts.
- [func chartYAxis(Visibility) -> some View](./view/chartyaxis%28_%29.md)
  Sets the visibility of the y axis.
- [func chartYAxis<Content>(content: () -> Content) -> some View](./view/chartyaxis%28content%29.md)
  Configures the y-axis for charts in the view.
- [func chartYAxisStyle<Content>(content: (ChartAxisContent) -> Content) -> some View](./view/chartyaxisstyle%28content%29.md)
  Configures the y axis content of charts.
- [func chartZAxis(Visibility) -> some View](./view/chartzaxis%28_%29.md)
  Sets the visibility of the z axis.
- [func chartZAxis<Content>(content: () -> Content) -> some View](./view/chartzaxis%28content%29.md)
  Configures the z-axis for 3D charts in the view.
### Axis Labels
- [func chartXAxisLabel(_:position:alignment:spacing:)](./view/chartxaxislabel%28_,position,alignment,spacing%29.md)
  Adds x axis label for charts in the view.
- [func chartXAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?, spacing: CGFloat?, content: () -> C) -> some View](./view/chartxaxislabel%28position,alignment,spacing,content%29.md)
  Adds x axis label for charts in the view.
- [func chartYAxisLabel(_:position:alignment:spacing:)](./view/chartyaxislabel%28_,position,alignment,spacing%29.md)
  Adds y axis label for charts in the view.
- [func chartYAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?, spacing: CGFloat?, content: () -> C) -> some View](./view/chartyaxislabel%28position,alignment,spacing,content%29.md)
  Adds y axis label for charts in the view.
- [func chartZAxisLabel(_:position:alignment:spacing:)](./view/chartzaxislabel%28_,position,alignment,spacing%29.md)
  Adds z axis label for charts in the view. It effects 3D charts only.
### Axis scales
- [func chartXScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](./view/chartxscale%28domain,range,type%29.md)
  Configures the x scale for charts.
- [func chartXScale<Domain>(domain: Domain, type: ScaleType?) -> some View](./view/chartxscale%28domain,type%29.md)
  Configures the x scale for charts.
- [func chartXScale<Range>(range: Range, type: ScaleType?) -> some View](./view/chartxscale%28range,type%29.md)
  Configures the x scale for charts.
- [func chartXScale(type: ScaleType?) -> some View](./view/chartxscale%28type%29.md)
  Configures the x scale for charts.
- [func chartYScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](./view/chartyscale%28domain,range,type%29.md)
  Configures the y scale for charts.
- [func chartYScale<Domain>(domain: Domain, type: ScaleType?) -> some View](./view/chartyscale%28domain,type%29.md)
  Configures the y scale for charts.
- [func chartYScale<Range>(range: Range, type: ScaleType?) -> some View](./view/chartyscale%28range,type%29.md)
  Configures the y scale for charts.
- [func chartYScale(type: ScaleType?) -> some View](./view/chartyscale%28type%29.md)
  Configures the y scale for charts.
- [func chartZScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](./view/chartzscale%28domain,range,type%29.md)
  Configures the z scale for 3D charts.
- [func chartZScale<Domain>(domain: Domain, type: ScaleType?) -> some View](./view/chartzscale%28domain,type%29.md)
  Configures the z scale for 3D charts.
- [func chartZScale<Range>(range: Range, type: ScaleType?) -> some View](./view/chartzscale%28range,type%29.md)
  Configures the z scale for 3D charts.
### Symbol scales
- [func chartSymbolScale(_:)](./view/chartsymbolscale%28_%29.md)
  Configures the symbol scale for charts.
- [func chartSymbolScale<Domain>(domain: Domain) -> some View](./view/chartsymbolscale%28domain%29.md)
  Configures the symbol style scale for charts.
- [func chartSymbolScale(domain:range:)](./view/chartsymbolscale%28domain,range%29.md)
  Configures the symbol style scale for charts.
- [func chartSymbolScale<Domain, S>(domain: Domain, mapping: (Domain.Element) -> S) -> some View](./view/chartsymbolscale%28domain,mapping%29.md)
  Configures the symbol scale for charts.
- [func chartSymbolScale<DataValue, S>(mapping: (DataValue) -> S) -> some View](./view/chartsymbolscale%28mapping%29.md)
  Configures the symbol scale for charts.
- [func chartSymbolScale(range:)](./view/chartsymbolscale%28range%29.md)
  Configures the symbol style scale for charts.
### Symbol size scales
- [func chartSymbolSizeScale<DataValue>(KeyValuePairs<DataValue, CGFloat>) -> some View](./view/chartsymbolsizescale%28_%29.md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType?) -> some View](./view/chartsymbolsizescale%28domain,range,type%29.md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<Domain>(domain: Domain, type: ScaleType?) -> some View](./view/chartsymbolsizescale%28domain,type%29.md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<Domain>(domain: Domain, mapping: (Domain.Element) -> CGFloat) -> some View](./view/chartsymbolsizescale%28domain,mapping%29.md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<DataValue>(mapping: (DataValue) -> CGFloat) -> some View](./view/chartsymbolsizescale%28mapping%29.md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale<Range>(range: Range, type: ScaleType?) -> some View](./view/chartsymbolsizescale%28range,type%29.md)
  Configures the symbol size scale for charts.
- [func chartSymbolSizeScale(type: ScaleType?) -> some View](./view/chartsymbolsizescale%28type%29.md)
  Configures the symbol size scale for charts.
### Line style scales
- [func chartLineStyleScale<DataValue>(KeyValuePairs<DataValue, StrokeStyle>) -> some View](./view/chartlinestylescale%28_%29.md)
  Configures the line style scale for charts.
- [func chartLineStyleScale<Domain>(domain: Domain) -> some View](./view/chartlinestylescale%28domain%29.md)
  Configures the line style scale for charts.
- [func chartLineStyleScale<Domain, Range>(domain: Domain, range: Range) -> some View](./view/chartlinestylescale%28domain,range%29.md)
  Configures the line style scale for charts.
- [func chartLineStyleScale<Range>(range: Range) -> some View](./view/chartlinestylescale%28range%29.md)
  Configures the line style scale for charts.
- [func chartLineStyleScale<Domain>(domain: Domain, mapping: (Domain.Element) -> StrokeStyle) -> some View](./view/chartlinestylescale%28domain,mapping%29.md)
  Configures the line style scale for charts.
- [func chartLineStyleScale<DataValue>(mapping: (DataValue) -> StrokeStyle) -> some View](./view/chartlinestylescale%28mapping%29.md)
  Configures the line style scale for charts.
### Scrolling
- [func chartScrollPosition(initialX: some Plottable) -> some View](./view/chartscrollposition%28initialx%29.md)
  Sets the initial scroll position along the x-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.
- [func chartScrollPosition(initialY: some Plottable) -> some View](./view/chartscrollposition%28initialy%29.md)
  Sets the initial scroll position along the y-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.
- [func chartScrollPosition(x: Binding<some Plottable>) -> some View](./view/chartscrollposition%28x%29.md)
  Associates a binding to be updated when the chart scrolls along the x-axis.
- [func chartScrollPosition(y: Binding<some Plottable>) -> some View](./view/chartscrollposition%28y%29.md)
  Associates a binding to be updated when the chart scrolls along the y-axis.
- [func chartScrollTargetBehavior(some ChartScrollTargetBehavior) -> some View](./view/chartscrolltargetbehavior%28_%29.md)
  Sets the scroll behavior of the scrollable chart.
- [func chartScrollableAxes(Axis.Set) -> some View](./view/chartscrollableaxes%28_%29.md)
  Configures the scrollable behavior of charts in this view.
### Selection
- [func chartXSelection<P>(range: Binding<ClosedRange<P>?>) -> some View](./view/chartxselection%28range%29.md)
- [func chartXSelection<P>(value: Binding<P?>) -> some View](./view/chartxselection%28value%29.md)
- [func chartYSelection<P>(range: Binding<ClosedRange<P>?>) -> some View](./view/chartyselection%28range%29.md)
- [func chartYSelection<P>(value: Binding<P?>) -> some View](./view/chartyselection%28value%29.md)
- [func chartZSelection<P>(range: Binding<ClosedRange<P>?>) -> some View](./view/chartzselection%28range%29.md)
- [func chartZSelection<P>(value: Binding<P?>) -> some View](./view/chartzselection%28value%29.md)
- [func chartAngleSelection<P>(value: Binding<P?>) -> some View](./view/chartangleselection%28value%29.md)
### Visible domain
- [func chartXVisibleDomain<P>(length: P) -> some View](./view/chartxvisibledomain%28length%29.md)
  Sets the length of the visible domain in the X dimension.
- [func chartYVisibleDomain<P>(length: P) -> some View](./view/chartyvisibledomain%28length%29.md)
  Sets the length of the visible domain in the Y dimension.
### Interaction
- [func chartGesture((ChartProxy) -> some Gesture) -> some View](./view/chartgesture%28_%29.md)

## See Also

### Configuring view elements
- [Accessibility modifiers](./view-accessibility.md)
  Make your SwiftUI apps accessible to everyone, including people with disabilities.
- [Appearance modifiers](./view-appearance.md)
  Configure a view’s foreground and background styles, controls, and visibility.
- [Text and symbol modifiers](./view-text-and-symbols.md)
  Manage the rendering, selection, and entry of text in your view.
- [Auxiliary view modifiers](./view-auxiliary-views.md)
  Add and configure supporting views, like toolbars and context menus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-chart-view)*