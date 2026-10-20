# items

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array containing the toolbar’s current items, in order.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
var items: [NSToolbarItem] { get }
```

```objc
@property (copy, readonly) NSArray<__kindof NSToolbarItem *> * items;
```

#### Discussion

To specify the default order of your toolbar’s items, implement the [`toolbarDefaultItemIdentifiers(_:)`](../nstoolbardelegate/toolbardefaultitemidentifiers%28_%29.md) method in your toolbar delegate object. Use other methods of your delegate object to manage the placement of items in the toolbar.

## See Also

### Managing items on the toolbar
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
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the item at the specified index in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/items)*