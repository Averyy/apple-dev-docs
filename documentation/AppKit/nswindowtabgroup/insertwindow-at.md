# insertWindow(_:at:)

**Framework**: AppKit  
**Kind**: method

Inserts a window at a specific location within the tab group.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func insertWindow(_ window: NSWindow, at index: Int)
```

#### Discussion

Inserts the window at the specified location within the tab group. If the window is already a member of another tab group, it is first removed from that group.

## Parameters

- `window`: The window to insert into the tab group.
- `index`: Raises an   if the index is negative or larger than the number of tabs in the group.

## See Also

- [var windows: [NSWindow]](nswindowtabgroup/windows.md)
  A collection of the windows that are currently grouped together by this window tab group.
- [var selectedWindow: NSWindow?](nswindowtabgroup/selectedwindow.md)
  The selected, or frontmost, window in the tab group.
- [func addWindow(NSWindow)](nswindowtabgroup/addwindow(_:).md)
  Adds a window to the tab group.
- [func removeWindow(NSWindow)](nswindowtabgroup/removewindow(_:).md)
  Removes a window from the tab group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtabgroup/insertwindow(_:at:))*