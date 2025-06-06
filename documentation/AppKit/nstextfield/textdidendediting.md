# textDidEndEditing(_:)

**Framework**: AppKit  
**Kind**: method

Posts a notification when the text is no longer in edit mode.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func textDidEndEditing(_ notification: Notification)
```

#### Discussion

After validating the new value, this method posts a [`textDidEndEditingNotification`](nscontrol/textdidendeditingnotification.md) to the default notification center, which causes the text field’s delegate to receive a [`controlTextDidEndEditing:`](https://developer.apple.com/documentation/objectivec/nsobject/1428847-controltextdidendediting) message. This method then sends [`endEditing(_:)`](nscell/endediting(_:).md) to the text field’s cell and handles the key that causes editing to end as follows:

- If the user ends editing by pressing Return, this method tries to send the text field’s action to its target. If unsuccessful, it sends [`performKeyEquivalent(with:)`](nsview/performkeyequivalent(with:).md) to its `NSView`, for example, to handle the default button on a panel. If that also fails, the text field selects its text.
- If the user ends editing by pressing Tab or Shift-Tab, the text field tries to have its `NSWindow` object select its next or previous key view, using the `NSWindow` method [`selectKeyView(following:)`](nswindow/selectkeyview(following:).md) or [`selectKeyView(preceding:)`](nswindow/selectkeyview(preceding:).md). If unsuccessful, the text field selects its text.

See [`NSControl`](nscontrol.md) for more information about the text delegate method.

## Parameters

- `notification`: The   to post to the default notification center.

## See Also

- [func textShouldBeginEditing(NSText) -> Bool](nstextfield/textshouldbeginediting(_:).md)
  Requests permission to begin editing a text object.
- [func textDidBeginEditing(Notification)](nstextfield/textdidbeginediting(_:).md)
  Posts a notification to the default notification center that the text is about to go into edit mode.
- [func textDidChange(Notification)](nstextfield/textdidchange(_:).md)
  Posts a notification when the text changes, and forwards the message to the text field’s cell if it responds.
- [func textShouldEndEditing(NSText) -> Bool](nstextfield/textshouldendediting(_:).md)
  Performs validation on the text field’s new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/textdidendediting(_:))*