# init(label:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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
init(@ContentBuilder label: () -> Label)
```

Available when `Label` conforms to `View` and `CurrentValueLabel` is `EmptyView`.

## Parameters

- `label`: A content builder that creates a view that describes the task in progress.

## See Also

### Creating an indeterminate progress view
- [init()](./init%28%29.md)
  Creates a progress view for showing indeterminate progress, without a label.
- [init(LocalizedStringKey)](./init%28_%29-6k5se.md)
  Creates a progress view for showing indeterminate progress that generates its label from a localized string.
- [init<S>(S)](./init%28_%29-3q5nf.md)
  Creates a progress view for showing indeterminate progress that generates its label from a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressview/init(label:))*