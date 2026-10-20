# textDidBeginEditing(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Informs the delegate that the text object has begun editing (that the user has begun changing it).

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func textDidBeginEditing(_ notification: Notification)
```

```objc
- (void) textDidBeginEditing:(NSNotification *) notification;
```

#### Discussion

The name of `aNotification` is [`didBeginEditingNotification`](../nstext/didbegineditingnotification.md).

## See Also

### Editing text
- [func textShouldBeginEditing(NSText) -> Bool](./textshouldbeginediting%28_%29.md)
  Invoked when a text object begins to change its text, this method requests permission for `aTextObject` to begin editing.
- [func textShouldEndEditing(NSText) -> Bool](./textshouldendediting%28_%29.md)
  Invoked from a text object’s implementation of [`resignFirstResponder()`](../nsresponder/resignfirstresponder%28%29.md), this method requests permission for `aTextObject` to end editing.
- [func textDidEndEditing(Notification)](./textdidendediting%28_%29.md)
  Informs the delegate that the text object has finished editing (that it has resigned first responder status).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextdelegate/textdidbeginediting(_:))*