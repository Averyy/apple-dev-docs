# removeItem(withObjectValue:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes all occurrences of the specified object from the combo box’s internal item list.

**Availability**:
- macOS

## Declaration

```swift
func removeItem(withObjectValue object: Any)
```

```objc
- (void) removeItemWithObjectValue:(id) object;
```

#### Discussion

This method logs a warning if [`usesDataSource`](./usesdatasource.md) is [`true`](../../Swift/true.md).

## Parameters

- `object`: The object to remove from the combo box’s internal item list. Objects are considered equal if they have the same id or if `isEqual:` returns [`true`](../../Swift/true.md).

## See Also

### Related Documentation
- [func indexOfItem(withObjectValue: Any) -> Int](./indexofitem%28withobjectvalue%29.md)
  Searches the combo box’s internal item list for the given object and returns the matching index number.
### Working with an Internal List
- [func addItems(withObjectValues: [Any])](./additems%28withobjectvalues%29.md)
  Adds multiple objects to the internal item list.
- [func addItem(withObjectValue: Any)](./additem%28withobjectvalue%29.md)
  Adds the specified object to the internal item list.
- [func insertItem(withObjectValue: Any, at: Int)](./insertitem%28withobjectvalue,at%29.md)
  Inserts an object at the specified location in the internal item list.
- [var objectValues: [Any]](./objectvalues.md)
  The combo box’s internal item list in an array.
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all items from the combo box’s internal item list.
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the object at the specified location from the combo box’s internal item list.
- [var numberOfItems: Int](./numberofitems.md)
  The total number of items in the pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/removeitem(withobjectvalue:))*