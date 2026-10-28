# init(_:value:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates an unsortable column that displays a string property that generates its label from a string.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, String>) where Content == Text, S : StringProtocol
```

Available when `RowValue` conforms to `Identifiable`, `Sort` is `Never`, `Content` conforms to `View`, and `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, String>) where Content == Text
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, String>) where Content == Text
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, String>) where Content == Text
```

## Discussion

This initializer creates a [`Text`](../text.md) view for you, and treats the title similar to [`init(_:)`](../text/init%28_%29.md). For information about localizing strings, see [`Text`](../text.md).

## Parameters

- `title`: A string that describes the column.
- `value`: The path to the property associated with the column. The table uses this to display the property as verbatim text in each row of the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:value:)-7nxlh)*