# centeredItemIdentifiers

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The set of custom items to display in the center of the toolbar.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
var centeredItemIdentifiers: Set<NSToolbarItem.Identifier> { get set }
```

```objc
@property (copy) NSSet<NSString *> * centeredItemIdentifiers;
```

## Discussion

Set this property to the items you want to appear together in the center of the toolbar. Specify the initial order of the items using the [`toolbarDefaultItemIdentifiers(_:)`](../nstoolbardelegate/toolbardefaultitemidentifiers%28_%29.md) method of your toolbar delegate object.

## See Also

### Managing items on the toolbar
- [var items: [NSToolbarItem]](./items.md)
  An array containing the toolbar’s current items, in order.
- [var visibleItems: [NSToolbarItem]?](./visibleitems.md)
  An array containing the toolbar’s currently visible items.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/centereditemidentifiers)*