# comboBox(_:objectValueForItemAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the object that corresponds to the item at the specified index in the combo box.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func comboBox(_ comboBox: NSComboBox, objectValueForItemAt index: Int) -> Any?
```

```objc
- (id) comboBox:(NSComboBox *) comboBox objectValueForItemAtIndex:(NSInteger) index;
```

#### Return Value

The object corresponding to the specified index number.

#### Discussion

An `NSComboBox` object uses this method to populate the items displayed in its pop-up list.

> ❗ **Important**:  While this method is marked as `@optional` in the protocol, you must implement this method if you are not providing the data for the combo box using Cocoa bindings.

## Parameters

- `comboBox`: The combo box.
- `index`: The index of the item to return.

## See Also

### Related Documentation
- [protocol NSComboBoxDataSource](../nscomboboxdatasource.md)
### Instance Methods
- [func comboBox(NSComboBox, completedString: String) -> String?](./combobox%28_,completedstring%29.md)
  Returns the first item from the pop-up list that starts with the text the user has typed.
- [func comboBox(NSComboBox, indexOfItemWithStringValue: String) -> Int](./combobox%28_,indexofitemwithstringvalue%29.md)
  Returns the index of the combo box item matching the specified string.
- [func numberOfItems(in: NSComboBox) -> Int](./numberofitems%28in%29.md)
  Returns the number of items that the data source manages for the combo box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxdatasource/combobox(_:objectvalueforitemat:))*