# objectValueOfSelectedItem

**Framework**: AppKit  
**Kind**: property

The object corresponding to the last item selected from the pop-up list.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var objectValueOfSelectedItem: Any? { get }
```

#### Discussion

The value of this property is the object from the combo box’s internal item list corresponding to the last item selected from the pop-up list, or `nil` if no item is selected.

Note that nothing is initially selected in a newly initialized combo box cell. Accessing this property logs a warning if [`usesDataSource`](nscomboboxcell/usesdatasource.md) is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [func deselectItem(at: Int)](nscomboboxcell/deselectitem(at:).md)
  Deselects the pop-up list item at the given index if it’s selected.
- [var indexOfSelectedItem: Int](nscomboboxcell/indexofselecteditem.md)
  The index of the last item selected from the pop-up list.
- [func selectItem(at: Int)](nscomboboxcell/selectitem(at:).md)
  Selects the pop-up list row at the given index.
- [func selectItem(withObjectValue: Any?)](nscomboboxcell/selectitem(withobjectvalue:).md)
  Selects the first pop-up list item that corresponds to the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/objectvalueofselecteditem)*