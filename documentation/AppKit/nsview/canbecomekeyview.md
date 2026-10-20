# canBecomeKeyView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view can become key view.

**Availability**:
- macOS

## Declaration

```swift
var canBecomeKeyView: Bool { get }
```

```objc
@property (readonly) BOOL canBecomeKeyView;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the view can become the key view. In order to become the key view, the view must be visible, it must be installed in a window that supports keyboard entry, and the view’s [`acceptsFirstResponder`](../nsresponder/acceptsfirstresponder.md) method must return [`true`](../../Swift/true.md).

## See Also

### Managing the Key-View Loop
- [var needsPanelToBecomeKey: Bool](./needspaneltobecomekey.md)
  A Boolean value indicating whether the view needs its panel to become the key window before it can handle keyboard input and navigation.
- [var nextKeyView: NSView?](./nextkeyview.md)
  The view object that follows the current view in the key view loop.
- [var nextValidKeyView: NSView?](./nextvalidkeyview.md)
  The closest view object in the key view loop that follows the current view in the key view loop and accepts first responder status.
- [var previousKeyView: NSView?](./previouskeyview.md)
  The view object preceding the current view in the key view loop.
- [var previousValidKeyView: NSView?](./previousvalidkeyview.md)
  The closest view object in the key view loop that precedes the current view and accepts first responder status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/canbecomekeyview)*