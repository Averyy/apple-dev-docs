# textDidChange(_:)

**Framework**: AppKit  
**Kind**: method

Posts a notification when the text changes, and forwards the message to the text field’s cell if it responds.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func textDidChange(_ notification: Notification)
```

#### Discussion

This method causes the text field’s delegate to receive a [`controlTextDidChange:`](https://developer.apple.com/documentation/objectivec/nsobject/1428982-controltextdidchange) message. See the [`NSControl`](nscontrol.md) class specification for more information about the text delegate method.

## Parameters

- `notification`: The   notification to post to the default notification center.

## See Also

- [func textShouldBeginEditing(NSText) -> Bool](nstextfield/textshouldbeginediting(_:).md)
  Requests permission to begin editing a text object.
- [func textDidBeginEditing(Notification)](nstextfield/textdidbeginediting(_:).md)
  Posts a notification to the default notification center that the text is about to go into edit mode.
- [func textShouldEndEditing(NSText) -> Bool](nstextfield/textshouldendediting(_:).md)
  Performs validation on the text field’s new value.
- [func textDidEndEditing(Notification)](nstextfield/textdidendediting(_:).md)
  Posts a notification when the text is no longer in edit mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/textdidchange(_:))*