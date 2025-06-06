# window(withWindowNumber:)

**Framework**: AppKit  
**Kind**: method

Returns the window corresponding to the specified window number.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func window(withWindowNumber windowNum: Int) -> NSWindow?
```

#### Return Value

The desired window object or `nil` if the window could not be found.

#### Discussion

[`window(withWindowNumber:)`](nsapplication/window(withwindownumber:).md) may return `nil` for window numbers found using [`windowNumbers(options:)`](nswindow/windownumbers(options:).md) if there is no corresponding window object owned by your app—for example, the menu bar.

## Parameters

- `windowNum`: The unique window number associated with the desired   object.

## See Also

- [var keyWindow: NSWindow?](nsapplication/keywindow.md)
  The window that currently receives keyboard events.
- [var mainWindow: NSWindow?](nsapplication/mainwindow.md)
  The app’s main window.
- [var windows: [NSWindow]](nsapplication/windows.md)
  An array of the app’s window objects.
- [func makeWindowsPerform(Selector, inOrder: Bool) -> NSWindow?](nsapplication/makewindowsperform(_:inorder:).md)
  Sends the specified message to each of the app’s window objects until one returns a non-`nil` value.
- [func enumerateWindows(options: NSApplication.WindowListOptions, using: (NSWindow, UnsafeMutablePointer<ObjCBool>) -> Void)](nsapplication/enumeratewindows(options:using:).md)
  Executes a block for each of the app’s windows.
- [NSApplication.WindowListOptions](nsapplication/windowlistoptions.md)
  This constant indicates a window ordering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/window(withwindownumber:))*