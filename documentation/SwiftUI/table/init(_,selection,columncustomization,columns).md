# init(_:selection:columnCustomization:columns:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a table that computes its rows based on a collection of identifiable data, that supports selecting multiple rows, and that has dynamically customizable columns.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<Data>(_ data: Data, selection: Binding<Set<Value.ID>>, columnCustomization: Binding<TableColumnCustomization<Value>>, @TableColumnBuilder<Value, Never> columns: () -> Columns) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Columns.TableRowValue == Data.Element
```

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to `TableRowContent`, `Columns` conforms to `TableColumnContent`, and `Rows.TableRowValue` is `Columns.TableRowValue`.

**Other overloads**:

```swift
nonisolated
init<Data>(_ data: Data, selection: Binding<Value.ID?>, columnCustomization: Binding<TableColumnCustomization<Value>>, @TableColumnBuilder<Value, Never> columns: () -> Columns) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Columns.TableRowValue == Data.Element
```

## Discussion

Each column in the table that should participate in customization is required to have an identifier, specified with [`customizationID(_:)`](../tablecolumncontent/customizationid%28_%29.md).

## Parameters

- `data`: The identifiable data for computing the table rows.
- `selection`: A binding to a set that identifies selected rows IDs.
- `columnCustomization`: A binding to the state of columns.
- `columns`: The columns to display in the table.

## See Also

### Creating a table with customizable columns
- [init<Data>(Data, columnCustomization: Binding<TableColumnCustomization<Value>>, columns: () -> Columns)](./init%28_,columncustomization,columns%29.md)
  Creates a table that computes its rows based on a collection of identifiable data and has dynamically customizable columns.
- [init(_:selection:sortOrder:columnCustomization:columns:)](./init%28_,selection,sortorder,columncustomization,columns%29.md)
  Creates a sortable table that computes its rows based on a collection of identifiable data, supports selecting multiple rows, and has dynamically customizable columns.
- [init<Data, Sort>(Data, sortOrder: Binding<[Sort]>, columnCustomization: Binding<TableColumnCustomization<Value>>, columns: () -> Columns)](./init%28_,sortorder,columncustomization,columns%29.md)
  Creates a sortable table that computes its rows based on a collection of identifiable data and has dynamically customizable columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/table/init(_:selection:columncustomization:columns:))*