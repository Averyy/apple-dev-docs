# isNavigational

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the item behaves as a navigation item in the toolbar.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
var isNavigational: Bool { get set }
```

```objc
@property (getter=isNavigational) BOOL navigational;
```

## Discussion

Mark a toolbar item as navigation if you use it to navigate around your content. When you set this property to [`true`](../../Swift/true.md), the system can position navigation items outside of the normal list of items in the toolbar. For example, the back and forward buttons in Finder windows are navigational, and the system positions them at the leading edge of the window’s title area. Specify the initial order of the items using the [`toolbarDefaultItemIdentifiers(_:)`](../nstoolbardelegate/toolbardefaultitemidentifiers%28_%29.md) method of the toolbar delegate object.

## See Also

### Getting the item’s configuration
- [var isVisible: Bool](./isvisible.md)
  A Boolean value that indicates whether the item is currently visible in the toolbar, and not in the overflow menu.
- [var isHidden: Bool](./ishidden.md)
  Determines whether an item is visible in the toolbar.
- [var isBordered: Bool](./isbordered.md)
  A Boolean value that indicates whether the toolbar item has a bordered style.
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
- [NSToolbarItem.VisibilityPriority](./visibilitypriority-swift.struct.md)
  Constants that indicate which toolbar items to keep in the toolbar when space is limited.
- [var tag: Int](./tag.md)
  An integer tag you can use to identify the toolbar item.
- [badge](./badge-2b38p.md)
  A badge that can be attached to an NSToolbarItem. This provides a way to display small visual indicators that can be used to highlight important information, such as unread notifications or status indicators.
- [NSItemBadge](../nsitembadge-c.class.md)
  `NSItemBadge` represents a badge that can be attached to an `NSToolbarItem`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/isnavigational)*