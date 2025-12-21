# usesDataSource

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the combo box retrieves its items from a data source object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var usesDataSource: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the combo box retrieves its items from the object in the [`dataSource`](nscombobox/datasource.md) property. When the value is [`false`](https://developer.apple.com/documentation/Swift/false), the combo box manages an internal list of items, which it gets from the ones specified at design time and the ones you add programmatically.

## See Also

- [var dataSource: (any NSComboBoxDataSource)?](nscombobox/datasource.md)
  The object that provides the item data for the combo box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/usesdatasource)*