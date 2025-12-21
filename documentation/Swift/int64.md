# Int64

**Framework**: Swift  
**Kind**: struct

A 64-bit signed integer value type.

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
struct Int64
```

## Topics

### Structures
- [struct Words](int64/words-swift.struct.md)
  A type that represents the words of this integer.
### Operators
- [static func != (Int64, Int64) -> Bool](int64/!=(_:_:).md)
- [static func &= (inout Int64, Int64)](int64/&=(_:_:).md)
  Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [static func &<<= (inout Int64, Int64)](int64/&__=(_:_:)-3hmto.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &>>= (inout Int64, Int64)](int64/&__=(_:_:)-7f5t8.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func *= (inout Int64, Int64)](int64/*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable.
- [static func += (inout Int64, Int64)](int64/+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable.
- [static func -= (inout Int64, Int64)](int64/-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable.
- [static func == (Int64, Int64) -> Bool](int64/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func < (Int64, Int64) -> Bool](int64/_(_:_:)-15gfv.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func %= (inout Int64, Int64)](int64/_=(_:_:)-6kyxv.md)
  Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [static func ^= (inout Int64, Int64)](int64/_=(_:_:)-8wdie.md)
  Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [static func |= (inout Int64, Int64)](int64/_=(_:_:)-8xard.md)
  Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [static func /= (inout Int64, Int64)](int64/_=(_:_:)-9q89m.md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable.
### Initializers
- [init(NSNumber)](int64/init(_:)-1d7o4.md)
- [init(Float)](int64/init(_:)-4goni.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Float16)](int64/init(_:)-5aiim.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Double)](int64/init(_:)-87ipw.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(CGFloat)](int64/init(_:)-ia49.md)
- [init(Float80)](int64/init(_:)-ro3j.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(bitPattern: UInt64)](int64/init(bitpattern:).md)
  Creates a new instance with the same memory representation as the given value.
- [init?(exactly: Double)](int64/init(exactly:)-5w39p.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float16)](int64/init(exactly:)-74h3v.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float)](int64/init(exactly:)-87idz.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float80)](int64/init(exactly:)-8nn2c.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: NSNumber)](int64/init(exactly:)-mpiy.md)
- [init(truncating: NSNumber)](int64/init(truncating:).md)
### Instance Properties
- [var byteSwapped: Int64](int64/byteswapped.md)
  A representation of this integer with the byte order swapped.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](int64/customplaygroundquicklook.md)
  A custom playground Quick Look for the `Int64` instance.
- [var leadingZeroBitCount: Int](int64/leadingzerobitcount.md)
  The number of leading zeros in this value’s binary representation.
- [var magnitude: UInt64](int64/magnitude-swift.property.md)
  The magnitude of this value.
- [var nonzeroBitCount: Int](int64/nonzerobitcount.md)
  The number of bits equal to 1 in this value’s binary representation.
- [var trailingZeroBitCount: Int](int64/trailingzerobitcount.md)
  The number of trailing zeros in this value’s binary representation.
- [var words: Int64.Words](int64/words-swift.property.md)
  A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
### Instance Methods
- [func addingReportingOverflow(Int64) -> (partialValue: Int64, overflow: Bool)](int64/addingreportingoverflow(_:).md)
  Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividedReportingOverflow(by: Int64) -> (partialValue: Int64, overflow: Bool)](int64/dividedreportingoverflow(by:).md)
  Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividingFullWidth((high: Int64, low: Int64.Magnitude)) -> (quotient: Int64, remainder: Int64)](int64/dividingfullwidth(_:).md)
  Returns a tuple containing the quotient and remainder of dividing the given value by this value.
- [func multipliedFullWidth(by: Int64) -> (high: Int64, low: Int64.Magnitude)](int64/multipliedfullwidth(by:).md)
  Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [func multipliedReportingOverflow(by: Int64) -> (partialValue: Int64, overflow: Bool)](int64/multipliedreportingoverflow(by:).md)
  Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func remainderReportingOverflow(dividingBy: Int64) -> (partialValue: Int64, overflow: Bool)](int64/remainderreportingoverflow(dividingby:).md)
  Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [func signum() -> Int64](int64/signum.md)
  Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
- [func subtractingReportingOverflow(Int64) -> (partialValue: Int64, overflow: Bool)](int64/subtractingreportingoverflow(_:).md)
  Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.
### Type Aliases
- [typealias IntegerLiteralType](int64/integerliteraltype.md)
  A type that represents an integer literal.
- [typealias Magnitude](int64/magnitude-swift.typealias.md)
  A type that can represent the absolute value of any possible value of this type.
- [typealias Stride](int64/stride.md)
  A type that represents the distance between two values.
### Type Properties
- [static var bitWidth: Int](int64/bitwidth.md)
  The number of bits used for the underlying binary representation of values of this type.
### Default Implementations
- [AdditiveArithmetic Implementations](int64/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](int64/atomicrepresentable-implementations.md)
- [BinaryInteger Implementations](int64/binaryinteger-implementations.md)
- [Comparable Implementations](int64/comparable-implementations.md)
- [CustomReflectable Implementations](int64/customreflectable-implementations.md)
- [Decodable Implementations](int64/decodable-implementations.md)
- [Encodable Implementations](int64/encodable-implementations.md)
- [Equatable Implementations](int64/equatable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](int64/expressiblebyintegerliteral-implementations.md)
- [FixedWidthInteger Implementations](int64/fixedwidthinteger-implementations.md)
- [Hashable Implementations](int64/hashable-implementations.md)
- [SIMDScalar Implementations](int64/simdscalar-implementations.md)
- [SignedInteger Implementations](int64/signedinteger-implementations.md)
- [SignedNumeric Implementations](int64/signednumeric-implementations.md)

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
- [MLDataValueConvertible](../CreateML/MLDataValueConvertible.md)
- [NetworkFixedWidthInteger](../Network/NetworkFixedWidthInteger.md)
- [Numeric](numeric.md)
- [Plottable](../Charts/Plottable.md)
- [PrimitivePlottableProtocol](../Charts/PrimitivePlottableProtocol.md)
- [SIMDScalar](simdscalar.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [SignedInteger](signedinteger.md)
- [SignedNumeric](signednumeric.md)
- [Strideable](strideable.md)

## See Also

- [struct Int8](int8.md)
  An 8-bit signed integer value type.
- [struct Int16](int16.md)
  A 16-bit signed integer value type.
- [struct Int32](int32.md)
  A 32-bit signed integer value type.
- [struct Int128](int128.md)
  A 128-bit signed integer value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int64)*