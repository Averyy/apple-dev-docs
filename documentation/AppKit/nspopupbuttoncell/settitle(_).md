# setTitle(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the string displayed in the receiver when the user isn’t pressing the mouse button.

**Availability**:
- macOS

## Declaration

```swift
func setTitle(_ string: String?)
```

```objc
- (void) setTitle:(NSString *) string;
```

#### Discussion

For pull-down menus that get their titles from a menu item, this method simply sets the pop-up button cell’s menu item to the first item in the menu. For pop-up menus, if a menu item whose title matches `aString` exists, this method makes that menu item the current selection; otherwise, it creates a new menu item with the title `aString`, adds it to the pop-up menu, and selects it.

## Parameters

- `string`: The string to display.

## See Also

### Related Documentation
- [init(textCell: String, pullsDown: Bool)](./init%28textcell,pullsdown%29.md)
  Returns an `NSPopUpButtonCell` object initialized with the specified title.
### Dealing with selection
- [func select(NSMenuItem?)](./select%28_%29.md)
  Selects the specified menu item.
- [func selectItem(at: Int)](./selectitem%28at%29.md)
  Selects the item in the menu at the specified index.
- [func selectItem(withTag: Int) -> Bool](./selectitem%28withtag%29.md)
  Selects the menu item with the specified tag.
- [func selectItem(withTitle: String)](./selectitem%28withtitle%29.md)
  Selects the item with the specified title.
- [var selectedItem: NSMenuItem?](./selecteditem.md)
  The menu item last selected by the user.
- [var indexOfSelectedItem: Int](./indexofselecteditem.md)
  The index of the item last selected by the user.
- [func synchronizeTitleAndSelectedItem()](./synchronizetitleandselecteditem%28%29.md)
  Synchronizes the pop-up button’s displayed item with the currently selected menu item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/settitle(_:))*