# resignFirstResponder()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Notifies the receiver that it’s been asked to relinquish its status as first responder in its window.

**Availability**:
- macOS

## Declaration

```swift
func resignFirstResponder() -> Bool
```

```objc
- (BOOL) resignFirstResponder;
```

## Discussion

The default implementation returns [`true`](../../Swift/true.md), resigning first responder status. Subclasses can override this method to update state or perform some action such as unhighlighting the selection, or to return [`false`](../../Swift/false.md), refusing to relinquish first responder status.

Use  the `NSWindow` [`makeFirstResponder(_:)`](../nswindow/makefirstresponder%28_%29.md) method, not this method, to make an object the first responder. Never invoke this method directly.

## See Also

### Changing the First Responder
- [var acceptsFirstResponder: Bool](./acceptsfirstresponder.md)
  A Boolean value that indicates whether the responder accepts first responder status.
- [func becomeFirstResponder() -> Bool](./becomefirstresponder%28%29.md)
  Notifies the receiver that it’s about to become first responder in its [`NSWindow`](../nswindow.md).
- [func validateProposedFirstResponder(NSResponder, for: NSEvent?) -> Bool](./validateproposedfirstresponder%28_,for%29.md)
  Allows controls to determine when they should become first responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/resignfirstresponder())*