# textShouldBeginEditing(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Requests permission to begin editing a text object.

**Availability**:
- macOS

## Declaration

```swift
func textShouldBeginEditing(_ textObject: NSText) -> Bool
```

```objc
- (BOOL) textShouldBeginEditing:(NSText *) textObject;
```

#### Return Value

[`true`](../../Swift/true.md) if editing can begin; otherwise, [`false`](../../Swift/false.md).

#### Discussion

If the text field isn’t editable, this method returns [`false`](../../Swift/false.md) immediately. If the text field is editable and its delegate responds to [`control(_:textShouldBeginEditing:)`](../nscontroltexteditingdelegate/control%28_,textshouldbeginediting%29.md), this method invokes that method and returns the result. Otherwise, it returns [`true`](../../Swift/true.md) to allow editing to occur. See [`NSControl`](../nscontrol.md) for more information about the text delegate method.

## Parameters

- `textObject`: The  object to begin editing.

## See Also

### Implementing delegate methods
- [func textDidBeginEditing(Notification)](./textdidbeginediting%28_%29.md)
  Posts a notification to the default notification center that the text is about to go into edit mode.
- [func textDidChange(Notification)](./textdidchange%28_%29.md)
  Posts a notification when the text changes, and forwards the message to the text field’s cell if it responds.
- [func textShouldEndEditing(NSText) -> Bool](./textshouldendediting%28_%29.md)
  Performs validation on the text field’s new value.
- [func textDidEndEditing(Notification)](./textdidendediting%28_%29.md)
  Posts a notification when the text is no longer in edit mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/textshouldbeginediting(_:))*