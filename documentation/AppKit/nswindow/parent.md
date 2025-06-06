# parent

**Framework**: AppKit  
**Kind**: property

The parent window to which the window is attached as a child.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var parent: NSWindow? { get set }
```

#### Discussion

This property should be set from a subclass when it is overridden by a subclass’s implementation. It should not be set otherwise.

Note that calling [`orderOut(_:)`](nswindow/orderout(_:).md) on a child window causes the window to be removed from its parent window before it is itself removed.

## See Also

- [var childWindows: [NSWindow]?](nswindow/childwindows.md)
  An array of the window’s attached child windows.
- [func addChildWindow(NSWindow, ordered: NSWindow.OrderingMode)](nswindow/addchildwindow(_:ordered:).md)
  Adds a given window as a child window of the window.
- [func removeChildWindow(NSWindow)](nswindow/removechildwindow(_:).md)
  Detaches a given child window from the window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/parent)*