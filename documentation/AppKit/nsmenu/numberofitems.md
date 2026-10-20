# numberOfItems

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of menu items in the menu, including separator items.

**Availability**:
- macOS

## Declaration

```swift
var numberOfItems: Int { get }
```

```objc
@property (readonly) NSInteger numberOfItems;
```

#### Discussion

This property contains a value of type `NSInteger` that indicates the number of menu items in the menu, including separator items.

## See Also

### Finding Menu Items
- [func item(withTag: Int) -> NSMenuItem?](./item%28withtag%29.md)
  Returns the first menu item in the menu with the specified tag.
- [func item(withTitle: String) -> NSMenuItem?](./item%28withtitle%29.md)
  Returns the first menu item in the menu with a specified title.
- [func item(at: Int) -> NSMenuItem?](./item%28at%29.md)
  Returns the menu item at a specific location of the menu.
- [var items: [NSMenuItem]](./items.md)
  An array containing the menu items in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/numberofitems)*