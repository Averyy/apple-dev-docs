# init(of:selection:sortOrder:columns:rows:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a sortable table with the given columns and rows that supports selecting zero or one row.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init<Sort>(of valueType: Value.Type, selection: Binding<Value.ID?>, sortOrder: Binding<[Sort]>, @TableColumnBuilder<Value, Sort> columns: () -> Columns, @TableRowBuilder<Value> rows: () -> Rows) where Sort : SortComparator, Columns.TableRowValue == Sort.Compared
```

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to `TableRowContent`, `Columns` conforms to `TableColumnContent`, and `Rows.TableRowValue` is `Columns.TableRowValue`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init<Sort>(of valueType: Value.Type, selection: Binding<Set<Value.ID>>, sortOrder: Binding<[Sort]>, @TableColumnBuilder<Value, Sort> columns: () -> Columns, @TableRowBuilder<Value> rows: () -> Rows) where Sort : SortComparator, Columns.TableRowValue == Sort.Compared
```

## Parameters

- `valueType`: The type of value used to derive the table’s contents.
- `selection`: A binding to the optional selected row ID.
- `sortOrder`: A binding to the ordered sorting of columns.
- `columns`: The columns to display in the table.
- `rows`: The rows to display in the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/table/init(of:selection:sortorder:columns:rows:)-6max4)*