# init(of:columnCustomization:columns:rows:)

**Framework**: SwiftUI  
**Kind**: init

Creates a table with the given columns and rows that generates its contents using values of the given type and has dynamically customizable columns.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(of valueType: Value.Type, columnCustomization: Binding<TableColumnCustomization<Value>>, @TableColumnBuilder<Value, Never> columns: () -> Columns, @TableRowBuilder<Value> rows: () -> Rows)
```

#### Discussion

Each column in the table that should participate in customization is required to have an identifier, specified with [`customizationID(_:)`](tablecolumncontent/customizationid(_:).md).

## Parameters

- `valueType`: The type of value used to derive the table’s contents.
- `columnCustomization`: A binding to the state of columns.
- `columns`: The columns to display in the table.
- `rows`: The rows to display in the table.

## See Also

- [init(of:selection:columnCustomization:columns:rows:)](table/init(of:selection:columncustomization:columns:rows:).md)
  Creates a table with the given columns and rows that supports selecting multiple rows that generates its data using values of the given type and has dynamically customizable columns.
- [init(of:selection:sortOrder:columnCustomization:columns:rows:)](table/init(of:selection:sortorder:columncustomization:columns:rows:).md)
  Creates a sortable table with the given columns and rows that supports selecting multiple rows and dynamically customizable columns.
- [init<Sort>(of: Value.Type, sortOrder: Binding<[Sort]>, columnCustomization: Binding<TableColumnCustomization<Value>>, columns: () -> Columns, rows: () -> Rows)](table/init(of:sortorder:columncustomization:columns:rows:).md)
  Creates a sortable table with the given columns and rows and has dynamically customizable columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/table/init(of:columncustomization:columns:rows:))*