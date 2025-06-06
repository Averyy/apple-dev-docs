# removeWindow(_:)

**Framework**: AppKit  
**Kind**: method

Removes a window from the tab group.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func removeWindow(_ window: NSWindow)
```

#### Discussion

You can use [`removeWindow(_:)`](nswindowtabgroup/removewindow(_:).md) to explicitly remove a window from the tab group. Windows are implicity removed from their associated tab groups when they order out.

## Parameters

- `window`: Raises an   if the window is not a member of the tab group.

## See Also

- [var windows: [NSWindow]](nswindowtabgroup/windows.md)
  A collection of the windows that are currently grouped together by this window tab group.
- [var selectedWindow: NSWindow?](nswindowtabgroup/selectedwindow.md)
  The selected, or frontmost, window in the tab group.
- [func addWindow(NSWindow)](nswindowtabgroup/addwindow(_:).md)
  Adds a window to the tab group.
- [func insertWindow(NSWindow, at: Int)](nswindowtabgroup/insertwindow(_:at:).md)
  Inserts a window at a specific location within the tab group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtabgroup/removewindow(_:))*