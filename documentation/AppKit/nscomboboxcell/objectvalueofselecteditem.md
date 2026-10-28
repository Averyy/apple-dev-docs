# objectValueOfSelectedItem

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The object corresponding to the last item selected from the pop-up list.

**Availability**:
- macOS

## Declaration

```swift
var objectValueOfSelectedItem: Any? { get }
```

```objc
@property (strong, readonly, nullable) id objectValueOfSelectedItem;
```

## Discussion

The value of this property is the object from the combo box’s internal item list corresponding to the last item selected from the pop-up list, or `nil` if no item is selected.

Note that nothing is initially selected in a newly initialized combo box cell. Accessing this property logs a warning if [`usesDataSource`](./usesdatasource.md) is [`true`](../../Swift/true.md).

## See Also

### Manipulating the Selection
- [func deselectItem(at: Int)](./deselectitem%28at%29.md)
  Deselects the pop-up list item at the given index if it’s selected.
- [var indexOfSelectedItem: Int](./indexofselecteditem.md)
  The index of the last item selected from the pop-up list.
- [func selectItem(at: Int)](./selectitem%28at%29.md)
  Selects the pop-up list row at the given index.
- [func selectItem(withObjectValue: Any?)](./selectitem%28withobjectvalue%29.md)
  Selects the first pop-up list item that corresponds to the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/objectvalueofselecteditem)*