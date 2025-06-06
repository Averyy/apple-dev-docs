# textShouldBeginEditing(_:)

**Framework**: AppKit  
**Kind**: method

Requests permission to begin editing a text object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func textShouldBeginEditing(_ textObject: NSText) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if editing can begin; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If the text field isn’t editable, this method returns [`false`](https://developer.apple.com/documentation/swift/false) immediately. If the text field is editable and its delegate responds to [`control(_:textShouldBeginEditing:)`](nscontroltexteditingdelegate/control(_:textshouldbeginediting:).md), this method invokes that method and returns the result. Otherwise, it returns [`true`](https://developer.apple.com/documentation/swift/true) to allow editing to occur. See [`NSControl`](nscontrol.md) for more information about the text delegate method.

## Parameters

- `textObject`: The  object to begin editing.

## See Also

- [func textDidBeginEditing(Notification)](nstextfield/textdidbeginediting(_:).md)
  Posts a notification to the default notification center that the text is about to go into edit mode.
- [func textDidChange(Notification)](nstextfield/textdidchange(_:).md)
  Posts a notification when the text changes, and forwards the message to the text field’s cell if it responds.
- [func textShouldEndEditing(NSText) -> Bool](nstextfield/textshouldendediting(_:).md)
  Performs validation on the text field’s new value.
- [func textDidEndEditing(Notification)](nstextfield/textdidendediting(_:).md)
  Posts a notification when the text is no longer in edit mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/textshouldbeginediting(_:))*