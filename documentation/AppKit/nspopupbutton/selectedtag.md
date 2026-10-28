# selectedTag

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The tag of the menu item that was last selected by the user.

**Availability**:
- macOS

## Declaration

```objc
@property (readonly) NSInteger selectedTag;
```

## Discussion

Tags are integers that you assign to items to identify them in your code. Tags are not used by AppKit.

If no menu item is selected, the value in this property is `-1`.

## See Also

### Getting the user’s selection
- [var selectedItem: NSMenuItem?](./selecteditem.md)
  The menu item that was last selected by the user.
- [var titleOfSelectedItem: String?](./titleofselecteditem.md)
  The title of the item that was last selected by the user.
- [var indexOfSelectedItem: Int](./indexofselecteditem.md)
  The index of the item that was last selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/selectedtag)*