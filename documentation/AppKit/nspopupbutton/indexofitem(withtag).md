# indexOfItem(withTag:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the menu item with the specified tag.

**Availability**:
- macOS

## Declaration

```swift
func indexOfItem(withTag tag: Int) -> Int
```

```objc
- (NSInteger) indexOfItemWithTag:(NSInteger) tag;
```

#### Return Value

The index of the item or `-1` if no item with the specified tag was found.

#### Discussion

This method invokes the method of the same name of its `NSPopUpButtonCell` object.

## Parameters

- `tag`: The tag of the menu item you want.

## See Also

### Getting the indices of menu items
- [func index(of: NSMenuItem) -> Int](./index%28of%29.md)
  Returns the index of the specified menu item.
- [func indexOfItem(withTitle: String) -> Int](./indexofitem%28withtitle%29.md)
  Returns the index of the item with the specified title.
- [func indexOfItem(withRepresentedObject: Any?) -> Int](./indexofitem%28withrepresentedobject%29.md)
  Returns the index of the menu item that holds the specified represented object.
- [func indexOfItem(withTarget: Any?, andAction: Selector?) -> Int](./indexofitem%28withtarget,andaction%29.md)
  Returns the index of the menu item with the specified target and action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/indexofitem(withtag:))*