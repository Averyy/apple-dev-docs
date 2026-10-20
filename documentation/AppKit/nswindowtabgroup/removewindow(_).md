# removeWindow(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes a window from the tab group.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func removeWindow(_ window: NSWindow)
```

```objc
- (void) removeWindow:(NSWindow *) window;
```

#### Discussion

You can use [`removeWindow(_:)`](./removewindow%28_%29.md) to explicitly remove a window from the tab group. Windows are implicity removed from their associated tab groups when they order out.

## Parameters

- `window`: The window to remove from the tab group. This window must already be a member of the tab group.

  Raises an `NSInternalInconsistencyException` if the window is not a member of the tab group.

## See Also

### Managing Tabbed Windows
- [var windows: [NSWindow]](./windows.md)
  A collection of the windows that are currently grouped together by this window tab group.
- [var selectedWindow: NSWindow?](./selectedwindow.md)
  The selected, or frontmost, window in the tab group.
- [func addWindow(NSWindow)](./addwindow%28_%29.md)
  Adds a window to the tab group.
- [func insertWindow(NSWindow, at: Int)](./insertwindow%28_,at%29.md)
  Inserts a window at a specific location within the tab group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtabgroup/removewindow(_:))*