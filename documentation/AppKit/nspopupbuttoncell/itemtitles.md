# itemTitles

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of `NSString` objects containing the titles of every item in the menu.

**Availability**:
- macOS

## Declaration

```swift
var itemTitles: [String] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * itemTitles;
```

#### Discussion

The titles appear in the order in which the items appear in the menu. If the menu contains separator items, the array contains an empty string (`@""`) for each separator item.

## See Also

### Title conveniences
- [func itemTitle(at: Int) -> String](./itemtitle%28at%29.md)
  Returns the title of the item at the specified index.
- [var titleOfSelectedItem: String?](./titleofselecteditem.md)
  The title of the item last selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/itemtitles)*