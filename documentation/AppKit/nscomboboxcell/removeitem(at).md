# removeItem(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the object at the specified location from the combo box’s internal item list.

**Availability**:
- macOS

## Declaration

```swift
func removeItem(at index: Int)
```

```objc
- (void) removeItemAtIndex:(NSInteger) index;
```

#### Discussion

The removed object receives a `release` message. This method raises an `NSRangeException` if `index` is beyond the end of the list and logs a warning if [`usesDataSource`](./usesdatasource.md) is [`true`](../../Swift/true.md).

## Parameters

- `index`: The index of the object to remove from the combo box’s internal item list. All items beyond `index` are moved up one slot to fill the gap.

## See Also

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
- [func removeItem(withObjectValue: Any)](./removeitem%28withobjectvalue%29.md)
  Removes all occurrences of the specified object from the combo box’s internal item list.
- [var numberOfItems: Int](./numberofitems.md)
  The total number of items in the pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/removeitem(at:))*