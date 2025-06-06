# addItem(_:)

**Framework**: AppKit  
**Kind**: method

Adds a menu item to the end of the menu.

**Availability**:
- macOS ?+

## Declaration

```swift
func addItem(_ newItem: NSMenuItem)
```

#### Discussion

This method invokes [`insertItem(_:at:)`](nsmenu/insertitem(_:at:).md). Thus, the menu does not accept the menu item if it already belongs to another menu. After adding the menu item, the menu updates itself.

## Parameters

- `newItem`: The menu item (an object conforming to the NSMenuItem protocol) to add to the menu.

## See Also

- [func insertItem(NSMenuItem, at: Int)](nsmenu/insertitem(_:at:).md)
  Inserts a menu item into the menu at a specific location.
- [func insertItem(withTitle: String, action: Selector?, keyEquivalent: String, at: Int) -> NSMenuItem](nsmenu/insertitem(withtitle:action:keyequivalent:at:).md)
  Creates and adds a menu item at a specified location in the menu.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/additem(_:))*