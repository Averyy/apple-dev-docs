# insertItem(withObjectValue:at:)

**Framework**: AppKit  
**Kind**: method

Inserts an object at the specified location in the receiver’s internal item list.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func insertItem(withObjectValue object: Any, at index: Int)
```

#### Discussion

This method logs a warning if the [`usesDataSource`](nscombobox/usesdatasource.md) property is [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `object`: The object to add to the internal item list.
- `index`: The index in the list at which to add the new object. The previous item at  —along with all following items—is shifted down one slot to make room

## See Also

- [func addItems(withObjectValues: [Any])](nscombobox/additems(withobjectvalues:).md)
  Adds multiple objects to the end of the receiver’s internal item list.
- [func addItem(withObjectValue: Any)](nscombobox/additem(withobjectvalue:).md)
  Adds an object to the end of the receiver’s internal item list.
- [var objectValues: [Any]](nscombobox/objectvalues.md)
  An array of the items from the combo box’s internal list.
- [func removeAllItems()](nscombobox/removeallitems.md)
  Removes all items from the receiver’s internal item list.
- [func removeItem(at: Int)](nscombobox/removeitem(at:).md)
  Removes the object at the specified location from the receiver’s internal item list.
- [func removeItem(withObjectValue: Any)](nscombobox/removeitem(withobjectvalue:).md)
  Removes all occurrences of the given object from the receiver’s internal item list.
- [var numberOfItems: Int](nscombobox/numberofitems.md)
  The total number of items in the pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/insertitem(withobjectvalue:at:))*