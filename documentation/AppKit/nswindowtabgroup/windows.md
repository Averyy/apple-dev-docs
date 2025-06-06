# windows

**Framework**: AppKit  
**Kind**: property

A collection of the windows that are currently grouped together by this window tab group.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var windows: [NSWindow] { get }
```

#### Discussion

The order of this array corresponds to the visual order of the tabs in this tab group, arranged from the leading edge of the tab bar to the trailing edge. You can monitor this property for changes using key-value observing.

## See Also

- [var selectedWindow: NSWindow?](nswindowtabgroup/selectedwindow.md)
  The selected, or frontmost, window in the tab group.
- [func addWindow(NSWindow)](nswindowtabgroup/addwindow(_:).md)
  Adds a window to the tab group.
- [func insertWindow(NSWindow, at: Int)](nswindowtabgroup/insertwindow(_:at:).md)
  Inserts a window at a specific location within the tab group.
- [func removeWindow(NSWindow)](nswindowtabgroup/removewindow(_:).md)
  Removes a window from the tab group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtabgroup/windows)*