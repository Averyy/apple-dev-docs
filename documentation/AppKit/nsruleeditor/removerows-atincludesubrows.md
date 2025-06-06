# removeRows(at:includeSubrows:)

**Framework**: AppKit  
**Kind**: method

Removes the rows at given indexes.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeRows(at rowIndexes: IndexSet, includeSubrows: Bool)
```

## Parameters

- `rowIndexes`: Indexes of one or more rows in the receiver.
- `includeSubrows`: If  , then sub-rows of deleted rows are also deleted; if  , then each sub-row is adopted by its first non-deleted ancestor, or becomes a root row.

## See Also

- [func addRow(Any?)](nsruleeditor/addrow(_:).md)
  Adds a row to the receiver.
- [func insertRow(at: Int, with: NSRuleEditor.RowType, asSubrowOfRow: Int, animate: Bool)](nsruleeditor/insertrow(at:with:assubrowofrow:animate:).md)
  Adds a new row of a given type at a given location.
- [func removeRow(at: Int)](nsruleeditor/removerow(at:).md)
  Removes the row at a given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/removerows(at:includesubrows:))*