# NSTrackingSeparatorToolbarItem

**Framework**: AppKit  
**Kind**: class

A toolbar separator that aligns with the vertical split view in the same window.

**Availability**:
- macOS 11.0+

## Declaration

```swift
@MainActor
class NSTrackingSeparatorToolbarItem
```

#### Overview

Use a `NSTrackingSeparatorToolbarItem` to divide an [`NSToolbar`](nstoolbar.md) into sections that visually align with the views on either side of the divider of the [`splitView`](nstrackingseparatortoolbaritem/splitview.md). This keeps [`NSToolbarItem`](nstoolbaritem.md)s above the content that’s the [`target`](nstoolbaritem/target.md) for the item’s [`target`](nstoolbaritem/target.md).

The `splitView` must be in the same window as the toolbar containing this item before showing the toolbar.

## Topics

### Creating a tracking separator
- [convenience init(identifier: NSToolbarItem.Identifier, splitView: NSSplitView, dividerIndex: Int)](nstrackingseparatortoolbaritem/init(identifier:splitview:dividerindex:).md)
  Creates a new tracking separator toolbar item and configures it to align with the divider of the split view.
### configuring a tracking separator
- [var dividerIndex: Int](nstrackingseparatortoolbaritem/dividerindex.md)
  The index of the split view divider to align with the tracking separator.
- [var splitView: NSSplitView](nstrackingseparatortoolbaritem/splitview.md)
  The vertical split view to align with the toolbar separator.

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
- [class NSSearchToolbarItem](nssearchtoolbaritem.md)
  A toolbar item that contains a search field optimized for performing text-based searches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstrackingseparatortoolbaritem)*