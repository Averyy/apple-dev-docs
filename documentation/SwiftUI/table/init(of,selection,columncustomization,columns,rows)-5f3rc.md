# init(of:selection:columnCustomization:columns:rows:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a table with the given columns and rows that supports selecting zero or one row that generates its data using values of the given type and has dynamically customizable columns.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init(of valueType: Value.Type, selection: Binding<Value.ID?>, columnCustomization: Binding<TableColumnCustomization<Value>>, @TableColumnBuilder<Value, Never> columns: () -> Columns, @TableRowBuilder<Value> rows: () -> Rows)
```

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to `TableRowContent`, `Columns` conforms to `TableColumnContent`, and `Rows.TableRowValue` is `Columns.TableRowValue`.

**Other overloads**:

```swift
nonisolated
init(of valueType: Value.Type, selection: Binding<Set<Value.ID>>, columnCustomization: Binding<TableColumnCustomization<Value>>, @TableColumnBuilder<Value, Never> columns: () -> Columns, @TableRowBuilder<Value> rows: () -> Rows)
```

## Discussion

Each column in the table that should participate in customization is required to have an identifier, specified with [`customizationID(_:)`](../tablecolumncontent/customizationid%28_%29.md).

## Parameters

- `valueType`: The type of value used to derive the table’s contents.
- `selection`: A binding to the optional selected row ID.
- `columnCustomization`: A binding to the state of columns.
- `columns`: The columns to display in the table.
- `rows`: The rows to display in the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/table/init(of:selection:columncustomization:columns:rows:)-5f3rc)*