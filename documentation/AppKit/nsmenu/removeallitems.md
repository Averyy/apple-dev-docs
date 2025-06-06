# removeAllItems()

**Framework**: AppKit  
**Kind**: method

Removes all the menu items in the menu.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func removeAllItems()
```

#### Discussion

This method is more efficient than removing menu items individually.

Unlike the other remove methods, this method does not post [`didChangeItemNotification`](nsmenu/didchangeitemnotification.md) notifications.

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
- [func itemChanged(NSMenuItem)](nsmenu/itemchanged(_:).md)
  Invoked when a menu item is modified visually (for example, its title changes).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/removeallitems())*