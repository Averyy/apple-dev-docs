# textDidEndEditing(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Posts a notification when the text is no longer in edit mode.

**Availability**:
- macOS

## Declaration

```swift
func textDidEndEditing(_ notification: Notification)
```

```objc
- (void) textDidEndEditing:(NSNotification *) notification;
```

#### Discussion

After validating the new value, this method posts a [`textDidEndEditingNotification`](../nscontrol/textdidendeditingnotification.md) to the default notification center, which causes the text field’s delegate to receive a [`controlTextDidEndEditing:`](../../ObjectiveC/nsobject-swift.class/controltextdidendediting_.md) message. This method then sends [`endEditing(_:)`](../nscell/endediting%28_%29.md) to the text field’s cell and handles the key that causes editing to end as follows:

- If the user ends editing by pressing Return, this method tries to send the text field’s action to its target. If unsuccessful, it sends [`performKeyEquivalent(with:)`](../nsview/performkeyequivalent%28with%29.md) to its `NSView`, for example, to handle the default button on a panel. If that also fails, the text field selects its text.
- If the user ends editing by pressing Tab or Shift-Tab, the text field tries to have its `NSWindow` object select its next or previous key view, using the `NSWindow` method [`selectKeyView(following:)`](../nswindow/selectkeyview%28following%29.md) or [`selectKeyView(preceding:)`](../nswindow/selectkeyview%28preceding%29.md). If unsuccessful, the text field selects its text.

See [`NSControl`](../nscontrol.md) for more information about the text delegate method.

## Parameters

- `notification`: The [`textDidEndEditingNotification`](../nscontrol/textdidendeditingnotification.md) to post to the default notification center.

## See Also

### Implementing delegate methods
- [func textShouldBeginEditing(NSText) -> Bool](./textshouldbeginediting%28_%29.md)
  Requests permission to begin editing a text object.
- [func textDidBeginEditing(Notification)](./textdidbeginediting%28_%29.md)
  Posts a notification to the default notification center that the text is about to go into edit mode.
- [func textDidChange(Notification)](./textdidchange%28_%29.md)
  Posts a notification when the text changes, and forwards the message to the text field’s cell if it responds.
- [func textShouldEndEditing(NSText) -> Bool](./textshouldendediting%28_%29.md)
  Performs validation on the text field’s new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/textdidendediting(_:))*