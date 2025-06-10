# NSToolbarItem.Style

**Framework**: AppKit  
**Kind**: enum

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
enum Style
```

## Topics

### Enumeration Cases
- [NSToolbarItem.Style.plain](nstoolbaritem/style-swift.enum/plain.md)
- [NSToolbarItem.Style.prominent](nstoolbaritem/style-swift.enum/prominent.md)
### Initializers
- [init?(rawValue: Int)](nstoolbaritem/style-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
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
- [var style: NSToolbarItem.Style](nstoolbaritem/style-swift.property.md)
  Defines the toolbar item’s appearance. The default style is plain. Prominent style tints the background. If a background tint color is set, it uses it; otherwise, it uses the app’s or system’s accent color. If grouped with other items, it moves to its own to avoid tinting other items’ background.
- [var visibilityPriority: NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.property.md)
  The display priority associated with the toolbar item.
- [NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.struct.md)
  Constants that indicate which toolbar items to keep in the toolbar when space is limited.
- [var tag: Int](nstoolbaritem/tag.md)
  An integer tag you can use to identify the toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/style-swift.enum)*