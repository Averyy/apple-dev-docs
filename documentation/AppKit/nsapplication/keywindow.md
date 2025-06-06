# keyWindow

**Framework**: AppKit  
**Kind**: property

The window that currently receives keyboard events.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var keyWindow: NSWindow? { get }
```

#### Discussion

The value of this property is `nil` when there is no window receiving keyboard events. The property might be `nil` because the app’s storyboard file has not yet finished loading or when the receiver is not active.

## See Also

- [var isKeyWindow: Bool](nswindow/iskeywindow.md)
  A Boolean value that indicates whether the window is the key window for the application.
- [var mainWindow: NSWindow?](nsapplication/mainwindow.md)
  The app’s main window.
- [func window(withWindowNumber: Int) -> NSWindow?](nsapplication/window(withwindownumber:).md)
  Returns the window corresponding to the specified window number.
- [var windows: [NSWindow]](nsapplication/windows.md)
  An array of the app’s window objects.
- [func makeWindowsPerform(Selector, inOrder: Bool) -> NSWindow?](nsapplication/makewindowsperform(_:inorder:).md)
  Sends the specified message to each of the app’s window objects until one returns a non-`nil` value.
- [func enumerateWindows(options: NSApplication.WindowListOptions, using: (NSWindow, UnsafeMutablePointer<ObjCBool>) -> Void)](nsapplication/enumeratewindows(options:using:).md)
  Executes a block for each of the app’s windows.
- [NSApplication.WindowListOptions](nsapplication/windowlistoptions.md)
  This constant indicates a window ordering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/keywindow)*