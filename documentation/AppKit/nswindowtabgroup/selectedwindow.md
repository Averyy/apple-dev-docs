# selectedWindow

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The selected, or frontmost, window in the tab group.

**Availability**:
- macOS 10.13+

## Declaration

```swift
weak var selectedWindow: NSWindow? { get set }
```

```objc
@property (weak) NSWindow * selectedWindow;
```

## Discussion

This property returns the currently selected window within the tabbed window group. Setting this property visually changes the selected tab.

> ❗ **Important**:  This property raises an exception if set to a window that is not already a member of the tab group.

You can monitor this property for changes using key-value observing.

## See Also

### Managing Tabbed Windows
- [var windows: [NSWindow]](./windows.md)
  A collection of the windows that are currently grouped together by this window tab group.
- [func addWindow(NSWindow)](./addwindow%28_%29.md)
  Adds a window to the tab group.
- [func insertWindow(NSWindow, at: Int)](./insertwindow%28_,at%29.md)
  Inserts a window at a specific location within the tab group.
- [func removeWindow(NSWindow)](./removewindow%28_%29.md)
  Removes a window from the tab group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtabgroup/selectedwindow)*