# acceptsFirstResponder

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the responder accepts first responder status.

**Availability**:
- macOS

## Declaration

```swift
var acceptsFirstResponder: Bool { get }
```

```objc
@property (readonly) BOOL acceptsFirstResponder;
```

#### Discussion

As first responder, the receiver is the first object in the responder chain to be sent key events and action messages. By default, this property is [`false`](../../Swift/false.md). Subclasses set this property to [`true`](../../Swift/true.md) if the receiver accepts first responder status.

## See Also

### Related Documentation
- [var needsPanelToBecomeKey: Bool](../nsview/needspaneltobecomekey.md)
  A Boolean value indicating whether the view needs its panel to become the key window before it can handle keyboard input and navigation.
- [class NSResponder](../nsresponder.md)
  An abstract class that forms the basis of event and command processing in AppKit.
### Changing the First Responder
- [func becomeFirstResponder() -> Bool](./becomefirstresponder%28%29.md)
  Notifies the receiver that it’s about to become first responder in its [`NSWindow`](../nswindow.md).
- [func resignFirstResponder() -> Bool](./resignfirstresponder%28%29.md)
  Notifies the receiver that it’s been asked to relinquish its status as first responder in its window.
- [func validateProposedFirstResponder(NSResponder, for: NSEvent?) -> Bool](./validateproposedfirstresponder%28_,for%29.md)
  Allows controls to determine when they should become first responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/acceptsfirstresponder)*