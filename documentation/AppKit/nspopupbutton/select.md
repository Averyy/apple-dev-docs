# select(_:)

**Framework**: AppKit  
**Kind**: method

Selects the specified menu item.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func select(_ item: NSMenuItem?)
```

## Parameters

- `item`: The menu item to select, or   if you want to deselect all menu items.

## See Also

- [func selectItem(at: Int)](nspopupbutton/selectitem(at:).md)
  Selects the item in the menu at the specified index.
- [func selectItem(withTag: Int) -> Bool](nspopupbutton/selectitem(withtag:).md)
  Selects the menu item with the specified tag.
- [func selectItem(withTitle: String)](nspopupbutton/selectitem(withtitle:).md)
  Selects the item with the specified title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/select(_:))*