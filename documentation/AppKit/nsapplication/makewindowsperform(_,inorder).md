# makeWindowsPerform(_:inOrder:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sends the specified message to each of the app’s window objects until one returns a non-`nil` value.

**Availability**:
- macOS 10.0+ - Deprecated in 10.14

> **Deprecated**: Use [`enumerateWindows(options:using:)`](./enumeratewindows%28options,using%29.md) instead.

## Declaration

```swift
func makeWindowsPerform(_ selector: Selector, inOrder: Bool) -> NSWindow?
```

```objc
- (NSWindow *) makeWindowsPerform:(SEL) selector inOrder:(BOOL) inOrder;
```

## Return Value

The window that returned a non-`nil` value or `nil` if all windows returned nil from `aSelector`.

## Parameters

- `selector`: The selector to perform on each window. This method must not take any arguments and must return a value whose type that can be compared to `nil`.
- `inOrder`: If [`true`](../../Swift/true.md), the `aSelector` message is sent to each of the window server’s onscreen windows, going in z-order, until one returns a non-`nil` value. A minimized window is not considered to be onscreen for this check. If [`false`](../../Swift/false.md), the message is sent to all windows in `NSApp`’s window list, regardless of whether or not they are onscreen. This order is unspecified.

## See Also

### Related Documentation
- [func tryToPerform(Selector, with: Any?) -> Bool](./trytoperform%28_,with%29.md)
  Dispatches an action message to the specified target.
- [func sendAction(Selector, to: Any?, from: Any?) -> Bool](./sendaction%28_,to,from%29.md)
  Sends the given action message to the given target.
### Managing App Windows
- [var keyWindow: NSWindow?](./keywindow.md)
  The window that currently receives keyboard events.
- [var mainWindow: NSWindow?](./mainwindow.md)
  The app’s main window.
- [func window(withWindowNumber: Int) -> NSWindow?](./window%28withwindownumber%29.md)
  Returns the window corresponding to the specified window number.
- [var windows: [NSWindow]](./windows.md)
  An array of the app’s window objects.
- [func enumerateWindows(options: NSApplication.WindowListOptions, using: (NSWindow, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratewindows%28options,using%29.md)
  Executes a block for each of the app’s windows.
- [NSApplication.WindowListOptions](./windowlistoptions.md)
  This constant indicates a window ordering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/makewindowsperform(_:inorder:))*