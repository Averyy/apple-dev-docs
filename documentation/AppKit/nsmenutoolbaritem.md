# NSMenuToolbarItem

**Framework**: AppKit  
**Kind**: class

A control that presents a menu in a window’s toolbar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
@MainActor
class NSMenuToolbarItem
```

#### Overview

If you set an action on an [`NSMenuToolbarItem`](nsmenutoolbaritem.md) control item, the user invokes the action when clicking on the item through pressing and holding to display the menu. If you set an action on the item and [`showsIndicator`](nsmenutoolbaritem/showsindicator.md) to [`true`](https://developer.apple.com/documentation/swift/true), the system displays the indicator as a separate segment so the user can invoke the menu with a click on that segment.

If you don’t set an action on the [`NSMenuToolbarItem`](nsmenutoolbaritem.md), a simple click invokes the menu, and the indicator is purely decorative.

## Topics

### Configuring a menu toolbar item
- [var showsIndicator: Bool](nsmenutoolbaritem/showsindicator.md)
  A Boolean value that determines whether the toolbar item displays an indicator of additional functionality.
- [var menu: NSMenu](nsmenutoolbaritem/menu.md)
  The menu presented from the toolbar item.
- [var itemMenu: UIMenu](nsmenutoolbaritem/itemmenu.md)

## Relationships

### Inherits From
- [NSToolbarItem](nstoolbaritem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMenuItemValidation](nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSValidatedUserInterfaceItem](nsvalidateduserinterfaceitem.md)

## See Also

- [class NSToolbarItem](nstoolbaritem.md)
  A single item that appears in a window’s toolbar.
- [class NSToolbarItemGroup](nstoolbaritemgroup.md)
  A group of subitems in a toolbar item.
- [NSToolbarItemGroup.ControlRepresentation](nstoolbaritemgroup/controlrepresentation-swift.enum.md)
- [NSToolbarItemGroup.SelectionMode](nstoolbaritemgroup/selectionmode-swift.enum.md)
  A value that indicates how a grouped toolbar item selects its subitems.
- [class NSSearchToolbarItem](nssearchtoolbaritem.md)
  A toolbar item that contains a search field optimized for performing text-based searches.
- [class NSTrackingSeparatorToolbarItem](nstrackingseparatortoolbaritem.md)
  A toolbar separator that aligns with the vertical split view in the same window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenutoolbaritem)*