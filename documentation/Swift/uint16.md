# UInt16

**Framework**: Swift  
**Kind**: struct

A 16-bit unsigned integer value type.

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
@frozen
struct UInt16
```

## Topics

### Structures
- [UInt16.Words](uint16/words-swift.struct.md)
  A type that represents the words of this integer.
### Operators
- [static func != (UInt16, UInt16) -> Bool](uint16/!=(_:_:).md)
- [static func &= (inout UInt16, UInt16)](uint16/&=(_:_:).md)
  Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [static func &<<= (inout UInt16, UInt16)](uint16/&__=(_:_:)-4uh81.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &>>= (inout UInt16, UInt16)](uint16/&__=(_:_:)-54gew.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func *= (inout UInt16, UInt16)](uint16/*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable.
- [static func += (inout UInt16, UInt16)](uint16/+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable.
- [static func -= (inout UInt16, UInt16)](uint16/-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable.
- [static func == (UInt16, UInt16) -> Bool](uint16/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func < (UInt16, UInt16) -> Bool](uint16/_(_:_:)-9tmro.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func |= (inout UInt16, UInt16)](uint16/_=(_:_:)-2tboh.md)
  Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [static func %= (inout UInt16, UInt16)](uint16/_=(_:_:)-5c5xh.md)
  Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [static func /= (inout UInt16, UInt16)](uint16/_=(_:_:)-7gmk4.md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable.
- [static func ^= (inout UInt16, UInt16)](uint16/_=(_:_:)-7q4om.md)
  Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
### Initializers
- [init(CGFloat)](uint16/init(_:)-1x3ws.md)
- [init(Double)](uint16/init(_:)-2gsqf.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Float16)](uint16/init(_:)-5vkwt.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(NSNumber)](uint16/init(_:)-67c9u.md)
- [init(Float80)](uint16/init(_:)-754ls.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Float)](uint16/init(_:)-8jre.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(bitPattern: Int16)](uint16/init(bitpattern:).md)
  Creates a new instance with the same memory representation as the given value.
- [init?(exactly: Double)](uint16/init(exactly:)-1l0o7.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: NSNumber)](uint16/init(exactly:)-1n42w.md)
- [init?(exactly: Float80)](uint16/init(exactly:)-3qv86.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float16)](uint16/init(exactly:)-4ljt.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float)](uint16/init(exactly:)-8jto3.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(truncating: NSNumber)](uint16/init(truncating:).md)
### Instance Properties
- [var byteSwapped: UInt16](uint16/byteswapped.md)
  A representation of this integer with the byte order swapped.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](uint16/customplaygroundquicklook.md)
  A custom playground Quick Look for the `UInt16` instance.
- [var leadingZeroBitCount: Int](uint16/leadingzerobitcount.md)
  The number of leading zeros in this value’s binary representation.
- [var nonzeroBitCount: Int](uint16/nonzerobitcount.md)
  The number of bits equal to 1 in this value’s binary representation.
- [var trailingZeroBitCount: Int](uint16/trailingzerobitcount.md)
  The number of trailing zeros in this value’s binary representation.
- [var words: UInt16.Words](uint16/words-swift.property.md)
  A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
### Instance Methods
- [func addingReportingOverflow(UInt16) -> (partialValue: UInt16, overflow: Bool)](uint16/addingreportingoverflow(_:).md)
  Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividedReportingOverflow(by: UInt16) -> (partialValue: UInt16, overflow: Bool)](uint16/dividedreportingoverflow(by:).md)
  Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividingFullWidth((high: UInt16, low: UInt16.Magnitude)) -> (quotient: UInt16, remainder: UInt16)](uint16/dividingfullwidth(_:).md)
  Returns a tuple containing the quotient and remainder of dividing the given value by this value.
- [func multipliedFullWidth(by: UInt16) -> (high: UInt16, low: UInt16.Magnitude)](uint16/multipliedfullwidth(by:).md)
  Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [func multipliedReportingOverflow(by: UInt16) -> (partialValue: UInt16, overflow: Bool)](uint16/multipliedreportingoverflow(by:).md)
  Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func remainderReportingOverflow(dividingBy: UInt16) -> (partialValue: UInt16, overflow: Bool)](uint16/remainderreportingoverflow(dividingby:).md)
  Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [func signum() -> UInt16](uint16/signum.md)
  Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
- [func subtractingReportingOverflow(UInt16) -> (partialValue: UInt16, overflow: Bool)](uint16/subtractingreportingoverflow(_:).md)
  Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.
### Type Aliases
- [typealias IntegerLiteralType](uint16/integerliteraltype.md)
  A type that represents an integer literal.
- [typealias Magnitude](uint16/magnitude.md)
  A type that can represent the absolute value of any possible value of this type.
- [typealias Stride](uint16/stride.md)
  A type that represents the distance between two values.
### Type Properties
- [static var bitWidth: Int](uint16/bitwidth.md)
  The number of bits used for the underlying binary representation of values of this type.
### Default Implementations
- [AdditiveArithmetic Implementations](uint16/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](uint16/atomicrepresentable-implementations.md)
- [BinaryInteger Implementations](uint16/binaryinteger-implementations.md)
- [Comparable Implementations](uint16/comparable-implementations.md)
- [CustomReflectable Implementations](uint16/customreflectable-implementations.md)
- [Decodable Implementations](uint16/decodable-implementations.md)
- [Encodable Implementations](uint16/encodable-implementations.md)
- [Equatable Implementations](uint16/equatable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](uint16/expressiblebyintegerliteral-implementations.md)
- [FixedWidthInteger Implementations](uint16/fixedwidthinteger-implementations.md)
- [Hashable Implementations](uint16/hashable-implementations.md)
- [SIMDScalar Implementations](uint16/simdscalar-implementations.md)
- [UnsignedInteger Implementations](uint16/unsignedinteger-implementations.md)

## Relationships

### Conforms To
- [AdditiveArithmetic](additivearithmetic.md)
- [AtomicRepresentable](../synchronization/atomicrepresentable.md)
- [BNNSScalar](../Accelerate/BNNSScalar.md)
- [BinaryInteger](binaryinteger.md)
- [BitwiseCopyable](bitwisecopyable.md)
- [CKRecordValueProtocol](../CloudKit/CKRecordValueProtocol.md)
- [CVarArg](cvararg.md)
- [Comparable](comparable.md)
- [Copyable](copyable.md)
- [CustomReflectable](customreflectable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md)
- [FixedWidthInteger](fixedwidthinteger.md)
- [Hashable](hashable.md)
- [LosslessStringConvertible](losslessstringconvertible.md)
- [MLTensorScalar](../CoreML/MLTensorScalar.md)
- [Numeric](numeric.md)
- [Plottable](../Charts/Plottable.md)
- [PrimitivePlottableProtocol](../Charts/PrimitivePlottableProtocol.md)
- [SIMDScalar](simdscalar.md)
- [Sendable](sendable.md)
- [Strideable](strideable.md)
- [UnsignedInteger](unsignedinteger.md)
- [vDSP_IntegerConvertable](../Accelerate/vDSP_IntegerConvertable.md)

## See Also

- [struct UInt](uint.md)
  An unsigned integer value type.
- [struct UInt8](uint8.md)
  An 8-bit unsigned integer value type.
- [struct UInt32](uint32.md)
  A 32-bit unsigned integer value type.
- [struct UInt64](uint64.md)
  A 64-bit unsigned integer value type.
- [struct UInt128](uint128.md)
  A 128-bit unsigned integer value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint16)*