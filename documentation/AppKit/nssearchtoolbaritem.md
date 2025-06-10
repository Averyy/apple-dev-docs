# NSSearchToolbarItem

**Framework**: AppKit  
**Kind**: class

A toolbar item that contains a search field optimized for performing text-based searches.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@MainActor
class NSSearchToolbarItem
```

#### Overview

[`NSSearchToolbarItem`](nssearchtoolbaritem.md) automatically resizes to accommodate typing when the focus switches to the toolbar item. When the toolbar is low on space, the system may collapse the search item into a button representation, which then expands to a full search field when the user clicks on it.

## Topics

### Configuring a search item
- [var preferredWidthForSearchField: CGFloat](nssearchtoolbaritem/preferredwidthforsearchfield.md)
  The preferred width for the toolbar item when it has keyboard focus.
- [var resignsFirstResponderWithCancel: Bool](nssearchtoolbaritem/resignsfirstresponderwithcancel.md)
  A Boolean value that enables the cancel button in the search field to resign the first responder in addition to clearing the contents.
- [var searchField: NSSearchField](nssearchtoolbaritem/searchfield.md)
  The search field inside the toolbar item.
### Controlling search interactions
- [func beginSearchInteraction()](nssearchtoolbaritem/beginsearchinteraction.md)
  Starts a search interaction and moves the keyboard focus to the search field.
- [func endSearchInteraction()](nssearchtoolbaritem/endsearchinteraction.md)
  Ends a search interaction by giving up the first responder and adjusting the size of the search field to the available width for the toolbar item if necessary.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSToolbarItem](nstoolbaritem.md)
  A single item that appears in a window’s toolbar.
- [class NSToolbarItemGroup](nstoolbaritemgroup.md)
  A group of subitems in a toolbar item.
- [NSToolbarItemGroup.ControlRepresentation](nstoolbaritemgroup/controlrepresentation-swift.enum.md)
- [NSToolbarItemGroup.SelectionMode](nstoolbaritemgroup/selectionmode-swift.enum.md)
  A value that indicates how a grouped toolbar item selects its subitems.
- [class NSMenuToolbarItem](nsmenutoolbaritem.md)
  A control that presents a menu in a window’s toolbar.
- [class NSTrackingSeparatorToolbarItem](nstrackingseparatortoolbaritem.md)
  A toolbar separator that aligns with the vertical split view in the same window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssearchtoolbaritem)*