# canBecomeKey

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window can become the key window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var canBecomeKey: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the window can become the key window, otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

Attempts to make the window the key window are abandoned if the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false). The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) if the window has a title bar or a resize bar, or [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

## See Also

- [var isKeyWindow: Bool](nswindow/iskeywindow.md)
  A Boolean value that indicates whether the window is the key window for the application.
- [func makeKey()](nswindow/makekey.md)
  Makes the window the key window.
- [func makeKeyAndOrderFront(Any?)](nswindow/makekeyandorderfront(_:).md)
  Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.
- [func becomeKey()](nswindow/becomekey.md)
  Informs the window that it has become the key window.
- [func resignKey()](nswindow/resignkey.md)
  Resigns the window’s key window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/canbecomekey)*