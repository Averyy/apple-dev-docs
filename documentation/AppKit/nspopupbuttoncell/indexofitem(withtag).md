# indexOfItem(withTag:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the menu item with the specified tag.

**Availability**:
- macOS

## Declaration

```swift
func indexOfItem(withTag tag: Int) -> Int
```

```objc
- (NSInteger) indexOfItemWithTag:(NSInteger) tag;
```

#### Return Value

The index of the item or `-1` if no item with the specified tag was found.

#### Discussion

Tags are values your application assigns to an object to identify it. You can assign tags to menu items using the setTag: method of [`NSMenuItem`](../nsmenuitem.md).

## Parameters

- `tag`: The tag of the menu item you want.

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
- [func indexOfItem(withRepresentedObject: Any?) -> Int](./indexofitem%28withrepresentedobject%29.md)
  Returns the index of the menu item that holds the specified represented object.
- [func indexOfItem(withTarget: Any?, andAction: Selector?) -> Int](./indexofitem%28withtarget,andaction%29.md)
  Returns the index of the menu item with the specified target and action.
- [func item(at: Int) -> NSMenuItem?](./item%28at%29.md)
  Returns the menu item at the specified index.
- [func item(withTitle: String) -> NSMenuItem?](./item%28withtitle%29.md)
  Returns the menu item with the specified title.
- [var lastItem: NSMenuItem?](./lastitem.md)
  The last item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/indexofitem(withtag:))*