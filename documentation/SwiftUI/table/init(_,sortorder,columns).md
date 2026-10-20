# init(_:sortOrder:columns:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a sortable table that computes its rows based on a collection of identifiable data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<Data, Sort>(_ data: Data, sortOrder: Binding<[Sort]>, @TableColumnBuilder<Value, Sort> columns: () -> Columns) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Sort : SortComparator, Columns.TableRowValue == Data.Element, Data.Element == Sort.Compared
```

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to `TableRowContent`, `Columns` conforms to `TableColumnContent`, and `Rows.TableRowValue` is `Columns.TableRowValue`.

## Parameters

- `data`: The identifiable data for computing the table rows.
- `sortOrder`: A binding to the ordered sorting of columns.
- `columns`: The columns to display in the table.

## See Also

### Creating a sortable table from columns
- [init(_:selection:sortOrder:columns:)](./init%28_,selection,sortorder,columns%29.md)
  Creates a sortable table that computes its rows based on a collection of identifiable data, and supports selecting multiple rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/table/init(_:sortorder:columns:))*