# init(of:columns:rows:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a table with the given columns and rows that generates its contents using values of the given type.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
@export(implementation)
nonisolated init(of valueType: Value.Type, @TableColumnBuilder<Value, Never> columns: () -> Columns, @TableRowBuilder<Value> rows: () -> Rows)
```

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to `TableRowContent`, `Columns` conforms to `TableColumnContent`, and `Rows.TableRowValue` is `Columns.TableRowValue`.

## Parameters

- `valueType`: The type of value used to derive the table’s contents.
- `columns`: The columns to display in the table.
- `rows`: The rows to display in the table.

## See Also

### Creating a table from columns and rows
- [init(of:selection:columns:rows:)](./init%28of,selection,columns,rows%29.md)
  Creates a table with the given columns and rows that supports selecting multiple rows that generates its data using values of the given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/table/init(of:columns:rows:))*