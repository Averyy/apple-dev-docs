# UInt32

**Framework**: Swift  
**Kind**: struct

A 32-bit unsigned integer value type.

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
struct UInt32
```

## Topics

### Structures
- [UInt32.Words](uint32/words-swift.struct.md)
  A type that represents the words of this integer.
### Operators
- [static func != (UInt32, UInt32) -> Bool](uint32/!=(_:_:).md)
- [static func &= (inout UInt32, UInt32)](uint32/&=(_:_:).md)
  Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [static func &<<= (inout UInt32, UInt32)](uint32/&__=(_:_:)-1qp80.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &>>= (inout UInt32, UInt32)](uint32/&__=(_:_:)-92fyx.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func *= (inout UInt32, UInt32)](uint32/*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable.
- [static func += (inout UInt32, UInt32)](uint32/+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable.
- [static func -= (inout UInt32, UInt32)](uint32/-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable.
- [static func == (UInt32, UInt32) -> Bool](uint32/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func < (UInt32, UInt32) -> Bool](uint32/_(_:_:)-3r38p.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func |= (inout UInt32, UInt32)](uint32/_=(_:_:)-4hx1l.md)
  Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [static func %= (inout UInt32, UInt32)](uint32/_=(_:_:)-6w0fj.md)
  Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [static func /= (inout UInt32, UInt32)](uint32/_=(_:_:)-8galu.md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable.
- [static func ^= (inout UInt32, UInt32)](uint32/_=(_:_:)-8vgdn.md)
  Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
### Initializers
- [init(Float)](uint32/init(_:)-1on5r.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Float16)](uint32/init(_:)-2w61y.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Float80)](uint32/init(_:)-42ptx.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Unicode.Scalar)](uint32/init(_:)-6tczc.md)
  Construct with value `v.value`.
- [init(CGFloat)](uint32/init(_:)-8t1sw.md)
- [init(NSNumber)](uint32/init(_:)-8xnzx.md)
- [init(Double)](uint32/init(_:)-9i7ab.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(bitPattern: Int32)](uint32/init(bitpattern:).md)
  Creates a new instance with the same memory representation as the given value.
- [init?(exactly: NSNumber)](uint32/init(exactly:)-33lic.md)
- [init?(exactly: Float80)](uint32/init(exactly:)-6lp3v.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Double)](uint32/init(exactly:)-7jkyf.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float16)](uint32/init(exactly:)-8qhoe.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float)](uint32/init(exactly:)-9c2y8.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(truncating: NSNumber)](uint32/init(truncating:).md)
### Instance Properties
- [var byteSwapped: UInt32](uint32/byteswapped.md)
  A representation of this integer with the byte order swapped.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](uint32/customplaygroundquicklook.md)
  A custom playground Quick Look for the `UInt32` instance.
- [var leadingZeroBitCount: Int](uint32/leadingzerobitcount.md)
  The number of leading zeros in this value’s binary representation.
- [var nonzeroBitCount: Int](uint32/nonzerobitcount.md)
  The number of bits equal to 1 in this value’s binary representation.
- [var trailingZeroBitCount: Int](uint32/trailingzerobitcount.md)
  The number of trailing zeros in this value’s binary representation.
- [var words: UInt32.Words](uint32/words-swift.property.md)
  A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
### Instance Methods
- [func addingReportingOverflow(UInt32) -> (partialValue: UInt32, overflow: Bool)](uint32/addingreportingoverflow(_:).md)
  Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividedReportingOverflow(by: UInt32) -> (partialValue: UInt32, overflow: Bool)](uint32/dividedreportingoverflow(by:).md)
  Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividingFullWidth((high: UInt32, low: UInt32.Magnitude)) -> (quotient: UInt32, remainder: UInt32)](uint32/dividingfullwidth(_:).md)
  Returns a tuple containing the quotient and remainder of dividing the given value by this value.
- [func multipliedFullWidth(by: UInt32) -> (high: UInt32, low: UInt32.Magnitude)](uint32/multipliedfullwidth(by:).md)
  Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [func multipliedReportingOverflow(by: UInt32) -> (partialValue: UInt32, overflow: Bool)](uint32/multipliedreportingoverflow(by:).md)
  Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func remainderReportingOverflow(dividingBy: UInt32) -> (partialValue: UInt32, overflow: Bool)](uint32/remainderreportingoverflow(dividingby:).md)
  Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [func signum() -> UInt32](uint32/signum.md)
  Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
- [func subtractingReportingOverflow(UInt32) -> (partialValue: UInt32, overflow: Bool)](uint32/subtractingreportingoverflow(_:).md)
  Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.
### Type Aliases
- [typealias IntegerLiteralType](uint32/integerliteraltype.md)
  A type that represents an integer literal.
- [typealias Magnitude](uint32/magnitude.md)
  A type that can represent the absolute value of any possible value of this type.
- [typealias Stride](uint32/stride.md)
  A type that represents the distance between two values.
### Type Properties
- [static var bitWidth: Int](uint32/bitwidth.md)
  The number of bits used for the underlying binary representation of values of this type.
### Default Implementations
- [AdditiveArithmetic Implementations](uint32/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](uint32/atomicrepresentable-implementations.md)
- [BinaryInteger Implementations](uint32/binaryinteger-implementations.md)
- [Comparable Implementations](uint32/comparable-implementations.md)
- [CustomReflectable Implementations](uint32/customreflectable-implementations.md)
- [Decodable Implementations](uint32/decodable-implementations.md)
- [Encodable Implementations](uint32/encodable-implementations.md)
- [Equatable Implementations](uint32/equatable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](uint32/expressiblebyintegerliteral-implementations.md)
- [FixedWidthInteger Implementations](uint32/fixedwidthinteger-implementations.md)
- [Hashable Implementations](uint32/hashable-implementations.md)
- [SIMDScalar Implementations](uint32/simdscalar-implementations.md)
- [UnsignedInteger Implementations](uint32/unsignedinteger-implementations.md)

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
- [struct UInt16](uint16.md)
  A 16-bit unsigned integer value type.
- [struct UInt64](uint64.md)
  A 64-bit unsigned integer value type.
- [struct UInt128](uint128.md)
  A 128-bit unsigned integer value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint32)*