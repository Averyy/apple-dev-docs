# insertItem(withItemIdentifier:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts an item into the toolbar at the specified index.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
func insertItem(withItemIdentifier itemIdentifier: NSToolbarItem.Identifier, at index: Int)
```

```objc
- (void) insertItemWithItemIdentifier:(NSToolbarItemIdentifier) itemIdentifier atIndex:(NSInteger) index;
```

#### Discussion

Typically, you don’t call this method directly from your code. Instead, you specify your toolbar’s allowed items, and the set of default items you want to appear. After that, you let the user customize the toolbar.

Any changes you make to the toolbar appear in all [`NSToolbar`](../nstoolbar.md) objects with the same [`identifier`](./identifier-swift.property.md) value. If a toolbar item with the specified identifier isn’t available, the toolbar calls the [`toolbar(_:itemForItemIdentifier:willBeInsertedIntoToolbar:)`](../nstoolbardelegate/toolbar%28_,itemforitemidentifier,willbeinsertedintotoolbar%29.md) method of its delegate to get the item. This method does not trigger a call to your delegate’s [`toolbar(_:itemIdentifier:canBeInsertedAt:)`](../nstoolbardelegate/toolbar%28_,itemidentifier,canbeinsertedat%29.md) method.

## Parameters

- `itemIdentifier`: The identifier of the toolbar item to insert.
- `index`: The index at which to insert the item.

## See Also

### Managing items on the toolbar
- [var items: [NSToolbarItem]](./items.md)
  An array containing the toolbar’s current items, in order.
- [var visibleItems: [NSToolbarItem]?](./visibleitems.md)
  An array containing the toolbar’s currently visible items.
- [var centeredItemIdentifiers: Set<NSToolbarItem.Identifier>](./centereditemidentifiers.md)
  The set of custom items to display in the center of the toolbar.
- [var selectedItemIdentifier: NSToolbarItem.Identifier?](./selecteditemidentifier.md)
  The identifier of the toolbar’s currently selected item.
- [class let willAddItemNotification: NSNotification.Name](./willadditemnotification.md)
  Posts before the toolbar adds a new item.
- [class let didRemoveItemNotification: NSNotification.Name](./didremoveitemnotification.md)
  Posted after an item is removed from a toolbar.
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the item at the specified index in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/insertitem(withitemidentifier:at:))*