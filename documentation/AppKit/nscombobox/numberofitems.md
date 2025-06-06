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

- [var numberOfVisibleItems: Int](nscombobox/numberofvisibleitems.md)
  The maximum number of visible items to display in the pop-up list at one time.
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
- [func removeItem(withObjectValue: Any)](nscombobox/removeitem(withobjectvalue:).md)
  Removes all occurrences of the given object from the receiver’s internal item list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/numberofitems)*