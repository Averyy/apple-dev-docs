# MLDataValue

**Framework**: Create ML  
**Kind**: enum

The value of a cell in a data table.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
enum MLDataValue
```

#### Overview

The [`MLDataValue`](mldatavalue.md) enumeration is the fundamental type that you use to store training data in a table. Classifiers use data values to store information like evaluation metrics. Data values wrap all of the possible data types you can use with Create ML.

To access the underlying information in a data value, you can use the properties that correspond to the type’s enumeration cases. If you aren’t sure which kind of value a data value wrapper contains, use a switch statement to unwrap the value, or check the value of the [`type`](mldatavalue/type.md) property.

## Topics

### Converting between types and data values
- [protocol MLDataValueConvertible](mldatavalueconvertible.md)
  A type that can convert itself to and from a data value.
### Creating a data value
- [MLDataValue.int(_:)](mldatavalue/int(_:).md)
  An integer value.
- [MLDataValue.double(_:)](mldatavalue/double(_:).md)
  A double value.
- [MLDataValue.string(_:)](mldatavalue/string(_:).md)
  A string value.
- [case dictionary(MLDataValue.DictionaryType)](mldatavalue/dictionary(_:).md)
  A dictionary of named data values.
- [case sequence(MLDataValue.SequenceType)](mldatavalue/sequence(_:).md)
  A sequence of data values.
- [case multiArray(MLDataValue.MultiArrayType)](mldatavalue/multiarray(_:).md)
  A multidimensional array of data values.
### Inspecting the type
- [var type: MLDataValue.ValueType](mldatavalue/type.md)
  The kind of the underlying value that the data value wraps.
- [MLDataValue.ValueType](mldatavalue/valuetype.md)
  An enumeration describing the supported underlying types that an `MLDataValue wraps`.
### Accessing numeric values
- [var intValue: Int?](mldatavalue/intvalue.md)
  The underlying integer value.
- [var doubleValue: Double?](mldatavalue/doublevalue.md)
  The underlying double value.
### Accessing string values
- [var stringValue: String?](mldatavalue/stringvalue.md)
  The underlying string value.
### Accessing dictionary values
- [var dictionaryValue: MLDataValue.DictionaryType?](mldatavalue/dictionaryvalue.md)
  The underlying dictionary.
- [MLDataValue.DictionaryType](mldatavalue/dictionarytype.md)
  A dictionary of named data values.
### Accessing array values
- [var sequenceValue: MLDataValue.SequenceType?](mldatavalue/sequencevalue.md)
  The underlying sequence.
- [MLDataValue.SequenceType](mldatavalue/sequencetype.md)
  A sequence of data values.
- [var multiArrayValue: MLDataValue.MultiArrayType?](mldatavalue/multiarrayvalue.md)
  The underlying multidimensional array.
- [MLDataValue.MultiArrayType](mldatavalue/multiarraytype.md)
  A multidimensional array of data values.
### Comparing data values
- [static func == (MLDataValue, MLDataValue) -> Bool](mldatavalue/==(_:_:).md)
  Returns a Boolean value indicating whether two data values wrap the same underlying value.
### Describing a data value
- [var description: String](mldatavalue/description.md)
  A text representation of the data value.
- [var debugDescription: String](mldatavalue/debugdescription.md)
  A text representation of the data value that’s suitable for output during debugging.
### Handling errors
- [MLDataValue.invalid](mldatavalue/invalid.md)
  An invalid value.
- [var isValid: Bool](mldatavalue/isvalid.md)
  A Boolean value indicating whether the data value is valid.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mldatavalue/customdebugstringconvertible-implementations.md)
- [CustomStringConvertible Implementations](mldatavalue/customstringconvertible-implementations.md)
- [Equatable Implementations](mldatavalue/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [struct MLDataTable](mldatatable.md)
  A table of data for training or evaluating a machine learning model.
- [Data visualizations](data-visualizations.md)
  Render images of data tables and columns in a playground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalue)*