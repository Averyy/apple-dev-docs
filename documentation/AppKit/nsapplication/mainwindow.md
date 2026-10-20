# mainWindow

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The app’s main window.

**Availability**:
- macOS

## Declaration

```swift
weak var mainWindow: NSWindow? { get }
```

```objc
@property (weak, readonly, nullable) NSWindow * mainWindow;
```

#### Discussion

The value in this property is `nil` when the app’s storyboard or nib file has not yet finished loading. It might also be `nil` when the app is inactive or hidden.

## See Also

### Related Documentation
- [var isMainWindow: Bool](../nswindow/ismainwindow.md)
  A Boolean value that indicates whether the window is the application’s main window.
### Managing App Windows
- [var keyWindow: NSWindow?](./keywindow.md)
  The window that currently receives keyboard events.
- [func window(withWindowNumber: Int) -> NSWindow?](./window%28withwindownumber%29.md)
  Returns the window corresponding to the specified window number.
- [var windows: [NSWindow]](./windows.md)
  An array of the app’s window objects.
- [func enumerateWindows(options: NSApplication.WindowListOptions, using: (NSWindow, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratewindows%28options,using%29.md)
  Executes a block for each of the app’s windows.
- [NSApplication.WindowListOptions](./windowlistoptions.md)
  This constant indicates a window ordering.
- [func makeWindowsPerform(Selector, inOrder: Bool) -> NSWindow?](./makewindowsperform%28_,inorder%29.md)
  Sends the specified message to each of the app’s window objects until one returns a non-`nil` value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/mainwindow)*