# dataValueType

**Framework**: Create ML  
**Kind**: property  
**Required**: Yes

The underlying type the conforming type uses when it wraps itself in a data value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static var dataValueType: MLDataValue.ValueType { get }
```

#### Discussion

See [`MLDataValue.ValueType`](mldatavalue/valuetype.md) for a list of available options.

## See Also

- [var dataValue: MLDataValue](mldatavalueconvertible/datavalue.md)
  The value of the conforming type’s instance wrapped in a data value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatavalueconvertible/datavaluetype)*