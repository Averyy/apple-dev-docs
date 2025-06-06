# SignedNumeric

**Framework**: Swift  
**Kind**: protocol

A numeric type with a negation operation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol SignedNumeric : Numeric
```

#### Overview

The `SignedNumeric` protocol extends the operations defined by the `Numeric` protocol to include a value’s additive inverse.

### Conforming to the Signednumeric Protocol

Because the `SignedNumeric` protocol provides default implementations of both of its required methods, you don’t need to do anything beyond declaring conformance to the protocol and ensuring that the values of your type support negation. To customize your type’s implementation, provide your own mutating `negate()` method.

When the additive inverse of a value is unrepresentable in a conforming type, the operation should either trap or return an exceptional value. For example, using the negation operator (prefix `-`) with `Int.min` results in a runtime error.

```swift
let x = Int.min
let y = -x
// Overflow error
```

## Topics

### Operators
- [static func - (Self) -> Self](signednumeric/-(_:).md)
  Returns the additive inverse of the specified value.
### Instance Methods
- [func negate()](signednumeric/negate.md)
  Replaces this value with its additive inverse.

## Relationships

### Inherits From
- [AdditiveArithmetic](additivearithmetic.md)
- [Equatable](equatable.md)
- [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md)
- [Numeric](numeric.md)
### Inherited By
- [BinaryFloatingPoint](binaryfloatingpoint.md)
- [FloatingPoint](floatingpoint.md)
- [SignedInteger](signedinteger.md)
### Conforming Types
- [Double](double.md)
- [Float](float.md)
- [Float16](float16.md)
- [Float80](float80.md)
- [Int](int.md)
- [Int128](int128.md)
- [Int16](int16.md)
- [Int32](int32.md)
- [Int64](int64.md)
- [Int8](int8.md)

## See Also

- [protocol AdditiveArithmetic](additivearithmetic.md)
  A type with values that support addition and subtraction.
- [protocol Numeric](numeric.md)
  A type with values that support multiplication.
- [protocol Strideable](strideable.md)
  A type representing continuous, one-dimensional values that can be offset and measured.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/signednumeric)*