# removeRow(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the row at a given index.

**Availability**:
- macOS

## Declaration

```swift
func removeRow(at rowIndex: Int)
```

```objc
- (void) removeRowAtIndex:(NSInteger) rowIndex;
```

#### Discussion

Any subrows of the deleted row are adopted by the parent of the deleted row, or are made root rows.

## Parameters

- `rowIndex`: The index of a row in the receiver.

  > ❗ **Important**:  Raises an `NSRangeException` if `rowIndex` is less than `0` or greater than or equal to the number of rows.

## See Also

### Manipulating Rows
- [func addRow(Any?)](./addrow%28_%29.md)
  Adds a row to the receiver.
- [func insertRow(at: Int, with: NSRuleEditor.RowType, asSubrowOfRow: Int, animate: Bool)](./insertrow%28at,with,assubrowofrow,animate%29.md)
  Adds a new row of a given type at a given location.
- [func removeRows(at: IndexSet, includeSubrows: Bool)](./removerows%28at,includesubrows%29.md)
  Removes the rows at given indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/removerow(at:))*