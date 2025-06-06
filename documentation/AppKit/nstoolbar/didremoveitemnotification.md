# didRemoveItemNotification

**Framework**: AppKit  
**Kind**: property

Posted after an item is removed from a toolbar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
class let didRemoveItemNotification: NSNotification.Name
```

#### Discussion

The notification item is the `NSToolbar` object that removed the item. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| [`itemKey`](nstoolbaruserinfokey/itemkey.md) | The `NSToolbarItem` object that was removed. |

## See Also

- [func toolbarDidRemoveItem(Notification)](nstoolbardelegate/toolbardidremoveitem(_:).md)
  Tells the delegate that the toolbar removed the specified item.
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
- [func insertItem(withItemIdentifier: NSToolbarItem.Identifier, at: Int)](nstoolbar/insertitem(withitemidentifier:at:).md)
  Inserts an item into the toolbar at the specified index.
- [func removeItem(at: Int)](nstoolbar/removeitem(at:).md)
  Removes the item at the specified index in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/didremoveitemnotification)*