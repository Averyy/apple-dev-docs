# addWindow(_:)

**Framework**: AppKit  
**Kind**: method

Adds a window to the tab group.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func addWindow(_ window: NSWindow)
```

#### Discussion

This method appends the window to the end of the tab group. If the window is already a member of another tab group, it is first removed from that group.

## Parameters

- `window`: The window to append to the tab group.

## See Also

- [var windows: [NSWindow]](nswindowtabgroup/windows.md)
  A collection of the windows that are currently grouped together by this window tab group.
- [var selectedWindow: NSWindow?](nswindowtabgroup/selectedwindow.md)
  The selected, or frontmost, window in the tab group.
- [func insertWindow(NSWindow, at: Int)](nswindowtabgroup/insertwindow(_:at:).md)
  Inserts a window at a specific location within the tab group.
- [func removeWindow(NSWindow)](nswindowtabgroup/removewindow(_:).md)
  Removes a window from the tab group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtabgroup/addwindow(_:))*