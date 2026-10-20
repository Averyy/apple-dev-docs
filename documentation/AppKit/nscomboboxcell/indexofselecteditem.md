# indexOfSelectedItem

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The index of the last item selected from the pop-up list.

**Availability**:
- macOS

## Declaration

```swift
var indexOfSelectedItem: Int { get }
```

```objc
@property (readonly) NSInteger indexOfSelectedItem;
```

#### Discussion

The index of the last item selected from the combo box’s pop-up list or –1 if no item is selected. Note that nothing is initially selected in a newly initialized combo box cell.

## See Also

### Manipulating the Selection
- [func deselectItem(at: Int)](./deselectitem%28at%29.md)
  Deselects the pop-up list item at the given index if it’s selected.
- [var objectValueOfSelectedItem: Any?](./objectvalueofselecteditem.md)
  The object corresponding to the last item selected from the pop-up list.
- [func selectItem(at: Int)](./selectitem%28at%29.md)
  Selects the pop-up list row at the given index.
- [func selectItem(withObjectValue: Any?)](./selectitem%28withobjectvalue%29.md)
  Selects the first pop-up list item that corresponds to the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/indexofselecteditem)*