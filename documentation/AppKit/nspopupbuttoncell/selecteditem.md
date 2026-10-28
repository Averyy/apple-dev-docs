# selectedItem

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The menu item last selected by the user.

**Availability**:
- macOS

## Declaration

```swift
var selectedItem: NSMenuItem? { get }
```

```objc
@property (strong, readonly, nullable) NSMenuItem * selectedItem;
```

## Discussion

The value of this property is the menu item that is currently selected, or `nil` if no item is selected. The last selected menu item is the one that was highlighted when the user released the mouse button. It is possible for a pull-down menu’s selected item to be its first item.

## See Also

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
- [var indexOfSelectedItem: Int](./indexofselecteditem.md)
  The index of the item last selected by the user.
- [func synchronizeTitleAndSelectedItem()](./synchronizetitleandselecteditem%28%29.md)
  Synchronizes the pop-up button’s displayed item with the currently selected menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/selecteditem)*