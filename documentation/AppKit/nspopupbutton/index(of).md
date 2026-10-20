# index(of:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the specified menu item.

**Availability**:
- macOS

## Declaration

```swift
func index(of item: NSMenuItem) -> Int
```

```objc
- (NSInteger) indexOfItem:(NSMenuItem *) item;
```

#### Return Value

The index of the item or `-1` if no such item was found.

#### Discussion

This method invokes the method of the same name of its `NSPopUpButtonCell` object.

## Parameters

- `item`: The menu item whose index you want.

## See Also

### Getting the indices of menu items
- [func indexOfItem(withTag: Int) -> Int](./indexofitem%28withtag%29.md)
  Returns the index of the menu item with the specified tag.
- [func indexOfItem(withTitle: String) -> Int](./indexofitem%28withtitle%29.md)
  Returns the index of the item with the specified title.
- [func indexOfItem(withRepresentedObject: Any?) -> Int](./indexofitem%28withrepresentedobject%29.md)
  Returns the index of the menu item that holds the specified represented object.
- [func indexOfItem(withTarget: Any?, andAction: Selector?) -> Int](./indexofitem%28withtarget,andaction%29.md)
  Returns the index of the menu item with the specified target and action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/index(of:))*