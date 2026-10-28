# textDidEndEditing(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when text editing ends.

**Availability**:
- macOS

## Declaration

```swift
func textDidEndEditing(_ notification: Notification)
```

```objc
- (void) textDidEndEditing:(NSNotification *) notification;
```

## Discussion

This method’s default behavior is to post an [`textDidEndEditingNotification`](../nscontrol/textdidendeditingnotification.md) along with the receiving object to the default notification center. The posted notification’s user info contains the contents of notification’s user info dictionary, plus an additional key-value pair. The additional key is “`NSFieldEditor`”; the value for this key is the text object that began editing. After posting the notification, [`NSMatrix`](../nsmatrix.md) sends an [`endEditing(_:)`](../nscell/endediting%28_%29.md) message to the selected cell, draws and makes the selected cell key, and then takes the appropriate action based on which key was used to end editing (Return, Tab, or Back-Tab).

## Parameters

- `notification`: The [`textDidEndEditingNotification`](../nscontrol/textdidendeditingnotification.md) notification.

## See Also

### Editing Text in Cells
- [func selectText(Any?)](./selecttext%28_%29.md)
  Selects text in the currently selected cell or in the key cell.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmatrix/textdidendediting(_:))*