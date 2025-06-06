# numberOfItems(in:)

**Framework**: AppKit  
**Kind**: method

Returns the number of items managed for the combo box cell by your data source object.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func numberOfItems(in comboBoxCell: NSComboBoxCell) -> Int
```

#### Return Value

The number of items your data source object manages.

#### Discussion

An `NSComboBoxCell` object uses this method to determine how many items it should display in its pop-up list.

> ❗ **Important**:  While this method is marked as `@optional` in the protocol, .

 While this method is marked as `@optional` in the protocol, .

## Parameters

- `comboBoxCell`: The combo box cell for which your data source manages items.

## See Also

- [func comboBoxCell(NSComboBoxCell, completedString: String) -> String?](nscomboboxcelldatasource/comboboxcell(_:completedstring:).md)
  Returns the item from the combo box’s pop-up list that matches the text entered by the user.
- [func comboBoxCell(NSComboBoxCell, indexOfItemWithStringValue: String) -> Int](nscomboboxcelldatasource/comboboxcell(_:indexofitemwithstringvalue:).md)
  Invoked by an `NSComboBoxCell` object to synchronize the pop-up list’s selected item with the text field’s contents.
- [func comboBoxCell(NSComboBoxCell, objectValueForItemAt: Int) -> Any](nscomboboxcelldatasource/comboboxcell(_:objectvalueforitemat:).md)
  Returns the object that corresponds to the item at the given index in the combo box cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcelldatasource/numberofitems(in:))*