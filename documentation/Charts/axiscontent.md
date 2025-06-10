# AxisContent

**Framework**: Swift Charts  
**Kind**: protocol

A type that represents the elements you use to build a chart’s axes.

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
protocol AxisContent
```

## Topics

### Instance Methods
- [func compositingLayer() -> some AxisContent](axiscontent/compositinglayer.md)
  Creates a compositing layer for the axis content.
- [func compositingLayer<V>(style: (PlaceholderContentView<Self>) -> V) -> some AxisContent](axiscontent/compositinglayer(style:).md)
  Creates a compositing layer for the axis content, and apply view modifiers to the compositing layer.

## Relationships

### Conforming Types
- [AnyAxisContent](anyaxiscontent.md)
- [AxisMarks](axismarks.md)
- [BuilderConditional](builderconditional.md)

## See Also

- [Customizing axes in Swift Charts](customizing-axes-in-swift-charts.md)
  Improve the clarity of your chart by configuring the appearance of its axes.
- [struct ChartAxisContent](chartaxiscontent.md)
  A view that represents a chart’s axis.
- [struct AxisMarks](axismarks.md)
  A group of visual marks that a chart draws to indicate the composition of a chart’s axes.
- [struct AnyAxisContent](anyaxiscontent.md)
  A type-erased element of a chart’s axis.
- [struct AxisContentBuilder](axiscontentbuilder.md)
  A result builder that constructs axis content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/axiscontent)*