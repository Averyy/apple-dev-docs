# isNavigational

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the item behaves as a navigation item in the toolbar.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
@MainActor
var isNavigational: Bool { get set }
```

#### Discussion

Mark a toolbar item as navigation if you use it to navigate around your content. When you set this property to [`true`](https://developer.apple.com/documentation/swift/true), the system can position navigation items outside of the normal list of items in the toolbar. For example, the back and forward buttons in Finder windows are navigational, and the system positions them at the leading edge of the window’s title area. Specify the initial order of the items using the [`toolbarDefaultItemIdentifiers(_:)`](nstoolbardelegate/toolbardefaultitemidentifiers(_:).md) method of the toolbar delegate object.

## See Also

- [var isVisible: Bool](nstoolbaritem/isvisible.md)
  A Boolean value that indicates whether the item is currently visible in the toolbar, and not in the overflow menu.
- [var isBordered: Bool](nstoolbaritem/isbordered.md)
  A Boolean value that indicates whether the toolbar item has a bordered style.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbaritem/isnavigational)*