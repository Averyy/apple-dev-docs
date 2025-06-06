# parentRow(forRow:)

**Framework**: AppKit  
**Kind**: method

Returns the index of the parent of a given row.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func parentRow(forRow rowIndex: Int) -> Int
```

#### Return Value

The index of the parent of the row at `rowIndex`. If the row at `rowIndex` is a root row, returns `-1`.

## Parameters

- `rowIndex`: The index of a row in the receiver.

## See Also

- [var numberOfRows: Int](nsruleeditor/numberofrows.md)
  The number of rows in the rule editor.
- [func row(forDisplayValue: Any) -> Int](nsruleeditor/row(fordisplayvalue:).md)
  Returns the index of the row containing a given value.
- [func rowType(forRow: Int) -> NSRuleEditor.RowType](nsruleeditor/rowtype(forrow:).md)
  Returns the type of a given row.
- [NSRuleEditor.RowType](nsruleeditor/rowtype.md)
  Specifies a type for row types.
- [func subrowIndexes(forRow: Int) -> IndexSet](nsruleeditor/subrowindexes(forrow:).md)
  Returns the immediate subrows of a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/parentrow(forrow:))*