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
  The maximum number of visible items to display in the pop-up list at one time.
### Configuring the Combo Box Items
- [func addItems(withObjectValues: [Any])](./additems%28withobjectvalues%29.md)
  Adds multiple objects to the end of the receiver’s internal item list.
- [func addItem(withObjectValue: Any)](./additem%28withobjectvalue%29.md)
  Adds an object to the end of the receiver’s internal item list.
- [func insertItem(withObjectValue: Any, at: Int)](./insertitem%28withobjectvalue,at%29.md)
  Inserts an object at the specified location in the receiver’s internal item list.
- [var objectValues: [Any]](./objectvalues.md)
  An array of the items from the combo box’s internal list.
- [func removeAllItems()](./removeallitems%28%29.md)
  Removes all items from the receiver’s internal item list.
- [func removeItem(at: Int)](./removeitem%28at%29.md)
  Removes the object at the specified location from the receiver’s internal item list.
- [func removeItem(withObjectValue: Any)](./removeitem%28withobjectvalue%29.md)
  Removes all occurrences of the given object from the receiver’s internal item list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/numberofitems)*