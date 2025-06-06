# enumerateWindows(options:using:)

**Framework**: AppKit  
**Kind**: method

Executes a block for each of the app’s windows.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
func enumerateWindows(options: NSApplication.WindowListOptions = [], using block: (NSWindow, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `options`: A constant that indicates window ordering. See   for possible values.
- `block`: The block to execute for each window. The block takes the following parameters:

## See Also

- [var keyWindow: NSWindow?](nsapplication/keywindow.md)
  The window that currently receives keyboard events.
- [var mainWindow: NSWindow?](nsapplication/mainwindow.md)
  The app’s main window.
- [func window(withWindowNumber: Int) -> NSWindow?](nsapplication/window(withwindownumber:).md)
  Returns the window corresponding to the specified window number.
- [var windows: [NSWindow]](nsapplication/windows.md)
  An array of the app’s window objects.
- [func makeWindowsPerform(Selector, inOrder: Bool) -> NSWindow?](nsapplication/makewindowsperform(_:inorder:).md)
  Sends the specified message to each of the app’s window objects until one returns a non-`nil` value.
- [NSApplication.WindowListOptions](nsapplication/windowlistoptions.md)
  This constant indicates a window ordering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/enumeratewindows(options:using:))*