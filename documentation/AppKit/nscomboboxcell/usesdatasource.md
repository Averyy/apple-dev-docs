# usesDataSource

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates if the combo box uses an external data source to populate its pop-up list.

**Availability**:
- macOS

## Declaration

```swift
var usesDataSource: Bool { get set }
```

```objc
@property BOOL usesDataSource;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the combo box uses an external data source to populate its pop-up list; when it is [`false`](../../Swift/false.md), the combo box uses an internal item list.

## See Also

### Accessing a Data Source
- [var dataSource: (any NSComboBoxCellDataSource)?](./datasource.md)
  The object that provides the data displayed in the combo box’s pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/usesdatasource)*