# windows

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A collection of the windows that are currently grouped together by this window tab group.

**Availability**:
- macOS 10.13+

## Declaration

```swift
var windows: [NSWindow] { get }
```

```objc
@property (copy, readonly) NSArray<NSWindow *> * windows;
```

#### Discussion

The order of this array corresponds to the visual order of the tabs in this tab group, arranged from the leading edge of the tab bar to the trailing edge. You can monitor this property for changes using key-value observing.

## See Also

### Managing Tabbed Windows
- [var selectedWindow: NSWindow?](./selectedwindow.md)
  The selected, or frontmost, window in the tab group.
- [func addWindow(NSWindow)](./addwindow%28_%29.md)
  Adds a window to the tab group.
- [func insertWindow(NSWindow, at: Int)](./insertwindow%28_,at%29.md)
  Inserts a window at a specific location within the tab group.
- [func removeWindow(NSWindow)](./removewindow%28_%29.md)
  Removes a window from the tab group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtabgroup/windows)*