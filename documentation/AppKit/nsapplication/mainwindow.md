# mainWindow

**Framework**: AppKit  
**Kind**: property

The app’s main window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var mainWindow: NSWindow? { get }
```

#### Discussion

The value in this property is `nil` when the app’s storyboard or nib file has not yet finished loading. It might also be `nil` when the app is inactive or hidden.

## See Also

- [var isMainWindow: Bool](nswindow/ismainwindow.md)
  A Boolean value that indicates whether the window is the application’s main window.
- [var keyWindow: NSWindow?](nsapplication/keywindow.md)
  The window that currently receives keyboard events.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/mainwindow)*