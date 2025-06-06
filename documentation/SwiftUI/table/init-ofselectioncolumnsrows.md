# init(of:selection:columns:rows:)

**Framework**: SwiftUI  
**Kind**: init

Creates a table with the given columns and rows that supports selecting multiple rows that generates its data using values of the given type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(of valueType: Value.Type, selection: Binding<Set<Value.ID>>, @TableColumnBuilder<Value, Never> columns: () -> Columns, @TableRowBuilder<Value> rows: () -> Rows)
```

## Parameters

- `valueType`: The type of value used to derive the table’s contents.
- `selection`: A binding to a set that identifies the selected rows IDs.
- `columns`: The columns to display in the table.
- `rows`: The rows to display in the table.

## See Also

- [init(of: Value.Type, columns: () -> Columns, rows: () -> Rows)](table/init(of:columns:rows:).md)
  Creates a table with the given columns and rows that generates its contents using values of the given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/table/init(of:selection:columns:rows:))*