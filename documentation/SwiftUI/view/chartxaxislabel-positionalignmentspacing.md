# chartXAxisLabel(_:position:alignment:spacing:)

**Framework**: SwiftUI  
**Kind**: method

Adds x axis label for charts in the view.

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
func chartXAxisLabel(_ labelKey: LocalizedStringKey, position: AnnotationPosition = .automatic, alignment: Alignment? = nil, spacing: CGFloat? = nil) -> some View
```

## Parameters

- `labelKey`: The key for the localized label string.
- `position`: The position of the label.
- `alignment`: The alignment of the label.
- `spacing`: The spacing of the label from the axis markers.

## See Also

- [func chartXAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?, spacing: CGFloat?, content: () -> C) -> some View](view/chartxaxislabel(position:alignment:spacing:content:).md)
  Adds x axis label for charts in the view.
- [func chartYAxisLabel(_:position:alignment:spacing:)](view/chartyaxislabel(_:position:alignment:spacing:).md)
  Adds y axis label for charts in the view.
- [func chartYAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?, spacing: CGFloat?, content: () -> C) -> some View](view/chartyaxislabel(position:alignment:spacing:content:).md)
  Adds y axis label for charts in the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartxaxislabel(_:position:alignment:spacing:))*