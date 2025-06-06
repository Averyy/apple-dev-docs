# UInt

**Framework**: Swift  
**Kind**: struct

An unsigned integer value type.

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
struct UInt
```

#### Overview

On 32-bit platforms, `UInt` is the same size as `UInt32`, and on 64-bit platforms, `UInt` is the same size as `UInt64`.

## Topics

### Structures
- [struct Words](uint/words-swift.struct.md)
  A type that represents the words of this integer.
### Operators
- [static func != (UInt, UInt) -> Bool](uint/!=(_:_:).md)
- [static func &= (inout UInt, UInt)](uint/&=(_:_:).md)
  Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [static func &<<= (inout UInt, UInt)](uint/&__=(_:_:)-5hags.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &>>= (inout UInt, UInt)](uint/&__=(_:_:)-69f19.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func *= (inout UInt, UInt)](uint/*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable.
- [static func += (inout UInt, UInt)](uint/+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable.
- [static func -= (inout UInt, UInt)](uint/-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable.
- [static func == (UInt, UInt) -> Bool](uint/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func < (UInt, UInt) -> Bool](uint/_(_:_:)-9v225.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func /= (inout UInt, UInt)](uint/_=(_:_:)-22lsj.md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable.
- [static func ^= (inout UInt, UInt)](uint/_=(_:_:)-2p0vs.md)
  Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [static func |= (inout UInt, UInt)](uint/_=(_:_:)-4bs9t.md)
  Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [static func %= (inout UInt, UInt)](uint/_=(_:_:)-85oek.md)
  Divides the first value by the second and stores the remainder in the left-hand-side variable.
### Initializers
- [init(Double)](uint/init(_:)-117g.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(NSNumber)](uint/init(_:)-5lcnv.md)
- [init(Float80)](uint/init(_:)-7mzx8.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Float)](uint/init(_:)-8jtgk.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Float16)](uint/init(_:)-9lrzt.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(CGFloat)](uint/init(_:)-jl4r.md)
- [init<P>(bitPattern: P?)](uint/init(bitpattern:)-3qf8b.md)
  Creates a new value with the bit pattern of the given pointer.
- [init(bitPattern: OpaquePointer?)](uint/init(bitpattern:)-7sd72.md)
  Creates a new value with the bit pattern of the given pointer.
- [init(bitPattern: Int)](uint/init(bitpattern:)-9qvv7.md)
  Creates a new instance with the same memory representation as the given value.
- [init(bitPattern: ObjectIdentifier)](uint/init(bitpattern:)-gk5x.md)
  Creates an integer that captures the full value of the given object identifier.
- [init?(exactly: NSNumber)](uint/init(exactly:)-22ddn.md)
- [init?(exactly: Float80)](uint/init(exactly:)-8zm2w.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Double)](uint/init(exactly:)-9cl5x.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float)](uint/init(exactly:)-9ve7w.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float16)](uint/init(exactly:)-wmyv.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(truncating: NSNumber)](uint/init(truncating:).md)
### Instance Properties
- [var byteSwapped: UInt](uint/byteswapped.md)
  A representation of this integer with the byte order swapped.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](uint/customplaygroundquicklook.md)
  A custom playground Quick Look for the `UInt` instance.
- [var leadingZeroBitCount: Int](uint/leadingzerobitcount.md)
  The number of leading zeros in this value’s binary representation.
- [var nonzeroBitCount: Int](uint/nonzerobitcount.md)
  The number of bits equal to 1 in this value’s binary representation.
- [var trailingZeroBitCount: Int](uint/trailingzerobitcount.md)
  The number of trailing zeros in this value’s binary representation.
- [var words: UInt.Words](uint/words-swift.property.md)
  A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
### Instance Methods
- [func addingReportingOverflow(UInt) -> (partialValue: UInt, overflow: Bool)](uint/addingreportingoverflow(_:).md)
  Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividedReportingOverflow(by: UInt) -> (partialValue: UInt, overflow: Bool)](uint/dividedreportingoverflow(by:).md)
  Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividingFullWidth((high: UInt, low: UInt.Magnitude)) -> (quotient: UInt, remainder: UInt)](uint/dividingfullwidth(_:).md)
  Returns a tuple containing the quotient and remainder of dividing the given value by this value.
- [func multipliedFullWidth(by: UInt) -> (high: UInt, low: UInt.Magnitude)](uint/multipliedfullwidth(by:).md)
  Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [func multipliedReportingOverflow(by: UInt) -> (partialValue: UInt, overflow: Bool)](uint/multipliedreportingoverflow(by:).md)
  Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func remainderReportingOverflow(dividingBy: UInt) -> (partialValue: UInt, overflow: Bool)](uint/remainderreportingoverflow(dividingby:).md)
  Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [func signum() -> UInt](uint/signum.md)
  Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
- [func subtractingReportingOverflow(UInt) -> (partialValue: UInt, overflow: Bool)](uint/subtractingreportingoverflow(_:).md)
  Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.
### Type Aliases
- [typealias IntegerLiteralType](uint/integerliteraltype.md)
  A type that represents an integer literal.
- [typealias Magnitude](uint/magnitude.md)
  A type that can represent the absolute value of any possible value of this type.
- [typealias Stride](uint/stride.md)
  A type that represents the distance between two values.
### Type Properties
- [static var bitWidth: Int](uint/bitwidth.md)
  The number of bits used for the underlying binary representation of values of this type.
### Default Implementations
- [AdditiveArithmetic Implementations](uint/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](uint/atomicrepresentable-implementations.md)
- [BinaryInteger Implementations](uint/binaryinteger-implementations.md)
- [Comparable Implementations](uint/comparable-implementations.md)
- [CustomReflectable Implementations](uint/customreflectable-implementations.md)
- [Decodable Implementations](uint/decodable-implementations.md)
- [Encodable Implementations](uint/encodable-implementations.md)
- [Equatable Implementations](uint/equatable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](uint/expressiblebyintegerliteral-implementations.md)
- [FixedWidthInteger Implementations](uint/fixedwidthinteger-implementations.md)
- [Hashable Implementations](uint/hashable-implementations.md)
- [SIMDScalar Implementations](uint/simdscalar-implementations.md)
- [UnsignedInteger Implementations](uint/unsignedinteger-implementations.md)

## Relationships

### Conforms To
- [AdditiveArithmetic](additivearithmetic.md)
- [AtomicRepresentable](../synchronization/atomicrepresentable.md)
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
- [Numeric](numeric.md)
- [Plottable](../Charts/Plottable.md)
- [PrimitivePlottableProtocol](../Charts/PrimitivePlottableProtocol.md)
- [SIMDScalar](simdscalar.md)
- [Sendable](sendable.md)
- [Strideable](strideable.md)
- [UnsignedInteger](unsignedinteger.md)

## See Also

- [struct UInt8](uint8.md)
  An 8-bit unsigned integer value type.
- [struct UInt16](uint16.md)
  A 16-bit unsigned integer value type.
- [struct UInt32](uint32.md)
  A 32-bit unsigned integer value type.
- [struct UInt64](uint64.md)
  A 64-bit unsigned integer value type.
- [struct UInt128](uint128.md)
  A 128-bit unsigned integer value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint)*