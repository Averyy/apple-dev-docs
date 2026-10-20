# MLDataValue.MultiArrayType

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

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
- [init(MLMultiArray)](./multiarraytype/init%28_%29.md)
- [init(shape: [Int])](./multiarraytype/init%28shape%29.md)
### Getting the array
- [var mlMultiArray: MLMultiArray](./multiarraytype/mlmultiarray.md)
### Getting an element
- [subscript(_:)](./multiarraytype/subscript%28_%29.md)
### Default Implementations
- [MLDataValueConvertible Implementations](./multiarraytype/mldatavalueconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [MLDataValueConvertible](../mldatavalueconvertible.md)

## See Also

### Accessing array values
- [var sequenceValue: MLDataValue.SequenceType?](./sequencevalue.md)
  The underlying sequence.
- [MLDataValue.SequenceType](./sequencetype.md)
  A sequence of data values.
- [var multiArrayValue: MLDataValue.MultiArrayType?](./multiarrayvalue.md)
  The underlying multidimensional array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue/multiarraytype)*