# keyWindow

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The window that currently receives keyboard events.

**Availability**:
- macOS

## Declaration

```swift
weak var keyWindow: NSWindow? { get }
```

```objc
@property (weak, readonly, nullable) NSWindow * keyWindow;
```

#### Discussion

The value of this property is `nil` when there is no window receiving keyboard events. The property might be `nil` because the app’s storyboard file has not yet finished loading or when the receiver is not active.

## See Also

### Related Documentation
- [var isKeyWindow: Bool](../nswindow/iskeywindow.md)
  A Boolean value that indicates whether the window is the key window for the application.
### Managing App Windows
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
- [func makeWindowsPerform(Selector, inOrder: Bool) -> NSWindow?](./makewindowsperform%28_,inorder%29.md)
  Sends the specified message to each of the app’s window objects until one returns a non-`nil` value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/keywindow)*