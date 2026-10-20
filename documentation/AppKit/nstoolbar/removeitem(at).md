# removeItem(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the item at the specified index in the toolbar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
func removeItem(at index: Int)
```

```objc
- (void) removeItemAtIndex:(NSInteger) index;
```

#### Discussion

Typically, you don’t call this method directly from your code. Instead, you specify your toolbar’s allowed items, and the set of default items you want to appear. After that, you let the user customize the toolbar.

Any changes you make to the toolbar appear in all [`NSToolbar`](../nstoolbar.md) objects with the same [`identifier`](./identifier-swift.property.md) value. This method does not trigger a call to your delegate’s [`toolbar(_:itemIdentifier:canBeInsertedAt:)`](../nstoolbardelegate/toolbar%28_,itemidentifier,canbeinsertedat%29.md) method for the removal of the item.

## Parameters

- `index`: The index of the item to remove.

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
- [func insertItem(withItemIdentifier: NSToolbarItem.Identifier, at: Int)](./insertitem%28withitemidentifier,at%29.md)
  Inserts an item into the toolbar at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/removeitem(at:))*