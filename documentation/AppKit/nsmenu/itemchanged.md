# itemChanged(_:)

**Framework**: AppKit  
**Kind**: method

Invoked when a menu item is modified visually (for example, its title changes).

**Availability**:
- macOS ?+

## Declaration

```swift
func itemChanged(_ item: NSMenuItem)
```

#### Discussion

This method is not called for changes involving the menu item’s action, target, represented object, or tag. Posts an [`didChangeItemNotification`](nsmenu/didchangeitemnotification.md).

## Parameters

- `item`: The menu item that has visually changed.

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
- [func removeItem(at: Int)](nsmenu/removeitem(at:).md)
  Removes the menu item at a specified location in the menu.
- [func removeAllItems()](nsmenu/removeallitems.md)
  Removes all the menu items in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/itemchanged(_:))*