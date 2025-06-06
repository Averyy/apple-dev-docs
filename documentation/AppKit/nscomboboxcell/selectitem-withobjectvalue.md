# selectItem(withObjectValue:)

**Framework**: AppKit  
**Kind**: method

Selects the first pop-up list item that corresponds to the specified object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectItem(withObjectValue object: Any?)
```

#### Discussion

This method logs a warning if [`usesDataSource`](nscomboboxcell/usesdatasource.md) is [`true`](https://developer.apple.com/documentation/swift/true). Posts an [`selectionDidChangeNotification`](nscombobox/selectiondidchangenotification.md) to the default notification center if the selection does in fact change. Note that this method doesn’t alter the contents of the combo box cell’s text field—see [`Setting the Combo Box’s Value`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ComboBox/Tasks/SettingComboBoxValue.html#//apple_ref/doc/uid/20000256) for more information.

## Parameters

- `object`: The object for which to select the corresponding pop-up list item. Objects are considered equal if they have the same id or if   returns  .

## See Also

- [var objectValue: Any?](nscontrol/objectvalue.md)
  The value of the receiver’s cell as an Objective-C object.
- [func deselectItem(at: Int)](nscomboboxcell/deselectitem(at:).md)
  Deselects the pop-up list item at the given index if it’s selected.
- [var indexOfSelectedItem: Int](nscomboboxcell/indexofselecteditem.md)
  The index of the last item selected from the pop-up list.
- [var objectValueOfSelectedItem: Any?](nscomboboxcell/objectvalueofselecteditem.md)
  The object corresponding to the last item selected from the pop-up list.
- [func selectItem(at: Int)](nscomboboxcell/selectitem(at:).md)
  Selects the pop-up list row at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/selectitem(withobjectvalue:))*