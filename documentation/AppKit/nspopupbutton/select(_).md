# select(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the specified menu item.

**Availability**:
- macOS

## Declaration

```swift
func select(_ item: NSMenuItem?)
```

```objc
- (void) selectItem:(NSMenuItem *) item;
```

## Parameters

- `item`: The menu item to select, or `nil` if you want to deselect all menu items.

## See Also

### Setting the current selection
- [func selectItem(at: Int)](./selectitem%28at%29.md)
  Selects the item in the menu at the specified index.
- [func selectItem(withTag: Int) -> Bool](./selectitem%28withtag%29.md)
  Selects the menu item with the specified tag.
- [func selectItem(withTitle: String)](./selectitem%28withtitle%29.md)
  Selects the item with the specified title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/select(_:))*