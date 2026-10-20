# canBecomeMain

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window can become the application’s main window.

**Availability**:
- macOS

## Declaration

```swift
var canBecomeMain: Bool { get }
```

```objc
@property (readonly) BOOL canBecomeMainWindow;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when the window can become the main window; otherwise, [`false`](../../Swift/false.md).

Attempts to make the window the main window are abandoned if the value of this property is [`false`](../../Swift/false.md). The value of the property is [`true`](../../Swift/true.md) if the window is visible, is not an [`NSPanel`](../nspanel.md) object, and has a title bar or a resize mechanism. Otherwise, the value is [`false`](../../Swift/false.md).

## See Also

### Managing Main Status
- [var isMainWindow: Bool](./ismainwindow.md)
  A Boolean value that indicates whether the window is the application’s main window.
- [func makeMain()](./makemain%28%29.md)
  Makes the window the main window.
- [func becomeMain()](./becomemain%28%29.md)
  Informs the window that it has become the main window.
- [func resignMain()](./resignmain%28%29.md)
  Resigns the window’s main window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/canbecomemain)*