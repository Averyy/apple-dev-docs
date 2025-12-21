# VectorizedBarPlotContent

**Framework**: Swift Charts  
**Kind**: struct

An opaque vectorized chart content type.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency struct VectorizedBarPlotContent<Data> where Data : RandomAccessCollection
```

#### Overview

Don’t use this type directly. Swift Charts automatically instantiates and consumes values of this type.

## Relationships

### Conforms To
- [ChartContent](chartcontent.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VectorizedChartContent](vectorizedchartcontent.md)

## See Also

- [var body: Self.Body](chartcontent/body-swift.property.md)
  The content and behavior of the chart content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/vectorizedbarplotcontent)*