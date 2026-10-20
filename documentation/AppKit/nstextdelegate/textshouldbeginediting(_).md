# textShouldBeginEditing(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked when a text object begins to change its text, this method requests permission for `aTextObject` to begin editing.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func textShouldBeginEditing(_ textObject: NSText) -> Bool
```

```objc
- (BOOL) textShouldBeginEditing:(NSText *) textObject;
```

#### Discussion

If the delegate returns [`true`](../../Swift/true.md), the text object proceeds to make changes. If the delegate returns [`false`](../../Swift/false.md), the text object abandons the editing operation. This method is also invoked when the user drags and drops a file onto the text object.

## See Also

### Related Documentation
- [func becomeFirstResponder() -> Bool](../nsresponder/becomefirstresponder%28%29.md)
  Notifies the receiver that it’s about to become first responder in its [`NSWindow`](../nswindow.md).
- [func makeFirstResponder(NSResponder?) -> Bool](../nswindow/makefirstresponder%28_%29.md)
  Attempts to make a given responder the first responder for the window.
### Editing text
- [func textDidBeginEditing(Notification)](./textdidbeginediting%28_%29.md)
  Informs the delegate that the text object has begun editing (that the user has begun changing it).
- [func textShouldEndEditing(NSText) -> Bool](./textshouldendediting%28_%29.md)
  Invoked from a text object’s implementation of [`resignFirstResponder()`](../nsresponder/resignfirstresponder%28%29.md), this method requests permission for `aTextObject` to end editing.
- [func textDidEndEditing(Notification)](./textdidendediting%28_%29.md)
  Informs the delegate that the text object has finished editing (that it has resigned first responder status).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextdelegate/textshouldbeginediting(_:))*