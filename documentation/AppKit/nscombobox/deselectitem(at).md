# deselectItem(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Deselects the pop-up list item at the specified index if it’s selected.

**Availability**:
- macOS

## Declaration

```swift
func deselectItem(at index: Int)
```

```objc
- (void) deselectItemAtIndex:(NSInteger) index;
```

#### Discussion

If the selection does in fact change, this method posts an [`selectionDidChangeNotification`](./selectiondidchangenotification.md) to the default notification center.

## Parameters

- `index`: The index of the item to deselect.

## See Also

### Related Documentation
- [var numberOfItems: Int](./numberofitems.md)
  The total number of items in the pop-up list.
### Manipulating the Selection
- [var indexOfSelectedItem: Int](./indexofselecteditem.md)
  The index of the last item selected from the pop-up list.
- [var objectValueOfSelectedItem: Any?](./objectvalueofselecteditem.md)
  The object corresponding to the last item selected from the pop-up list.
- [func selectItem(at: Int)](./selectitem%28at%29.md)
  Selects the pop-up list row at the given index.
- [func selectItem(withObjectValue: Any?)](./selectitem%28withobjectvalue%29.md)
  Selects the first pop-up list item that corresponds to the given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/deselectitem(at:))*