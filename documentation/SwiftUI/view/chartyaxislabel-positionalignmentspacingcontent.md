# chartYAxisLabel(position:alignment:spacing:content:)

**Framework**: SwiftUI  
**Kind**: method

Adds y axis label for charts in the view.

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
func chartYAxisLabel<C>(position: AnnotationPosition = .automatic, alignment: Alignment? = nil, spacing: CGFloat? = nil, @ViewBuilder content: () -> C) -> some View where C : View
```

## Parameters

- `position`: The position of the label.
- `alignment`: The alignment of the label.
- `spacing`: The spacing of the label from the axis markers.
- `content`: The label content.

## See Also

- [func chartXAxisLabel(_:position:alignment:spacing:)](view/chartxaxislabel(_:position:alignment:spacing:).md)
  Adds x axis label for charts in the view.
- [func chartXAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?, spacing: CGFloat?, content: () -> C) -> some View](view/chartxaxislabel(position:alignment:spacing:content:).md)
  Adds x axis label for charts in the view.
- [func chartYAxisLabel(_:position:alignment:spacing:)](view/chartyaxislabel(_:position:alignment:spacing:).md)
  Adds y axis label for charts in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartyaxislabel(position:alignment:spacing:content:))*