# selectItem(withTag:)

**Framework**: AppKit  
**Kind**: method

Selects the menu item with the specified tag.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectItem(withTag tag: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the item was successfully selected; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

If no item with the specified tag is found, this method returns [`false`](https://developer.apple.com/documentation/swift/false) and leaves the menu state unchanged.

You typically assign tags to menu items from Interface Builder, but you can also assign them programmatically using the setTag: method of `NSMenuItem`.

## Parameters

- `tag`: The tag of the item you want to select.

## See Also

- [func indexOfItem(withTag: Int) -> Int](nspopupbutton/indexofitem(withtag:).md)
  Returns the index of the menu item with the specified tag.
- [func select(NSMenuItem?)](nspopupbutton/select(_:).md)
  Selects the specified menu item.
- [func selectItem(at: Int)](nspopupbutton/selectitem(at:).md)
  Selects the item in the menu at the specified index.
- [func selectItem(withTitle: String)](nspopupbutton/selectitem(withtitle:).md)
  Selects the item with the specified title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/selectitem(withtag:))*