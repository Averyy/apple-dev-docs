# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a progress view for showing indeterminate progress that generates its label from a string.

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
init<S>(_ title: S) where Label == Text, S : StringProtocol
```

Available when `Label` conforms to `View` and `CurrentValueLabel` is `EmptyView`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource) where Label == Text
```

```swift
nonisolated
init(_ configuration: ProgressViewStyleConfiguration) where Label == ProgressViewStyleConfiguration.Label, CurrentValueLabel == ProgressViewStyleConfiguration.CurrentValueLabel
```

```swift
nonisolated
init(_ progress: Progress) where Label == EmptyView, CurrentValueLabel == EmptyView
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey) where Label == Text
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf, and treats the title similar to [`init(verbatim:)`](../text/init%28verbatim%29.md). See [`Text`](../text.md) for more information about localizing strings. To initialize a progress view with a localized string key, use the corresponding initializer that takes a `LocalizedStringKey` instance.

## Parameters

- `title`: A string that describes the task in progress.

## See Also

### Creating an indeterminate progress view
- [init()](./init%28%29.md)
  Creates a progress view for showing indeterminate progress, without a label.
- [init(label: () -> Label)](./init%28label%29.md)
  Creates a progress view for showing indeterminate progress that displays a custom label.
- [init(LocalizedStringKey)](./init%28_%29-6k5se.md)
  Creates a progress view for showing indeterminate progress that generates its label from a localized string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressview/init(_:)-3q5nf)*