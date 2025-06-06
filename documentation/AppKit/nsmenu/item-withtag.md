# item(withTag:)

**Framework**: AppKit  
**Kind**: method

Returns the first menu item in the menu with the specified tag.

**Availability**:
- macOS ?+

## Declaration

```swift
func item(withTag tag: Int) -> NSMenuItem?
```

#### Return Value

The found menu item (an object conforming to the NSMenuItem protocol) or `nil` if the object couldn’t be found.

## Parameters

- `tag`: A numeric tag associated with a menu item.

## See Also

- [func indexOfItem(withTag: Int) -> Int](nsmenu/indexofitem(withtag:).md)
  Returns the index of the first menu item in the menu identified by a tag.
- [func item(withTitle: String) -> NSMenuItem?](nsmenu/item(withtitle:).md)
  Returns the first menu item in the menu with a specified title.
- [func item(at: Int) -> NSMenuItem?](nsmenu/item(at:).md)
  Returns the menu item at a specific location of the menu.
- [var numberOfItems: Int](nsmenu/numberofitems.md)
  The number of menu items in the menu, including separator items.
- [var items: [NSMenuItem]](nsmenu/items.md)
  An array containing the menu items in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/item(withtag:))*