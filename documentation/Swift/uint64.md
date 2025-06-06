# UInt64

**Framework**: Swift  
**Kind**: struct

A 64-bit unsigned integer value type.

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
struct UInt64
```

## Topics

### Structures
- [UInt64.Words](uint64/words-swift.struct.md)
  A type that represents the words of this integer.
### Operators
- [static func != (UInt64, UInt64) -> Bool](uint64/!=(_:_:).md)
- [static func &= (inout UInt64, UInt64)](uint64/&=(_:_:).md)
  Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [static func &>>= (inout UInt64, UInt64)](uint64/&__=(_:_:)-9z0pp.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &<<= (inout UInt64, UInt64)](uint64/&__=(_:_:)-p2fc.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func *= (inout UInt64, UInt64)](uint64/*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable.
- [static func += (inout UInt64, UInt64)](uint64/+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable.
- [static func -= (inout UInt64, UInt64)](uint64/-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable.
- [static func == (UInt64, UInt64) -> Bool](uint64/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func < (UInt64, UInt64) -> Bool](uint64/_(_:_:)-1zzq5.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func %= (inout UInt64, UInt64)](uint64/_=(_:_:)-20phr.md)
  Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [static func |= (inout UInt64, UInt64)](uint64/_=(_:_:)-3oy72.md)
  Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [static func ^= (inout UInt64, UInt64)](uint64/_=(_:_:)-7dm2a.md)
  Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [static func /= (inout UInt64, UInt64)](uint64/_=(_:_:)-9jhbb.md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable.
### Initializers
- [init(CGFloat)](uint64/init(_:)-31scj.md)
- [init(Float16)](uint64/init(_:)-6bhfg.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Double)](uint64/init(_:)-71bjo.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(NSNumber)](uint64/init(_:)-7pz4t.md)
- [init(Unicode.Scalar)](uint64/init(_:)-7yfzu.md)
  Construct with value `v.value`.
- [init(Float80)](uint64/init(_:)-86c9y.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Float)](uint64/init(_:)-8hpyb.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(bitPattern: Int64)](uint64/init(bitpattern:).md)
  Creates a new instance with the same memory representation as the given value.
- [init?(exactly: Float80)](uint64/init(exactly:)-1laz5.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: NSNumber)](uint64/init(exactly:)-1rz30.md)
- [init?(exactly: Double)](uint64/init(exactly:)-4pdnv.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float16)](uint64/init(exactly:)-92on5.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float)](uint64/init(exactly:)-gsjs.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(truncating: NSNumber)](uint64/init(truncating:).md)
### Instance Properties
- [var byteSwapped: UInt64](uint64/byteswapped.md)
  A representation of this integer with the byte order swapped.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](uint64/customplaygroundquicklook.md)
  A custom playground Quick Look for the `UInt64` instance.
- [var leadingZeroBitCount: Int](uint64/leadingzerobitcount.md)
  The number of leading zeros in this value’s binary representation.
- [var nonzeroBitCount: Int](uint64/nonzerobitcount.md)
  The number of bits equal to 1 in this value’s binary representation.
- [var trailingZeroBitCount: Int](uint64/trailingzerobitcount.md)
  The number of trailing zeros in this value’s binary representation.
- [var words: UInt64.Words](uint64/words-swift.property.md)
  A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
### Instance Methods
- [func addingReportingOverflow(UInt64) -> (partialValue: UInt64, overflow: Bool)](uint64/addingreportingoverflow(_:).md)
  Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividedReportingOverflow(by: UInt64) -> (partialValue: UInt64, overflow: Bool)](uint64/dividedreportingoverflow(by:).md)
  Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividingFullWidth((high: UInt64, low: UInt64.Magnitude)) -> (quotient: UInt64, remainder: UInt64)](uint64/dividingfullwidth(_:).md)
  Returns a tuple containing the quotient and remainder of dividing the given value by this value.
- [func multipliedFullWidth(by: UInt64) -> (high: UInt64, low: UInt64.Magnitude)](uint64/multipliedfullwidth(by:).md)
  Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [func multipliedReportingOverflow(by: UInt64) -> (partialValue: UInt64, overflow: Bool)](uint64/multipliedreportingoverflow(by:).md)
  Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func remainderReportingOverflow(dividingBy: UInt64) -> (partialValue: UInt64, overflow: Bool)](uint64/remainderreportingoverflow(dividingby:).md)
  Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [func signum() -> UInt64](uint64/signum.md)
  Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
- [func subtractingReportingOverflow(UInt64) -> (partialValue: UInt64, overflow: Bool)](uint64/subtractingreportingoverflow(_:).md)
  Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.
### Type Aliases
- [typealias IntegerLiteralType](uint64/integerliteraltype.md)
  A type that represents an integer literal.
- [typealias Magnitude](uint64/magnitude.md)
  A type that can represent the absolute value of any possible value of this type.
- [typealias Stride](uint64/stride.md)
  A type that represents the distance between two values.
### Type Properties
- [static var bitWidth: Int](uint64/bitwidth.md)
  The number of bits used for the underlying binary representation of values of this type.
### Default Implementations
- [AdditiveArithmetic Implementations](uint64/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](uint64/atomicrepresentable-implementations.md)
- [BinaryInteger Implementations](uint64/binaryinteger-implementations.md)
- [Comparable Implementations](uint64/comparable-implementations.md)
- [CustomReflectable Implementations](uint64/customreflectable-implementations.md)
- [Decodable Implementations](uint64/decodable-implementations.md)
- [Encodable Implementations](uint64/encodable-implementations.md)
- [Equatable Implementations](uint64/equatable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](uint64/expressiblebyintegerliteral-implementations.md)
- [FixedWidthInteger Implementations](uint64/fixedwidthinteger-implementations.md)
- [Hashable Implementations](uint64/hashable-implementations.md)
- [SIMDScalar Implementations](uint64/simdscalar-implementations.md)
- [UnsignedInteger Implementations](uint64/unsignedinteger-implementations.md)

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
- [Numeric](numeric.md)
- [Plottable](../Charts/Plottable.md)
- [PrimitivePlottableProtocol](../Charts/PrimitivePlottableProtocol.md)
- [SIMDScalar](simdscalar.md)
- [Sendable](sendable.md)
- [Strideable](strideable.md)
- [SynchronizationPeerID](../RealityKit/SynchronizationPeerID.md)
- [UnsignedInteger](unsignedinteger.md)

## See Also

- [struct UInt](uint.md)
  An unsigned integer value type.
- [struct UInt8](uint8.md)
  An 8-bit unsigned integer value type.
- [struct UInt16](uint16.md)
  A 16-bit unsigned integer value type.
- [struct UInt32](uint32.md)
  A 32-bit unsigned integer value type.
- [struct UInt128](uint128.md)
  A 128-bit unsigned integer value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint64)*