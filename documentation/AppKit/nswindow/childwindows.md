# childWindows

**Framework**: AppKit  
**Kind**: property

An array of the window’s attached child windows.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var childWindows: [NSWindow]? { get }
```

## See Also

- [func addChildWindow(NSWindow, ordered: NSWindow.OrderingMode)](nswindow/addchildwindow(_:ordered:).md)
  Adds a given window as a child window of the window.
- [func removeChildWindow(NSWindow)](nswindow/removechildwindow(_:).md)
  Detaches a given child window from the window.
- [var parent: NSWindow?](nswindow/parent.md)
  The parent window to which the window is attached as a child.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/childwindows)*