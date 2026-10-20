# indexOfItem(withTarget:andAction:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the first menu item in the menu that has a specified action and target.

**Availability**:
- macOS

## Declaration

```swift
func indexOfItem(withTarget target: Any?, andAction actionSelector: Selector?) -> Int
```

```objc
- (NSInteger) indexOfItemWithTarget:(id) target andAction:(SEL) actionSelector;
```

#### Return Value

The integer index of the menu item or, if no such menu item is in the menu, –1.

## Parameters

- `target`: An object that is set as the target of a menu item of the menu.
- `actionSelector`: A selector identifying an action method. If `actionSelector` is `NULL`, the first menu item in the menu that has target `anObject` is returned.

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
- [func indexOfItem(withRepresentedObject: Any?) -> Int](./indexofitem%28withrepresentedobject%29.md)
  Returns the index of the first menu item in the menu that has a given represented object.
- [func indexOfItem(withSubmenu: NSMenu?) -> Int](./indexofitem%28withsubmenu%29.md)
  Returns the index of the menu item in the menu with the given submenu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmenu/indexofitem(withtarget:andaction:))*