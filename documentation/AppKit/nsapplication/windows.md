# windows

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of the app’s window objects.

**Availability**:
- macOS

## Declaration

```swift
var windows: [NSWindow] { get }
```

```objc
@property (copy, readonly) NSArray<NSWindow *> * windows;
```

## Discussion

This property contains an array of [`NSWindow`](../nswindow.md) objects corresponding to all currently existing windows for the app. The array includes all onscreen and offscreen windows, whether or not they are visible on any space. There is no guarantee of the order of the windows in the array.

## See Also

### Managing App Windows
- [var keyWindow: NSWindow?](./keywindow.md)
  The window that currently receives keyboard events.
- [var mainWindow: NSWindow?](./mainwindow.md)
  The app’s main window.
- [func window(withWindowNumber: Int) -> NSWindow?](./window%28withwindownumber%29.md)
  Returns the window corresponding to the specified window number.
- [func enumerateWindows(options: NSApplication.WindowListOptions, using: (NSWindow, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratewindows%28options,using%29.md)
  Executes a block for each of the app’s windows.
- [NSApplication.WindowListOptions](./windowlistoptions.md)
  This constant indicates a window ordering.
- [func makeWindowsPerform(Selector, inOrder: Bool) -> NSWindow?](./makewindowsperform%28_,inorder%29.md)
  Sends the specified message to each of the app’s window objects until one returns a non-`nil` value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/windows)*