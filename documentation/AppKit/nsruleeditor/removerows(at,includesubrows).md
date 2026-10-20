# removeRows(at:includeSubrows:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the rows at given indexes.

**Availability**:
- macOS

## Declaration

```swift
func removeRows(at rowIndexes: IndexSet, includeSubrows: Bool)
```

```objc
- (void) removeRowsAtIndexes:(NSIndexSet *) rowIndexes includeSubrows:(BOOL) includeSubrows;
```

## Parameters

- `rowIndexes`: Indexes of one or more rows in the receiver.

  > ❗ **Important**:  Raises an `NSRangeException` if any index in `rowIndexes` is less than `0` or greater than or equal to the number of rows.
- `includeSubrows`: If [`true`](../../Swift/true.md), then sub-rows of deleted rows are also deleted; if [`false`](../../Swift/false.md), then each sub-row is adopted by its first non-deleted ancestor, or becomes a root row.

## See Also

### Manipulating Rows
- [func addRow(Any?)](./addrow%28_%29.md)
  Adds a row to the receiver.
- [func insertRow(at: Int, with: NSRuleEditor.RowType, asSubrowOfRow: Int, animate: Bool)](./insertrow%28at,with,assubrowofrow,animate%29.md)
  Adds a new row of a given type at a given location.
- [func removeRow(at: Int)](./removerow%28at%29.md)
  Removes the row at a given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/removerows(at:includesubrows:))*