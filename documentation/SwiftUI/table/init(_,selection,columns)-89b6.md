# init(_:selection:columns:)

**Framework**: SwiftUI  
**Kind**: init  
**Role**: Initializer

Creates a table that computes its rows based on a collection of identifiable data, and that supports selecting zero or one row.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<Data>(_ data: Data, selection: Binding<Value.ID?>, @TableColumnBuilder<Value, Never> columns: () -> Columns) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Columns.TableRowValue == Data.Element
```

Available when `Value` is `Rows.TableRowValue`, `Rows` conforms to `TableRowContent`, `Columns` conforms to `TableColumnContent`, and `Rows.TableRowValue` is `Columns.TableRowValue`.

**Other overloads**:

```swift
nonisolated
init<Data>(_ data: Data, selection: Binding<Set<Value.ID>>, @TableColumnBuilder<Value, Never> columns: () -> Columns) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Columns.TableRowValue == Data.Element
```

## Parameters

- `data`: The identifiable data for computing the table rows.
- `selection`: A binding to the optional selected row ID.
- `columns`: The columns to display in the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/table/init(_:selection:columns:)-89b6)*