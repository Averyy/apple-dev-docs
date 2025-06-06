# isKeyWindow

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window is the key window for the application.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isKeyWindow: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the window is the key window for the application; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isMainWindow: Bool](nswindow/ismainwindow.md)
  A Boolean value that indicates whether the window is the application’s main window.
- [var canBecomeKey: Bool](nswindow/canbecomekey.md)
  A Boolean value that indicates whether the window can become the key window.
- [func makeKey()](nswindow/makekey.md)
  Makes the window the key window.
- [func makeKeyAndOrderFront(Any?)](nswindow/makekeyandorderfront(_:).md)
  Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.
- [func becomeKey()](nswindow/becomekey.md)
  Informs the window that it has become the key window.
- [func resignKey()](nswindow/resignkey.md)
  Resigns the window’s key window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/iskeywindow)*