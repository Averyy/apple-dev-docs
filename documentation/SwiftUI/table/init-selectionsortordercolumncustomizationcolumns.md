# init(_:selection:sortOrder:columnCustomization:columns:)

**Framework**: SwiftUI  
**Kind**: init

Creates a sortable table that computes its rows based on a collection of identifiable data, supports selecting multiple rows, and has dynamically customizable columns.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<Data, Sort>(_ data: Data, selection: Binding<Set<Value.ID>>, sortOrder: Binding<[Sort]>, columnCustomization: Binding<TableColumnCustomization<Value>>, @TableColumnBuilder<Value, Sort> columns: () -> Columns) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Sort : SortComparator, Columns.TableRowValue == Data.Element, Data.Element == Sort.Compared
```

#### Discussion

Each column in the table that should participate in customization is required to have an identifier, specified with [`customizationID(_:)`](tablecolumncontent/customizationid(_:).md).

## Parameters

- `data`: The identifiable data for computing the table rows.
- `selection`: A binding to a set that identifies selected rows IDs.
- `sortOrder`: A binding to the ordered sorting of columns.
- `columnCustomization`: A binding to the state of columns.
- `columns`: The columns to display in the table.

## See Also

- [init<Data>(Data, columnCustomization: Binding<TableColumnCustomization<Value>>, columns: () -> Columns)](table/init(_:columncustomization:columns:).md)
  Creates a table that computes its rows based on a collection of identifiable data and has dynamically customizable columns.
- [init(_:selection:columnCustomization:columns:)](table/init(_:selection:columncustomization:columns:).md)
  Creates a table that computes its rows based on a collection of identifiable data, that supports selecting multiple rows, and that has dynamically customizable columns.
- [init<Data, Sort>(Data, sortOrder: Binding<[Sort]>, columnCustomization: Binding<TableColumnCustomization<Value>>, columns: () -> Columns)](table/init(_:sortorder:columncustomization:columns:).md)
  Creates a sortable table that computes its rows based on a collection of identifiable data and has dynamically customizable columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/table/init(_:selection:sortorder:columncustomization:columns:))*