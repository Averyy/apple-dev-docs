# selectText(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects text in the currently selected cell or in the key cell.

**Availability**:
- macOS

## Declaration

```swift
func selectText(_ sender: Any?)
```

```objc
- (void) selectText:(id) sender;
```

#### Discussion

If the currently selected cell is editable and enabled, its text is selected. Otherwise, the key cell is selected.

## See Also

### Related Documentation
- [func selectText(Any?)](../nstextfield/selecttext%28_%29.md)
  Ends editing in the text field and, if it’s selectable, selects the entire text content.
- [var keyCell: NSCell?](./keycell.md)
  The cell that will be clicked when the user presses the Space bar.
### Editing Text in Cells
- [func selectText(atRow: Int, column: Int) -> NSCell?](./selecttext%28atrow,column%29.md)
  Selects the text in the cell at the specified location and returns the cell.
- [func textShouldBeginEditing(NSText) -> Bool](./textshouldbeginediting%28_%29.md)
  Requests permission to begin editing text.
- [func textDidBeginEditing(Notification)](./textdidbeginediting%28_%29.md)
  Invoked when there’s a change in the text after the receiver gains first responder status.
- [func textDidChange(Notification)](./textdidchange%28_%29.md)
  Invoked when a key-down event or paste operation occurs that changes the receiver’s contents.
- [func textShouldEndEditing(NSText) -> Bool](./textshouldendediting%28_%29.md)
  Requests permission to end editing.
- [func textDidEndEditing(Notification)](./textdidendediting%28_%29.md)
  Invoked when text editing ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/selecttext(_:))*