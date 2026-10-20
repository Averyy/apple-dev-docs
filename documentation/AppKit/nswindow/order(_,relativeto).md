# order(_:relativeTo:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Repositions the window’s window device in the window server’s screen list.

**Availability**:
- macOS

## Declaration

```swift
func order(_ place: NSWindow.OrderingMode, relativeTo otherWin: Int)
```

```objc
- (void) orderWindow:(NSWindowOrderingMode) place relativeTo:(NSInteger) otherWin;
```

## Parameters

- `place`:

  - [`NSWindow.OrderingMode.out`](./orderingmode/out.md): The window is removed from the screen list and `otherWin` is ignored.

  - [`NSWindow.OrderingMode.above`](./orderingmode/above.md): The window is ordered immediately in front of the window whose window number is `otherWin`
  - [`NSWindow.OrderingMode.below`](./orderingmode/below.md): The window is placed immediately behind the window represented by `otherWin`.
- `otherWin`: The number of the window the window is to be placed in front of or behind. Pass `0` to place the window in front of (when `place` is `NSWindowAbove`) or behind (when `place` is `NSWindowBelow`) all other windows in its level.

## See Also

### Related Documentation
- [var windowNumber: Int](./windownumber.md)
  The window number of the window’s window device.
- [func makeKeyAndOrderFront(Any?)](./makekeyandorderfront%28_%29.md)
  Moves the window to the front of the screen list, within its level, and makes it the key window; that is, it shows the window.
### Managing Window Layers
- [func orderOut(Any?)](./orderout%28_%29.md)
  Removes the window from the screen list, which hides the window.
- [func orderBack(Any?)](./orderback%28_%29.md)
  Moves the window to the back of its level in the screen list, without changing either the key window or the main window.
- [func orderFront(Any?)](./orderfront%28_%29.md)
  Moves the window to the front of its level in the screen list, without changing either the key window or the main window.
- [func orderFrontRegardless()](./orderfrontregardless%28%29.md)
  Moves the window to the front of its level, even if its application isn’t active, without changing either the key window or the main window.
- [var level: NSWindow.Level](./level-swift.property.md)
  The window level of the window.
- [NSWindow.Level](./level-swift.struct.md)
  The standard window levels in macOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/order(_:relativeto:))*