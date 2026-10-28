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

## Discussion

The value of this property is `-1` if no item is selected; otherwise, it is the index of the selected item. Nothing is selected in a newly initialized combo box.

## See Also

### Manipulating the Selection
- [func deselectItem(at: Int)](./deselectitem%28at%29.md)
  Deselects the pop-up list item at the specified index if it’s selected.
- [var objectValueOfSelectedItem: Any?](./objectvalueofselecteditem.md)
  The object corresponding to the last item selected from the pop-up list.
- [func selectItem(at: Int)](./selectitem%28at%29.md)
  Selects the pop-up list row at the given index.
- [func selectItem(withObjectValue: Any?)](./selectitem%28withobjectvalue%29.md)
  Selects the first pop-up list item that corresponds to the given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/indexofselecteditem)*