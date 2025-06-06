# visibleItems

**Framework**: AppKit  
**Kind**: property

An array containing the toolbar’s currently visible items.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
var visibleItems: [NSToolbarItem]? { get }
```

#### Discussion

This property doesn’t contain items in the overflow menu because those items aren’t visible.

## See Also

- [var items: [NSToolbarItem]](nstoolbar/items.md)
  An array containing the toolbar’s current items, in order.
- [var centeredItemIdentifiers: Set<NSToolbarItem.Identifier>](nstoolbar/centereditemidentifiers.md)
  The set of custom items to display in the center of the toolbar.
- [var selectedItemIdentifier: NSToolbarItem.Identifier?](nstoolbar/selecteditemidentifier.md)
  The identifier of the toolbar’s currently selected item.
- [class let willAddItemNotification: NSNotification.Name](nstoolbar/willadditemnotification.md)
  Posts before the toolbar adds a new item.
- [class let didRemoveItemNotification: NSNotification.Name](nstoolbar/didremoveitemnotification.md)
  Posted after an item is removed from a toolbar.
- [func insertItem(withItemIdentifier: NSToolbarItem.Identifier, at: Int)](nstoolbar/insertitem(withitemidentifier:at:).md)
  Inserts an item into the toolbar at the specified index.
- [func removeItem(at: Int)](nstoolbar/removeitem(at:).md)
  Removes the item at the specified index in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/visibleitems)*