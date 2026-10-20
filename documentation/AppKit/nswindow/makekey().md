# makeKey()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Makes the window the key window.

**Availability**:
- macOS

## Declaration

```swift
func makeKey()
```

```objc
- (void) makeKeyWindow;
```

## See Also

### Related Documentation
- [func makeMain()](./makemain%28%29.md)
  Makes the window the main window.
### Managing Key Status
- [var isKeyWindow: Bool](./iskeywindow.md)
  A Boolean value that indicates whether the window is the key window for the application.
- [var canBecomeKey: Bool](./canbecomekey.md)
  A Boolean value that indicates whether the window can become the key window.
- [func makeKeyAndOrderFront(Any?)](./makekeyandorderfront%28_%29.md)
  Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.
- [func becomeKey()](./becomekey%28%29.md)
  Informs the window that it has become the key window.
- [func resignKey()](./resignkey%28%29.md)
  Resigns the window’s key window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/makekey())*