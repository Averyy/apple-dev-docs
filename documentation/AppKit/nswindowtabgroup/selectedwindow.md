# selectedWindow

**Framework**: AppKit  
**Kind**: property

The selected, or frontmost, window in the tab group.

**Availability**:
- macOS 10.13+

## Declaration

```swift
weak var selectedWindow: NSWindow? { get set }
```

#### Discussion

This property returns the currently selected window within the tabbed window group. Setting this property visually changes the selected tab.

> ❗ **Important**:  This property raises an exception if set to a window that is not already a member of the tab group.

You can monitor this property for changes using key-value observing.

## See Also

- [var windows: [NSWindow]](nswindowtabgroup/windows.md)
  A collection of the windows that are currently grouped together by this window tab group.
- [func addWindow(NSWindow)](nswindowtabgroup/addwindow(_:).md)
  Adds a window to the tab group.
- [func insertWindow(NSWindow, at: Int)](nswindowtabgroup/insertwindow(_:at:).md)
  Inserts a window at a specific location within the tab group.
- [func removeWindow(NSWindow)](nswindowtabgroup/removewindow(_:).md)
  Removes a window from the tab group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtabgroup/selectedwindow)*