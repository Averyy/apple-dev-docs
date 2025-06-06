# makeWindowsPerform(_:inOrder:)

**Framework**: AppKit  
**Kind**: method

Sends the specified message to each of the app’s window objects until one returns a non-`nil` value.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
func makeWindowsPerform(_ selector: Selector, inOrder: Bool) -> NSWindow?
```

#### Return Value

The window that returned a non-`nil` value or `nil` if all windows returned nil from `aSelector`.

## Parameters

- `selector`: The selector to perform on each window. This method must not take any arguments and must return a value whose type that can be compared to  .
- `inOrder`: If  , the   message is sent to each of the window server’s onscreen windows, going in z-order, until one returns a non-  value. A minimized window is not considered to be onscreen for this check. If  , the message is sent to all windows in  ’s window list, regardless of whether or not they are onscreen. This order is unspecified.

## See Also

- [func tryToPerform(Selector, with: Any?) -> Bool](nsapplication/trytoperform(_:with:).md)
  Dispatches an action message to the specified target.
- [func sendAction(Selector, to: Any?, from: Any?) -> Bool](nsapplication/sendaction(_:to:from:).md)
  Sends the given action message to the given target.
- [var keyWindow: NSWindow?](nsapplication/keywindow.md)
  The window that currently receives keyboard events.
- [var mainWindow: NSWindow?](nsapplication/mainwindow.md)
  The app’s main window.
- [func window(withWindowNumber: Int) -> NSWindow?](nsapplication/window(withwindownumber:).md)
  Returns the window corresponding to the specified window number.
- [var windows: [NSWindow]](nsapplication/windows.md)
  An array of the app’s window objects.
- [func enumerateWindows(options: NSApplication.WindowListOptions, using: (NSWindow, UnsafeMutablePointer<ObjCBool>) -> Void)](nsapplication/enumeratewindows(options:using:).md)
  Executes a block for each of the app’s windows.
- [NSApplication.WindowListOptions](nsapplication/windowlistoptions.md)
  This constant indicates a window ordering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/makewindowsperform(_:inorder:))*