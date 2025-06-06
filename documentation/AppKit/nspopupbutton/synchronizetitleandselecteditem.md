# synchronizeTitleAndSelectedItem()

**Framework**: AppKit  
**Kind**: method

Ensures that the item being displayed by the receiver agrees with the selected item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func synchronizeTitleAndSelectedItem()
```

#### Discussion

If there’s no selected item, this method selects the first item in the item menu and sets the receiver’s item to match. For pull-down menus, this method makes sure that the first item is being displayed (the `NSPopUpButtonCell` object must be set to use the selected menu item, which happens by default).

## See Also

- [var indexOfSelectedItem: Int](nspopupbutton/indexofselecteditem.md)
  The index of the item that was last selected by the user.
- [var itemArray: [NSMenuItem]](nspopupbutton/itemarray.md)
  The array of menu item objects associated with the button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/synchronizetitleandselecteditem())*