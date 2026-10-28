# window(withWindowNumber:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the window corresponding to the specified window number.

**Availability**:
- macOS

## Declaration

```swift
func window(withWindowNumber windowNum: Int) -> NSWindow?
```

```objc
- (NSWindow *) windowWithWindowNumber:(NSInteger) windowNum;
```

## Return Value

The desired window object or `nil` if the window could not be found.

## Discussion

[`window(withWindowNumber:)`](./window%28withwindownumber%29.md) may return `nil` for window numbers found using [`windowNumbers(options:)`](../nswindow/windownumbers%28options%29.md) if there is no corresponding window object owned by your app—for example, the menu bar.

## Parameters

- `windowNum`: The unique window number associated with the desired [`NSWindow`](../nswindow.md) object.

## See Also

### Managing App Windows
- [var keyWindow: NSWindow?](./keywindow.md)
  The window that currently receives keyboard events.
- [var mainWindow: NSWindow?](./mainwindow.md)
  The app’s main window.
- [var windows: [NSWindow]](./windows.md)
  An array of the app’s window objects.
- [func enumerateWindows(options: NSApplication.WindowListOptions, using: (NSWindow, UnsafeMutablePointer<ObjCBool>) -> Void)](./enumeratewindows%28options,using%29.md)
  Executes a block for each of the app’s windows.
- [NSApplication.WindowListOptions](./windowlistoptions.md)
  This constant indicates a window ordering.
- [func makeWindowsPerform(Selector, inOrder: Bool) -> NSWindow?](./makewindowsperform%28_,inorder%29.md)
  Sends the specified message to each of the app’s window objects until one returns a non-`nil` value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/window(withwindownumber:))*