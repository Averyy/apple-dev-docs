# indexOfSelectedItem

**Framework**: AppKit  
**Kind**: property

The index of the last item selected from the pop-up list.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var indexOfSelectedItem: Int { get }
```

#### Discussion

The index of the last item selected from the combo box’s pop-up list or –1 if no item is selected. Note that nothing is initially selected in a newly initialized combo box cell.

## See Also

- [func deselectItem(at: Int)](nscomboboxcell/deselectitem(at:).md)
  Deselects the pop-up list item at the given index if it’s selected.
- [var objectValueOfSelectedItem: Any?](nscomboboxcell/objectvalueofselecteditem.md)
  The object corresponding to the last item selected from the pop-up list.
- [func selectItem(at: Int)](nscomboboxcell/selectitem(at:).md)
  Selects the pop-up list row at the given index.
- [func selectItem(withObjectValue: Any?)](nscomboboxcell/selectitem(withobjectvalue:).md)
  Selects the first pop-up list item that corresponds to the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/indexofselecteditem)*