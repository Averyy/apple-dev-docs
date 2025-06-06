# textDidChange(_:)

**Framework**: AppKit  
**Kind**: method

Invoked when a key-down event or paste operation occurs that changes the receiver’s contents.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func textDidChange(_ notification: Notification)
```

#### Discussion

This method’s default behavior is to pass this message on to the selected cell (if the selected cell responds to `textDidChange:`) and then to post an [`textDidChangeNotification`](nscontrol/textdidchangenotification.md) along with the receiving object to the default notification center. The posted notification’s user info contains the contents of notification’s user info dictionary, plus an additional key-value pair. The additional key is “`NSFieldEditor`”; the value for this key is the text object that changed.

## Parameters

- `notification`: The   notification.

## See Also

- [func selectText(Any?)](nsmatrix/selecttext(_:).md)
  Selects text in the currently selected cell or in the key cell.
- [func selectText(atRow: Int, column: Int) -> NSCell?](nsmatrix/selecttext(atrow:column:).md)
  Selects the text in the cell at the specified location and returns the cell.
- [func textShouldBeginEditing(NSText) -> Bool](nsmatrix/textshouldbeginediting(_:).md)
  Requests permission to begin editing text.
- [func textDidBeginEditing(Notification)](nsmatrix/textdidbeginediting(_:).md)
  Invoked when there’s a change in the text after the receiver gains first responder status.
- [func textShouldEndEditing(NSText) -> Bool](nsmatrix/textshouldendediting(_:).md)
  Requests permission to end editing.
- [func textDidEndEditing(Notification)](nsmatrix/textdidendediting(_:).md)
  Invoked when text editing ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/textdidchange(_:))*