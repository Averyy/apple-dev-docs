# isMainWindow

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window is the application’s main window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var isMainWindow: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the window is the main window for the application; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var isKeyWindow: Bool](nswindow/iskeywindow.md)
  A Boolean value that indicates whether the window is the key window for the application.
- [var canBecomeMain: Bool](nswindow/canbecomemain.md)
  A Boolean value that indicates whether the window can become the application’s main window.
- [func makeMain()](nswindow/makemain.md)
  Makes the window the main window.
- [func becomeMain()](nswindow/becomemain.md)
  Informs the window that it has become the main window.
- [func resignMain()](nswindow/resignmain.md)
  Resigns the window’s main window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/ismainwindow)*