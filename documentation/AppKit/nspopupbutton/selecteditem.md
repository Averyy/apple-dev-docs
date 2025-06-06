# selectedItem

**Framework**: AppKit  
**Kind**: property

The menu item that was last selected by the user.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var selectedItem: NSMenuItem? { get }
```

#### Discussion

The last selected menu item is the one that was highlighted when the user released the mouse button. It is possible for a pull-down menu’s selected item to be its first item. If no item is selected, the value in this property is `nil`.

## See Also

- [var titleOfSelectedItem: String?](nspopupbutton/titleofselecteditem.md)
  The title of the item that was last selected by the user.
- [var indexOfSelectedItem: Int](nspopupbutton/indexofselecteditem.md)
  The index of the item that was last selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/selecteditem)*