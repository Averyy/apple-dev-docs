# init(_:selection:sortOrder:columns:)

**Framework**: SwiftUI  
**Kind**: init

Creates a sortable table that computes its rows based on a collection of identifiable data, and supports selecting multiple rows.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<Data, Sort>(_ data: Data, selection: Binding<Set<Value.ID>>, sortOrder: Binding<[Sort]>, @TableColumnBuilder<Value, Sort> columns: () -> Columns) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Sort : SortComparator, Columns.TableRowValue == Data.Element, Data.Element == Sort.Compared
```

## Parameters

- `data`: The identifiable data for computing the table rows.
- `selection`: A binding to a set that identifies selected rows IDs.
- `sortOrder`: A binding to the ordered sorting of columns.
- `columns`: The columns to display in the table.

## See Also

- [init<Data, Sort>(Data, sortOrder: Binding<[Sort]>, columns: () -> Columns)](table/init(_:sortorder:columns:).md)
  Creates a sortable table that computes its rows based on a collection of identifiable data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/table/init(_:selection:sortorder:columns:))*