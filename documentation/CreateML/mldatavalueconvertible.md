# MLDataValueConvertible

**Framework**: Create ML  
**Kind**: protocol

A type that can convert itself to and from a data value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol MLDataValueConvertible
```

#### Overview

You can use any type that conforms to the [`MLDataValueConvertible`](mldatavalueconvertible.md) protocol in an [`MLDataValue`](mldatavalue.md) or an [`MLDataTable`](mldatatable.md). For example, you can create a data table by using its [`init(dictionary:)`](mldatatable/init(dictionary:).md) initializer with a `[`[`String`](https://developer.apple.com/documentation/Swift/String)`: ``MLDataValueConvertible``]` dictionary.

## Topics

### Converting from a data value to a type’s instance
- [init()](mldatavalueconvertible/init.md)
  Creates a new default instance of the conforming type when a data value is missing or invalid.
- [init?(from: MLDataValue)](mldatavalueconvertible/init(from:).md)
  Creates an instance of the conforming type from a data value.
### Converting from a type’s instance to a data value
- [var dataValue: MLDataValue](mldatavalueconvertible/datavalue.md)
  The value of the conforming type’s instance wrapped in a data value.
- [static var dataValueType: MLDataValue.ValueType](mldatavalueconvertible/datavaluetype.md)
  The underlying type the conforming type uses when it wraps itself in a data value.

## Relationships

### Conforming Types
- [MLDataValue.DictionaryType](mldatavalue/dictionarytype.md)
- [MLDataValue.MultiArrayType](mldatavalue/multiarraytype.md)
- [MLDataValue.SequenceType](mldatavalue/sequencetype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalueconvertible)*