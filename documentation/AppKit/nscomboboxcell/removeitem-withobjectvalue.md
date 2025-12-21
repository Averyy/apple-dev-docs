# removeItem(withObjectValue:)

**Framework**: AppKit  
**Kind**: method

Removes all occurrences of the specified object from the combo box’s internal item list.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeItem(withObjectValue object: Any)
```

#### Discussion

This method logs a warning if [`usesDataSource`](nscomboboxcell/usesdatasource.md) is [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `object`: The object to remove from the combo box’s internal item list. Objects are considered equal if they have the same id or if   returns  .

## See Also

- [func indexOfItem(withObjectValue: Any) -> Int](nscomboboxcell/indexofitem(withobjectvalue:).md)
  Searches the combo box’s internal item list for the given object and returns the matching index number.
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
- [func removeItem(at: Int)](nscomboboxcell/removeitem(at:).md)
  Removes the object at the specified location from the combo box’s internal item list.
- [var numberOfItems: Int](nscomboboxcell/numberofitems.md)
  The total number of items in the pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/removeitem(withobjectvalue:))*