# insertWindow(_:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts a window at a specific location within the tab group.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func insertWindow(_ window: NSWindow, at index: Int)
```

```objc
- (void) insertWindow:(NSWindow *) window atIndex:(NSInteger) index;
```

#### Discussion

Inserts the window at the specified location within the tab group. If the window is already a member of another tab group, it is first removed from that group.

## Parameters

- `window`: The window to insert into the tab group.
- `index`: The location in the tab group at which to insert window. This value must not be negative, and must not be greater than the number of windows in the tab group.

  Raises an `NSInternalInconsistencyException` if the index is negative or larger than the number of tabs in the group.

## See Also

### Managing Tabbed Windows
- [var windows: [NSWindow]](./windows.md)
  A collection of the windows that are currently grouped together by this window tab group.
- [var selectedWindow: NSWindow?](./selectedwindow.md)
  The selected, or frontmost, window in the tab group.
- [func addWindow(NSWindow)](./addwindow%28_%29.md)
  Adds a window to the tab group.
- [func removeWindow(NSWindow)](./removewindow%28_%29.md)
  Removes a window from the tab group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtabgroup/insertwindow(_:at:))*