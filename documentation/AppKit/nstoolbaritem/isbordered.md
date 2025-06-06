# isBordered

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the toolbar item has a bordered style.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
@MainActor
var isBordered: Bool { get set }
```

#### Discussion

If your toolbar item displays a custom view, modifying this property applies the image to the view’s [`isBordered`](nstoolbaritem/isbordered.md) property, if one exists. The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

> **Note**:  In macOS 12 and earlier, [`NSToolbarItem`](nstoolbaritem.md) doesn’t support custom views in Mac apps built with Mac Catalyst.

 In macOS 12 and earlier, [`NSToolbarItem`](nstoolbaritem.md) doesn’t support custom views in Mac apps built with Mac Catalyst.

## See Also

- [var isVisible: Bool](nstoolbaritem/isvisible.md)
  A Boolean value that indicates whether the item is currently visible in the toolbar, and not in the overflow menu.
- [var isNavigational: Bool](nstoolbaritem/isnavigational.md)
  A Boolean value that indicates whether the item behaves as a navigation item in the toolbar.
- [var isEnabled: Bool](nstoolbaritem/isenabled.md)
  A Boolean value that indicates whether the item is enabled.
- [var allowsDuplicatesInToolbar: Bool](nstoolbaritem/allowsduplicatesintoolbar.md)
  A Boolean value that indicates whether the toolbar item can appear more than once in a toolbar.
- [var visibilityPriority: NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.property.md)
  The display priority associated with the toolbar item.
- [NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.struct.md)
  Constants that indicate which toolbar items to keep in the toolbar when space is limited.
- [var tag: Int](nstoolbaritem/tag.md)
  An integer tag you can use to identify the toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/isbordered)*