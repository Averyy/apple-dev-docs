# isVisible

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the item is currently visible in the toolbar, and not in the overflow menu.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+

## Declaration

```swift
@MainActor
var isVisible: Bool { get }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) when the item is visible in the toolbar, and [`false`](https://developer.apple.com/documentation/swift/false) when it isn’t in the toolbar or is present in the toolbar’s overflow menu. This property is key-value observing (KVO) compliant.

## See Also

- [var isHidden: Bool](nstoolbaritem/ishidden.md)
- [var isBordered: Bool](nstoolbaritem/isbordered.md)
  A Boolean value that indicates whether the toolbar item has a bordered style.
- [var isNavigational: Bool](nstoolbaritem/isnavigational.md)
  A Boolean value that indicates whether the item behaves as a navigation item in the toolbar.
- [var isEnabled: Bool](nstoolbaritem/isenabled.md)
  A Boolean value that indicates whether the item is enabled.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/isvisible)*