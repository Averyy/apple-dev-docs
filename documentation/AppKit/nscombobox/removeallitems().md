# removeAllItems()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes all items from the receiver’s internal item list.

**Availability**:
- macOS

## Declaration

```swift
func removeAllItems()
```

```objc
- (void) removeAllItems;
```

## Discussion

This method logs a warning if the [`usesDataSource`](./usesdatasource.md) property is [`true`](../../Swift/true.md).

## See Also

### Configuring the Combo Box Items
- [func addItems(withObjectValues: [Any])](./additems%28withobjectvalues%29.md)
  Adds multiple objects to the end of the receiver’s internal item list.
- [func addItem(withObjectValue: Any)](./additem%28withobjectvalue%29.md)
  Adds an object to the end of the receiver’s internal item list.
- [func insertItem(withObjectValue: Any, at: Int)](./insertitem%28withobjectvalue,at%29.md)
  Inserts an object at the specified location in the receiver’s internal item list.
- [var objectValues: [Any]](./objectvalues.md)
  An array of the items from the combo box’s internal list.
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the object at the specified location from the receiver’s internal item list.
- [func removeItem(withObjectValue: Any)](./removeitem%28withobjectvalue%29.md)
  Removes all occurrences of the given object from the receiver’s internal item list.
- [var numberOfItems: Int](./numberofitems.md)
  The total number of items in the pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/removeallitems())*