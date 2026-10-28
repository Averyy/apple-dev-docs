# init(_:value:comparator:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a sortable column that displays a string property and has a text label.

**Availability**:
- iOS 16.6+
- iPadOS 16.6+
- Mac Catalyst 16.6+
- macOS 13.5+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, String>, comparator: String.StandardComparator = .localizedStandard) where Content == Text
```

Available when `RowValue` conforms to `Identifiable`, `Sort` is `KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, String>, comparator: String.StandardComparator = .localizedStandard) where Content == Text
```

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, String>, comparator: String.StandardComparator = .localizedStandard) where Content == Text
```

```swift
nonisolated
init(_ text: Text, value: KeyPath<RowValue, String>, comparator: String.StandardComparator = .localizedStandard) where Content == Text
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, String>, comparator: String.StandardComparator = .localizedStandard) where Content == Text
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, value: KeyPath<RowValue, String>, comparator: String.StandardComparator = .localizedStandard) where Content == Text
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, String>, comparator: String.StandardComparator = .localizedStandard) where Content == Text, S : StringProtocol
```

```swift
nonisolated
init<S>(_ title: S, value: KeyPath<RowValue, String>, comparator: String.StandardComparator = .localizedStandard) where Content == Text, S : StringProtocol
```

## Discussion

This initializer creates a [`Text`](../text.md) view for you, and treats the title similar to [`init(_:)`](../text/init%28_%29.md). For more information about localizing strings, see [`Text`](../text.md).

## Parameters

- `text`: The column’s label.
- `value`: The path to the property associated with the column, to display verbatim as text in each row of a table, and the key path used to create a sort comparator when sorting the column.
- `comparator`: The `SortComparator` used to order the string values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:value:comparator:)-2jbdz)*