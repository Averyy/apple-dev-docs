# index(of:)

**Framework**: AppKit  
**Kind**: method

Returns the index identifying the location of a specified menu item in the menu.

**Availability**:
- macOS ?+

## Declaration

```swift
func index(of item: NSMenuItem) -> Int
```

#### Return Value

The integer index of the menu item or, if no such menu item is in the menu, –1.

## Parameters

- `item`: A menu item—that is an object conforming to the NSMenuItem protocol.

## See Also

- [func item(at: Int) -> NSMenuItem?](nsmenu/item(at:).md)
  Returns the menu item at a specific location of the menu.
- [func insertItem(NSMenuItem, at: Int)](nsmenu/insertitem(_:at:).md)
  Inserts a menu item into the menu at a specific location.
- [func indexOfItem(withTitle: String) -> Int](nsmenu/indexofitem(withtitle:).md)
  Returns the index of the first menu item in the menu that has a specified title.
- [func indexOfItem(withTag: Int) -> Int](nsmenu/indexofitem(withtag:).md)
  Returns the index of the first menu item in the menu identified by a tag.
- [func indexOfItem(withTarget: Any?, andAction: Selector?) -> Int](nsmenu/indexofitem(withtarget:andaction:).md)
  Returns the index of the first menu item in the menu that has a specified action and target.
- [func indexOfItem(withRepresentedObject: Any?) -> Int](nsmenu/indexofitem(withrepresentedobject:).md)
  Returns the index of the first menu item in the menu that has a given represented object.
- [func indexOfItem(withSubmenu: NSMenu?) -> Int](nsmenu/indexofitem(withsubmenu:).md)
  Returns the index of the menu item in the menu with the given submenu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/index(of:))*