# MLDataTable.PackType

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

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
- [MLDataTable.PackType.sequence](./packtype/sequence.md)
  A packing type that combines the values of several columns into a sequence type.
- [MLDataTable.PackType.dictionary](./packtype/dictionary.md)
  A packing type that combines the values of several columns into a dictionary type.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Compacting columns
- [func pack(columnsNamed: String..., to: String, type: MLDataTable.PackType, filling: MLDataValue) -> MLDataTable](./pack%28columnsnamed,to,type,filling%29.md)
  Creates a new data table with an additional column that contains the combined values of the given columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/packtype)*