# items

**Framework**: AppKit  
**Kind**: property

An array containing the menu items in the menu.

**Availability**:
- macOS ?+

## Declaration

```swift
var items: [NSMenuItem] { get set }
```

#### Discussion

This property contains an array of menu items in the menu.

## See Also

- [func item(withTag: Int) -> NSMenuItem?](nsmenu/item(withtag:).md)
  Returns the first menu item in the menu with the specified tag.
- [func item(withTitle: String) -> NSMenuItem?](nsmenu/item(withtitle:).md)
  Returns the first menu item in the menu with a specified title.
- [func item(at: Int) -> NSMenuItem?](nsmenu/item(at:).md)
  Returns the menu item at a specific location of the menu.
- [var numberOfItems: Int](nsmenu/numberofitems.md)
  The number of menu items in the menu, including separator items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/items)*