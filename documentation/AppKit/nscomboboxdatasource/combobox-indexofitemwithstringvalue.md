# comboBox(_:indexOfItemWithStringValue:)

**Framework**: AppKit  
**Kind**: method

Returns the index of the combo box item matching the specified string.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func comboBox(_ comboBox: NSComboBox, indexOfItemWithStringValue string: String) -> Int
```

#### Return Value

The index for the item that matches the specified string, or `NSNotFound` if no item matches.

#### Discussion

An `NSComboBox` object uses this method to synchronize the pop-up list’s selected item with the text field’s contents.  If you don’t implement this method the receiver does not synchronize the pop-up list’s selected item with the text field’s contents.

## Parameters

- `comboBox`: The combo box.
- `string`: The string to match against the items in the combo box.  If the datasource implements , this is the string returned by that method. Otherwise, it is the text that the user has typed.

## See Also

- [func comboBox(NSComboBox, completedString: String) -> String?](nscomboboxdatasource/combobox(_:completedstring:).md)
  Returns the first item from the pop-up list that starts with the text the user has typed.
- [func comboBox(NSComboBox, objectValueForItemAt: Int) -> Any?](nscomboboxdatasource/combobox(_:objectvalueforitemat:).md)
  Returns the object that corresponds to the item at the specified index in the combo box.
- [func numberOfItems(in: NSComboBox) -> Int](nscomboboxdatasource/numberofitems(in:).md)
  Returns the number of items that the data source manages for the combo box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxdatasource/combobox(_:indexofitemwithstringvalue:))*