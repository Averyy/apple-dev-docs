# selectText(atRow:column:)

**Framework**: AppKit  
**Kind**: method

Selects the text in the cell at the specified location and returns the cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectText(atRow row: Int, column col: Int) -> NSCell?
```

#### Return Value

If it is both editable and selectable, the cell at the specified row and column. If the cell at the specified location, is either not editable or not selectable, this method does nothing and returns nil. If `row` and `column` indicate a cell that is outside the receiver, this method does nothing and returns the receiver.

## Parameters

- `row`: The row containing the text to select.
- `col`: The column containing the text to select.

## See Also

- [func selectText(Any?)](nsmatrix/selecttext(_:).md)
  Selects text in the currently selected cell or in the key cell.
- [func textShouldBeginEditing(NSText) -> Bool](nsmatrix/textshouldbeginediting(_:).md)
  Requests permission to begin editing text.
- [func textDidBeginEditing(Notification)](nsmatrix/textdidbeginediting(_:).md)
  Invoked when there’s a change in the text after the receiver gains first responder status.
- [func textDidChange(Notification)](nsmatrix/textdidchange(_:).md)
  Invoked when a key-down event or paste operation occurs that changes the receiver’s contents.
- [func textShouldEndEditing(NSText) -> Bool](nsmatrix/textshouldendediting(_:).md)
  Requests permission to end editing.
- [func textDidEndEditing(Notification)](nsmatrix/textdidendediting(_:).md)
  Invoked when text editing ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/selecttext(atrow:column:))*