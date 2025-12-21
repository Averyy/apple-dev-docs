# NSToolbarItem.VisibilityPriority

**Framework**: AppKit  
**Kind**: struct

Constants that indicate which toolbar items to keep in the toolbar when space is limited.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
struct VisibilityPriority
```

#### Overview

When a toolbar doesn’t have enough space to fit all its items, it pushes items into the overflow menu to make space. Use these constants to suggest a priority for individual toolbar items. The toolbar pushes low-priority items to the overflow menu first, followed by standard items and high-priority items. When two or more items share the same priority, the toolbar pushes the one closest to the trailing edge first.

## Topics

### Visibility priorities
- [static let standard: NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.struct/standard.md)
  The default visibility priority.
- [static let low: NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.struct/low.md)
  The lowest-priority for a toolbar item.
- [static let high: NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.struct/high.md)
  A high priority that makes it less likely for the toolbar item to move to the overflow item.
- [static let user: NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.struct/user.md)
  The highest priority for items in the toolbar.
### Initializers
- [init(Int)](nstoolbaritem/visibilitypriority-swift.struct/init(_:).md)
  Creates a visibility priority structure.
- [init(rawValue: Int)](nstoolbaritem/visibilitypriority-swift.struct/init(rawvalue:).md)
  Creates a visibility priority structure with the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Comparable](../Swift/Comparable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isVisible: Bool](nstoolbaritem/isvisible.md)
  A Boolean value that indicates whether the item is currently visible in the toolbar, and not in the overflow menu.
- [var isHidden: Bool](nstoolbaritem/ishidden.md)
- [var isBordered: Bool](nstoolbaritem/isbordered.md)
  A Boolean value that indicates whether the toolbar item has a bordered style.
- [var isNavigational: Bool](nstoolbaritem/isnavigational.md)
  A Boolean value that indicates whether the item behaves as a navigation item in the toolbar.
- [var isEnabled: Bool](nstoolbaritem/isenabled.md)
  A Boolean value that indicates whether the item is enabled.
- [var badge: NSItemBadge?](nstoolbaritem/badge-17r3r.md)
  A badge that can be attached to an NSToolbarItem. This provides a way to display small visual indicators that can be used to highlight important information, such as unread notifications or status indicators.
- [struct NSItemBadge](nsitembadge-swift.struct.md)
  `NSItemBadge` represents a badge that can be attached to an `NSToolbarItem`.
- [var style: NSToolbarItem.Style](nstoolbaritem/style-swift.property.md)
  Defines the toolbar item’s appearance. The default style is plain. Prominent style tints the background. If a background tint color is set, it uses it; otherwise, it uses the app’s or system’s accent color. If grouped with other items, it moves to its own to avoid tinting other items’ background.
- [NSToolbarItem.Style](nstoolbaritem/style-swift.enum.md)
- [var visibilityPriority: NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.property.md)
  The display priority associated with the toolbar item.
- [var tag: Int](nstoolbaritem/tag.md)
  An integer tag you can use to identify the toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/visibilitypriority-swift.struct)*