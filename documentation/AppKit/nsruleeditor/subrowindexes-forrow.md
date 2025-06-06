# subrowIndexes(forRow:)

**Framework**: AppKit  
**Kind**: method

Returns the immediate subrows of a given row.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func subrowIndexes(forRow rowIndex: Int) -> IndexSet
```

#### Return Value

The immediate subrows of the row at `rowIndex`.

#### Discussion

Rows are numbered starting at `0`.

## Parameters

- `rowIndex`: The index of a row in the receiver, or   to get the top-level rows.

## See Also

- [var numberOfRows: Int](nsruleeditor/numberofrows.md)
  The number of rows in the rule editor.
- [func parentRow(forRow: Int) -> Int](nsruleeditor/parentrow(forrow:).md)
  Returns the index of the parent of a given row.
- [func row(forDisplayValue: Any) -> Int](nsruleeditor/row(fordisplayvalue:).md)
  Returns the index of the row containing a given value.
- [func rowType(forRow: Int) -> NSRuleEditor.RowType](nsruleeditor/rowtype(forrow:).md)
  Returns the type of a given row.
- [NSRuleEditor.RowType](nsruleeditor/rowtype.md)
  Specifies a type for row types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/subrowindexes(forrow:))*