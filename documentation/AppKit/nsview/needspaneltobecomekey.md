# needsPanelToBecomeKey

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the view needs its panel to become the key window before it can handle keyboard input and navigation.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var needsPanelToBecomeKey: Bool { get }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false). Subclasses can override this property and use their implementation to determine if the view requires its panel to become the key window so that it can handle keyboard input and navigation. Such a subclass should also override [`acceptsFirstResponder`](nsresponder/acceptsfirstresponder.md) to return [`true`](https://developer.apple.com/documentation/swift/true).

This property is also used in keyboard navigation. It determines if a mouse click should give focus to a view—that is, make it the first responder). Some views (for example, text fields) want to receive the keyboard focus when you click in them. Other views (for example, buttons) receive focus only when you tab to them. You wouldn’t want focus to shift from a textfield that has editing in progress simply because you clicked on a check box.

## See Also

- [var becomesKeyOnlyIfNeeded: Bool](nspanel/becomeskeyonlyifneeded.md)
  A Boolean value that indicates whether the receiver becomes the key window only when needed.
- [var canBecomeKeyView: Bool](nsview/canbecomekeyview.md)
  A Boolean value indicating whether the view can become key view.
- [var nextKeyView: NSView?](nsview/nextkeyview.md)
  The view object that follows the current view in the key view loop.
- [var nextValidKeyView: NSView?](nsview/nextvalidkeyview.md)
  The closest view object in the key view loop that follows the current view in the key view loop and accepts first responder status.
- [var previousKeyView: NSView?](nsview/previouskeyview.md)
  The view object preceding the current view in the key view loop.
- [var previousValidKeyView: NSView?](nsview/previousvalidkeyview.md)
  The closest view object in the key view loop that precedes the current view and accepts first responder status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/needspaneltobecomekey)*