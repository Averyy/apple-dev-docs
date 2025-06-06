# removeRow(at:)

**Framework**: AppKit  
**Kind**: method

Removes the row at a given index.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeRow(at rowIndex: Int)
```

#### Discussion

Any subrows of the deleted row are adopted by the parent of the deleted row, or are made root rows.

## Parameters

- `rowIndex`: The index of a row in the receiver.

## See Also

- [func addRow(Any?)](nsruleeditor/addrow(_:).md)
  Adds a row to the receiver.
- [func insertRow(at: Int, with: NSRuleEditor.RowType, asSubrowOfRow: Int, animate: Bool)](nsruleeditor/insertrow(at:with:assubrowofrow:animate:).md)
  Adds a new row of a given type at a given location.
- [func removeRows(at: IndexSet, includeSubrows: Bool)](nsruleeditor/removerows(at:includesubrows:).md)
  Removes the rows at given indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/removerow(at:))*