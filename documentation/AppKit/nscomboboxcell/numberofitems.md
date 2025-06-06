# numberOfItems

**Framework**: AppKit  
**Kind**: property

The total number of items in the pop-up list.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var numberOfItems: Int { get }
```

## See Also

- [var numberOfVisibleItems: Int](nscomboboxcell/numberofvisibleitems.md)
  The maximum number of items visible in the pop-up list at any one time.
- [func numberOfItems(in: NSComboBoxCell) -> Int](nscomboboxcelldatasource/numberofitems(in:).md)
  Returns the number of items managed for the combo box cell by your data source object.
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
- [func removeItem(withObjectValue: Any)](nscomboboxcell/removeitem(withobjectvalue:).md)
  Removes all occurrences of the specified object from the combo box’s internal item list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/numberofitems)*