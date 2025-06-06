# selectItem(at:)

**Framework**: AppKit  
**Kind**: method

Selects the pop-up list row at the given index.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectItem(at index: Int)
```

#### Discussion

Posts an [`selectionDidChangeNotification`](nscombobox/selectiondidchangenotification.md) to the default notification center if the selection does in fact change. Note that this method does not alter the contents of the combo box cell’s text field—see [`Combo Box Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ComboBox/ComboBox.html#//apple_ref/doc/uid/10000020i) for more information.

## Parameters

- `index`: The index of the row to select.

## See Also

- [var objectValue: Any?](nscontrol/objectvalue.md)
  The value of the receiver’s cell as an Objective-C object.
- [func deselectItem(at: Int)](nscomboboxcell/deselectitem(at:).md)
  Deselects the pop-up list item at the given index if it’s selected.
- [var indexOfSelectedItem: Int](nscomboboxcell/indexofselecteditem.md)
  The index of the last item selected from the pop-up list.
- [var objectValueOfSelectedItem: Any?](nscomboboxcell/objectvalueofselecteditem.md)
  The object corresponding to the last item selected from the pop-up list.
- [func selectItem(withObjectValue: Any?)](nscomboboxcell/selectitem(withobjectvalue:).md)
  Selects the first pop-up list item that corresponds to the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/selectitem(at:))*