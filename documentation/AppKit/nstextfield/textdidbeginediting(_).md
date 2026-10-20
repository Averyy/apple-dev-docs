# textDidBeginEditing(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Posts a notification to the default notification center that the text is about to go into edit mode.

**Availability**:
- macOS

## Declaration

```swift
func textDidBeginEditing(_ notification: Notification)
```

```objc
- (void) textDidBeginEditing:(NSNotification *) notification;
```

#### Discussion

This action causes the text field’s delegate to receive a [`controlTextDidBeginEditing:`](../../ObjectiveC/nsobject-swift.class/controltextdidbeginediting_.md) message. See [`NSControl`](../nscontrol.md) for more information about the text delegate method.

## Parameters

- `notification`: The [`textDidBeginEditingNotification`](../nscontrol/textdidbegineditingnotification.md) notification to post to the default notification center.

## See Also

### Implementing delegate methods
- [func textShouldBeginEditing(NSText) -> Bool](./textshouldbeginediting%28_%29.md)
  Requests permission to begin editing a text object.
- [func textDidChange(Notification)](./textdidchange%28_%29.md)
  Posts a notification when the text changes, and forwards the message to the text field’s cell if it responds.
- [func textShouldEndEditing(NSText) -> Bool](./textshouldendediting%28_%29.md)
  Performs validation on the text field’s new value.
- [func textDidEndEditing(Notification)](./textdidendediting%28_%29.md)
  Posts a notification when the text is no longer in edit mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/textdidbeginediting(_:))*