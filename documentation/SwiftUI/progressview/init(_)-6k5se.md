# init(_:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

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
init<S>(_ title: S) where Label == Text, S : StringProtocol
```

#### Discussion

This initializer creates a [`Text`](../text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](../text/init%28_,tablename,bundle,comment%29.md). See [`Text`](../text.md) for more information about localizing strings. To initialize a indeterminate progress view with a string variable, use the corresponding initializer that takes a `StringProtocol` instance.

## Parameters

- `titleKey`: The key for the progress view’s localized title that describes the task in progress.

## See Also

### Creating an indeterminate progress view
- [init()](./init%28%29.md)
  Creates a progress view for showing indeterminate progress, without a label.
- [init(label: () -> Label)](./init%28label%29.md)
  Creates a progress view for showing indeterminate progress that displays a custom label.
- [init<S>(S)](./init%28_%29-3q5nf.md)
  Creates a progress view for showing indeterminate progress that generates its label from a string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/progressview/init(_:)-6k5se)*