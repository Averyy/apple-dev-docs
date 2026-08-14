# selectItem(withObjectValue:)

**Framework**: AppKit  
**Kind**: method

Selects the first pop-up list item that corresponds to the given object.

**Availability**:
- macOS ?+

## Declaration

```swift
func selectItem(withObjectValue object: Any?)
```

#### Discussion

This method logs a warning if [`usesDataSource`](nscombobox/usesdatasource.md) returns [`true`](https://developer.apple.com/documentation/swift/true). Posts an [`selectionDidChangeNotification`](nscombobox/selectiondidchangenotification.md) to the default notification center if the selection does in fact change. Note that this method doesn’t alter the contents of the combo box’s text field.

## Parameters

- `object`: The object to select in the pop-up list.  Objects are considered equal if they have the same id or if `isEqual:` returns [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [var objectValue: Any?](nscontrol/objectvalue.md)
  The value of the receiver’s cell as an Objective-C object.
- [func deselectItem(at: Int)](nscombobox/deselectitem(at:).md)
  Deselects the pop-up list item at the specified index if it’s selected.
- [var indexOfSelectedItem: Int](nscombobox/indexofselecteditem.md)
  The index of the last item selected from the pop-up list.
- [var objectValueOfSelectedItem: Any?](nscombobox/objectvalueofselecteditem.md)
  The object corresponding to the last item selected from the pop-up list.
- [func selectItem(at: Int)](nscombobox/selectitem(at:).md)
  Selects the pop-up list row at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/selectitem(withobjectvalue:))*