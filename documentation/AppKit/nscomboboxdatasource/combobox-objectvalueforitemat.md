# comboBox(_:objectValueForItemAt:)

**Framework**: AppKit  
**Kind**: method

Returns the object that corresponds to the item at the specified index in the combo box.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
optional func comboBox(_ comboBox: NSComboBox, objectValueForItemAt index: Int) -> Any?
```

#### Return Value

The object corresponding to the specified index number.

#### Discussion

An `NSComboBox` object uses this method to populate the items displayed in its pop-up list.

> ❗ **Important**:  While this method is marked as `@optional` in the protocol, you must implement this method if you are not providing the data for the combo box using Cocoa bindings.

 While this method is marked as `@optional` in the protocol, you must implement this method if you are not providing the data for the combo box using Cocoa bindings.

## Parameters

- `comboBox`: The combo box.
- `index`: The index of the item to return.

## See Also

- [Combo Box Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ComboBox/ComboBox.html#//apple_ref/doc/uid/10000020i)
- [func comboBox(NSComboBox, completedString: String) -> String?](nscomboboxdatasource/combobox(_:completedstring:).md)
  Returns the first item from the pop-up list that starts with the text the user has typed.
- [func comboBox(NSComboBox, indexOfItemWithStringValue: String) -> Int](nscomboboxdatasource/combobox(_:indexofitemwithstringvalue:).md)
  Returns the index of the combo box item matching the specified string.
- [func numberOfItems(in: NSComboBox) -> Int](nscomboboxdatasource/numberofitems(in:).md)
  Returns the number of items that the data source manages for the combo box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxdatasource/combobox(_:objectvalueforitemat:))*