# textDidBeginEditing(_:)

**Framework**: AppKit  
**Kind**: method

Informs the delegate that the text object has begun editing (that the user has begun changing it).

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func textDidBeginEditing(_ notification: Notification)
```

#### Discussion

The name of `aNotification` is [`didBeginEditingNotification`](nstext/didbegineditingnotification.md).

## See Also

- [func textShouldBeginEditing(NSText) -> Bool](nstextdelegate/textshouldbeginediting(_:).md)
  Invoked when a text object begins to change its text, this method requests permission for `aTextObject` to begin editing.
- [func textShouldEndEditing(NSText) -> Bool](nstextdelegate/textshouldendediting(_:).md)
  Invoked from a text object’s implementation of [`resignFirstResponder()`](nsresponder/resignfirstresponder().md), this method requests permission for `aTextObject` to end editing.
- [func textDidEndEditing(Notification)](nstextdelegate/textdidendediting(_:).md)
  Informs the delegate that the text object has finished editing (that it has resigned first responder status).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextdelegate/textdidbeginediting(_:))*