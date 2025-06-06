# NSComboBoxDataSource

**Framework**: AppKit  
**Kind**: protocol

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSComboBoxDataSource : NSObjectProtocol
```

## Topics

### Instance Methods
- [func comboBox(NSComboBox, completedString: String) -> String?](nscomboboxdatasource/combobox(_:completedstring:).md)
  Returns the first item from the pop-up list that starts with the text the user has typed.
- [func comboBox(NSComboBox, indexOfItemWithStringValue: String) -> Int](nscomboboxdatasource/combobox(_:indexofitemwithstringvalue:).md)
  Returns the index of the combo box item matching the specified string.
- [func comboBox(NSComboBox, objectValueForItemAt: Int) -> Any?](nscomboboxdatasource/combobox(_:objectvalueforitemat:).md)
  Returns the object that corresponds to the item at the specified index in the combo box.
- [func numberOfItems(in: NSComboBox) -> Int](nscomboboxdatasource/numberofitems(in:).md)
  Returns the number of items that the data source manages for the combo box.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSComboBoxDelegate](nscomboboxdelegate.md)
  A set of optional methods implemented by delegates of combo box objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxdatasource)*