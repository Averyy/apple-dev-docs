# init(_:children:selection:columnCustomization:columns:)

**Framework**: SwiftUI  
**Kind**: init

Creates a hierarchical table that computes its rows based on a collection of identifiable data and key path to the children of that data, and supports selecting multiple rows.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<Data>(_ data: Data, children: KeyPath<Data.Element, Data?>, selection: Binding<Set<Value.ID>>, columnCustomization: Binding<TableColumnCustomization<Value>>? = nil, @TableColumnBuilder<Value, Never> columns: () -> Columns) where Rows == TableOutlineGroupContent<Data>, Data : RandomAccessCollection, Columns.TableRowValue == Data.Element
```

#### Discussion

Each column in the table that should participate in customization is required to have an identifier, specified with [`customizationID(_:)`](tablecolumncontent/customizationid(_:).md).

## Parameters

- `data`: The identifiable data for computing the table rows.
- `children`: A key path to a property whose non-  value gives the   children of  , and whose   value represents a leaf row of   the hierarchy, which is not capable of having children.
- `selection`: A binding to a set that identifies selected rows IDs.
- `columnCustomization`: A binding to the state of columns.
- `columns`: The columns to display in the table.

## See Also

- [init<Data>(Data, children: KeyPath<Value, Data?>, columnCustomization: Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)](table/init(_:children:columncustomization:columns:).md)
  Creates a hierarchical table that computes its rows based on a collection of identifiable data and key path to the children of that data.
- [init(_:children:selection:sortOrder:columnCustomization:columns:)](table/init(_:children:selection:sortorder:columncustomization:columns:).md)
  Creates a sortable, hierarchical table that computes its rows based on a collection of identifiable data and key path to the children of that data, and supports selecting multiple rows.
- [init<Data, Sort>(Data, children: KeyPath<Data.Element, Data?>, sortOrder: Binding<[Sort]>, columnCustomization: Binding<TableColumnCustomization<Value>>?, columns: () -> Columns)](table/init(_:children:sortorder:columncustomization:columns:).md)
  Creates a sortable, hierarchical table that computes its rows based on a collection of identifiable data and key path to the children of that data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/table/init(_:children:selection:columncustomization:columns:))*