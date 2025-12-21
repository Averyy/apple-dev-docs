# NSItemBadge

**Framework**: AppKit  
**Kind**: struct

`NSItemBadge` represents a badge that can be attached to an `NSToolbarItem`.

**Availability**:
- Mac Catalyst ?+
- macOS 26.0+

## Declaration

```swift
struct NSItemBadge
```

#### Overview

This badge provides a way to display small visual indicators, such as counts and text labels, within a toolbar item. Badges can be used to highlight important information, such as unread notifications or status indicators.

## Topics

### Instance Properties
- [var text: String](nsitembadge-swift.struct/text.md)
  The text to be displayed within the badge.
### Type Properties
- [static var indicator: NSItemBadge](nsitembadge-swift.struct/indicator.md)
  Creates a badge styled as an indicator. In this context, an indicator is simply a badge without any text.
### Type Methods
- [static func count(Int) -> NSItemBadge](nsitembadge-swift.struct/count(_:).md)
  Creates a badge displaying a localized numerical count.
- [static func text(String) -> NSItemBadge](nsitembadge-swift.struct/text(_:).md)
  Creates a badge displaying a text.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)

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
- [var style: NSToolbarItem.Style](nstoolbaritem/style-swift.property.md)
  Defines the toolbar item’s appearance. The default style is plain. Prominent style tints the background. If a background tint color is set, it uses it; otherwise, it uses the app’s or system’s accent color. If grouped with other items, it moves to its own to avoid tinting other items’ background.
- [NSToolbarItem.Style](nstoolbaritem/style-swift.enum.md)
- [var visibilityPriority: NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.property.md)
  The display priority associated with the toolbar item.
- [NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.struct.md)
  Constants that indicate which toolbar items to keep in the toolbar when space is limited.
- [var tag: Int](nstoolbaritem/tag.md)
  An integer tag you can use to identify the toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsitembadge-swift.struct)*