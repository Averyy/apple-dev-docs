# textDidBeginEditing(_:)

**Framework**: AppKit  
**Kind**: method

Posts a notification to the default notification center that the text is about to go into edit mode.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func textDidBeginEditing(_ notification: Notification)
```

#### Discussion

This action causes the text field’s delegate to receive a [`controlTextDidBeginEditing:`](https://developer.apple.com/documentation/objectivec/nsobject/1428934-controltextdidbeginediting) message. See [`NSControl`](nscontrol.md) for more information about the text delegate method.

## Parameters

- `notification`: The   notification to post to the default notification center.

## See Also

- [func textShouldBeginEditing(NSText) -> Bool](nstextfield/textshouldbeginediting(_:).md)
  Requests permission to begin editing a text object.
- [func textDidChange(Notification)](nstextfield/textdidchange(_:).md)
  Posts a notification when the text changes, and forwards the message to the text field’s cell if it responds.
- [func textShouldEndEditing(NSText) -> Bool](nstextfield/textshouldendediting(_:).md)
  Performs validation on the text field’s new value.
- [func textDidEndEditing(Notification)](nstextfield/textdidendediting(_:).md)
  Posts a notification when the text is no longer in edit mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/textdidbeginediting(_:))*