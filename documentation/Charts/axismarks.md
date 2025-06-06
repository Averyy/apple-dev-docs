# AxisMarks

**Framework**: Swift Charts  
**Kind**: struct

A group of visual marks that a chart draws to indicate the composition of a chart’s axes.

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
struct AxisMarks<Content> where Content : AxisMark
```

## Mentions

- [Customizing axes in Swift Charts](customizing-axes-in-swift-charts.md)

## Topics

### Supporting types
- [struct AxisMarkPreset](axismarkpreset.md)
  Describes preset styles for axis markers.
- [struct AxisMarkValues](axismarkvalues.md)
  Describes the values the axis markers will present (one for each value).
- [struct AxisMarkPosition](axismarkposition.md)
  Describes the position of axis markers.
### Initializers
- [init<Format>(format: Format, preset: AxisMarkPreset, position: AxisMarkPosition, values: AxisMarkValues, stroke: StrokeStyle?)](axismarks/init(format:preset:position:values:stroke:)-8fe1o.md)
  Creates axis markers with the given properties, will override default markers. Default content will be used for the axis markers.
- [init<Value, Format>(format: Format, preset: AxisMarkPreset, position: AxisMarkPosition, values: [Value], stroke: StrokeStyle?)](axismarks/init(format:preset:position:values:stroke:)-98cpl.md)
  Creates axis markers with the given properties, will override default markers. Default content will be used for the axis markers.
- [init<Value>(preset: AxisMarkPreset, position: AxisMarkPosition, values: [Value], content: (AxisValue) -> Content)](axismarks/init(preset:position:values:content:)-1n9x7.md)
  Creates axis markers with the given properties, will override default markers.
- [init<Value>(preset: AxisMarkPreset, position: AxisMarkPosition, values: [Value], content: () -> Content)](axismarks/init(preset:position:values:content:)-4a4x7.md)
  Creates axis markers with the given properties, will override default markers.
- [init(preset: AxisMarkPreset, position: AxisMarkPosition, values: AxisMarkValues, content: () -> Content)](axismarks/init(preset:position:values:content:)-6b1jq.md)
  Creates axis markers with the given properties,will override default markers.
- [init(preset: AxisMarkPreset, position: AxisMarkPosition, values: AxisMarkValues, content: (AxisValue) -> Content)](axismarks/init(preset:position:values:content:)-7414i.md)
  Creates axis markers with the given properties,will override default markers.
- [init(preset: AxisMarkPreset, position: AxisMarkPosition, values: AxisMarkValues, stroke: StrokeStyle?)](axismarks/init(preset:position:values:stroke:)-8uk65.md)
  Creates axis markers with the given properties, will override default markers. Default content will be used for the axis markers.
- [init<Value>(preset: AxisMarkPreset, position: AxisMarkPosition, values: [Value], stroke: StrokeStyle?)](axismarks/init(preset:position:values:stroke:)-8xkl5.md)
  Creates axis markers with the given properties, will override default markers. Default content will be used for the axis markers.

## Relationships

### Conforms To
- [AxisContent](axiscontent.md)

## See Also

- [Customizing axes in Swift Charts](customizing-axes-in-swift-charts.md)
  Improve the clarity of your chart by configuring the appearance of its axes.
- [struct ChartAxisContent](chartaxiscontent.md)
  A view that represents a chart’s axis.
- [protocol AxisContent](axiscontent.md)
  A type that represents the elements you use to build a chart’s axes.
- [struct AnyAxisContent](anyaxiscontent.md)
  A type-erased element of a chart’s axis.
- [struct AxisContentBuilder](axiscontentbuilder.md)
  A result builder that constructs axis content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/axismarks)*