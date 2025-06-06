# becomeFirstResponder()

**Framework**: AppKit  
**Kind**: method

Notifies the receiver that it’s about to become first responder in its [`NSWindow`](nswindow.md).

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func becomeFirstResponder() -> Bool
```

#### Discussion

The default implementation returns [`true`](https://developer.apple.com/documentation/swift/true), accepting first responder status. Subclasses can override this method to update state or perform some action such as highlighting the selection, or to return [`false`](https://developer.apple.com/documentation/swift/false), refusing first responder status.

Use the `NSWindow` [`makeFirstResponder(_:)`](nswindow/makefirstresponder(_:).md) method, not this method, to make an object the first responder. Never invoke this method directly.

## See Also

- [var acceptsFirstResponder: Bool](nsresponder/acceptsfirstresponder.md)
  A Boolean value that indicates whether the responder accepts first responder status.
- [func resignFirstResponder() -> Bool](nsresponder/resignfirstresponder.md)
  Notifies the receiver that it’s been asked to relinquish its status as first responder in its window.
- [func validateProposedFirstResponder(NSResponder, for: NSEvent?) -> Bool](nsresponder/validateproposedfirstresponder(_:for:).md)
  Allows controls to determine when they should become first responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/becomefirstresponder())*