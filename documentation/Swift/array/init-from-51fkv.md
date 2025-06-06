# init(from:)

**Framework**: Swift  
**Kind**: init

Creates an instance of the conforming type from a data value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init?(from dataValue: MLDataValue)
```

## See Also

- [init(MLDataColumn<Element>)](array/init(_:)-2ln1a.md)
  Constructs an Array with the elements of a DataColumn.
- [init(MLUntypedColumn)](array/init(_:)-86ka8.md)
  Constructs an Array with the elements of an MLUntypedColumn.
- [var dataValue: MLDataValue](array/datavalue.md)
  The value of the conforming type’s instance wrapped in a data value.
- [static var dataValueType: MLDataValue.ValueType](array/datavaluetype.md)
  The underlying type the conforming type uses when it wraps itself in a data value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/init(from:)-51fkv)*