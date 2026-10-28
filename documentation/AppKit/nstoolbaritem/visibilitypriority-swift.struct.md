# NSToolbarItem.VisibilityPriority

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that indicate which toolbar items to keep in the toolbar when space is limited.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
struct VisibilityPriority
```

```c
typedef NSInteger NSToolbarItemVisibilityPriority;
```

## Overview

When a toolbar doesn’t have enough space to fit all its items, it pushes items into the overflow menu to make space. Use these constants to suggest a priority for individual toolbar items. The toolbar pushes low-priority items to the overflow menu first, followed by standard items and high-priority items. When two or more items share the same priority, the toolbar pushes the one closest to the trailing edge first.

## Topics

### Visibility priorities
- [static var standard: NSToolbarItem.VisibilityPriority](./visibilitypriority-swift.struct/standard.md)
  The default visibility priority.
- [static var low: NSToolbarItem.VisibilityPriority](./visibilitypriority-swift.struct/low.md)
  The lowest-priority for a toolbar item.
- [static var high: NSToolbarItem.VisibilityPriority](./visibilitypriority-swift.struct/high.md)
  A high priority that makes it less likely for the toolbar item to move to the overflow item.
- [static var user: NSToolbarItem.VisibilityPriority](./visibilitypriority-swift.struct/user.md)
  The highest priority for items in the toolbar.
### Initializers
- [init(Int)](./visibilitypriority-swift.struct/init%28_%29.md)
  Creates a visibility priority structure.
- [init(rawValue: Int)](./visibilitypriority-swift.struct/init%28rawvalue%29.md)
  Creates a visibility priority structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Comparable](../../Swift/comparable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the item’s configuration
- [var isVisible: Bool](./isvisible.md)
  A Boolean value that indicates whether the item is currently visible in the toolbar, and not in the overflow menu.
- [var isHidden: Bool](./ishidden.md)
  Determines whether an item is visible in the toolbar.
- [var isBordered: Bool](./isbordered.md)
  A Boolean value that indicates whether the toolbar item has a bordered style.
- [var isNavigational: Bool](./isnavigational.md)
  A Boolean value that indicates whether the item behaves as a navigation item in the toolbar.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that indicates whether the item is enabled.
- [var badge: NSItemBadge?](./badge-17r3r.md)
  A badge that can be attached to an NSToolbarItem. This provides a way to display small visual indicators that can be used to highlight important information, such as unread notifications or status indicators.
- [struct NSItemBadge](../nsitembadge-swift.struct.md)
  `NSItemBadge` represents a badge that can be attached to an `NSToolbarItem`.
- [var style: NSToolbarItem.Style](./style-swift.property.md)
  Defines the toolbar item’s appearance. The default style is plain. Prominent style tints the background. If a background tint color is set, it uses it; otherwise, it uses the app’s or system’s accent color. If grouped with other items, it moves to its own to avoid tinting other items’ background.
- [NSToolbarItem.Style](./style-swift.enum.md)
- [var visibilityPriority: NSToolbarItem.VisibilityPriority](./visibilitypriority-swift.property.md)
  The display priority associated with the toolbar item.
- [var tag: Int](./tag.md)
  An integer tag you can use to identify the toolbar item.
- [badge](./badge-2b38p.md)
  A badge that can be attached to an NSToolbarItem. This provides a way to display small visual indicators that can be used to highlight important information, such as unread notifications or status indicators.
- [NSItemBadge](../nsitembadge-c.class.md)
  `NSItemBadge` represents a badge that can be attached to an `NSToolbarItem`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/visibilitypriority-swift.struct)*