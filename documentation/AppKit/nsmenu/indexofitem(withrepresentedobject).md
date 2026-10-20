# indexOfItem(withRepresentedObject:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the first menu item in the menu that has a given represented object.

**Availability**:
- macOS

## Declaration

```swift
func indexOfItem(withRepresentedObject object: Any?) -> Int
```

```objc
- (NSInteger) indexOfItemWithRepresentedObject:(id) object;
```

#### Return Value

The integer index of the menu item or, if no such menu item is in the menu, –1.

## Parameters

- `object`: A represented object of the menu.

## See Also

### Related Documentation
- [func item(at: Int) -> NSMenuItem?](./item%28at%29.md)
  Returns the menu item at a specific location of the menu.
- [func insertItem(NSMenuItem, at: Int)](./insertitem%28_,at%29.md)
  Inserts a menu item into the menu at a specific location.
### Finding Indices of Menu Items
- [func index(of: NSMenuItem) -> Int](./index%28of%29.md)
  Returns the index identifying the location of a specified menu item in the menu.
- [func indexOfItem(withTitle: String) -> Int](./indexofitem%28withtitle%29.md)
  Returns the index of the first menu item in the menu that has a specified title.
- [func indexOfItem(withTag: Int) -> Int](./indexofitem%28withtag%29.md)
  Returns the index of the first menu item in the menu identified by a tag.
- [func indexOfItem(withTarget: Any?, andAction: Selector?) -> Int](./indexofitem%28withtarget,andaction%29.md)
  Returns the index of the first menu item in the menu that has a specified action and target.
- [func indexOfItem(withSubmenu: NSMenu?) -> Int](./indexofitem%28withsubmenu%29.md)
  Returns the index of the menu item in the menu with the given submenu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/indexofitem(withrepresentedobject:))*