# ChartContent

**Framework**: Swift Charts  
**Kind**: protocol

A type that represents the content that you draw on a chart.

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
@MainActor
@preconcurrency protocol ChartContent
```

#### Overview

You build a [`Chart`](chart.md) by adding instances that conform to the `ChartContent` protocol to the chart’s `content` closure. The following example adds three explicit [`BarMark`](barmark.md) instances to a chart:

```swift
Chart {
    BarMark(
        x: .value("Shape Type", "Cube"),
        y: .value("Total Count", 5)
    )
    BarMark(
        x: .value("Shape Type", "Sphere"),
        y: .value("Total Count", 6)
    )
    BarMark(
        x: .value("Shape Type", "Pyramid"),
        y: .value("Total Count", 4)
    )
}
```

The chart draws marks that correspond to the instances that you specify:

![A bar chart with three vertical bars, all in the same color. The first is labeled Cube and has a value of 5. The second is labeled Sphere and has a value of 6. The third is labeled Pyramid and has a value of 4.](https://docs-assets.developer.apple.com/published/10e238580e604d90ac847a51c40dd670/ChartContent-1-macOS%402x.png)

You can combine any number of marks or types of marks in a single chart by listing them individually as shown in the above example, wrapping them in a [`ForEach`](https://developer.apple.com/documentation/SwiftUI/ForEach), or any combination of these. For some mark types, like [`LineMark`](linemark.md), you can group the marks into series using the mark’s `series` initialization parameter.

##### Configure Chart Content

The `ChartContent` protocol provides a set of modifiers that you use to configure the properties of chart content. These behave like SwiftUI view modifiers, except that they act on chart content rather than views. Any of the types that conform to the protocol can use these modifiers. For example, you can add the [`foregroundStyle(_:)`](chartcontent/foregroundstyle(_:).md) modifier to the bar representing the number of spheres in the previous example to make it red:

```swift
BarMark(
    x: .value("Shape Type", "Sphere"),
    y: .value("Total Count", 6)
)
.foregroundStyle(.red)
```

![A bar chart with three vertical bars. The first and third bars are blue while the middle bar is red. The first is labeled Cube and has a value of 5. The second is labeled Sphere and has a value of 6. The third is labeled Pyramid and has a value of 4.](https://docs-assets.developer.apple.com/published/cb9c5bf4aed7bdd60ab03e1ca0489ac2/ChartContent-2-macOS%402x.png)

## Topics

### Styling marks
- [func foregroundStyle<S>(S) -> some ChartContent](chartcontent/foregroundstyle(_:).md)
  Sets the foreground style for the chart content.
- [func opacity(Double) -> some ChartContent](chartcontent/opacity(_:).md)
  Sets the opacity for the chart content.
- [func cornerRadius(CGFloat, style: RoundedCornerStyle) -> some ChartContent](chartcontent/cornerradius(_:style:).md)
  Sets the corner radius of the chart content.
- [func lineStyle(StrokeStyle) -> some ChartContent](chartcontent/linestyle(_:).md)
  Sets the style for line marks.
- [func interpolationMethod(InterpolationMethod) -> some ChartContent](chartcontent/interpolationmethod(_:).md)
  Plots line and area marks with the interpolation method that you specify.
### Positioning marks
- [func offset(CGSize) -> some ChartContent](chartcontent/offset(_:).md)
  Applies an offset that you specify as a size to the chart content.
- [func offset(x: CGFloat, y: CGFloat) -> some ChartContent](chartcontent/offset(x:y:).md)
  Applies a vertical and horizontal offset to the chart content.
- [func offset(x: CGFloat, yStart: CGFloat, yEnd: CGFloat) -> some ChartContent](chartcontent/offset(x:ystart:yend:).md)
  Applies an offset to the chart content.
- [func offset(xStart: CGFloat, xEnd: CGFloat, y: CGFloat) -> some ChartContent](chartcontent/offset(xstart:xend:y:).md)
  Applies an offset to the chart content.
- [func offset(xStart: CGFloat, xEnd: CGFloat, yStart: CGFloat, yEnd: CGFloat) -> some ChartContent](chartcontent/offset(xstart:xend:ystart:yend:).md)
  Applies an offset to the chart content.
- [func alignsMarkStylesWithPlotArea(Bool) -> some ChartContent](chartcontent/alignsmarkstyleswithplotarea(_:).md)
  Aligns this item’s styles with the chart’s plot area.
### Setting symbol appearance
- [func symbol<S>(S) -> some ChartContent](chartcontent/symbol(_:).md)
  Sets a plotting symbol type for the chart content.
- [func symbol<V>(symbol: () -> V) -> some ChartContent](chartcontent/symbol(symbol:).md)
  Sets a SwiftUI view to use as the symbol for the chart content.
- [func symbolSize(CGSize) -> some ChartContent](chartcontent/symbolsize(_:)-7s0vk.md)
  Sets the plotting symbol size for the chart content.
- [func symbolSize(CGFloat) -> some ChartContent](chartcontent/symbolsize(_:)-8dtyt.md)
  Sets the plotting symbol size for the chart content according to a perceived area.
### Encoding data into mark characteristics
- [func foregroundStyle<D>(by: PlottableValue<D>) -> some ChartContent](chartcontent/foregroundstyle(by:).md)
  Represents data using a foreground style.
- [func lineStyle<D>(by: PlottableValue<D>) -> some ChartContent](chartcontent/linestyle(by:).md)
  Represents data using line styles.
- [func position<P>(by: PlottableValue<P>, axis: Axis?, span: MarkDimension) -> some ChartContent](chartcontent/position(by:axis:span:).md)
  Represents data using position.
- [func symbol<D>(by: PlottableValue<D>) -> some ChartContent](chartcontent/symbol(by:).md)
  Represents data using different kinds of symbols.
- [func symbolSize<D>(by: PlottableValue<D>) -> some ChartContent](chartcontent/symbolsize(by:).md)
  Represents data using symbol sizes.
### Annotating marks
- [func annotation<C>(position: AnnotationPosition, alignment: Alignment, spacing: CGFloat?, content: () -> C) -> some ChartContent](chartcontent/annotation(position:alignment:spacing:content:)-65emh.md)
  Annotates this mark or collection of marks with a view positioned relative to its bounds.
- [func annotation<C>(position: AnnotationPosition, alignment: Alignment, spacing: CGFloat?, content: (AnnotationContext) -> C) -> some ChartContent](chartcontent/annotation(position:alignment:spacing:content:)-26b2f.md)
  Annotates this mark or collection of marks with a view positioned relative to its bounds.
### Masking and clipping
- [func mask<C>(content: () -> C) -> some ChartContent](chartcontent/mask(content:).md)
  Masks chart content using the alpha channel of the specified content.
- [func clipShape(some Shape, style: FillStyle) -> some ChartContent](chartcontent/clipshape(_:style:).md)
  Sets a clip shape for the chart content.
### Configuring accessibility
- [func accessibilityHidden(Bool) -> some ChartContent](chartcontent/accessibilityhidden(_:).md)
  Specifies whether to hide this chart content from system accessibility features.
- [func accessibilityIdentifier(String) -> some ChartContent](chartcontent/accessibilityidentifier(_:).md)
  Adds an identifier string to the chart content.
- [func accessibilityLabel(LocalizedStringKey) -> some ChartContent](chartcontent/accessibilitylabel(_:)-40zjp.md)
  Adds a label to the chart content that describes its contents.
- [func accessibilityLabel<S>(S) -> some ChartContent](chartcontent/accessibilitylabel(_:)-5gk8d.md)
  Adds a label to the chart content that describes its contents.
- [func accessibilityLabel(Text) -> some ChartContent](chartcontent/accessibilitylabel(_:)-28985.md)
  Adds a label to the chart content that describes its contents.
- [func accessibilityValue(LocalizedStringKey) -> some ChartContent](chartcontent/accessibilityvalue(_:)-33c0e.md)
  Adds a description of the value that the chart content contains.
- [func accessibilityValue<S>(S) -> some ChartContent](chartcontent/accessibilityvalue(_:)-4k545.md)
  Adds a description of the value that the chart content contains.
- [func accessibilityValue(Text) -> some ChartContent](chartcontent/accessibilityvalue(_:)-5g7o4.md)
  Adds a description of the value that the chart content contains.
### Implementing chart content
- [var body: Self.Body](chartcontent/body-swift.property.md)
  The content and behavior of the chart content.
- [associatedtype Body : ChartContent](chartcontent/body-swift.associatedtype.md)
  The type of chart content contained in the body of this instance.
### Supporting types
- [struct AnyChartContent](anychartcontent.md)
  A type-erased chart content.
### Instance Methods
- [func annotation<C>(position: AnnotationPosition, alignment: Alignment, spacing: CGFloat?, overflowResolution: AnnotationOverflowResolution, content: () -> C) -> some ChartContent](chartcontent/annotation(position:alignment:spacing:overflowresolution:content:)-1kiow.md)
  Annotates this mark or collection of marks with a view positioned relative to its bounds.
- [func annotation<C>(position: AnnotationPosition, alignment: Alignment, spacing: CGFloat?, overflowResolution: AnnotationOverflowResolution, content: (AnnotationContext) -> C) -> some ChartContent](chartcontent/annotation(position:alignment:spacing:overflowresolution:content:)-6w4p3.md)
  Annotates this mark or collection of marks with a view positioned relative to its bounds.
- [func blur(radius: CGFloat) -> some ChartContent](chartcontent/blur(radius:).md)
  Applies a Gaussian blur to this chart content.
- [func compositingLayer() -> some ChartContent](chartcontent/compositinglayer.md)
- [func compositingLayer<V>(style: (PlaceholderContentView<Self>) -> V) -> some ChartContent](chartcontent/compositinglayer(style:).md)
- [func shadow(color: Color, radius: CGFloat, x: CGFloat, y: CGFloat) -> some ChartContent](chartcontent/shadow(color:radius:x:y:).md)
  A chart content that adds a shadow to this chart content.
- [func zIndex(Double) -> some ChartContent](chartcontent/zindex(_:).md)
  Controls the display order of overlapping chart content.

## Relationships

### Inherited By
- [VectorizedChartContent](vectorizedchartcontent.md)
### Conforming Types
- [AnyChartContent](anychartcontent.md)
- [AreaMark](areamark.md)
- [AreaPlot](areaplot.md)
- [BarMark](barmark.md)
- [BarPlot](barplot.md)
- [BuilderConditional](builderconditional.md)
- [FunctionAreaPlotContent](functionareaplotcontent.md)
- [FunctionLinePlotContent](functionlineplotcontent.md)
- [LineMark](linemark.md)
- [LinePlot](lineplot.md)
- [Plot](plot.md)
- [PointMark](pointmark.md)
- [PointPlot](pointplot.md)
- [RectangleMark](rectanglemark.md)
- [RectanglePlot](rectangleplot.md)
- [RuleMark](rulemark.md)
- [RulePlot](ruleplot.md)
- [SectorMark](sectormark.md)
- [SectorPlot](sectorplot.md)
- [VectorizedAreaPlotContent](vectorizedareaplotcontent.md)
- [VectorizedBarPlotContent](vectorizedbarplotcontent.md)
- [VectorizedLinePlotContent](vectorizedlineplotcontent.md)
- [VectorizedPointPlotContent](vectorizedpointplotcontent.md)
- [VectorizedRectanglePlotContent](vectorizedrectangleplotcontent.md)
- [VectorizedRulePlotContent](vectorizedruleplotcontent.md)
- [VectorizedSectorPlotContent](vectorizedsectorplotcontent.md)

## See Also

- [Creating a chart using Swift Charts](creating-a-chart-using-swift-charts.md)
  Make a chart by combining chart building blocks in SwiftUI.
- [Visualizing your app’s data](visualizing_your_app_s_data.md)
  Build complex and interactive charts using Swift Charts.
- [struct Chart](chart.md)
  A SwiftUI view that displays a chart.
- [struct ChartContentBuilder](chartcontentbuilder.md)
  A result builder that you use to compose the contents of a chart.
- [struct Plot](plot.md)
  A mechanism for grouping chart contents into a single entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontent)*