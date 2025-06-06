# init(_:columns:)

**Framework**: SwiftUI  
**Kind**: init

Creates a table that computes its rows based on a collection of identifiable data.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
init<Data>(_ data: Data, @TableColumnBuilder<Value, Never> columns: () -> Columns) where Rows == TableForEachContent<Data>, Data : RandomAccessCollection, Columns.TableRowValue == Data.Element
```

## Parameters

- `data`: The identifiable data for computing the table rows.
- `columns`: The columns to display in the table.

## See Also

- [init(_:selection:columns:)](table/init(_:selection:columns:).md)
  Creates a table that computes its rows based on a collection of identifiable data, and that supports selecting multiple rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/table/init(_:columns:))*