# centeredItemIdentifiers

**Framework**: AppKit  
**Kind**: property

The set of custom items to display in the center of the toolbar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
@MainActor
var centeredItemIdentifiers: Set<NSToolbarItem.Identifier> { get set }
```

#### Discussion

Set this property to the items you want to appear together in the center of the toolbar. Specify the initial order of the items using the [`toolbarDefaultItemIdentifiers(_:)`](nstoolbardelegate/toolbardefaultitemidentifiers(_:).md) method of your toolbar delegate object.

## See Also

- [var items: [NSToolbarItem]](nstoolbar/items.md)
  An array containing the toolbar’s current items, in order.
- [var visibleItems: [NSToolbarItem]?](nstoolbar/visibleitems.md)
  An array containing the toolbar’s currently visible items.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/centereditemidentifiers)*