# init(_:sortUsing:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a sortable column that generates its label from a localized string resource.

**Availability**:
- iOS 16.6+
- iPadOS 16.6+
- Mac Catalyst 16.6+
- macOS 13.5+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, sortUsing comparator: Sort, @ContentBuilder content: @escaping (RowValue) -> Content)
```

Available when `RowValue` conforms to `Identifiable`, `RowValue` is `Sort.Compared`, `Sort` conforms to `SortComparator`, `Content` conforms to `View`, and `Label` is `Text`.

**Other overloads**:

```swift
nonisolated
init(_ text: Text, sortUsing comparator: Sort, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, sortUsing comparator: Sort, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init<S>(_ title: S, sortUsing comparator: Sort, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

#### Discussion

This initializer creates a [`Text`](../text.md) view on your behalf. For more information about localizing strings, see[`Text`](../text.md).

## Parameters

- `titleResource`: Text resource for the column’s localized title.
- `comparator`: The prototype sort comparator to use when representing this column. When a person taps or clicks the column header, the containing table’s `sortOrder` incorporates this value, potentially with a flipped order.
- `content`: The view content to display for each row in a table.

## See Also

### Creating a sortable column
- [init(_:value:content:)](./init%28_,value,content%29.md)
  Creates a sortable column for Boolean values that generates its label from a localized string resource.
- [init(_:value:comparator:)](./init%28_,value,comparator%29.md)
  Creates a sortable column that displays a string property, and generates its label from a localized string resource.
- [init(_:value:comparator:content:)](./init%28_,value,comparator,content%29.md)
  Creates a sortable column that generates its label from a localized string resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:sortusing:content:))*