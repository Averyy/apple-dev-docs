# objectValues

**Framework**: AppKit  
**Kind**: property

An array of the items from the combo box’s internal list.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var objectValues: [Any] { get }
```

#### Discussion

The array contains the objects you added or inserted into the combo box, so the type of each object can vary. Accessing this property logs a warning if the [`usesDataSource`](nscombobox/usesdatasource.md) property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [func addItems(withObjectValues: [Any])](nscombobox/additems(withobjectvalues:).md)
  Adds multiple objects to the end of the receiver’s internal item list.
- [func addItem(withObjectValue: Any)](nscombobox/additem(withobjectvalue:).md)
  Adds an object to the end of the receiver’s internal item list.
- [func insertItem(withObjectValue: Any, at: Int)](nscombobox/insertitem(withobjectvalue:at:).md)
  Inserts an object at the specified location in the receiver’s internal item list.
- [func removeAllItems()](nscombobox/removeallitems.md)
  Removes all items from the receiver’s internal item list.
- [func removeItem(at: Int)](nscombobox/removeitem(at:).md)
  Removes the object at the specified location from the receiver’s internal item list.
- [func removeItem(withObjectValue: Any)](nscombobox/removeitem(withobjectvalue:).md)
  Removes all occurrences of the given object from the receiver’s internal item list.
- [var numberOfItems: Int](nscombobox/numberofitems.md)
  The total number of items in the pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/objectvalues)*