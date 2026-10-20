# itemTitle(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the title of the item at the specified index.

**Availability**:
- macOS

## Declaration

```swift
func itemTitle(at index: Int) -> String
```

```objc
- (NSString *) itemTitleAtIndex:(NSInteger) index;
```

#### Return Value

The title of the item, or an empty string if no item exists at the specified index.

## Parameters

- `index`: The index of the item you want.

## See Also

### Related Documentation
- [func item(at: Int) -> NSMenuItem?](./item%28at%29.md)
  Returns the menu item at the specified index.
### Title conveniences
- [var itemTitles: [String]](./itemtitles.md)
  An array of `NSString` objects containing the titles of every item in the menu.
- [var titleOfSelectedItem: String?](./titleofselecteditem.md)
  The title of the item last selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/itemtitle(at:))*