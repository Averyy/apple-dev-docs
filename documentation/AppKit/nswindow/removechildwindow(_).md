# removeChildWindow(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Detaches a given child window from the window.

**Availability**:
- macOS

## Declaration

```swift
func removeChildWindow(_ childWin: NSWindow)
```

```objc
- (void) removeChildWindow:(NSWindow *) childWin;
```

## Parameters

- `childWin`: The child window to detach.

## See Also

### Managing Attached Windows
- [var childWindows: [NSWindow]?](./childwindows.md)
  An array of the window’s attached child windows.
- [func addChildWindow(NSWindow, ordered: NSWindow.OrderingMode)](./addchildwindow%28_,ordered%29.md)
  Adds a given window as a child window of the window.
- [var parent: NSWindow?](./parent.md)
  The parent window to which the window is attached as a child.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/removechildwindow(_:))*