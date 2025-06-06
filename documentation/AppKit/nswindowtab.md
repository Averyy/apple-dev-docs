# NSWindowTab

**Framework**: AppKit  
**Kind**: class

A tab associated with a window that is part of a tabbing group.

**Availability**:
- macOS 10.13+

## Declaration

```swift
class NSWindowTab
```

#### Overview

[`NSWindowTab`](nswindowtab.md) describes the way a window displays as part of a tabbed window group. The properties of [`NSWindowTab`](nswindowtab.md) are configurable at any time, but only take effect when the associated [`NSWindow`](nswindow.md) displays in a tab.

AppKit automatically creates an instance of [`NSWindowTab`](nswindowtab.md) for each [`NSWindow`](nswindow.md). You can access a window’s tab object using the [`tab`](nswindow/tab.md) property.

## Topics

### Customizing the Title
- [var title: String!](nswindowtab/title.md)
  The title for the window tab.
- [var attributedTitle: NSAttributedString?](nswindowtab/attributedtitle.md)
  The title for the window tab, specified as an attributed string.
### Customizing the Tooltip
- [var toolTip: String!](nswindowtab/tooltip.md)
  The tooltip for this window tab.
### Adding an Accessory View
- [var accessoryView: NSView?](nswindowtab/accessoryview.md)
  An optional accessory view for the tab.

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

- [var tabbingIdentifier: NSWindow.TabbingIdentifier](nswindow/tabbingidentifier-swift.property.md)
  A value that allows a group of related windows.
- [class NSWindow](nswindow.md)
  A window that an app displays on the screen.
- [class NSPanel](nspanel.md)
  A special kind of window that typically performs a function that is auxiliary to the main window.
- [protocol NSWindowDelegate](nswindowdelegate.md)
  A set of optional methods that a window’s delegate can implement to respond to events, such as window resizing, moving, exposing, and minimizing.
- [class NSWindowTabGroup](nswindowtabgroup.md)
  A group of windows that display together as a single tabbed window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindowtab)*