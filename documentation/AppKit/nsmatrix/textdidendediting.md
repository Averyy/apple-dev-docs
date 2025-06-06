# textDidEndEditing(_:)

**Framework**: AppKit  
**Kind**: method

Invoked when text editing ends.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func textDidEndEditing(_ notification: Notification)
```

#### Discussion

This method’s default behavior is to post an [`textDidEndEditingNotification`](nscontrol/textdidendeditingnotification.md) along with the receiving object to the default notification center. The posted notification’s user info contains the contents of notification’s user info dictionary, plus an additional key-value pair. The additional key is “`NSFieldEditor`”; the value for this key is the text object that began editing. After posting the notification, [`NSMatrix`](nsmatrix.md) sends an [`endEditing(_:)`](nscell/endediting(_:).md) message to the selected cell, draws and makes the selected cell key, and then takes the appropriate action based on which key was used to end editing (Return, Tab, or Back-Tab).

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
- [func textDidChange(Notification)](nsmatrix/textdidchange(_:).md)
  Invoked when a key-down event or paste operation occurs that changes the receiver’s contents.
- [func textShouldEndEditing(NSText) -> Bool](nsmatrix/textshouldendediting(_:).md)
  Requests permission to end editing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/textdidendediting(_:))*