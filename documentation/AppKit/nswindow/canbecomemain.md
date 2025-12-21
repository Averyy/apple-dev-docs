# canBecomeMain

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window can become the application’s main window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var canBecomeMain: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/Swift/true) when the window can become the main window; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

Attempts to make the window the main window are abandoned if the value of this property is [`false`](https://developer.apple.com/documentation/Swift/false). The value of the property is [`true`](https://developer.apple.com/documentation/Swift/true) if the window is visible, is not an [`NSPanel`](nspanel.md) object, and has a title bar or a resize mechanism. Otherwise, the value is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var isMainWindow: Bool](nswindow/ismainwindow.md)
  A Boolean value that indicates whether the window is the application’s main window.
- [func makeMain()](nswindow/makemain.md)
  Makes the window the main window.
- [func becomeMain()](nswindow/becomemain.md)
  Informs the window that it has become the main window.
- [func resignMain()](nswindow/resignmain.md)
  Resigns the window’s main window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/canbecomemain)*