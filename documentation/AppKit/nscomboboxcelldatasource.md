# NSComboBoxCellDataSource

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- macOS

## Declaration

```swift
protocol NSComboBoxCellDataSource : NSObjectProtocol
```

```objc
@protocol NSComboBoxCellDataSource <NSObject>
```

## Topics

### Instance Methods
- [func comboBoxCell(NSComboBoxCell, completedString: String) -> String?](./nscomboboxcelldatasource/comboboxcell%28_,completedstring%29.md)
  Returns the item from the combo box’s pop-up list that matches the text entered by the user.
- [func comboBoxCell(NSComboBoxCell, indexOfItemWithStringValue: String) -> Int](./nscomboboxcelldatasource/comboboxcell%28_,indexofitemwithstringvalue%29.md)
  Invoked by an `NSComboBoxCell` object to synchronize the pop-up list’s selected item with the text field’s contents.
- [func comboBoxCell(NSComboBoxCell, objectValueForItemAt: Int) -> Any](./nscomboboxcelldatasource/comboboxcell%28_,objectvalueforitemat%29.md)
  Returns the object that corresponds to the item at the given index in the combo box cell.
- [func numberOfItems(in: NSComboBoxCell) -> Int](./nscomboboxcelldatasource/numberofitems%28in%29.md)
  Returns the number of items managed for the combo box cell by your data source object.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Cells
- [class NSComboBoxCell](./nscomboboxcell.md)
  The user interface of a combo box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcelldatasource)*