# numberOfItems

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The total number of items in the pop-up list.

**Availability**:
- macOS

## Declaration

```swift
var numberOfItems: Int { get }
```

```objc
@property (readonly) NSInteger numberOfItems;
```

## See Also

### Related Documentation
- [var numberOfVisibleItems: Int](./numberofvisibleitems.md)
  The maximum number of items visible in the pop-up list at any one time.
- [func numberOfItems(in: NSComboBoxCell) -> Int](../nscomboboxcelldatasource/numberofitems%28in%29.md)
  Returns the number of items managed for the combo box cell by your data source object.
### Working with an Internal List
- [func addItems(withObjectValues: [Any])](./additems%28withobjectvalues%29.md)
  Adds multiple objects to the internal item list.
- [func addItem(withObjectValue: Any)](./additem%28withobjectvalue%29.md)
  Adds the specified object to the internal item list.
- [func insertItem(withObjectValue: Any, at: Int)](./insertitem%28withobjectvalue,at%29.md)
  Inserts an object at the specified location in the internal item list.
- [var objectValues: [Any]](./objectvalues.md)
  The combo box’s internal item list in an array.
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all items from the combo box’s internal item list.
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the object at the specified location from the combo box’s internal item list.
- [func removeItem(withObjectValue: Any)](./removeitem%28withobjectvalue%29.md)
  Removes all occurrences of the specified object from the combo box’s internal item list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/numberofitems)*