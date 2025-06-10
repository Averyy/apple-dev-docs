# NSToolbarItemGroup

**Framework**: AppKit  
**Kind**: class

A group of subitems in a toolbar item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.5+

## Declaration

```swift
@MainActor
class NSToolbarItemGroup
```

#### Overview

An [`NSToolbarItemGroup`](nstoolbaritemgroup.md) represents a collection set of subitems in a toolbar that the system displays based on available space and settings that you specify. The system uses the views and labels of the subitems, but the parent’s attributes take precedence. This differs from other [`NSToolbarItem`](nstoolbaritem.md) objects because they’re attached — the user drags them together as a single item rather than separately.

If a subitem of the group has an action set on it, the group uses that action instead of its own when the user clicks or taps on that item. The system prefers the subitem’s action if it exists, otherwise it uses the group’s action.

To configure an instance of [`NSToolbarItemGroup`](nstoolbaritemgroup.md), you first create the individual toolbar subitems:

```objc
NSToolbarItem *item1 = [[NSToolbarItem alloc] initWithItemIdentifier:@"Item1"];
NSToolbarItem *item2 = [[NSToolbarItem alloc] initWithItemIdentifier:@"Item2"];
[item1 setImage:[NSImage imageNamed:@"LeftArrow"]];
[item2 setImage:[NSImage imageNamed:@"RightArrow"]];
[item1 setLabel:@"Prev"];
[item2 setLabel:@"Next"];
```

Then, you put them in a grouped item:

```objc
NSToolbarItemGroup *group = [[NSToolbarItemGroup alloc] initWithItemIdentifier:@"GroupItem"];
[group setSubitems:[NSArray arrayWithObjects:item1, item2, nil]];
```

In this configuration, you get two grouped items, and two labels.

If you set a label on the parent item, you get two grouped items with one shared label:

```objc
[group setLabel:@"Navigate"];
```

If instead you set a view on the parent item, you get two labels with one shared view:

```objc
[group setView:someSegmentedControl];
```

## Topics

### Creating grouped toolbar items
- [convenience init(itemIdentifier: NSToolbarItem.Identifier, images: [UIImage], selectionMode: NSToolbarItemGroup.SelectionMode, labels: [String]?, target: Any?, action: Selector?)](nstoolbaritemgroup/init(itemidentifier:images:selectionmode:labels:target:action:).md)
  Creates a grouped toolbar item with images.
- [convenience init(itemIdentifier: NSToolbarItem.Identifier, titles: [String], selectionMode: NSToolbarItemGroup.SelectionMode, labels: [String]?, target: Any?, action: Selector?)](nstoolbaritemgroup/init(itemidentifier:titles:selectionmode:labels:target:action:).md)
  Creates a grouped toolbar item with labels.
### Working with subitems
- [var subitems: [NSToolbarItem]](nstoolbaritemgroup/subitems.md)
  The subitems of the grouped toolbar item.
- [var selectedIndex: Int](nstoolbaritemgroup/selectedindex.md)
  The index value for the most recently selected subitem of a grouped toolbar item.
- [func isSelected(at: Int) -> Bool](nstoolbaritemgroup/isselected(at:).md)
  Indicates whether a specified index is currently selected.
- [func setSelected(Bool, at: Int)](nstoolbaritemgroup/setselected(_:at:).md)
  Sets the selected state of a subitem in a grouped toolbar item.
### Configuring grouped toolbar items
- [var controlRepresentation: NSToolbarItemGroup.ControlRepresentation](nstoolbaritemgroup/controlrepresentation-swift.property.md)
  A value that represents how a toolbar displays a grouped toolbar item.
- [NSToolbarItemGroup.ControlRepresentation](nstoolbaritemgroup/controlrepresentation-swift.enum.md)
- [var selectionMode: NSToolbarItemGroup.SelectionMode](nstoolbaritemgroup/selectionmode-swift.property.md)
  The selection mode of the grouped toolbar item.
- [NSToolbarItemGroup.SelectionMode](nstoolbaritemgroup/selectionmode-swift.enum.md)
  A value that indicates how a grouped toolbar item selects its subitems.

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
- [NSToolbarItemGroup.ControlRepresentation](nstoolbaritemgroup/controlrepresentation-swift.enum.md)
- [NSToolbarItemGroup.SelectionMode](nstoolbaritemgroup/selectionmode-swift.enum.md)
  A value that indicates how a grouped toolbar item selects its subitems.
- [class NSMenuToolbarItem](nsmenutoolbaritem.md)
  A control that presents a menu in a window’s toolbar.
- [class NSSearchToolbarItem](nssearchtoolbaritem.md)
  A toolbar item that contains a search field optimized for performing text-based searches.
- [class NSTrackingSeparatorToolbarItem](nstrackingseparatortoolbaritem.md)
  A toolbar separator that aligns with the vertical split view in the same window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritemgroup)*