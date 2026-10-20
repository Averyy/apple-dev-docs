# textShouldEndEditing(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Performs validation on the text field’s new value.

**Availability**:
- macOS

## Declaration

```swift
func textShouldEndEditing(_ textObject: NSText) -> Bool
```

```objc
- (BOOL) textShouldEndEditing:(NSText *) textObject;
```

#### Return Value

[`true`](../../Swift/true.md) if the new value is valid; otherwise, [`false`](../../Swift/false.md).

#### Discussion

This method validates the text field’s new value using the `NSCell` method [`isEntryAcceptable:`](../nscell/isentryacceptable_.md). If the new value is valid and the delegate responds to [`control(_:textShouldEndEditing:)`](../nscontroltexteditingdelegate/control%28_,textshouldendediting%29.md), this method invokes that method and returns the result. If the delegate returns [`false`](../../Swift/false.md), the system beeps to indicate that the text field can’t validate the text. See [`NSControl`](../nscontrol.md) for more information about the text delegate method.

## Parameters

- `textObject`: The text object that requests permission to end editing.

## See Also

### Implementing delegate methods
- [func textShouldBeginEditing(NSText) -> Bool](./textshouldbeginediting%28_%29.md)
  Requests permission to begin editing a text object.
- [func textDidBeginEditing(Notification)](./textdidbeginediting%28_%29.md)
  Posts a notification to the default notification center that the text is about to go into edit mode.
- [func textDidChange(Notification)](./textdidchange%28_%29.md)
  Posts a notification when the text changes, and forwards the message to the text field’s cell if it responds.
- [func textDidEndEditing(Notification)](./textdidendediting%28_%29.md)
  Posts a notification when the text is no longer in edit mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/textshouldendediting(_:))*