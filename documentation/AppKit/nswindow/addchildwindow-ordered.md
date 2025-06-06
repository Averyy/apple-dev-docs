# addChildWindow(_:ordered:)

**Framework**: AppKit  
**Kind**: method

Adds a given window as a child window of the window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func addChildWindow(_ childWin: NSWindow, ordered place: NSWindow.OrderingMode)
```

#### Discussion

After the `childWin` is added as a child of the window, it is maintained in relative position indicated by `place` for subsequent ordering operations involving either window. While this attachment is active, moving `childWin` will not cause the window to move (as in sliding a drawer in or out), but moving the window will cause `childWin` to move.

Note that you should not create cycles between parent and child windows. For example, you should not add window B as child of window A, then add window A as a child of window B.

## Parameters

- `childWin`: The child window to order.
- `place`: -  :   is ordered immediately in front of the window.

## See Also

- [var childWindows: [NSWindow]?](nswindow/childwindows.md)
  An array of the window’s attached child windows.
- [func removeChildWindow(NSWindow)](nswindow/removechildwindow(_:).md)
  Detaches a given child window from the window.
- [var parent: NSWindow?](nswindow/parent.md)
  The parent window to which the window is attached as a child.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/addchildwindow(_:ordered:))*