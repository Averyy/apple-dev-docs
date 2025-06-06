# allowsDuplicatesInToolbar

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the toolbar item can appear more than once in a toolbar.

**Availability**:
- macOS 10.0+

## Declaration

```swift
@MainActor
var allowsDuplicatesInToolbar: Bool { get }
```

#### Discussion

If the value in this property is [`true`](https://developer.apple.com/documentation/swift/true), the toolbar allows someone to drag more than one copy of the toolbar item from the customization palette. If the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), the toolbar prevents someone from dragging more than one copy of the item from the customization palette.

By default, if an item with the same identifier is already in the toolbar, dragging it in again will effectively move it to the new position.

## See Also

- [var isVisible: Bool](nstoolbaritem/isvisible.md)
  A Boolean value that indicates whether the item is currently visible in the toolbar, and not in the overflow menu.
- [var isBordered: Bool](nstoolbaritem/isbordered.md)
  A Boolean value that indicates whether the toolbar item has a bordered style.
- [var isNavigational: Bool](nstoolbaritem/isnavigational.md)
  A Boolean value that indicates whether the item behaves as a navigation item in the toolbar.
- [var isEnabled: Bool](nstoolbaritem/isenabled.md)
  A Boolean value that indicates whether the item is enabled.
- [var visibilityPriority: NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.property.md)
  The display priority associated with the toolbar item.
- [NSToolbarItem.VisibilityPriority](nstoolbaritem/visibilitypriority-swift.struct.md)
  Constants that indicate which toolbar items to keep in the toolbar when space is limited.
- [var tag: Int](nstoolbaritem/tag.md)
  An integer tag you can use to identify the toolbar item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/allowsduplicatesintoolbar)*