# dataSource

**Framework**: AppKit  
**Kind**: property

The object that provides the data displayed in the combo box’s pop-up list.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
unowned(unsafe) var dataSource: (any NSComboBoxCellDataSource)? { get set }
```

#### Discussion

The value of this property should be an object that implements the appropriate methods of the NSComboBoxCellDataSource informal protocol. Note that setting this property doesn’t automatically set [`usesDataSource`](nscomboboxcell/usesdatasource.md) to [`false`](https://developer.apple.com/documentation/Swift/false) and in fact logs a warning if [`usesDataSource`](nscomboboxcell/usesdatasource.md) is [`false`](https://developer.apple.com/documentation/Swift/false). If you set this property to an object that doesn’t respond to either numberOfItemsInComboBoxCell: or comboBoxCell:objectValueForItemAtIndex:, a warning is logged if [`usesDataSource`](nscomboboxcell/usesdatasource.md) is [`false`](https://developer.apple.com/documentation/Swift/false). See the class description and the NSComboBoxCellDataSource informal protocol specification for more information on combo box cell data source objects.

## See Also

- [var usesDataSource: Bool](nscomboboxcell/usesdatasource.md)
  A Boolean value that indicates if the combo box uses an external data source to populate its pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/datasource)*