# init(of:selection:columns:rows:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a table with the given columns and rows that supports selecting zero or one row that generates its data using values of the given type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init(of valueType: Value.Type, selection: Binding<Value.ID?>, @TableColumnBuilder<Value, Never> columns: () -> Columns, @TableRowBuilder<Value> rows: () -> Rows)
```

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to `TableRowContent`, `Columns` conforms to `TableColumnContent`, and `Rows.TableRowValue` is `Columns.TableRowValue`.

**Other overloads**:

```swift
@export(implementation)
nonisolated init(of valueType: Value.Type, selection: Binding<Set<Value.ID>>, @TableColumnBuilder<Value, Never> columns: () -> Columns, @TableRowBuilder<Value> rows: () -> Rows)
```

## Parameters

- `valueType`: The type of value used to derive the table’s contents.
- `selection`: A binding to the optional selected row ID.
- `columns`: The columns to display in the table.
- `rows`: The rows to display in the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/table/init(of:selection:columns:rows:)-n09k)*