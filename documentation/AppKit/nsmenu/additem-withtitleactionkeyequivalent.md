# addItem(withTitle:action:keyEquivalent:)

**Framework**: AppKit  
**Kind**: method

Creates a new menu item and adds it to the end of the menu.

**Availability**:
- macOS ?+

## Declaration

```swift
func addItem(withTitle string: String, action selector: Selector?, keyEquivalent charCode: String) -> NSMenuItem
```

#### Return Value

The created menu item (an object conforming to the NSMenuItem protocol) or `nil` if the object couldn’t be created.

## Parameters

- `string`: A string to be made the title of the menu item.
- `selector`: The action-message selector to assign to the menu item.
- `charCode`: A string identifying the key to use as a key equivalent for the menu item. If you do not want the menu item to have a key equivalent,   should be an empty string ( ) and not  .

## See Also

- [func insertItem(NSMenuItem, at: Int)](nsmenu/insertitem(_:at:).md)
  Inserts a menu item into the menu at a specific location.
- [func insertItem(withTitle: String, action: Selector?, keyEquivalent: String, at: Int) -> NSMenuItem](nsmenu/insertitem(withtitle:action:keyequivalent:at:).md)
  Creates and adds a menu item at a specified location in the menu.
- [func addItem(NSMenuItem)](nsmenu/additem(_:).md)
  Adds a menu item to the end of the menu.
- [func removeItem(NSMenuItem)](nsmenu/removeitem(_:).md)
  Removes a menu item from the menu.
- [func removeItem(at: Int)](nsmenu/removeitem(at:).md)
  Removes the menu item at a specified location in the menu.
- [func itemChanged(NSMenuItem)](nsmenu/itemchanged(_:).md)
  Invoked when a menu item is modified visually (for example, its title changes).
- [func removeAllItems()](nsmenu/removeallitems.md)
  Removes all the menu items in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/additem(withtitle:action:keyequivalent:))*