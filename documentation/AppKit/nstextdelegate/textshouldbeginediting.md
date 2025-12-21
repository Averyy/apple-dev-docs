# textShouldBeginEditing(_:)

**Framework**: AppKit  
**Kind**: method

Invoked when a text object begins to change its text, this method requests permission for `aTextObject` to begin editing.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func textShouldBeginEditing(_ textObject: NSText) -> Bool
```

#### Discussion

If the delegate returns [`true`](https://developer.apple.com/documentation/Swift/true), the text object proceeds to make changes. If the delegate returns [`false`](https://developer.apple.com/documentation/Swift/false), the text object abandons the editing operation. This method is also invoked when the user drags and drops a file onto the text object.

## See Also

- [func becomeFirstResponder() -> Bool](nsresponder/becomefirstresponder.md)
  Notifies the receiver that it’s about to become first responder in its [`NSWindow`](nswindow.md).
- [func makeFirstResponder(NSResponder?) -> Bool](nswindow/makefirstresponder(_:).md)
  Attempts to make a given responder the first responder for the window.
- [func textDidBeginEditing(Notification)](nstextdelegate/textdidbeginediting(_:).md)
  Informs the delegate that the text object has begun editing (that the user has begun changing it).
- [func textShouldEndEditing(NSText) -> Bool](nstextdelegate/textshouldendediting(_:).md)
  Invoked from a text object’s implementation of [`resignFirstResponder()`](nsresponder/resignfirstresponder().md), this method requests permission for `aTextObject` to end editing.
- [func textDidEndEditing(Notification)](nstextdelegate/textdidendediting(_:).md)
  Informs the delegate that the text object has finished editing (that it has resigned first responder status).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextdelegate/textshouldbeginediting(_:))*