# init(sortOrder:columns:rows:)

**Framework**: SwiftUI  
**Kind**: init

Creates a sortable table with the given columns and rows.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<Sort>(sortOrder: Binding<[Sort]>, @TableColumnBuilder<Value, Sort> columns: () -> Columns, @TableRowBuilder<Value> rows: () -> Rows) where Sort : SortComparator, Columns.TableRowValue == Sort.Compared
```

## Parameters

- `sortOrder`: A binding to the ordered sorting of columns.
- `columns`: The columns to display in the table.
- `rows`: The rows to display in the table.

## See Also

- [init<Sort>(of: Value.Type, sortOrder: Binding<[Sort]>, columns: () -> Columns, rows: () -> Rows)](table/init(of:sortorder:columns:rows:).md)
  Creates a sortable table with the given columns and rows.
- [init(of:selection:sortOrder:columns:rows:)](table/init(of:selection:sortorder:columns:rows:).md)
  Creates a sortable table with the given columns and rows that supports selecting multiple rows.
- [init(selection:sortOrder:columns:rows:)](table/init(selection:sortorder:columns:rows:).md)
  Creates a sortable table with the given columns and rows that supports selecting multiple rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/table/init(sortorder:columns:rows:))*