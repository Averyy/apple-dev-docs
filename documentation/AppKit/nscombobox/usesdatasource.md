# usesDataSource

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the combo box retrieves its items from a data source object.

**Availability**:
- macOS

## Declaration

```swift
var usesDataSource: Bool { get set }
```

```objc
@property BOOL usesDataSource;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the combo box retrieves its items from the object in the [`dataSource`](./datasource.md) property. When the value is [`false`](../../Swift/false.md), the combo box manages an internal list of items, which it gets from the ones specified at design time and the ones you add programmatically.

## See Also

### Setting a Data Source
- [var dataSource: (any NSComboBoxDataSource)?](./datasource.md)
  The object that provides the item data for the combo box.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscombobox/usesdatasource)*