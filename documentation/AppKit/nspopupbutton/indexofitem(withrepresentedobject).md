# indexOfItem(withRepresentedObject:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the menu item that holds the specified represented object.

**Availability**:
- macOS

## Declaration

```swift
func indexOfItem(withRepresentedObject obj: Any?) -> Int
```

```objc
- (NSInteger) indexOfItemWithRepresentedObject:(id) obj;
```

## Return Value

The index of the menu item that owns the specified object, or `-1` if no such menu item was found.

## Discussion

Represented objects bear some direct relation to the title or image of a menu item; for example, an item entitled “100” might have an `NSNumber` object encapsulating that value as its represented object. This method invokes the method of the same name of its `NSPopUpButtonCell` object.

## Parameters

- `obj`: The represented object associated with a menu item.

## See Also

### Getting the indices of menu items
- [func index(of: NSMenuItem) -> Int](./index%28of%29.md)
  Returns the index of the specified menu item.
- [func indexOfItem(withTag: Int) -> Int](./indexofitem%28withtag%29.md)
  Returns the index of the menu item with the specified tag.
- [func indexOfItem(withTitle: String) -> Int](./indexofitem%28withtitle%29.md)
  Returns the index of the item with the specified title.
- [func indexOfItem(withTarget: Any?, andAction: Selector?) -> Int](./indexofitem%28withtarget,andaction%29.md)
  Returns the index of the menu item with the specified target and action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbutton/indexofitem(withrepresentedobject:))*