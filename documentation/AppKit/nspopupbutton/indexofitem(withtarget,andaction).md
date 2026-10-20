# indexOfItem(withTarget:andAction:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the menu item with the specified target and action.

**Availability**:
- macOS

## Declaration

```swift
func indexOfItem(withTarget target: Any?, andAction actionSelector: Selector?) -> Int
```

```objc
- (NSInteger) indexOfItemWithTarget:(id) target andAction:(SEL) actionSelector;
```

#### Return Value

The index of the menu item, or `-1` if no menu item contains the specified target and action.

#### Discussion

If you specify `NULL` for the `actionSelector` parameter, the index of the first menu item with the specified target is returned. This method invokes the method of the same name of its `NSPopUpButtonCell` object.

## Parameters

- `target`: The target object associated with the menu item.
- `actionSelector`: The action method associated with the menu item.

## See Also

### Getting the indices of menu items
- [func index(of: NSMenuItem) -> Int](./index%28of%29.md)
  Returns the index of the specified menu item.
- [func indexOfItem(withTag: Int) -> Int](./indexofitem%28withtag%29.md)
  Returns the index of the menu item with the specified tag.
- [func indexOfItem(withTitle: String) -> Int](./indexofitem%28withtitle%29.md)
  Returns the index of the item with the specified title.
- [func indexOfItem(withRepresentedObject: Any?) -> Int](./indexofitem%28withrepresentedobject%29.md)
  Returns the index of the menu item that holds the specified represented object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/indexofitem(withtarget:andaction:))*