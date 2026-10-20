# chartYAxisLabel(_:position:alignment:spacing:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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
func chartYAxisLabel(_ labelKey: LocalizedStringKey, position: AnnotationPosition = .automatic, alignment: Alignment? = nil, spacing: CGFloat? = nil) -> some View
```

**Other overloads**:

```swift
nonisolated
func chartYAxisLabel(_ labelResource: LocalizedStringResource, position: AnnotationPosition = .automatic, alignment: Alignment? = nil, spacing: CGFloat? = nil) -> some View
```

```swift
nonisolated
func chartYAxisLabel<S>(_ label: S, position: AnnotationPosition = .automatic, alignment: Alignment? = nil, spacing: CGFloat? = nil) -> some View where S : StringProtocol
```

## Parameters

- `labelKey`: The key for the localized label string.
- `position`: The position of the label.
- `alignment`: The alignment of the label.
- `spacing`: The spacing of the label from the axis markers.

## See Also

### Axis Labels
- [func chartXAxisLabel(_:position:alignment:spacing:)](./chartxaxislabel%28_,position,alignment,spacing%29.md)
  Adds x axis label for charts in the view.
- [func chartXAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?, spacing: CGFloat?, content: () -> C) -> some View](./chartxaxislabel%28position,alignment,spacing,content%29.md)
  Adds x axis label for charts in the view.
- [func chartYAxisLabel<C>(position: AnnotationPosition, alignment: Alignment?, spacing: CGFloat?, content: () -> C) -> some View](./chartyaxislabel%28position,alignment,spacing,content%29.md)
  Adds y axis label for charts in the view.
- [func chartZAxisLabel(_:position:alignment:spacing:)](./chartzaxislabel%28_,position,alignment,spacing%29.md)
  Adds z axis label for charts in the view. It effects 3D charts only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartyaxislabel(_:position:alignment:spacing:))*