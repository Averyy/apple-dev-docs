# deselectItem(at:)

**Framework**: AppKit  
**Kind**: method

Deselects the pop-up list item at the given index if it’s selected.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func deselectItem(at index: Int)
```

#### Discussion

If the selection does in fact change, this method posts an [`selectionDidChangeNotification`](nscombobox/selectiondidchangenotification.md) to the default notification center.

## Parameters

- `index`: The index of the item to deselect.

## See Also

- [var numberOfItems: Int](nscomboboxcell/numberofitems.md)
  The total number of items in the pop-up list.
- [var indexOfSelectedItem: Int](nscomboboxcell/indexofselecteditem.md)
  The index of the last item selected from the pop-up list.
- [var objectValueOfSelectedItem: Any?](nscomboboxcell/objectvalueofselecteditem.md)
  The object corresponding to the last item selected from the pop-up list.
- [func selectItem(at: Int)](nscomboboxcell/selectitem(at:).md)
  Selects the pop-up list row at the given index.
- [func selectItem(withObjectValue: Any?)](nscomboboxcell/selectitem(withobjectvalue:).md)
  Selects the first pop-up list item that corresponds to the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/deselectitem(at:))*