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

#### Discussion

For combo boxes that use their own internally maintained list of items, this property contains the object in that list that is selected. If no item is selected, the value in this property is `nil`. Nothing is selected in a newly initialized combo box. This method logs a warning if the [`usesDataSource`](./usesdatasource.md) property is [`true`](../../Swift/true.md).

## See Also

### Manipulating the Selection
- [func deselectItem(at: Int)](./deselectitem%28at%29.md)
  Deselects the pop-up list item at the specified index if it’s selected.
- [var indexOfSelectedItem: Int](./indexofselecteditem.md)
  The index of the last item selected from the pop-up list.
- [func selectItem(at: Int)](./selectitem%28at%29.md)
  Selects the pop-up list row at the given index.
- [func selectItem(withObjectValue: Any?)](./selectitem%28withobjectvalue%29.md)
  Selects the first pop-up list item that corresponds to the given object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/objectvalueofselecteditem)*