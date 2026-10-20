# insertItem(_:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts a menu item into the menu at a specific location.

**Availability**:
- macOS

## Declaration

```swift
func insertItem(_ newItem: NSMenuItem, at index: Int)
```

```objc
- (void) insertItem:(NSMenuItem *) newItem atIndex:(NSInteger) index;
```

#### Discussion

This method posts an [`didAddItemNotification`](./didadditemnotification.md), allowing interested observers to update as appropriate. This method is a primitive method. All item-addition methods end up calling this method, so this is where you should implement custom behavior on adding new items to a menu in a custom subclass. If the menu item already exists in another menu, it is not inserted and the method raises an exception of type [`internalInconsistencyException`](../../Foundation/nsexceptionname/internalinconsistencyexception.md).

## Parameters

- `newItem`: An object conforming to the `NSMenuItem` protocol that represents a menu item.
- `index`: An integer index identifying the location of the menu item in the menu.

## See Also

### Related Documentation
- [func item(at: Int) -> NSMenuItem?](./item%28at%29.md)
  Returns the menu item at a specific location of the menu.
### Adding and Removing Menu Items
- [func insertItem(withTitle: String, action: Selector?, keyEquivalent: String, at: Int) -> NSMenuItem](./insertitem%28withtitle,action,keyequivalent,at%29.md)
  Creates and adds a menu item at a specified location in the menu.
- [func addItem(NSMenuItem)](./additem%28_%29.md)
  Adds a menu item to the end of the menu.
- [func addItem(withTitle: String, action: Selector?, keyEquivalent: String) -> NSMenuItem](./additem%28withtitle,action,keyequivalent%29.md)
  Creates a new menu item and adds it to the end of the menu.
- [func removeItem(NSMenuItem)](./removeitem%28_%29.md)
  Removes a menu item from the menu.
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the menu item at a specified location in the menu.
- [func itemChanged(NSMenuItem)](./itemchanged%28_%29.md)
  Invoked when a menu item is modified visually (for example, its title changes).
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all the menu items in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/insertitem(_:at:))*