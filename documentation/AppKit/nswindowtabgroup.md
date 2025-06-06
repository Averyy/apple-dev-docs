# NSWindowTabGroup

**Framework**: AppKit  
**Kind**: class

A group of windows that display together as a single tabbed window.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class NSWindowTabGroup
```

#### Overview

AppKit automatically creates instances of [`NSWindowTabGroup`](nswindowtabgroup.md) to reflect the tabbing state of your windows. You can access a window’s current tab group using the [`tabGroup`](nswindow/tabgroup.md) property.

## Topics

### Checking the Group Identifier
- [var identifier: NSWindow.TabbingIdentifier](nswindowtabgroup/identifier.md)
  The unique identifier for a tabbed window group.
### Configuring the Tab User Interface
- [var isOverviewVisible: Bool](nswindowtabgroup/isoverviewvisible.md)
  A Boolean value indicating if the tab overview is currently displayed.
- [var isTabBarVisible: Bool](nswindowtabgroup/istabbarvisible.md)
  A Boolean value indicating whether the tabbed window group currently displays a tab bar.
### Managing Tabbed Windows
- [var windows: [NSWindow]](nswindowtabgroup/windows.md)
  A collection of the windows that are currently grouped together by this window tab group.
- [var selectedWindow: NSWindow?](nswindowtabgroup/selectedwindow.md)
  The selected, or frontmost, window in the tab group.
- [func addWindow(NSWindow)](nswindowtabgroup/addwindow(_:).md)
  Adds a window to the tab group.
- [func insertWindow(NSWindow, at: Int)](nswindowtabgroup/insertwindow(_:at:).md)
  Inserts a window at a specific location within the tab group.
- [func removeWindow(NSWindow)](nswindowtabgroup/removewindow(_:).md)
  Removes a window from the tab group.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var tabGroup: NSWindowTabGroup?](nswindow/tabgroup.md)
  A group of windows that display together as a tab group.
- [class NSWindow](nswindow.md)
  A window that an app displays on the screen.
- [class NSPanel](nspanel.md)
  A special kind of window that typically performs a function that is auxiliary to the main window.
- [protocol NSWindowDelegate](nswindowdelegate.md)
  A set of optional methods that a window’s delegate can implement to respond to events, such as window resizing, moving, exposing, and minimizing.
- [class NSWindowTab](nswindowtab.md)
  A tab associated with a window that is part of a tabbing group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtabgroup)*