# textDidChange(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Posts a notification when the text changes, and forwards the message to the text field’s cell if it responds.

**Availability**:
- macOS

## Declaration

```swift
func textDidChange(_ notification: Notification)
```

```objc
- (void) textDidChange:(NSNotification *) notification;
```

## Discussion

This method causes the text field’s delegate to receive a [`controlTextDidChange:`](../../ObjectiveC/nsobject-swift.class/controltextdidchange_.md) message. See the [`NSControl`](../nscontrol.md) class specification for more information about the text delegate method.

## Parameters

- `notification`: The [`textDidChangeNotification`](../nscontrol/textdidchangenotification.md) notification to post to the default notification center.

## See Also

### Implementing delegate methods
- [func textShouldBeginEditing(NSText) -> Bool](./textshouldbeginediting%28_%29.md)
  Requests permission to begin editing a text object.
- [func textDidBeginEditing(Notification)](./textdidbeginediting%28_%29.md)
  Posts a notification to the default notification center that the text is about to go into edit mode.
- [func textShouldEndEditing(NSText) -> Bool](./textshouldendediting%28_%29.md)
  Performs validation on the text field’s new value.
- [func textDidEndEditing(Notification)](./textdidendediting%28_%29.md)
  Posts a notification when the text is no longer in edit mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/textdidchange(_:))*