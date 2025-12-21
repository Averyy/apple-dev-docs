# MLDataValue.MultiArrayType

**Framework**: Create ML  
**Kind**: struct

A multidimensional array of data values.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MultiArrayType
```

## Topics

### Creating an array type
- [init(MLMultiArray)](mldatavalue/multiarraytype/init(_:).md)
- [init(shape: [Int])](mldatavalue/multiarraytype/init(shape:).md)
### Getting the array
- [var mlMultiArray: MLMultiArray](mldatavalue/multiarraytype/mlmultiarray.md)
### Getting an element
- [subscript(_:)](mldatavalue/multiarraytype/subscript(_:).md)
### Default Implementations
- [MLDataValueConvertible Implementations](mldatavalue/multiarraytype/mldatavalueconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [MLDataValueConvertible](mldatavalueconvertible.md)

## See Also

- [var sequenceValue: MLDataValue.SequenceType?](mldatavalue/sequencevalue.md)
  The underlying sequence.
- [MLDataValue.SequenceType](mldatavalue/sequencetype.md)
  A sequence of data values.
- [var multiArrayValue: MLDataValue.MultiArrayType?](mldatavalue/multiarrayvalue.md)
  The underlying multidimensional array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/multiarraytype)*