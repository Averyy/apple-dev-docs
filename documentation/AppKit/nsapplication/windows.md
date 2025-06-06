# windows

**Framework**: AppKit  
**Kind**: property

An array of the app’s window objects.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var windows: [NSWindow] { get }
```

#### Discussion

This property contains an array of [`NSWindow`](nswindow.md) objects corresponding to all currently existing windows for the app. The array includes all onscreen and offscreen windows, whether or not they are visible on any space. There is no guarantee of the order of the windows in the array.

## See Also

- [var keyWindow: NSWindow?](nsapplication/keywindow.md)
  The window that currently receives keyboard events.
- [var mainWindow: NSWindow?](nsapplication/mainwindow.md)
  The app’s main window.
- [func window(withWindowNumber: Int) -> NSWindow?](nsapplication/window(withwindownumber:).md)
  Returns the window corresponding to the specified window number.
- [func makeWindowsPerform(Selector, inOrder: Bool) -> NSWindow?](nsapplication/makewindowsperform(_:inorder:).md)
  Sends the specified message to each of the app’s window objects until one returns a non-`nil` value.
- [func enumerateWindows(options: NSApplication.WindowListOptions, using: (NSWindow, UnsafeMutablePointer<ObjCBool>) -> Void)](nsapplication/enumeratewindows(options:using:).md)
  Executes a block for each of the app’s windows.
- [NSApplication.WindowListOptions](nsapplication/windowlistoptions.md)
  This constant indicates a window ordering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/windows)*