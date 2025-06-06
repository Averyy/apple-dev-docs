# dataValueType

**Framework**: Swift  
**Kind**: property

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

See `MLDataValue/ValueType` for a list of available options.

## See Also

- [init?(from: MLDataValue)](int/init(from:)-kl1p.md)
  Creates an instance of the conforming type from a data value.
- [var dataValue: MLDataValue](int/datavalue.md)
  The value of the conforming type’s instance wrapped in a data value.
- [var identifierValue: MLDataValue](int/identifiervalue.md)
  The value of the unique identifier wrapped in a data value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/datavaluetype)*