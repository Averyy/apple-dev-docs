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
- [subscript(MLDataTable.Row.Key) -> MLDataTable.Row.Value?](mldatatable/row/subscript(_:)-7fw28.md)
- [subscript<T>(MLDataTable.Row.Key, T.Type) -> T?](mldatatable/row/subscript(_:_:).md)
### Default Implementations
- [Collection Implementations](mldatatable/row/collection-implementations.md)
- [CustomDebugStringConvertible Implementations](mldatatable/row/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mldatatable/row/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mldatatable/row/customstringconvertible-implementations.md)
- [Equatable Implementations](mldatatable/row/equatable-implementations.md)
- [Sequence Implementations](mldatatable/row/sequence-implementations.md)

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

- [MLDataTable.Rows.Element](mldatatable/rows-swift.struct/element.md)
  The Element of a DataTable is a Row. This is represented as a Dictionary-like type containing all Column names and their corresponding values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/row)*