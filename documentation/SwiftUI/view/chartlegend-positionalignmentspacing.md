# chartLegend(position:alignment:spacing:)

**Framework**: SwiftUI  
**Kind**: method

Configures the legend for charts.

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
@preconcurrency func chartLegend(position: AnnotationPosition = .automatic, alignment: Alignment? = nil, spacing: CGFloat? = nil) -> some View
```

## Parameters

- `position`: Configures the position of the legend.
- `alignment`: Alignment of the legend within the space   available to it. Use   for default alignment.
- `spacing`: Distance between the legend and the chart.   Use   for the default spacing.

## See Also

- [func chartLegend(Visibility) -> some View](view/chartlegend(_:).md)
  Configures the legend for charts.
- [func chartLegend<Content>(position: AnnotationPosition, alignment: Alignment?, spacing: CGFloat?, content: () -> Content) -> some View](view/chartlegend(position:alignment:spacing:content:).md)
  Configures the legend for charts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartlegend(position:alignment:spacing:))*