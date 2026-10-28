# isVisible

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the item is currently visible in the toolbar, and not in the overflow menu.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+

## Declaration

```swift
var isVisible: Bool { get }
```

```objc
@property (readonly, getter=isVisible) BOOL visible;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) when the item is visible in the toolbar, and [`false`](../../Swift/false.md) when it isn’t in the toolbar or is present in the toolbar’s overflow menu. This property is key-value observing (KVO) compliant.

## See Also

### Getting the item’s configuration
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
- [NSToolbarItem.VisibilityPriority](./visibilitypriority-swift.struct.md)
  Constants that indicate which toolbar items to keep in the toolbar when space is limited.
- [var tag: Int](./tag.md)
  An integer tag you can use to identify the toolbar item.
- [badge](./badge-2b38p.md)
  A badge that can be attached to an NSToolbarItem. This provides a way to display small visual indicators that can be used to highlight important information, such as unread notifications or status indicators.
- [NSItemBadge](../nsitembadge-c.class.md)
  `NSItemBadge` represents a badge that can be attached to an `NSToolbarItem`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/isvisible)*