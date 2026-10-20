# indexOfSelectedItem

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The index of the item last selected by the user.

**Availability**:
- macOS

## Declaration

```swift
var indexOfSelectedItem: Int { get }
```

```objc
@property (readonly) NSInteger indexOfSelectedItem;
```

#### Discussion

The value of this property is the index of the selected item, or `-1` if no item is selected.

## See Also

### Related Documentation
- [func indexOfItem(withTag: Int) -> Int](./indexofitem%28withtag%29.md)
  Returns the index of the menu item with the specified tag.
- [func indexOfItem(withTitle: String) -> Int](./indexofitem%28withtitle%29.md)
  Returns the index of the item with the specified title.
- [func index(of: NSMenuItem) -> Int](./index%28of%29.md)
  Returns the index of the specified menu item.
- [func indexOfItem(withTarget: Any?, andAction: Selector?) -> Int](./indexofitem%28withtarget,andaction%29.md)
  Returns the index of the menu item with the specified target and action.
- [func indexOfItem(withRepresentedObject: Any?) -> Int](./indexofitem%28withrepresentedobject%29.md)
  Returns the index of the menu item that holds the specified represented object.
### Dealing with selection
- [func select(NSMenuItem?)](./select%28_%29.md)
  Selects the specified menu item.
- [func selectItem(at: Int)](./selectitem%28at%29.md)
  Selects the item in the menu at the specified index.
- [func selectItem(withTag: Int) -> Bool](./selectitem%28withtag%29.md)
  Selects the menu item with the specified tag.
- [func selectItem(withTitle: String)](./selectitem%28withtitle%29.md)
  Selects the item with the specified title.
- [func setTitle(String?)](./settitle%28_%29.md)
  Sets the string displayed in the receiver when the user isn’t pressing the mouse button.
- [var selectedItem: NSMenuItem?](./selecteditem.md)
  The menu item last selected by the user.
- [func synchronizeTitleAndSelectedItem()](./synchronizetitleandselecteditem%28%29.md)
  Synchronizes the pop-up button’s displayed item with the currently selected menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/indexofselecteditem)*