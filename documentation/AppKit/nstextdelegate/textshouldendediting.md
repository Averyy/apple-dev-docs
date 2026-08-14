# textShouldEndEditing(_:)

**Framework**: AppKit  
**Kind**: method

Invoked from a text object’s implementation of [`resignFirstResponder()`](nsresponder/resignfirstresponder().md), this method requests permission for `aTextObject` to end editing.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func textShouldEndEditing(_ textObject: NSText) -> Bool
```

#### Discussion

If the delegate returns [`true`](https://developer.apple.com/documentation/swift/true), the text object proceeds to finish editing and resign first responder status. If the delegate returns [`false`](https://developer.apple.com/documentation/swift/false), the text object selects all of its text and remains the first responder.

## See Also

- [func resignFirstResponder() -> Bool](nsresponder/resignfirstresponder.md)
  Notifies the receiver that it’s been asked to relinquish its status as first responder in its window.
- [func textShouldBeginEditing(NSText) -> Bool](nstextdelegate/textshouldbeginediting(_:).md)
  Invoked when a text object begins to change its text, this method requests permission for `aTextObject` to begin editing.
- [func textDidBeginEditing(Notification)](nstextdelegate/textdidbeginediting(_:).md)
  Informs the delegate that the text object has begun editing (that the user has begun changing it).
- [func textDidEndEditing(Notification)](nstextdelegate/textdidendediting(_:).md)
  Informs the delegate that the text object has finished editing (that it has resigned first responder status).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextdelegate/textshouldendediting(_:))*