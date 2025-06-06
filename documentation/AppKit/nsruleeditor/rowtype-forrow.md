# rowType(forRow:)

**Framework**: AppKit  
**Kind**: method

Returns the type of a given row.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func rowType(forRow rowIndex: Int) -> NSRuleEditor.RowType
```

#### Return Value

The type of the row at `rowIndex`.

## Parameters

- `rowIndex`: The index of a row in the receiver.

## See Also

- [var numberOfRows: Int](nsruleeditor/numberofrows.md)
  The number of rows in the rule editor.
- [func parentRow(forRow: Int) -> Int](nsruleeditor/parentrow(forrow:).md)
  Returns the index of the parent of a given row.
- [func row(forDisplayValue: Any) -> Int](nsruleeditor/row(fordisplayvalue:).md)
  Returns the index of the row containing a given value.
- [NSRuleEditor.RowType](nsruleeditor/rowtype.md)
  Specifies a type for row types.
- [func subrowIndexes(forRow: Int) -> IndexSet](nsruleeditor/subrowindexes(forrow:).md)
  Returns the immediate subrows of a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/rowtype(forrow:))*