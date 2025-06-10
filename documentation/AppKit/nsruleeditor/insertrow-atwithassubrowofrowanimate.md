# insertRow(at:with:asSubrowOfRow:animate:)

**Framework**: AppKit  
**Kind**: method

Adds a new row of a given type at a given location.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func insertRow(at rowIndex: Int, with rowType: NSRuleEditor.RowType, asSubrowOfRow parentRow: Int, animate shouldAnimate: Bool)
```

#### Discussion

> ❗ **Important**:  If `parentRow` is greater than or equal to `rowIndex`, or if `rowIndex` would fall amongst the children of some other parent, or if the nesting mode forbids this configuration, an `NSInvalidArgumentException` is raised.

## Parameters

- `rowIndex`: The index at which the new row should be inserted.   must be greater than  , and much specify a row that does not fall amongst the children of some other parent.
- `rowType`: The type of the new row.
- `parentRow`: The index of the row of which the new row is a child. Pass   to indicate that the new row should be a root row.
- `shouldAnimate`:   if creation of the new row should be animated, otherwise  .

## See Also

- [func addRow(Any?)](nsruleeditor/addrow(_:).md)
  Adds a row to the receiver.
- [func removeRow(at: Int)](nsruleeditor/removerow(at:).md)
  Removes the row at a given index.
- [func removeRows(at: IndexSet, includeSubrows: Bool)](nsruleeditor/removerows(at:includesubrows:).md)
  Removes the rows at given indexes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/insertrow(at:with:assubrowofrow:animate:))*