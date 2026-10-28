# removeItem(withObjectValue:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes all occurrences of the given object from the receiver’s internal item list.

**Availability**:
- macOS

## Declaration

```swift
func removeItem(withObjectValue object: Any)
```

```objc
- (void) removeItemWithObjectValue:(id) object;
```

## Discussion

This method logs a warning if the [`usesDataSource`](./usesdatasource.md) property is [`true`](../../Swift/true.md).

## Parameters

- `object`: The object to remove from the internal item list. Objects are considered equal if they have the same id or if `isEqual:` returns [`true`](../../Swift/true.md).

## See Also

### Related Documentation
- [func indexOfItem(withObjectValue: Any) -> Int](./indexofitem%28withobjectvalue%29.md)
  Searches the receiver’s internal item list for the specified object and returns the lowest matching index.
### Configuring the Combo Box Items
- [func addItems(withObjectValues: [Any])](./additems%28withobjectvalues%29.md)
  Adds multiple objects to the end of the receiver’s internal item list.
- [func addItem(withObjectValue: Any)](./additem%28withobjectvalue%29.md)
  Adds an object to the end of the receiver’s internal item list.
- [func insertItem(withObjectValue: Any, at: Int)](./insertitem%28withobjectvalue,at%29.md)
  Inserts an object at the specified location in the receiver’s internal item list.
- [var objectValues: [Any]](./objectvalues.md)
  An array of the items from the combo box’s internal list.
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all items from the receiver’s internal item list.
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the object at the specified location from the receiver’s internal item list.
- [var numberOfItems: Int](./numberofitems.md)
  The total number of items in the pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/removeitem(withobjectvalue:))*