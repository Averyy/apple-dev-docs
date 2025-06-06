# insertItem(_:at:)

**Framework**: AppKit  
**Kind**: method

Inserts a menu item into the menu at a specific location.

**Availability**:
- macOS ?+

## Declaration

```swift
func insertItem(_ newItem: NSMenuItem, at index: Int)
```

#### Discussion

This method posts an [`didAddItemNotification`](nsmenu/didadditemnotification.md), allowing interested observers to update as appropriate. This method is a primitive method. All item-addition methods end up calling this method, so this is where you should implement custom behavior on adding new items to a menu in a custom subclass. If the menu item already exists in another menu, it is not inserted and the method raises an exception of type [`internalInconsistencyException`](https://developer.apple.com/documentation/foundation/nsexceptionname/1416220-internalinconsistencyexception).

## Parameters

- `newItem`: An object conforming to the   protocol that represents a menu item.
- `index`: An integer index identifying the location of the menu item in the menu.

## See Also

- [func item(at: Int) -> NSMenuItem?](nsmenu/item(at:).md)
  Returns the menu item at a specific location of the menu.
- [func insertItem(withTitle: String, action: Selector?, keyEquivalent: String, at: Int) -> NSMenuItem](nsmenu/insertitem(withtitle:action:keyequivalent:at:).md)
  Creates and adds a menu item at a specified location in the menu.
- [func addItem(NSMenuItem)](nsmenu/additem(_:).md)
  Adds a menu item to the end of the menu.
- [func addItem(withTitle: String, action: Selector?, keyEquivalent: String) -> NSMenuItem](nsmenu/additem(withtitle:action:keyequivalent:).md)
  Creates a new menu item and adds it to the end of the menu.
- [func removeItem(NSMenuItem)](nsmenu/removeitem(_:).md)
  Removes a menu item from the menu.
- [func removeItem(at: Int)](nsmenu/removeitem(at:).md)
  Removes the menu item at a specified location in the menu.
- [func itemChanged(NSMenuItem)](nsmenu/itemchanged(_:).md)
  Invoked when a menu item is modified visually (for example, its title changes).
- [func removeAllItems()](nsmenu/removeallitems.md)
  Removes all the menu items in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/insertitem(_:at:))*