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

The value of this property is `-1` if no item is selected; otherwise, it is the index of the selected item. Nothing is selected in a newly initialized combo box.

## See Also

- [func deselectItem(at: Int)](nscombobox/deselectitem(at:).md)
  Deselects the pop-up list item at the specified index if it’s selected.
- [var objectValueOfSelectedItem: Any?](nscombobox/objectvalueofselecteditem.md)
  The object corresponding to the last item selected from the pop-up list.
- [func selectItem(at: Int)](nscombobox/selectitem(at:).md)
  Selects the pop-up list row at the given index.
- [func selectItem(withObjectValue: Any?)](nscombobox/selectitem(withobjectvalue:).md)
  Selects the first pop-up list item that corresponds to the given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/indexofselecteditem)*