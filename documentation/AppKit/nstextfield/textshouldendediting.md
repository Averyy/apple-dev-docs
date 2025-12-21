# textShouldEndEditing(_:)

**Framework**: AppKit  
**Kind**: method

Performs validation on the text field’s new value.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func textShouldEndEditing(_ textObject: NSText) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the new value is valid; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method validates the text field’s new value using the `NSCell` method [`isEntryAcceptable:`](nscell/isentryacceptable:.md). If the new value is valid and the delegate responds to [`control(_:textShouldEndEditing:)`](nscontroltexteditingdelegate/control(_:textshouldendediting:).md), this method invokes that method and returns the result. If the delegate returns [`false`](https://developer.apple.com/documentation/Swift/false), the system beeps to indicate that the text field can’t validate the text. See [`NSControl`](nscontrol.md) for more information about the text delegate method.

## Parameters

- `textObject`: The text object that requests permission to end editing.

## See Also

- [func textShouldBeginEditing(NSText) -> Bool](nstextfield/textshouldbeginediting(_:).md)
  Requests permission to begin editing a text object.
- [func textDidBeginEditing(Notification)](nstextfield/textdidbeginediting(_:).md)
  Posts a notification to the default notification center that the text is about to go into edit mode.
- [func textDidChange(Notification)](nstextfield/textdidchange(_:).md)
  Posts a notification when the text changes, and forwards the message to the text field’s cell if it responds.
- [func textDidEndEditing(Notification)](nstextfield/textdidendediting(_:).md)
  Posts a notification when the text is no longer in edit mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/textshouldendediting(_:))*