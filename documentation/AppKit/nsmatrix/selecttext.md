# selectText(_:)

**Framework**: AppKit  
**Kind**: method

Selects text in the currently selected cell or in the key cell.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectText(_ sender: Any?)
```

#### Discussion

If the currently selected cell is editable and enabled, its text is selected. Otherwise, the key cell is selected.

## See Also

- [func selectText(Any?)](nstextfield/selecttext(_:).md)
  Ends editing in the text field and, if it’s selectable, selects the entire text content.
- [var keyCell: NSCell?](nsmatrix/keycell.md)
  The cell that will be clicked when the user presses the Space bar.
- [func selectText(atRow: Int, column: Int) -> NSCell?](nsmatrix/selecttext(atrow:column:).md)
  Selects the text in the cell at the specified location and returns the cell.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/selecttext(_:))*