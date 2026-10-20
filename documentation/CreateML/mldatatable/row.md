# MLDataTable.Row

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

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
- [var keys: MLDataTable.Row.Keys](./row/keys-swift.property.md)
- [var values: MLDataTable.Row.Values](./row/values-swift.property.md)
- [MLDataTable.Row.Key](./row/key.md)
- [MLDataTable.Row.Keys](./row/keys-swift.typealias.md)
- [MLDataTable.Row.Value](./row/value.md)
- [MLDataTable.Row.Values](./row/values-swift.struct.md)
### Getting a row
- [func index(forKey: MLDataTable.Row.Key) -> MLDataTable.Row.Index?](./row/index%28forkey%29.md)
### Accessing rows
- [subscript(MLDataTable.Row.Key) -> MLDataTable.Row.Value?](./row/subscript%28_%29.md)
- [subscript<T>(MLDataTable.Row.Key, T.Type) -> T?](./row/subscript%28_,_%29.md)

## Relationships

### Conforms To
- [Collection](../../Swift/collection.md)
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomPlaygroundDisplayConvertible](../../Swift/customplaygrounddisplayconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Sequence](../../Swift/sequence.md)

## See Also

### Getting information about a data table’s rows
- [var rows: MLDataTable.Rows](./rows-swift.property.md)
  The rows of data in the table.
- [MLDataTable.Rows](./rows-swift.struct.md)
  A collection of rows in a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/row)*