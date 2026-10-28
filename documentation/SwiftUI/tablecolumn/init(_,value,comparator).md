# init(_:value:comparator:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a sortable column that displays a string property, and generates its label from a localized string resource.

**Availability**:
- iOS 16.6+
- iPadOS 16.6+
- Mac Catalyst 16.6+
- macOS 13.5+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, value: KeyPath<RowValue, String>, comparator: String.StandardComparator = .localizedStandard) where Content == Text
```

Available when `RowValue` conforms to `Identifiable`, `Sort` is `KeyPathComparator<RowValue>`, `Content` conforms to `View`, and `Label` is `Text`.

**Other overloads**:

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

This initializer creates a [`Text`](../text.md) view for you. For more information about localizing strings, see [`Text`](../text.md).

## Parameters

- `titleResource`: Text resource for the column’s localized title.
- `value`: The path to the property associated with the column, to display verbatim as text in each row of a table, and the key path used to create a sort comparator when sorting the column.
- `comparator`: The `SortComparator` used to order the string values.

## See Also

### Creating a sortable column
- [init(_:value:content:)](./init%28_,value,content%29.md)
  Creates a sortable column for Boolean values that generates its label from a localized string resource.
- [init(_:value:comparator:content:)](./init%28_,value,comparator,content%29.md)
  Creates a sortable column that generates its label from a localized string resource.
- [init(_:sortUsing:content:)](./init%28_,sortusing,content%29.md)
  Creates a sortable column that generates its label from a localized string resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:value:comparator:))*