# tag

**Framework**: AppKit  
**Kind**: property

An integer tag you can use to identify the toolbar item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
var tag: Int { get set }
```

#### Discussion

The toolbar doesn’t use this value. You can use it for your own custom purposes.

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
- [NSToolbarItem.Style](nstoolbaritem/style-swift.enum.md)
- [var visibilityPriority: NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.property.md)
  The display priority associated with the toolbar item.
- [NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.struct.md)
  Constants that indicate which toolbar items to keep in the toolbar when space is limited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/tag)*