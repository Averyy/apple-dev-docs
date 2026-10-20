# dataSource

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The object that provides the data displayed in the combo box’s pop-up list.

**Availability**:
- macOS

## Declaration

```swift
unowned(unsafe) var dataSource: (any NSComboBoxCellDataSource)? { get set }
```

```objc
@property (assign, nullable) id<NSComboBoxCellDataSource> dataSource;
```

#### Discussion

The value of this property should be an object that implements the appropriate methods of the NSComboBoxCellDataSource informal protocol. Note that setting this property doesn’t automatically set [`usesDataSource`](./usesdatasource.md) to [`false`](../../Swift/false.md) and in fact logs a warning if [`usesDataSource`](./usesdatasource.md) is [`false`](../../Swift/false.md). If you set this property to an object that doesn’t respond to either numberOfItemsInComboBoxCell: or comboBoxCell:objectValueForItemAtIndex:, a warning is logged if [`usesDataSource`](./usesdatasource.md) is [`false`](../../Swift/false.md). See the class description and the NSComboBoxCellDataSource informal protocol specification for more information on combo box cell data source objects.

## See Also

### Accessing a Data Source
- [var usesDataSource: Bool](./usesdatasource.md)
  A Boolean value that indicates if the combo box uses an external data source to populate its pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/datasource)*