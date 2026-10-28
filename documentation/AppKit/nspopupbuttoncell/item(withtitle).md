# item(withTitle:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the menu item with the specified title.

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

The menu item, or `nil` if no item with the specified title exists in the menu.

## Parameters

- `title`: The title of the menu item you want.

## See Also

### Related Documentation
- [func itemTitle(at: Int) -> String](./itemtitle%28at%29.md)
  Returns the title of the item at the specified index.
### Accessing the items
- [var itemArray: [NSMenuItem]](./itemarray.md)
  An array of [`NSMenuItem`](../nsmenuitem.md) objects that represent the items in the menu.
- [var numberOfItems: Int](./numberofitems.md)
  The number of items in the menu.
- [func index(of: NSMenuItem) -> Int](./index%28of%29.md)
  Returns the index of the specified menu item.
- [func indexOfItem(withTitle: String) -> Int](./indexofitem%28withtitle%29.md)
  Returns the index of the item with the specified title.
- [func indexOfItem(withTag: Int) -> Int](./indexofitem%28withtag%29.md)
  Returns the index of the menu item with the specified tag.
- [func indexOfItem(withRepresentedObject: Any?) -> Int](./indexofitem%28withrepresentedobject%29.md)
  Returns the index of the menu item that holds the specified represented object.
- [func indexOfItem(withTarget: Any?, andAction: Selector?) -> Int](./indexofitem%28withtarget,andaction%29.md)
  Returns the index of the menu item with the specified target and action.
- [func item(at: Int) -> NSMenuItem?](./item%28at%29.md)
  Returns the menu item at the specified index.
- [var lastItem: NSMenuItem?](./lastitem.md)
  The last item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/item(withtitle:))*