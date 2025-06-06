# reloadData(forRowIndexes:inColumn:)

**Framework**: AppKit  
**Kind**: method

Updates the rows in the column with the specified column index with indexes in the specified set.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func reloadData(forRowIndexes rowIndexes: IndexSet, inColumn column: Int)
```

## Parameters

- `rowIndexes`: The set of row indexes of the rows to be updated.
- `column`: The column containing the rows to be updated.

## See Also

- [func noteHeightOfRowsWithIndexesChanged(IndexSet, inColumn: Int)](nsbrowser/noteheightofrowswithindexeschanged(_:incolumn:).md)
  Immediately retiles the browser’s columns using row heights specified by the browser’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/reloaddata(forrowindexes:incolumn:))*