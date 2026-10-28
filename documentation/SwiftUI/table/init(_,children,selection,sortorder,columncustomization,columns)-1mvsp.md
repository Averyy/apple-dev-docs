# init(_:children:selection:sortOrder:columnCustomization:columns:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a sortable, hierarchical table that computes its rows based on a collection of identifiable data and key path to the children of that data, and supports selecting zero or one row.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<Data, Sort>(_ data: Data, children: KeyPath<Data.Element, Data?>, selection: Binding<Value.ID?>, sortOrder: Binding<[Sort]>, columnCustomization: Binding<TableColumnCustomization<Value>>? = nil, @TableColumnBuilder<Value, Sort> columns: () -> Columns) where Rows == TableOutlineGroupContent<Data>, Data : RandomAccessCollection, Sort : SortComparator, Columns.TableRowValue == Data.Element, Data.Element == Sort.Compared
```

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to `TableRowContent`, `Columns` conforms to `TableColumnContent`, and `Rows.TableRowValue` is `Columns.TableRowValue`.

**Other overloads**:

```swift
nonisolated
init<Data, Sort>(_ data: Data, children: KeyPath<Data.Element, Data?>, selection: Binding<Set<Value.ID>>, sortOrder: Binding<[Sort]>, columnCustomization: Binding<TableColumnCustomization<Value>>? = nil, @TableColumnBuilder<Value, Sort> columns: () -> Columns) where Rows == TableOutlineGroupContent<Data>, Data : RandomAccessCollection, Sort : SortComparator, Columns.TableRowValue == Data.Element, Data.Element == Sort.Compared
```

## Discussion

Each column in the table that should participate in customization is required to have an identifier, specified with [`customizationID(_:)`](../tablecolumncontent/customizationid%28_%29.md).

## Parameters

- `data`: The identifiable data for computing the table rows.
- `children`: A key path to a property whose non-`nil` value gives the children of `data`, and whose `nil` value represents a leaf row of the hierarchy, which is not capable of having children.
- `selection`: A binding to the optional selected row ID.
- `sortOrder`: A binding to the ordered sorting of columns.
- `columnCustomization`: A binding to the state of columns.
- `columns`: The columns to display in the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/table/init(_:children:selection:sortorder:columncustomization:columns:)-1mvsp)*