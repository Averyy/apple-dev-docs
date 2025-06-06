# init(_:)

**Framework**: SwiftUI  
**Kind**: init

Creates a progress view for showing indeterminate progress that generates its label from a localized string.

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
init(_ titleKey: LocalizedStringKey) where Label == Text
```

#### Discussion

This initializer creates a [`Text`](text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](text/init(_:tablename:bundle:comment:).md). See [`Text`](text.md) for more information about localizing strings. To initialize a indeterminate progress view with a string variable, use the corresponding initializer that takes a `StringProtocol` instance.

## Parameters

- `titleKey`: The key for the progress view’s localized title that   describes the task in progress.

## See Also

- [init()](progressview/init.md)
  Creates a progress view for showing indeterminate progress, without a label.
- [init(label: () -> Label)](progressview/init(label:).md)
  Creates a progress view for showing indeterminate progress that displays a custom label.
- [init<S>(S)](progressview/init(_:)-3q5nf.md)
  Creates a progress view for showing indeterminate progress that generates its label from a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressview/init(_:)-6k5se)*