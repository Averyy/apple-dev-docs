# item(withTitle:)

**Framework**: AppKit  
**Kind**: method

Returns the first menu item in the menu with a specified title.

**Availability**:
- macOS ?+

## Declaration

```swift
func item(withTitle title: String) -> NSMenuItem?
```

#### Return Value

The found menu item (an object conforming to the NSMenuItem protocol) or `nil` if the object couldn’t be found.

## Parameters

- `title`: The title of a menu item.

## See Also

- [func indexOfItem(withTitle: String) -> Int](nsmenu/indexofitem(withtitle:).md)
  Returns the index of the first menu item in the menu that has a specified title.
- [func item(withTag: Int) -> NSMenuItem?](nsmenu/item(withtag:).md)
  Returns the first menu item in the menu with the specified tag.
- [func item(at: Int) -> NSMenuItem?](nsmenu/item(at:).md)
  Returns the menu item at a specific location of the menu.
- [var numberOfItems: Int](nsmenu/numberofitems.md)
  The number of menu items in the menu, including separator items.
- [var items: [NSMenuItem]](nsmenu/items.md)
  An array containing the menu items in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/item(withtitle:))*