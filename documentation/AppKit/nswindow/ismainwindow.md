# isMainWindow

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window is the application’s main window.

**Availability**:
- macOS

## Declaration

```swift
var isMainWindow: Bool { get }
```

```objc
@property (readonly, getter=isMainWindow) BOOL mainWindow;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) when the window is the main window for the application; otherwise, [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [var isKeyWindow: Bool](./iskeywindow.md)
  A Boolean value that indicates whether the window is the key window for the application.
### Managing Main Status
- [var canBecomeMain: Bool](./canbecomemain.md)
  A Boolean value that indicates whether the window can become the application’s main window.
- [func makeMain()](./makemain%28%29.md)
  Makes the window the main window.
- [func becomeMain()](./becomemain%28%29.md)
  Informs the window that it has become the main window.
- [func resignMain()](./resignmain%28%29.md)
  Resigns the window’s main window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/ismainwindow)*