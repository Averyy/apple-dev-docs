# indexOfSelectedItem

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The index of the item that was last selected by the user.

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

If no item is selected, the value in this property is `-1`.

## See Also

### Getting the user’s selection
- [var selectedItem: NSMenuItem?](./selecteditem.md)
  The menu item that was last selected by the user.
- [var titleOfSelectedItem: String?](./titleofselecteditem.md)
  The title of the item that was last selected by the user.
- [selectedTag](./selectedtag.md)
  The tag of the menu item that was last selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/indexofselecteditem)*