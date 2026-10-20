# titleOfSelectedItem

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The title of the item last selected by the user.

**Availability**:
- macOS

## Declaration

```swift
var titleOfSelectedItem: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * titleOfSelectedItem;
```

#### Discussion

The value of this property is the title of the selected menu item, or an empty string if no item is selected.

## See Also

### Related Documentation
- [func selectItem(withTitle: String)](./selectitem%28withtitle%29.md)
  Selects the item with the specified title.
### Title conveniences
- [func itemTitle(at: Int) -> String](./itemtitle%28at%29.md)
  Returns the title of the item at the specified index.
- [var itemTitles: [String]](./itemtitles.md)
  An array of `NSString` objects containing the titles of every item in the menu.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/titleofselecteditem)*