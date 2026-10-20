# didRemoveItemNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted after an item is removed from a toolbar.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
class let didRemoveItemNotification: NSNotification.Name
```

```c
extern NSNotificationName NSToolbarDidRemoveItemNotification;
```

#### Discussion

The notification item is the `NSToolbar` object that removed the item. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| [`itemKey`](../nstoolbaruserinfokey/itemkey.md) | The `NSToolbarItem` object that was removed. |

## See Also

### Related Documentation
- [func toolbarDidRemoveItem(Notification)](../nstoolbardelegate/toolbardidremoveitem%28_%29.md)
  Tells the delegate that the toolbar removed the specified item.
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
- [func insertItem(withItemIdentifier: NSToolbarItem.Identifier, at: Int)](./insertitem%28withitemidentifier,at%29.md)
  Inserts an item into the toolbar at the specified index.
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the item at the specified index in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/didremoveitemnotification)*