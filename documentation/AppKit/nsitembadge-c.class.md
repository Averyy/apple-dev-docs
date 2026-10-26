# NSItemBadge

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

`NSItemBadge` represents a badge that can be attached to an `NSToolbarItem`.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```objc
@interface NSItemBadge : NSObject
```

#### Overview

This badge provides a way to display small visual indicators, such as counts and text labels, within a toolbar item. Badges can be used to highlight important information, such as unread notifications or status indicators.

## Topics

### Instance Properties
- [text](./nsitembadge-c.class/text.md)
  The text to be displayed within the badge.
### Type Methods
- [+ badgeWithCount:](./nsitembadge-c.class/badgewithcount_.md)
  Creates a badge displaying a localized numerical count.
- [+ badgeWithText:](./nsitembadge-c.class/badgewithtext_.md)
  Creates a badge displaying a text.
- [+ indicatorBadge](./nsitembadge-c.class/indicatorbadge.md)
  Creates a badge styled as an indicator. In this context, an indicator is simply a badge without any text.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Getting the item’s configuration
- [var isVisible: Bool](./nstoolbaritem/isvisible.md)
  A Boolean value that indicates whether the item is currently visible in the toolbar, and not in the overflow menu.
- [var isHidden: Bool](./nstoolbaritem/ishidden.md)
  Determines whether an item is visible in the toolbar.
- [var isBordered: Bool](./nstoolbaritem/isbordered.md)
  A Boolean value that indicates whether the toolbar item has a bordered style.
- [var isNavigational: Bool](./nstoolbaritem/isnavigational.md)
  A Boolean value that indicates whether the item behaves as a navigation item in the toolbar.
- [var isEnabled: Bool](./nstoolbaritem/isenabled.md)
  A Boolean value that indicates whether the item is enabled.
- [badge](./nstoolbaritem/badge-2b38p.md)
  A badge that can be attached to an NSToolbarItem. This provides a way to display small visual indicators that can be used to highlight important information, such as unread notifications or status indicators.
- [var style: NSToolbarItem.Style](./nstoolbaritem/style-swift.property.md)
  Defines the toolbar item’s appearance. The default style is plain. Prominent style tints the background. If a background tint color is set, it uses it; otherwise, it uses the app’s or system’s accent color. If grouped with other items, it moves to its own to avoid tinting other items’ background.
- [NSToolbarItem.Style](./nstoolbaritem/style-swift.enum.md)
- [var visibilityPriority: NSToolbarItem.VisibilityPriority](./nstoolbaritem/visibilitypriority-swift.property.md)
  The display priority associated with the toolbar item.
- [NSToolbarItem.VisibilityPriority](./nstoolbaritem/visibilitypriority-swift.struct.md)
  Constants that indicate which toolbar items to keep in the toolbar when space is limited.
- [var tag: Int](./nstoolbaritem/tag.md)
  An integer tag you can use to identify the toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsitembadge-c.class)*