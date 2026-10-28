# item(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the menu item at a specific location of the menu.

**Availability**:
- macOS

## Declaration

```swift
func item(at index: Int) -> NSMenuItem?
```

```objc
- (NSMenuItem *) itemAtIndex:(NSInteger) index;
```

## Return Value

The found menu item (an object conforming to the NSMenuItem protocol) or `nil` if the object couldn’t be found.

## Discussion

This method raises an exception if `index` is out of bounds.

## Parameters

- `index`: An integer index locating a menu item in a menu.

## See Also

### Related Documentation
- [func index(of: NSMenuItem) -> Int](./index%28of%29.md)
  Returns the index identifying the location of a specified menu item in the menu.
### Finding Menu Items
- [func item(withTag: Int) -> NSMenuItem?](./item%28withtag%29.md)
  Returns the first menu item in the menu with the specified tag.
- [func item(withTitle: String) -> NSMenuItem?](./item%28withtitle%29.md)
  Returns the first menu item in the menu with a specified title.
- [var numberOfItems: Int](./numberofitems.md)
  The number of menu items in the menu, including separator items.
- [var items: [NSMenuItem]](./items.md)
  An array containing the menu items in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/item(at:))*