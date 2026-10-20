# items

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array containing the menu items in the menu.

**Availability**:
- macOS

## Declaration

```swift
var items: [NSMenuItem] { get set }
```

```objc
@property (copy) NSArray<NSMenuItem *> * itemArray;
```

#### Discussion

This property contains an array of menu items in the menu.

## See Also

### Finding Menu Items
- [func item(withTag: Int) -> NSMenuItem?](./item%28withtag%29.md)
  Returns the first menu item in the menu with the specified tag.
- [func item(withTitle: String) -> NSMenuItem?](./item%28withtitle%29.md)
  Returns the first menu item in the menu with a specified title.
- [func item(at: Int) -> NSMenuItem?](./item%28at%29.md)
  Returns the menu item at a specific location of the menu.
- [var numberOfItems: Int](./numberofitems.md)
  The number of menu items in the menu, including separator items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/items)*