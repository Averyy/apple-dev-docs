# orderOut(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the window from the screen list, which hides the window.

**Availability**:
- macOS

## Declaration

```swift
func orderOut(_ sender: Any?)
```

```objc
- (void) orderOut:(id) sender;
```

## Discussion

If the window is the key or main window, the window object immediately behind it is made key or main in its place. Calling [`orderOut(_:)`](./orderout%28_%29.md) causes the window to be removed from the screen, but does not cause it to be released. See the [`close()`](./close%28%29.md) method for information on when a window is released. Calling [`orderOut(_:)`](./orderout%28_%29.md) on a child window causes the window to be removed from its parent window before being removed.

The default animation based on the window type will be used when the window is ordered out unless it has been modified by the [`animationBehavior`](./animationbehavior-swift.property.md) property.

## Parameters

- `sender`: The window to remove.

## See Also

### Related Documentation
- [var isReleasedWhenClosed: Bool](./isreleasedwhenclosed.md)
  A Boolean value that indicates whether the window is released when it receives the `close` message.
### Managing Window Layers
- [func orderBack(Any?)](./orderback%28_%29.md)
  Moves the window to the back of its level in the screen list, without changing either the key window or the main window.
- [func orderFront(Any?)](./orderfront%28_%29.md)
  Moves the window to the front of its level in the screen list, without changing either the key window or the main window.
- [func orderFrontRegardless()](./orderfrontregardless%28%29.md)
  Moves the window to the front of its level, even if its application isn’t active, without changing either the key window or the main window.
- [func order(NSWindow.OrderingMode, relativeTo: Int)](./order%28_,relativeto%29.md)
  Repositions the window’s window device in the window server’s screen list.
- [var level: NSWindow.Level](./level-swift.property.md)
  The window level of the window.
- [NSWindow.Level](./level-swift.struct.md)
  The standard window levels in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/orderout(_:))*