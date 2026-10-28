# titleOfSelectedItem

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The title of the item that was last selected by the user.

**Availability**:
- macOS

## Declaration

```swift
var titleOfSelectedItem: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * titleOfSelectedItem;
```

## Discussion

If no item is selected, the value in this property is `nil`.

## See Also

### Getting the user’s selection
- [var selectedItem: NSMenuItem?](./selecteditem.md)
  The menu item that was last selected by the user.
- [var indexOfSelectedItem: Int](./indexofselecteditem.md)
  The index of the item that was last selected by the user.
- [selectedTag](./selectedtag.md)
  The tag of the menu item that was last selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/titleofselecteditem)*