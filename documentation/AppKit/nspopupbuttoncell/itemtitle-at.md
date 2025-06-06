# itemTitle(at:)

**Framework**: AppKit  
**Kind**: method

Returns the title of the item at the specified index.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func itemTitle(at index: Int) -> String
```

#### Return Value

The title of the item, or an empty string if no item exists at the specified index.

## Parameters

- `index`: The index of the item you want.

## See Also

- [func item(at: Int) -> NSMenuItem?](nspopupbuttoncell/item(at:).md)
  Returns the menu item at the specified index.
- [var itemTitles: [String]](nspopupbuttoncell/itemtitles.md)
  An array of `NSString` objects containing the titles of every item in the menu.
- [var titleOfSelectedItem: String?](nspopupbuttoncell/titleofselecteditem.md)
  The title of the item last selected by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/itemtitle(at:))*