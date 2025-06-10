# numberOfItems(in:)

**Framework**: AppKit  
**Kind**: method

Returns the number of items that the data source manages for the combo box.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func numberOfItems(in comboBox: NSComboBox) -> Int
```

#### Return Value

The number of items that the data source object manages for the specified combo box.

#### Discussion

An `NSComboBox` object uses this method to determine how many items it should display in its pop-up list.

> ❗ **Important**:  While this method is marked as `@optional` in the protocol, you must implement this method if you are not providing the data for the combo box using Cocoa bindings.

## Parameters

- `comboBox`: The combo box.

## See Also

- [func comboBox(NSComboBox, completedString: String) -> String?](nscomboboxdatasource/combobox(_:completedstring:).md)
  Returns the first item from the pop-up list that starts with the text the user has typed.
- [func comboBox(NSComboBox, indexOfItemWithStringValue: String) -> Int](nscomboboxdatasource/combobox(_:indexofitemwithstringvalue:).md)
  Returns the index of the combo box item matching the specified string.
- [func comboBox(NSComboBox, objectValueForItemAt: Int) -> Any?](nscomboboxdatasource/combobox(_:objectvalueforitemat:).md)
  Returns the object that corresponds to the item at the specified index in the combo box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxdatasource/numberofitems(in:))*