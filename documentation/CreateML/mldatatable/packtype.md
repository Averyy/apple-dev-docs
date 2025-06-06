# MLDataTable.PackType

**Framework**: Create ML  
**Kind**: enum

The storage operations for combining multiple columns into one.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum PackType
```

## Topics

### Selecting a packing operation
- [MLDataTable.PackType.sequence](mldatatable/packtype/sequence.md)
  A packing type that combines the values of several columns into a sequence type.
- [MLDataTable.PackType.dictionary](mldatatable/packtype/dictionary.md)
  A packing type that combines the values of several columns into a dictionary type.
### Describing a packing operation
- [var hashValue: Int](mldatatable/packtype/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](mldatatable/packtype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Comparing packing operations
- [static func == (MLDataTable.PackType, MLDataTable.PackType) -> Bool](mldatatable/packtype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](mldatatable/packtype/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Default Implementations
- [Equatable Implementations](mldatatable/packtype/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func pack(columnsNamed: String..., to: String, type: MLDataTable.PackType, filling: MLDataValue) -> MLDataTable](mldatatable/pack(columnsnamed:to:type:filling:).md)
  Creates a new data table with an additional column that contains the combined values of the given columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/packtype)*