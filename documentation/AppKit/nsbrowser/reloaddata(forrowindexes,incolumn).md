# reloadData(forRowIndexes:inColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Updates the rows in the column with the specified column index with indexes in the specified set.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func reloadData(forRowIndexes rowIndexes: IndexSet, inColumn column: Int)
```

```objc
- (void) reloadDataForRowIndexes:(NSIndexSet *) rowIndexes inColumn:(NSInteger) column;
```

## Parameters

- `rowIndexes`: The set of row indexes of the rows to be updated.
- `column`: The column containing the rows to be updated.

## See Also

### Updating Browsers
- [func noteHeightOfRowsWithIndexesChanged(IndexSet, inColumn: Int)](./noteheightofrowswithindexeschanged%28_,incolumn%29.md)
  Immediately retiles the browser’s columns using row heights specified by the browser’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/reloaddata(forrowindexes:incolumn:))*