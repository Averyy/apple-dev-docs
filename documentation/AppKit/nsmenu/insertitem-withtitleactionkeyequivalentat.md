# insertItem(withTitle:action:keyEquivalent:at:)

**Framework**: AppKit  
**Kind**: method

Creates and adds a menu item at a specified location in the menu.

**Availability**:
- macOS ?+

## Declaration

```swift
func insertItem(withTitle string: String, action selector: Selector?, keyEquivalent charCode: String, at index: Int) -> NSMenuItem
```

#### Return Value

The new menu item (an object conforming to the NSMenuItem protocol) or `nil` if the item could not be created

## Parameters

- `string`: A string to be made the title of the menu item.
- `selector`: The action-message selector to assign to the menu item.
- `charCode`: A string identifying the key to use as a key equivalent for the menu item. If you do not want the menu item to have a key equivalent,   should be an empty string ( ) and not  .
- `index`: An integer index identifying the location of the menu item in the menu.

## See Also

- [func insertItem(NSMenuItem, at: Int)](nsmenu/insertitem(_:at:).md)
  Inserts a menu item into the menu at a specific location.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/insertitem(withtitle:action:keyequivalent:at:))*