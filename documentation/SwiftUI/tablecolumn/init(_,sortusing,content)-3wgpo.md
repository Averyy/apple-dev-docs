# init(_:sortUsing:content:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a sortable column that generates its label from a localized string key.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(_ titleKey: LocalizedStringKey, sortUsing comparator: Sort, @ContentBuilder content: @escaping (RowValue) -> Content)
```

Available when `RowValue` conforms to `Identifiable`, `RowValue` is `Sort.Compared`, `Sort` conforms to `SortComparator`, `Content` conforms to `View`, and `Label` is `Text`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(_ titleResource: LocalizedStringResource, sortUsing comparator: Sort, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init(_ text: Text, sortUsing comparator: Sort, @ContentBuilder content: @escaping (RowValue) -> Content)
```

```swift
nonisolated
init<S>(_ title: S, sortUsing comparator: Sort, @ContentBuilder content: @escaping (RowValue) -> Content) where S : StringProtocol
```

## Discussion

This initializer creates a [`Text`](../text.md) view on your behalf, and treats the localized key similar to [`init(_:tableName:bundle:comment:)`](../text/init%28_,tablename,bundle,comment%29.md). For more information about localizing strings, see[`Text`](../text.md).

## Parameters

- `titleKey`: The key for the column’s localized title.
- `comparator`: The prototype sort comparator to use when representing this column. When a person taps or clicks the column header, the containing table’s `sortOrder` incorporates this value, potentially with a flipped order.
- `content`: The view content to display for each row in a table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tablecolumn/init(_:sortusing:content:)-3wgpo)*