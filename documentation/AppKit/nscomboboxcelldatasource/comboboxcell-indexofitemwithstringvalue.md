# comboBoxCell(_:indexOfItemWithStringValue:)

**Framework**: AppKit  
**Kind**: method

Invoked by an `NSComboBoxCell` object to synchronize the pop-up list’s selected item with the text field’s contents.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func comboBoxCell(_ comboBoxCell: NSComboBoxCell, indexOfItemWithStringValue string: String) -> Int
```

#### Return Value

The index for the pop-up list item matching `aString`, or `NSNotFound` if no item matches.

#### Discussion

If you don’t implement this method, the receiver does not synchronize the pop-up list’s selected item with the text field’s contents.

## Parameters

- `comboBoxCell`: The combo box cell.
- `string`: The string to match. If   is implemented,   is the string returned by that method. Otherwise,   is the text that the user has typed.

## See Also

- [func comboBoxCell(NSComboBoxCell, completedString: String) -> String?](nscomboboxcelldatasource/comboboxcell(_:completedstring:).md)
  Returns the item from the combo box’s pop-up list that matches the text entered by the user.
- [func comboBoxCell(NSComboBoxCell, objectValueForItemAt: Int) -> Any](nscomboboxcelldatasource/comboboxcell(_:objectvalueforitemat:).md)
  Returns the object that corresponds to the item at the given index in the combo box cell.
- [func numberOfItems(in: NSComboBoxCell) -> Int](nscomboboxcelldatasource/numberofitems(in:).md)
  Returns the number of items managed for the combo box cell by your data source object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcelldatasource/comboboxcell(_:indexofitemwithstringvalue:))*