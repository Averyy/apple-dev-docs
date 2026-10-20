# insertItem(withObjectValue:at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts an object at the specified location in the internal item list.

**Availability**:
- macOS

## Declaration

```swift
func insertItem(withObjectValue object: Any, at index: Int)
```

```objc
- (void) insertItemWithObjectValue:(id) object atIndex:(NSInteger) index;
```

#### Discussion

This method logs a warning if [`usesDataSource`](./usesdatasource.md) is [`true`](../../Swift/true.md).

## Parameters

- `object`: The object to add to the combo box’s internal item list.
- `index`: The index at which to add the specified object.  The previous item at `index`—along with all following items—is shifted down one slot to make room.

## See Also

### Working with an Internal List
- [func addItems(withObjectValues: [Any])](./additems%28withobjectvalues%29.md)
  Adds multiple objects to the internal item list.
- [func addItem(withObjectValue: Any)](./additem%28withobjectvalue%29.md)
  Adds the specified object to the internal item list.
- [var objectValues: [Any]](./objectvalues.md)
  The combo box’s internal item list in an array.
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all items from the combo box’s internal item list.
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the object at the specified location from the combo box’s internal item list.
- [func removeItem(withObjectValue: Any)](./removeitem%28withobjectvalue%29.md)
  Removes all occurrences of the specified object from the combo box’s internal item list.
- [var numberOfItems: Int](./numberofitems.md)
  The total number of items in the pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/insertitem(withobjectvalue:at:))*