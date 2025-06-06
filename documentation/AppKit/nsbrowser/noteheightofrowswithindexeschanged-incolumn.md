# noteHeightOfRowsWithIndexesChanged(_:inColumn:)

**Framework**: AppKit  
**Kind**: method

Immediately retiles the browser’s columns using row heights specified by the browser’s delegate.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
func noteHeightOfRowsWithIndexesChanged(_ indexSet: IndexSet, inColumn columnIndex: Int)
```

#### Discussion

The browser’s delegate must implement

## Parameters

- `indexSet`: The indexes of the rows to resize.
- `columnIndex`: The column to retile.

## See Also

- [func reloadData(forRowIndexes: IndexSet, inColumn: Int)](nsbrowser/reloaddata(forrowindexes:incolumn:).md)
  Updates the rows in the column with the specified column index with indexes in the specified set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/noteheightofrowswithindexeschanged(_:incolumn:))*