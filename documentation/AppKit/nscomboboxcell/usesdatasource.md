# usesDataSource

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates if the combo box uses an external data source to populate its pop-up list.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var usesDataSource: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/swift/true), the combo box uses an external data source to populate its pop-up list; when it is [`false`](https://developer.apple.com/documentation/swift/false), the combo box uses an internal item list.

## See Also

- [var dataSource: (any NSComboBoxCellDataSource)?](nscomboboxcell/datasource.md)
  The object that provides the data displayed in the combo box’s pop-up list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscomboboxcell/usesdatasource)*