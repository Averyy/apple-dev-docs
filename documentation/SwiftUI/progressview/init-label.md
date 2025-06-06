# init(label:)

**Framework**: SwiftUI  
**Kind**: init

Creates a progress view for showing indeterminate progress that displays a custom label.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
init(@ViewBuilder label: () -> Label)
```

## Parameters

- `label`: A view builder that creates a view that describes the task   in progress.

## See Also

- [init()](progressview/init.md)
  Creates a progress view for showing indeterminate progress, without a label.
- [init(LocalizedStringKey)](progressview/init(_:)-6k5se.md)
  Creates a progress view for showing indeterminate progress that generates its label from a localized string.
- [init<S>(S)](progressview/init(_:)-3q5nf.md)
  Creates a progress view for showing indeterminate progress that generates its label from a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressview/init(label:))*