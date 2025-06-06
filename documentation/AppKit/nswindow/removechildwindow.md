# removeChildWindow(_:)

**Framework**: AppKit  
**Kind**: method

Detaches a given child window from the window.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeChildWindow(_ childWin: NSWindow)
```

## Parameters

- `childWin`: The child window to detach.

## See Also

- [var childWindows: [NSWindow]?](nswindow/childwindows.md)
  An array of the window’s attached child windows.
- [func addChildWindow(NSWindow, ordered: NSWindow.OrderingMode)](nswindow/addchildwindow(_:ordered:).md)
  Adds a given window as a child window of the window.
- [var parent: NSWindow?](nswindow/parent.md)
  The parent window to which the window is attached as a child.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/removechildwindow(_:))*