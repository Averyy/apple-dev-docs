# chartXAxisLabel(_:position:alignment:spacing:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

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
func chartXAxisLabel(_ labelResource: LocalizedStringResource, position: AnnotationPosition = .automatic, alignment: Alignment? = nil, spacing: CGFloat? = nil) -> some View
```

**Other overloads**:

```swift
nonisolated
func chartXAxisLabel(_ labelKey: LocalizedStringKey, position: AnnotationPosition = .automatic, alignment: Alignment? = nil, spacing: CGFloat? = nil) -> some View
```

```swift
nonisolated
func chartXAxisLabel<S>(_ label: S, position: AnnotationPosition = .automatic, alignment: Alignment? = nil, spacing: CGFloat? = nil) -> some View where S : StringProtocol
```

## Parameters

- `labelResource`: The resource for the localized label string.
- `position`: The position of the label.
- `alignment`: The alignment of the label.
- `spacing`: The spacing of the label from the axis markers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/chartxaxislabel(_:position:alignment:spacing:)-4avsl)*