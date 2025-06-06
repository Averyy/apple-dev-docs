# removeItem(at:)

**Framework**: AppKit  
**Kind**: method

Removes the menu item at a specified location in the menu.

**Availability**:
- macOS ?+

## Declaration

```swift
func removeItem(at index: Int)
```

#### Discussion

After it removes the menu item, this method posts an [`didRemoveItemNotification`](nsmenu/didremoveitemnotification.md).

## Parameters

- `index`: An integer index identifying the menu item.

## See Also

- [func insertItem(NSMenuItem, at: Int)](nsmenu/insertitem(_:at:).md)
  Inserts a menu item into the menu at a specific location.
- [func insertItem(withTitle: String, action: Selector?, keyEquivalent: String, at: Int) -> NSMenuItem](nsmenu/insertitem(withtitle:action:keyequivalent:at:).md)
  Creates and adds a menu item at a specified location in the menu.
- [func addItem(NSMenuItem)](nsmenu/additem(_:).md)
  Adds a menu item to the end of the menu.
- [func addItem(withTitle: String, action: Selector?, keyEquivalent: String) -> NSMenuItem](nsmenu/additem(withtitle:action:keyequivalent:).md)
  Creates a new menu item and adds it to the end of the menu.
- [func removeItem(NSMenuItem)](nsmenu/removeitem(_:).md)
  Removes a menu item from the menu.
- [func itemChanged(NSMenuItem)](nsmenu/itemchanged(_:).md)
  Invoked when a menu item is modified visually (for example, its title changes).
- [func removeAllItems()](nsmenu/removeallitems.md)
  Removes all the menu items in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/removeitem(at:))*