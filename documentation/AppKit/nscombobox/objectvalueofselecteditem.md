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

For combo boxes that use their own internally maintained list of items, this property contains the object in that list that is selected. If no item is selected, the value in this property is `nil`. Nothing is selected in a newly initialized combo box. This method logs a warning if the [`usesDataSource`](nscombobox/usesdatasource.md) property is [`true`](https://developer.apple.com/documentation/swift/true).

## See Also

- [func deselectItem(at: Int)](nscombobox/deselectitem(at:).md)
  Deselects the pop-up list item at the specified index if it’s selected.
- [var indexOfSelectedItem: Int](nscombobox/indexofselecteditem.md)
  The index of the last item selected from the pop-up list.
- [func selectItem(at: Int)](nscombobox/selectitem(at:).md)
  Selects the pop-up list row at the given index.
- [func selectItem(withObjectValue: Any?)](nscombobox/selectitem(withobjectvalue:).md)
  Selects the first pop-up list item that corresponds to the given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/objectvalueofselecteditem)*