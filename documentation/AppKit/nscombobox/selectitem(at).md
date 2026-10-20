# selectItem(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the pop-up list row at the given index.

**Availability**:
- macOS

## Declaration

```swift
func selectItem(at index: Int)
```

```objc
- (void) selectItemAtIndex:(NSInteger) index;
```

#### Discussion

Posts an [`selectionDidChangeNotification`](./selectiondidchangenotification.md) to the default notification center if the selection does in fact change. Note that this method does not alter the contents of the combo box’s text field.

## Parameters

- `index`: The index of the item to select in the pop-up list.

## See Also

### Related Documentation
- [var objectValue: Any?](../nscontrol/objectvalue.md)
  The value of the receiver’s cell as an Objective-C object.
### Manipulating the Selection
- [func deselectItem(at: Int)](./deselectitem%28at%29.md)
  Deselects the pop-up list item at the specified index if it’s selected.
- [var indexOfSelectedItem: Int](./indexofselecteditem.md)
  The index of the last item selected from the pop-up list.
- [var objectValueOfSelectedItem: Any?](./objectvalueofselecteditem.md)
  The object corresponding to the last item selected from the pop-up list.
- [func selectItem(withObjectValue: Any?)](./selectitem%28withobjectvalue%29.md)
  Selects the first pop-up list item that corresponds to the given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/selectitem(at:))*