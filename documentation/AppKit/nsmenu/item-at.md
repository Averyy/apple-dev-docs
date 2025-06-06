# item(at:)

**Framework**: AppKit  
**Kind**: method

Returns the menu item at a specific location of the menu.

**Availability**:
- macOS ?+

## Declaration

```swift
func item(at index: Int) -> NSMenuItem?
```

#### Return Value

The found menu item (an object conforming to the NSMenuItem protocol) or `nil` if the object couldn’t be found.

#### Discussion

This method raises an exception if `index` is out of bounds.

## Parameters

- `index`: An integer index locating a menu item in a menu.

## See Also

- [func index(of: NSMenuItem) -> Int](nsmenu/index(of:).md)
  Returns the index identifying the location of a specified menu item in the menu.
- [func item(withTag: Int) -> NSMenuItem?](nsmenu/item(withtag:).md)
  Returns the first menu item in the menu with the specified tag.
- [func item(withTitle: String) -> NSMenuItem?](nsmenu/item(withtitle:).md)
  Returns the first menu item in the menu with a specified title.
- [var numberOfItems: Int](nsmenu/numberofitems.md)
  The number of menu items in the menu, including separator items.
- [var items: [NSMenuItem]](nsmenu/items.md)
  An array containing the menu items in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/item(at:))*