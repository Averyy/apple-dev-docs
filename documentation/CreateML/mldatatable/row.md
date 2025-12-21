# MLDataTable.Row

**Framework**: Create ML  
**Kind**: struct

A row of untyped values in a data table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct Row
```

## Topics

### Accessing parameters
- [var keys: MLDataTable.Row.Keys](mldatatable/row/keys-swift.property.md)
- [var values: MLDataTable.Row.Values](mldatatable/row/values-swift.property.md)
- [MLDataTable.Row.Key](mldatatable/row/key.md)
- [MLDataTable.Row.Keys](mldatatable/row/keys-swift.typealias.md)
- [MLDataTable.Row.Value](mldatatable/row/value.md)
- [MLDataTable.Row.Values](mldatatable/row/values-swift.struct.md)
### Getting a row
- [func index(forKey: MLDataTable.Row.Key) -> MLDataTable.Row.Index?](mldatatable/row/index(forkey:).md)
### Accessing rows
- [subscript(MLDataTable.Row.Key) -> MLDataTable.Row.Value?](mldatatable/row/subscript(_:).md)
- [subscript<T>(MLDataTable.Row.Key, T.Type) -> T?](mldatatable/row/subscript(_:_:).md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [var rows: MLDataTable.Rows](mldatatable/rows-swift.property.md)
  The rows of data in the table.
- [MLDataTable.Rows](mldatatable/rows-swift.struct.md)
  A collection of rows in a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/row)*