# Plot

**Framework**: Swift Charts  
**Kind**: struct

A mechanism for grouping chart contents into a single entity.

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
@preconcurrency struct Plot<Content> where Content : ChartContent
```

## Topics

### Initializers
- [init(content: () -> Content)](plot/init(content:).md)

## Relationships

### Conforms To
- [ChartContent](chartcontent.md)
- [Copyable](../Swift/Copyable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Creating a chart using Swift Charts](creating-a-chart-using-swift-charts.md)
  Make a chart by combining chart building blocks in SwiftUI.
- [Visualizing your app’s data](visualizing-your-app-s-data.md)
  Build complex and interactive charts using Swift Charts.
- [struct Chart](chart.md)
  A SwiftUI view that displays a chart.
- [protocol ChartContent](chartcontent.md)
  A type that represents the content that you draw on a chart.
- [struct ChartContentBuilder](chartcontentbuilder.md)
  A result builder that you use to compose the contents of a chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/plot)*