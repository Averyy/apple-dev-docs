# willAddItemNotification

**Framework**: AppKit  
**Kind**: property

Posts before the toolbar adds a new item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
class let willAddItemNotification: NSNotification.Name
```

#### Discussion

The notification item is the `NSToolbar` object that’s about to add the item. The `userInfo` dictionary contains the following information:

| Key | Value |
| --- | --- |
| [`itemKey`](nstoolbaruserinfokey/itemkey.md) | The `NSToolbarItem` object being added. |

## See Also

- [func toolbarWillAddItem(Notification)](nstoolbardelegate/toolbarwilladditem(_:).md)
  Tells the delegate that the toolbar is about to add the specified item.
- [var items: [NSToolbarItem]](nstoolbar/items.md)
  An array containing the toolbar’s current items, in order.
- [var visibleItems: [NSToolbarItem]?](nstoolbar/visibleitems.md)
  An array containing the toolbar’s currently visible items.
- [var centeredItemIdentifiers: Set<NSToolbarItem.Identifier>](nstoolbar/centereditemidentifiers.md)
  The set of custom items to display in the center of the toolbar.
- [var selectedItemIdentifier: NSToolbarItem.Identifier?](nstoolbar/selecteditemidentifier.md)
  The identifier of the toolbar’s currently selected item.
- [class let didRemoveItemNotification: NSNotification.Name](nstoolbar/didremoveitemnotification.md)
  Posted after an item is removed from a toolbar.
- [func insertItem(withItemIdentifier: NSToolbarItem.Identifier, at: Int)](nstoolbar/insertitem(withitemidentifier:at:).md)
  Inserts an item into the toolbar at the specified index.
- [func removeItem(at: Int)](nstoolbar/removeitem(at:).md)
  Removes the item at the specified index in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/willadditemnotification)*