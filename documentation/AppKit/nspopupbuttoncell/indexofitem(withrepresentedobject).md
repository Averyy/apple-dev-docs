# indexOfItem(withRepresentedObject:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the menu item that holds the specified represented object.

**Availability**:
- macOS

## Declaration

```swift
func indexOfItem(withRepresentedObject obj: Any?) -> Int
```

```objc
- (NSInteger) indexOfItemWithRepresentedObject:(id) obj;
```

## Return Value

The index of the menu item that owns the specified object, or `-1` if no such menu item was found.

## Parameters

- `obj`: The represented object associated with a menu item.

## See Also

### Related Documentation
- [var indexOfSelectedItem: Int](./indexofselecteditem.md)
  The index of the item last selected by the user.
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
- [func indexOfItem(withTarget: Any?, andAction: Selector?) -> Int](./indexofitem%28withtarget,andaction%29.md)
  Returns the index of the menu item with the specified target and action.
- [func item(at: Int) -> NSMenuItem?](./item%28at%29.md)
  Returns the menu item at the specified index.
- [func item(withTitle: String) -> NSMenuItem?](./item%28withtitle%29.md)
  Returns the menu item with the specified title.
- [var lastItem: NSMenuItem?](./lastitem.md)
  The last item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/indexofitem(withrepresentedobject:))*