# indexOfSelectedItem

**Framework**: AppKit  
**Kind**: property

The index of the item that was last selected by the user.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var indexOfSelectedItem: Int { get }
```

#### Discussion

If no item is selected, the value in this property is `-1`.

## See Also

- [var selectedItem: NSMenuItem?](nspopupbutton/selecteditem.md)
  The menu item that was last selected by the user.
- [var titleOfSelectedItem: String?](nspopupbutton/titleofselecteditem.md)
  The title of the item that was last selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/indexofselecteditem)*