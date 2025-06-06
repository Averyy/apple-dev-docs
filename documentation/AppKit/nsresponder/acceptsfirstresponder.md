# acceptsFirstResponder

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the responder accepts first responder status.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var acceptsFirstResponder: Bool { get }
```

#### Discussion

As first responder, the receiver is the first object in the responder chain to be sent key events and action messages. By default, this property is [`false`](https://developer.apple.com/documentation/swift/false). Subclasses set this property to [`true`](https://developer.apple.com/documentation/swift/true) if the receiver accepts first responder status.

## See Also

- [var needsPanelToBecomeKey: Bool](nsview/needspaneltobecomekey.md)
  A Boolean value indicating whether the view needs its panel to become the key window before it can handle keyboard input and navigation.
- [Cocoa Event Handling Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/EventOverview/Introduction/Introduction.html#//apple_ref/doc/uid/10000060i)
- [func becomeFirstResponder() -> Bool](nsresponder/becomefirstresponder.md)
  Notifies the receiver that it’s about to become first responder in its [`NSWindow`](nswindow.md).
- [func resignFirstResponder() -> Bool](nsresponder/resignfirstresponder.md)
  Notifies the receiver that it’s been asked to relinquish its status as first responder in its window.
- [func validateProposedFirstResponder(NSResponder, for: NSEvent?) -> Bool](nsresponder/validateproposedfirstresponder(_:for:).md)
  Allows controls to determine when they should become first responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/acceptsfirstresponder)*