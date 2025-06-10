# Int32

**Framework**: Swift  
**Kind**: struct

A 32-bit signed integer value type.

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
struct Int32
```

## Topics

### Structures
- [struct Words](int32/words-swift.struct.md)
  A type that represents the words of this integer.
### Operators
- [static func != (Int32, Int32) -> Bool](int32/!=(_:_:).md)
- [static func &= (inout Int32, Int32)](int32/&=(_:_:).md)
  Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [static func &<<= (inout Int32, Int32)](int32/&__=(_:_:)-5xpt1.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &>>= (inout Int32, Int32)](int32/&__=(_:_:)-9l16.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func *= (inout Int32, Int32)](int32/*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable.
- [static func += (inout Int32, Int32)](int32/+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable.
- [static func -= (inout Int32, Int32)](int32/-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable.
- [static func == (Int32, Int32) -> Bool](int32/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func < (Int32, Int32) -> Bool](int32/_(_:_:)-3k2xk.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func ^= (inout Int32, Int32)](int32/_=(_:_:)-46xu7.md)
  Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [static func |= (inout Int32, Int32)](int32/_=(_:_:)-6hsuo.md)
  Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [static func %= (inout Int32, Int32)](int32/_=(_:_:)-8flrz.md)
  Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [static func /= (inout Int32, Int32)](int32/_=(_:_:)-997bi.md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable.
### Initializers
- [init(Float80)](int32/init(_:)-1817u.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Float)](int32/init(_:)-2px8y.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Float16)](int32/init(_:)-34fue.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(NSNumber)](int32/init(_:)-3zpp6.md)
- [init(CGFloat)](int32/init(_:)-5nznu.md)
- [init(Double)](int32/init(_:)-k0sh.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(bitPattern: UInt32)](int32/init(bitpattern:).md)
  Creates a new instance with the same memory representation as the given value.
- [init?(exactly: Float16)](int32/init(exactly:)-3dltv.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: NSNumber)](int32/init(exactly:)-5hlj9.md)
- [init?(exactly: Double)](int32/init(exactly:)-79vj5.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float80)](int32/init(exactly:)-7dio6.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float)](int32/init(exactly:)-9tpyy.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(truncating: NSNumber)](int32/init(truncating:).md)
### Instance Properties
- [var byteSwapped: Int32](int32/byteswapped.md)
  A representation of this integer with the byte order swapped.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](int32/customplaygroundquicklook.md)
  A custom playground Quick Look for the `Int32` instance.
- [var leadingZeroBitCount: Int](int32/leadingzerobitcount.md)
  The number of leading zeros in this value’s binary representation.
- [var magnitude: UInt32](int32/magnitude-swift.property.md)
  The magnitude of this value.
- [var nonzeroBitCount: Int](int32/nonzerobitcount.md)
  The number of bits equal to 1 in this value’s binary representation.
- [var trailingZeroBitCount: Int](int32/trailingzerobitcount.md)
  The number of trailing zeros in this value’s binary representation.
- [var words: Int32.Words](int32/words-swift.property.md)
  A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
### Instance Methods
- [func addingReportingOverflow(Int32) -> (partialValue: Int32, overflow: Bool)](int32/addingreportingoverflow(_:).md)
  Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividedReportingOverflow(by: Int32) -> (partialValue: Int32, overflow: Bool)](int32/dividedreportingoverflow(by:).md)
  Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividingFullWidth((high: Int32, low: Int32.Magnitude)) -> (quotient: Int32, remainder: Int32)](int32/dividingfullwidth(_:).md)
  Returns a tuple containing the quotient and remainder of dividing the given value by this value.
- [func multipliedFullWidth(by: Int32) -> (high: Int32, low: Int32.Magnitude)](int32/multipliedfullwidth(by:).md)
  Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [func multipliedReportingOverflow(by: Int32) -> (partialValue: Int32, overflow: Bool)](int32/multipliedreportingoverflow(by:).md)
  Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func remainderReportingOverflow(dividingBy: Int32) -> (partialValue: Int32, overflow: Bool)](int32/remainderreportingoverflow(dividingby:).md)
  Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [func signum() -> Int32](int32/signum.md)
  Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
- [func subtractingReportingOverflow(Int32) -> (partialValue: Int32, overflow: Bool)](int32/subtractingreportingoverflow(_:).md)
  Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.
### Type Aliases
- [typealias IntegerLiteralType](int32/integerliteraltype.md)
  A type that represents an integer literal.
- [typealias Magnitude](int32/magnitude-swift.typealias.md)
  A type that can represent the absolute value of any possible value of this type.
- [typealias Stride](int32/stride.md)
  A type that represents the distance between two values.
### Type Properties
- [static var bitWidth: Int](int32/bitwidth.md)
  The number of bits used for the underlying binary representation of values of this type.
- [static var mlMultiArrayDataType: MLMultiArrayDataType](int32/mlmultiarraydatatype.md)
### Default Implementations
- [AdditiveArithmetic Implementations](int32/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](int32/atomicrepresentable-implementations.md)
- [BinaryInteger Implementations](int32/binaryinteger-implementations.md)
- [Comparable Implementations](int32/comparable-implementations.md)
- [CustomReflectable Implementations](int32/customreflectable-implementations.md)
- [Decodable Implementations](int32/decodable-implementations.md)
- [Encodable Implementations](int32/encodable-implementations.md)
- [Equatable Implementations](int32/equatable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](int32/expressiblebyintegerliteral-implementations.md)
- [FixedWidthInteger Implementations](int32/fixedwidthinteger-implementations.md)
- [Hashable Implementations](int32/hashable-implementations.md)
- [SIMDScalar Implementations](int32/simdscalar-implementations.md)
- [SignedInteger Implementations](int32/signedinteger-implementations.md)
- [SignedNumeric Implementations](int32/signednumeric-implementations.md)

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
- [MLShapedArrayScalar](../CoreML/MLShapedArrayScalar.md)
- [MLTensorScalar](../CoreML/MLTensorScalar.md)
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
- [vDSP_IntegerConvertable](../Accelerate/vDSP_IntegerConvertable.md)

## See Also

- [struct Int8](int8.md)
  An 8-bit signed integer value type.
- [struct Int16](int16.md)
  A 16-bit signed integer value type.
- [struct Int64](int64.md)
  A 64-bit signed integer value type.
- [struct Int128](int128.md)
  A 128-bit signed integer value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int32)*