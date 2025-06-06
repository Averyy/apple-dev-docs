# row(forDisplayValue:)

**Framework**: AppKit  
**Kind**: method

Returns the index of the row containing a given value.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func row(forDisplayValue displayValue: Any) -> Int
```

#### Return Value

The index of the row containing `displayValue`, or `NSNotFound`.

#### Discussion

This method searches each row via pointer equality for the given display value, which may be present as an alternative in a popup menu for that row.

## Parameters

- `displayValue`: The display value (string, view, or menu item) of an item in the receiver. This value must not be  .

## See Also

- [var numberOfRows: Int](nsruleeditor/numberofrows.md)
  The number of rows in the rule editor.
- [func parentRow(forRow: Int) -> Int](nsruleeditor/parentrow(forrow:).md)
  Returns the index of the parent of a given row.
- [func rowType(forRow: Int) -> NSRuleEditor.RowType](nsruleeditor/rowtype(forrow:).md)
  Returns the type of a given row.
- [NSRuleEditor.RowType](nsruleeditor/rowtype.md)
  Specifies a type for row types.
- [func subrowIndexes(forRow: Int) -> IndexSet](nsruleeditor/subrowindexes(forrow:).md)
  Returns the immediate subrows of a given row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/row(fordisplayvalue:))*