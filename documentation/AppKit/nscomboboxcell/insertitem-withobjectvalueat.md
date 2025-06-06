# insertItem(withObjectValue:at:)

**Framework**: AppKit  
**Kind**: method

Inserts an object at the specified location in the internal item list.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func insertItem(withObjectValue object: Any, at index: Int)
```

#### Discussion

This method logs a warning if [`usesDataSource`](nscomboboxcell/usesdatasource.md) is [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `object`: The object to add to the combo box’s internal item list.
- `index`: The index at which to add the specified object.  The previous item at  —along with all following items—is shifted down one slot to make room.

## See Also

- [func addItems(withObjectValues: [Any])](nscomboboxcell/additems(withobjectvalues:).md)
  Adds multiple objects to the internal item list.
- [func addItem(withObjectValue: Any)](nscomboboxcell/additem(withobjectvalue:).md)
  Adds the specified object to the internal item list.
- [var objectValues: [Any]](nscomboboxcell/objectvalues.md)
  The combo box’s internal item list in an array.
- [func removeAllItems()](nscomboboxcell/removeallitems.md)
  Removes all items from the combo box’s internal item list.
- [func removeItem(at: Int)](nscomboboxcell/removeitem(at:).md)
  Removes the object at the specified location from the combo box’s internal item list.
- [func removeItem(withObjectValue: Any)](nscomboboxcell/removeitem(withobjectvalue:).md)
  Removes all occurrences of the specified object from the combo box’s internal item list.
- [var numberOfItems: Int](nscomboboxcell/numberofitems.md)
  The total number of items in the pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/insertitem(withobjectvalue:at:))*