# textShouldEndEditing(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invoked from a text object’s implementation of [`resignFirstResponder()`](../nsresponder/resignfirstresponder%28%29.md), this method requests permission for `aTextObject` to end editing.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func textShouldEndEditing(_ textObject: NSText) -> Bool
```

```objc
- (BOOL) textShouldEndEditing:(NSText *) textObject;
```

## Discussion

If the delegate returns [`true`](../../Swift/true.md), the text object proceeds to finish editing and resign first responder status. If the delegate returns [`false`](../../Swift/false.md), the text object selects all of its text and remains the first responder.

## See Also

### Related Documentation
- [func resignFirstResponder() -> Bool](../nsresponder/resignfirstresponder%28%29.md)
  Notifies the receiver that it’s been asked to relinquish its status as first responder in its window.
### Editing text
- [func textShouldBeginEditing(NSText) -> Bool](./textshouldbeginediting%28_%29.md)
  Invoked when a text object begins to change its text, this method requests permission for `aTextObject` to begin editing.
- [func textDidBeginEditing(Notification)](./textdidbeginediting%28_%29.md)
  Informs the delegate that the text object has begun editing (that the user has begun changing it).
- [func textDidEndEditing(Notification)](./textdidendediting%28_%29.md)
  Informs the delegate that the text object has finished editing (that it has resigned first responder status).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextdelegate/textshouldendediting(_:))*