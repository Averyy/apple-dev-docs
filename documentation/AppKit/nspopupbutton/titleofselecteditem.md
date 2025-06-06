# titleOfSelectedItem

**Framework**: AppKit  
**Kind**: property

The title of the item that was last selected by the user.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var titleOfSelectedItem: String? { get }
```

#### Discussion

If no item is selected, the value in this property is `nil`.

## See Also

- [var selectedItem: NSMenuItem?](nspopupbutton/selecteditem.md)
  The menu item that was last selected by the user.
- [var indexOfSelectedItem: Int](nspopupbutton/indexofselecteditem.md)
  The index of the item that was last selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/titleofselecteditem)*