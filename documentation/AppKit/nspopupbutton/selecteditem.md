# selectedItem

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The menu item that was last selected by the user.

**Availability**:
- macOS

## Declaration

```swift
var selectedItem: NSMenuItem? { get }
```

```objc
@property (strong, readonly, nullable) NSMenuItem * selectedItem;
```

#### Discussion

The last selected menu item is the one that was highlighted when the user released the mouse button. It is possible for a pull-down menu’s selected item to be its first item. If no item is selected, the value in this property is `nil`.

## See Also

### Getting the user’s selection
- [var titleOfSelectedItem: String?](./titleofselecteditem.md)
  The title of the item that was last selected by the user.
- [var indexOfSelectedItem: Int](./indexofselecteditem.md)
  The index of the item that was last selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/selecteditem)*