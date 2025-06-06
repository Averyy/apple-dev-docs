# numberOfItems

**Framework**: AppKit  
**Kind**: property

The number of menu items in the menu, including separator items.

**Availability**:
- macOS ?+

## Declaration

```swift
var numberOfItems: Int { get }
```

#### Discussion

This property contains a value of type `NSInteger` that indicates the number of menu items in the menu, including separator items.

## See Also

- [func item(withTag: Int) -> NSMenuItem?](nsmenu/item(withtag:).md)
  Returns the first menu item in the menu with the specified tag.
- [func item(withTitle: String) -> NSMenuItem?](nsmenu/item(withtitle:).md)
  Returns the first menu item in the menu with a specified title.
- [func item(at: Int) -> NSMenuItem?](nsmenu/item(at:).md)
  Returns the menu item at a specific location of the menu.
- [var items: [NSMenuItem]](nsmenu/items.md)
  An array containing the menu items in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/numberofitems)*