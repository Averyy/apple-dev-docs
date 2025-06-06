# insertItem(withItemIdentifier:at:)

**Framework**: AppKit  
**Kind**: method

Inserts an item into the toolbar at the specified index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
@MainActor
func insertItem(withItemIdentifier itemIdentifier: NSToolbarItem.Identifier, at index: Int)
```

#### Discussion

Typically, you don’t call this method directly from your code. Instead, you specify your toolbar’s allowed items, and the set of default items you want to appear. After that, you let the user customize the toolbar.

Any changes you make to the toolbar appear in all [`NSToolbar`](nstoolbar.md) objects with the same [`identifier`](nstoolbar/identifier-swift.property.md) value. If a toolbar item with the specified identifier isn’t available, the toolbar calls the [`toolbar(_:itemForItemIdentifier:willBeInsertedIntoToolbar:)`](nstoolbardelegate/toolbar(_:itemforitemidentifier:willbeinsertedintotoolbar:).md) method of its delegate to get the item. This method does not trigger a call to your delegate’s [`toolbar(_:itemIdentifier:canBeInsertedAt:)`](nstoolbardelegate/toolbar(_:itemidentifier:canbeinsertedat:).md) method.

## Parameters

- `itemIdentifier`: The identifier of the toolbar item to insert.
- `index`: The index at which to insert the item.

## See Also

- [var items: [NSToolbarItem]](nstoolbar/items.md)
  An array containing the toolbar’s current items, in order.
- [var visibleItems: [NSToolbarItem]?](nstoolbar/visibleitems.md)
  An array containing the toolbar’s currently visible items.
- [var centeredItemIdentifiers: Set<NSToolbarItem.Identifier>](nstoolbar/centereditemidentifiers.md)
  The set of custom items to display in the center of the toolbar.
- [var selectedItemIdentifier: NSToolbarItem.Identifier?](nstoolbar/selecteditemidentifier.md)
  The identifier of the toolbar’s currently selected item.
- [class let willAddItemNotification: NSNotification.Name](nstoolbar/willadditemnotification.md)
  Posts before the toolbar adds a new item.
- [class let didRemoveItemNotification: NSNotification.Name](nstoolbar/didremoveitemnotification.md)
  Posted after an item is removed from a toolbar.
- [func removeItem(at: Int)](nstoolbar/removeitem(at:).md)
  Removes the item at the specified index in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/insertitem(withitemidentifier:at:))*