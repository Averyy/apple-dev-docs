# removeItem(at:)

**Framework**: AppKit  
**Kind**: method

Removes the object at the specified location from the receiver’s internal item list.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeItem(at index: Int)
```

#### Discussion

The removed object receives a `release` message. This method raises an `NSRangeException` if `index` is beyond the end of the list and logs a warning if the [`usesDataSource`](nscombobox/usesdatasource.md) property is [`true`](https://developer.apple.com/documentation/swift/true).

## Parameters

- `index`: The index of the object to remove. All items beyond   are moved up one slot to fill the gap.

## See Also

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
- [func removeItem(withObjectValue: Any)](nscombobox/removeitem(withobjectvalue:).md)
  Removes all occurrences of the given object from the receiver’s internal item list.
- [var numberOfItems: Int](nscombobox/numberofitems.md)
  The total number of items in the pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/removeitem(at:))*