# comboBox(_:indexOfItemWithStringValue:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the combo box item matching the specified string.

**Availability**:
- macOS

## Declaration

```swift
@MainActor
optional func comboBox(_ comboBox: NSComboBox, indexOfItemWithStringValue string: String) -> Int
```

```objc
- (NSUInteger) comboBox:(NSComboBox *) comboBox indexOfItemWithStringValue:(NSString *) string;
```

## Return Value

The index for the item that matches the specified string, or `NSNotFound` if no item matches.

## Discussion

An `NSComboBox` object uses this method to synchronize the pop-up list’s selected item with the text field’s contents.  If you don’t implement this method the receiver does not synchronize the pop-up list’s selected item with the text field’s contents.

## Parameters

- `comboBox`: The combo box.
- `string`: The string to match against the items in the combo box.  If the datasource implements[`comboBox(_:completedString:)`](./combobox%28_,completedstring%29.md), this is the string returned by that method. Otherwise, it is the text that the user has typed.

## See Also

### Instance Methods
- [func comboBox(NSComboBox, completedString: String) -> String?](./combobox%28_,completedstring%29.md)
  Returns the first item from the pop-up list that starts with the text the user has typed.
- [func comboBox(NSComboBox, objectValueForItemAt: Int) -> Any?](./combobox%28_,objectvalueforitemat%29.md)
  Returns the object that corresponds to the item at the specified index in the combo box.
- [func numberOfItems(in: NSComboBox) -> Int](./numberofitems%28in%29.md)
  Returns the number of items that the data source manages for the combo box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxdatasource/combobox(_:indexofitemwithstringvalue:))*