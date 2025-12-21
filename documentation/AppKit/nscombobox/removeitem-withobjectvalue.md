# removeItem(withObjectValue:)

**Framework**: AppKit  
**Kind**: method

Removes all occurrences of the given object from the receiver’s internal item list.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeItem(withObjectValue object: Any)
```

#### Discussion

This method logs a warning if the [`usesDataSource`](nscombobox/usesdatasource.md) property is [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `object`: The object to remove from the internal item list. Objects are considered equal if they have the same id or if   returns  .

## See Also

- [func indexOfItem(withObjectValue: Any) -> Int](nscombobox/indexofitem(withobjectvalue:).md)
  Searches the receiver’s internal item list for the specified object and returns the lowest matching index.
- [func addItems(withObjectValues: [Any])](nscombobox/additems(withobjectvalues:).md)
  Adds multiple objects to the end of the receiver’s internal item list.
- [func addItem(withObjectValue: Any)](nscombobox/additem(withobjectvalue:).md)
  Adds an object to the end of the receiver’s internal item list.
- [func insertItem(withObjectValue: Any, at: Int)](nscombobox/insertitem(withobjectvalue:at:).md)
  Inserts an object at the specified location in the receiver’s internal item list.
- [var objectValues: [Any]](nscombobox/objectvalues.md)
  An array of the items from the combo box’s internal list.
- [func removeAllItems()](nscombobox/removeallitems.md)
  Removes all items from the receiver’s internal item list.
- [func removeItem(at: Int)](nscombobox/removeitem(at:).md)
  Removes the object at the specified location from the receiver’s internal item list.
- [var numberOfItems: Int](nscombobox/numberofitems.md)
  The total number of items in the pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/removeitem(withobjectvalue:))*