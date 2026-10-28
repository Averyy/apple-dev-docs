# item(withTitle:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the first menu item in the menu with a specified title.

**Availability**:
- macOS

## Declaration

```swift
func item(withTitle title: String) -> NSMenuItem?
```

```objc
- (NSMenuItem *) itemWithTitle:(NSString *) title;
```

## Return Value

The found menu item (an object conforming to the NSMenuItem protocol) or `nil` if the object couldn’t be found.

## Parameters

- `title`: The title of a menu item.

## See Also

### Related Documentation
- [func indexOfItem(withTitle: String) -> Int](./indexofitem%28withtitle%29.md)
  Returns the index of the first menu item in the menu that has a specified title.
### Finding Menu Items
- [func item(withTag: Int) -> NSMenuItem?](./item%28withtag%29.md)
  Returns the first menu item in the menu with the specified tag.
- [func item(at: Int) -> NSMenuItem?](./item%28at%29.md)
  Returns the menu item at a specific location of the menu.
- [var numberOfItems: Int](./numberofitems.md)
  The number of menu items in the menu, including separator items.
- [var items: [NSMenuItem]](./items.md)
  An array containing the menu items in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/item(withtitle:))*