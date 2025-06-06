# dataSource

**Framework**: AppKit  
**Kind**: property

The object that provides the item data for the combo box.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
unowned(unsafe) var dataSource: (any NSComboBoxDataSource)? { get set }
```

#### Discussion

Assigning an object to this property does not automatically set the [`usesDataSource`](nscombobox/usesdatasource.md) property to [`true`](https://developer.apple.com/documentation/swift/true). If the  [`usesDataSource`](nscombobox/usesdatasource.md) property is [`false`](https://developer.apple.com/documentation/swift/false), accessing this property logs a warning. The default value of this property is `nil`.

For information about how to implement a combo box data source, see `NSComboBoxDataSource`.

## See Also

- [var usesDataSource: Bool](nscombobox/usesdatasource.md)
  A Boolean value indicating whether the combo box retrieves its items from a data source object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/datasource)*