# selectedItemIdentifier

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The identifier of the toolbar’s currently selected item.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
var selectedItemIdentifier: NSToolbarItem.Identifier? { get set }
```

```objc
@property (copy, nullable) NSToolbarItemIdentifier selectedItemIdentifier;
```

#### Discussion

The value of this property is `nil` if the toolbar doesn’t have a selected item.

## See Also

### Managing items on the toolbar
- [var items: [NSToolbarItem]](./items.md)
  An array containing the toolbar’s current items, in order.
- [var visibleItems: [NSToolbarItem]?](./visibleitems.md)
  An array containing the toolbar’s currently visible items.
- [var centeredItemIdentifiers: Set<NSToolbarItem.Identifier>](./centereditemidentifiers.md)
  The set of custom items to display in the center of the toolbar.
- [class let willAddItemNotification: NSNotification.Name](./willadditemnotification.md)
  Posts before the toolbar adds a new item.
- [class let didRemoveItemNotification: NSNotification.Name](./didremoveitemnotification.md)
  Posted after an item is removed from a toolbar.
- [func insertItem(withItemIdentifier: NSToolbarItem.Identifier, at: Int)](./insertitem%28withitemidentifier,at%29.md)
  Inserts an item into the toolbar at the specified index.
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the item at the specified index in the toolbar.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstoolbar/selecteditemidentifier)*