# comboBoxCell(_:objectValueForItemAt:)

**Framework**: AppKit  
**Kind**: method

Returns the object that corresponds to the item at the given index in the combo box cell.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func comboBoxCell(_ comboBoxCell: NSComboBoxCell, objectValueForItemAt index: Int) -> Any
```

#### Return Value

The object corresponding to the item at the specified index in the given combo box cell.

#### Discussion

An `NSComboBoxCell` object uses this method to populate the items displayed in its pop-up list.

> ❗ **Important**:  While this method is marked as `@optional` in the protocol, .

 While this method is marked as `@optional` in the protocol, .

## Parameters

- `comboBoxCell`: The combo box cell for which to return the item.
- `index`: The index of the item to return.

## See Also

- [Combo Box Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ComboBox/ComboBox.html#//apple_ref/doc/uid/10000020i)
- [func comboBoxCell(NSComboBoxCell, completedString: String) -> String?](nscomboboxcelldatasource/comboboxcell(_:completedstring:).md)
  Returns the item from the combo box’s pop-up list that matches the text entered by the user.
- [func comboBoxCell(NSComboBoxCell, indexOfItemWithStringValue: String) -> Int](nscomboboxcelldatasource/comboboxcell(_:indexofitemwithstringvalue:).md)
  Invoked by an `NSComboBoxCell` object to synchronize the pop-up list’s selected item with the text field’s contents.
- [func numberOfItems(in: NSComboBoxCell) -> Int](nscomboboxcelldatasource/numberofitems(in:).md)
  Returns the number of items managed for the combo box cell by your data source object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcelldatasource/comboboxcell(_:objectvalueforitemat:))*