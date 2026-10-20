# enumerateWindows(options:using:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Executes a block for each of the app’s windows.

**Availability**:
- macOS 10.12+

## Declaration

```swift
func enumerateWindows(options: NSApplication.WindowListOptions = [], using block: (NSWindow, UnsafeMutablePointer<ObjCBool>) -> Void)
```

```objc
- (void) enumerateWindowsWithOptions:(NSWindowListOptions) options usingBlock:(void (^)(NSWindow *window, BOOL *stop)) block;
```

## Parameters

- `options`: A constant that indicates window ordering. See [`NSApplication.WindowListOptions`](./windowlistoptions.md) for possible values.
- `block`: The block to execute for each window. The block takes the following parameters:

  - **window**: The window for which to execute the block.
  - **stop**: A Boolean value that stops the enumeration early when set to [`true`](../../Swift/true.md) (the default value is [`false`](../../Swift/false.md)).

## See Also

### Managing App Windows
- [var keyWindow: NSWindow?](./keywindow.md)
  The window that currently receives keyboard events.
- [var mainWindow: NSWindow?](./mainwindow.md)
  The app’s main window.
- [func window(withWindowNumber: Int) -> NSWindow?](./window%28withwindownumber%29.md)
  Returns the window corresponding to the specified window number.
- [var windows: [NSWindow]](./windows.md)
  An array of the app’s window objects.
- [NSApplication.WindowListOptions](./windowlistoptions.md)
  This constant indicates a window ordering.
- [func makeWindowsPerform(Selector, inOrder: Bool) -> NSWindow?](./makewindowsperform%28_,inorder%29.md)
  Sends the specified message to each of the app’s window objects until one returns a non-`nil` value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/enumeratewindows(options:using:))*