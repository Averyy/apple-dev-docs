# indexOfItem(withTitle:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the item with the specified title.

**Availability**:
- macOS

## Declaration

```swift
func indexOfItem(withTitle title: String) -> Int
```

```objc
- (NSInteger) indexOfItemWithTitle:(NSString *) title;
```

#### Return Value

The index of the item or `-1` if no item with the specified title was found.

## Parameters

- `title`: The title of the item you want.

## See Also

### Getting the indices of menu items
- [func index(of: NSMenuItem) -> Int](./index%28of%29.md)
  Returns the index of the specified menu item.
- [func indexOfItem(withTag: Int) -> Int](./indexofitem%28withtag%29.md)
  Returns the index of the menu item with the specified tag.
- [func indexOfItem(withRepresentedObject: Any?) -> Int](./indexofitem%28withrepresentedobject%29.md)
  Returns the index of the menu item that holds the specified represented object.
- [func indexOfItem(withTarget: Any?, andAction: Selector?) -> Int](./indexofitem%28withtarget,andaction%29.md)
  Returns the index of the menu item with the specified target and action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/indexofitem(withtitle:))*