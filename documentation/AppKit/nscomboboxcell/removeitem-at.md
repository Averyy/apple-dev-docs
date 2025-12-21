# removeItem(at:)

**Framework**: AppKit  
**Kind**: method

Removes the object at the specified location from the combo box’s internal item list.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeItem(at index: Int)
```

#### Discussion

The removed object receives a `release` message. This method raises an `NSRangeException` if `index` is beyond the end of the list and logs a warning if [`usesDataSource`](nscomboboxcell/usesdatasource.md) is [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `index`: The index of the object to remove from the combo box’s internal item list. All items beyond   are moved up one slot to fill the gap.

## See Also

- [func addItems(withObjectValues: [Any])](nscomboboxcell/additems(withobjectvalues:).md)
  Adds multiple objects to the internal item list.
- [func addItem(withObjectValue: Any)](nscomboboxcell/additem(withobjectvalue:).md)
  Adds the specified object to the internal item list.
- [func insertItem(withObjectValue: Any, at: Int)](nscomboboxcell/insertitem(withobjectvalue:at:).md)
  Inserts an object at the specified location in the internal item list.
- [var objectValues: [Any]](nscomboboxcell/objectvalues.md)
  The combo box’s internal item list in an array.
- [func removeAllItems()](nscomboboxcell/removeallitems.md)
  Removes all items from the combo box’s internal item list.
- [func removeItem(withObjectValue: Any)](nscomboboxcell/removeitem(withobjectvalue:).md)
  Removes all occurrences of the specified object from the combo box’s internal item list.
- [var numberOfItems: Int](nscomboboxcell/numberofitems.md)
  The total number of items in the pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/removeitem(at:))*