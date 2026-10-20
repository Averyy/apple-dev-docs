# noteHeightOfRowsWithIndexesChanged(_:inColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Immediately retiles the browser’s columns using row heights specified by the browser’s delegate.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func noteHeightOfRowsWithIndexesChanged(_ indexSet: IndexSet, inColumn columnIndex: Int)
```

```objc
- (void) noteHeightOfRowsWithIndexesChanged:(NSIndexSet *) indexSet inColumn:(NSInteger) columnIndex;
```

#### Discussion

The browser’s delegate must implement

## Parameters

- `indexSet`: The indexes of the rows to resize.
- `columnIndex`: The column to retile.

## See Also

### Updating Browsers
- [func reloadData(forRowIndexes: IndexSet, inColumn: Int)](./reloaddata%28forrowindexes,incolumn%29.md)
  Updates the rows in the column with the specified column index with indexes in the specified set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/noteheightofrowswithindexeschanged(_:incolumn:))*