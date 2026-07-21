# selectItem(at:)

**Framework**: AppKit  
**Kind**: method

Selects the pop-up list row at the given index.

**Availability**:
- macOS ?+

## Declaration

```swift
func selectItem(at index: Int)
```

#### Discussion

Posts an [`selectionDidChangeNotification`](nscombobox/selectiondidchangenotification.md) to the default notification center if the selection does in fact change. Note that this method does not alter the contents of the combo box’s text field.

## Parameters

- `index`: The index of the item to select in the pop-up list.

## See Also

- [var objectValue: Any?](nscontrol/objectvalue.md)
  The value of the receiver’s cell as an Objective-C object.
- [func deselectItem(at: Int)](nscombobox/deselectitem(at:).md)
  Deselects the pop-up list item at the specified index if it’s selected.
- [var indexOfSelectedItem: Int](nscombobox/indexofselecteditem.md)
  The index of the last item selected from the pop-up list.
- [var objectValueOfSelectedItem: Any?](nscombobox/objectvalueofselecteditem.md)
  The object corresponding to the last item selected from the pop-up list.
- [func selectItem(withObjectValue: Any?)](nscombobox/selectitem(withobjectvalue:).md)
  Selects the first pop-up list item that corresponds to the given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/selectitem(at:))*