# selectItem(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the item in the menu at the specified index.

**Availability**:
- macOS

## Declaration

```swift
func selectItem(at index: Int)
```

```objc
- (void) selectItemAtIndex:(NSInteger) index;
```

## Parameters

- `index`: The index of the item you want to select, or `-1` you want to deselect all menu items.

## See Also

### Related Documentation
- [var indexOfSelectedItem: Int](./indexofselecteditem.md)
  The index of the item that was last selected by the user.
### Setting the current selection
- [func select(NSMenuItem?)](./select%28_%29.md)
  Selects the specified menu item.
- [func selectItem(withTag: Int) -> Bool](./selectitem%28withtag%29.md)
  Selects the menu item with the specified tag.
- [func selectItem(withTitle: String)](./selectitem%28withtitle%29.md)
  Selects the item with the specified title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/selectitem(at:))*