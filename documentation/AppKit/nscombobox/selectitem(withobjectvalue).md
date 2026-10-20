# selectItem(withObjectValue:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Selects the first pop-up list item that corresponds to the given object.

**Availability**:
- macOS

## Declaration

```swift
func selectItem(withObjectValue object: Any?)
```

```objc
- (void) selectItemWithObjectValue:(id) object;
```

#### Discussion

This method logs a warning if [`usesDataSource`](./usesdatasource.md) returns [`true`](../../Swift/true.md). Posts an [`selectionDidChangeNotification`](./selectiondidchangenotification.md) to the default notification center if the selection does in fact change. Note that this method doesn’t alter the contents of the combo box’s text field.

## Parameters

- `object`: The object to select in the pop-up list.  Objects are considered equal if they have the same id or if `isEqual:` returns [`true`](../../Swift/true.md).

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
- [func selectItem(at: Int)](./selectitem%28at%29.md)
  Selects the pop-up list row at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/selectitem(withobjectvalue:))*