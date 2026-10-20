# item(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the menu item at the specified index.

**Availability**:
- macOS

## Declaration

```swift
func item(at index: Int) -> NSMenuItem?
```

```objc
- (NSMenuItem *) itemAtIndex:(NSInteger) index;
```

#### Return Value

The menu item, or `nil` if no item exists at the specified index.

## Parameters

- `index`: The index of the item you want. The specified index must refer to an existing menu item.

## See Also

### Related Documentation
- [func item(at: Int) -> NSMenuItem?](../nsmenu/item%28at%29.md)
  Returns the menu item at a specific location of the menu.
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
- [func item(withTitle: String) -> NSMenuItem?](./item%28withtitle%29.md)
  Returns the menu item with the specified title.
- [var lastItem: NSMenuItem?](./lastitem.md)
  The last item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/item(at:))*