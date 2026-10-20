# makeKeyAndOrderFront(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.

**Availability**:
- macOS

## Declaration

```swift
func makeKeyAndOrderFront(_ sender: Any?)
```

```objc
- (void) makeKeyAndOrderFront:(id) sender;
```

## Parameters

- `sender`: The message’s sender.

## See Also

### Related Documentation
- [func orderBack(Any?)](./orderback%28_%29.md)
  Moves the window to the back of its level in the screen list, without changing either the key window or the main window.
- [func orderFront(Any?)](./orderfront%28_%29.md)
  Moves the window to the front of its level in the screen list, without changing either the key window or the main window.
- [var level: NSWindow.Level](./level-swift.property.md)
  The window level of the window.
- [func order(NSWindow.OrderingMode, relativeTo: Int)](./order%28_,relativeto%29.md)
  Repositions the window’s window device in the window server’s screen list.
- [func orderOut(Any?)](./orderout%28_%29.md)
  Removes the window from the screen list, which hides the window.
### Managing Key Status
- [var isKeyWindow: Bool](./iskeywindow.md)
  A Boolean value that indicates whether the window is the key window for the application.
- [var canBecomeKey: Bool](./canbecomekey.md)
  A Boolean value that indicates whether the window can become the key window.
- [func makeKey()](./makekey%28%29.md)
  Makes the window the key window.
- [func becomeKey()](./becomekey%28%29.md)
  Informs the window that it has become the key window.
- [func resignKey()](./resignkey%28%29.md)
  Resigns the window’s key window status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/makekeyandorderfront(_:))*