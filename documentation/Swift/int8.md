# Int8

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

An 8-bit signed integer value type.

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
struct Int8
```

## Topics

### Structures
- [struct Words](./int8/words-swift.struct.md)
  A type that represents the words of this integer.
### Operators
- [static func != (Int8, Int8) -> Bool](./int8/noteq%28_,_%29.md)
- [static func &= (inout Int8, Int8)](./int8/ampeq%28_,_%29.md)
  Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [static func &>>= (inout Int8, Int8)](./int8/ampopopeq%28_,_%29-17e9w.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &<<= (inout Int8, Int8)](./int8/ampopopeq%28_,_%29-7gdrc.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func *= (inout Int8, Int8)](./int8/stareq%28_,_%29.md)
  Multiplies two values and stores the result in the left-hand-side variable.
- [static func += (inout Int8, Int8)](./int8/pluseq%28_,_%29.md)
  Adds two values and stores the result in the left-hand-side variable.
- [static func -= (inout Int8, Int8)](./int8/minuseq%28_,_%29.md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable.
- [static func == (Int8, Int8) -> Bool](./int8/eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are equal.
- [static func < (Int8, Int8) -> Bool](./int8/op%28_,_%29-1kdfe.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func |= (inout Int8, Int8)](./int8/opeq%28_,_%29-19gzu.md)
  Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [static func /= (inout Int8, Int8)](./int8/opeq%28_,_%29-2auqb.md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable.
- [static func ^= (inout Int8, Int8)](./int8/opeq%28_,_%29-2mpgr.md)
  Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [static func %= (inout Int8, Int8)](./int8/opeq%28_,_%29-3o9cs.md)
  Divides the first value by the second and stores the remainder in the left-hand-side variable.
### Initializers
- [init(CGFloat)](./int8/init%28_%29-2vdru.md)
- [init(Float16)](./int8/init%28_%29-44cer.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Double)](./int8/init%28_%29-47zy8.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(NSNumber)](./int8/init%28_%29-4erk2.md)
- [init(Float)](./int8/init%28_%29-6g8q9.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Float80)](./int8/init%28_%29-7renq.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(bitPattern: UInt8)](./int8/init%28bitpattern%29.md)
  Creates a new instance with the same memory representation as the given value.
- [init?(exactly: Float80)](./int8/init%28exactly%29-1vh5j.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float)](./int8/init%28exactly%29-6zkv6.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Double)](./int8/init%28exactly%29-72z4.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float16)](./int8/init%28exactly%29-78es1.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: NSNumber)](./int8/init%28exactly%29-9cjj7.md)
- [init(truncating: NSNumber)](./int8/init%28truncating%29.md)
### Instance Properties
- [var byteSwapped: Int8](./int8/byteswapped.md)
  A representation of this integer with the byte order swapped.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](./int8/customplaygroundquicklook.md)
  A custom playground Quick Look for the `Int8` instance.
- [var leadingZeroBitCount: Int](./int8/leadingzerobitcount.md)
  The number of leading zeros in this value’s binary representation.
- [var magnitude: UInt8](./int8/magnitude-swift.property.md)
  The magnitude of this value.
- [var nonzeroBitCount: Int](./int8/nonzerobitcount.md)
  The number of bits equal to 1 in this value’s binary representation.
- [var trailingZeroBitCount: Int](./int8/trailingzerobitcount.md)
  The number of trailing zeros in this value’s binary representation.
- [var words: Int8.Words](./int8/words-swift.property.md)
  A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
### Instance Methods
- [func addingReportingOverflow(Int8) -> (partialValue: Int8, overflow: Bool)](./int8/addingreportingoverflow%28_%29.md)
  Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividedReportingOverflow(by: Int8) -> (partialValue: Int8, overflow: Bool)](./int8/dividedreportingoverflow%28by%29.md)
  Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividingFullWidth((high: Int8, low: Int8.Magnitude)) -> (quotient: Int8, remainder: Int8)](./int8/dividingfullwidth%28_%29.md)
  Returns a tuple containing the quotient and remainder of dividing the given value by this value.
- [func multipliedFullWidth(by: Int8) -> (high: Int8, low: Int8.Magnitude)](./int8/multipliedfullwidth%28by%29.md)
  Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [func multipliedReportingOverflow(by: Int8) -> (partialValue: Int8, overflow: Bool)](./int8/multipliedreportingoverflow%28by%29.md)
  Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func remainderReportingOverflow(dividingBy: Int8) -> (partialValue: Int8, overflow: Bool)](./int8/remainderreportingoverflow%28dividingby%29.md)
  Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [func signum() -> Int8](./int8/signum%28%29.md)
  Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
- [func subtractingReportingOverflow(Int8) -> (partialValue: Int8, overflow: Bool)](./int8/subtractingreportingoverflow%28_%29.md)
  Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.
### Type Aliases
- [typealias IntegerLiteralType](./int8/integerliteraltype.md)
  A type that represents an integer literal.
- [typealias Magnitude](./int8/magnitude-swift.typealias.md)
  A type that can represent the absolute value of any possible value of this type.
- [typealias Stride](./int8/stride.md)
  A type that represents the distance between two values.
### Type Properties
- [static var bitWidth: Int](./int8/bitwidth.md)
  The number of bits used for the underlying binary representation of values of this type.
### Default Implementations
- [AdditiveArithmetic Implementations](./int8/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](./int8/atomicrepresentable-implementations.md)
- [BinaryInteger Implementations](./int8/binaryinteger-implementations.md)
- [Comparable Implementations](./int8/comparable-implementations.md)
- [CustomReflectable Implementations](./int8/customreflectable-implementations.md)
- [Decodable Implementations](./int8/decodable-implementations.md)
- [Encodable Implementations](./int8/encodable-implementations.md)
- [Equatable Implementations](./int8/equatable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](./int8/expressiblebyintegerliteral-implementations.md)
- [FixedWidthInteger Implementations](./int8/fixedwidthinteger-implementations.md)
- [Hashable Implementations](./int8/hashable-implementations.md)
- [SIMDScalar Implementations](./int8/simdscalar-implementations.md)
- [SignedInteger Implementations](./int8/signedinteger-implementations.md)
- [SignedNumeric Implementations](./int8/signednumeric-implementations.md)

## Relationships

### Conforms To
- [AdditiveArithmetic](./additivearithmetic.md)
- [AtomicRepresentable](../Synchronization/atomicrepresentable.md)
- [BNNSScalar](../Accelerate/bnnsscalar.md)
- [BinaryInteger](./binaryinteger.md)
- [BitwiseCopyable](./bitwisecopyable.md)
- [CKRecordValueProtocol](../CloudKit/ckrecordvalueprotocol.md)
- [CVAttachmentValueRepresentable](../CoreVideo/cvattachmentvaluerepresentable.md)
- [CVarArg](./cvararg.md)
- [Comparable](./comparable.md)
- [ConvertibleFromBytes](./convertiblefrombytes.md)
- [ConvertibleToBytes](./convertibletobytes.md)
- [Copyable](./copyable.md)
- [CustomReflectable](./customreflectable.md)
- [CustomStringConvertible](./customstringconvertible.md)
- [Decodable](./decodable.md)
- [Encodable](./encodable.md)
- [Equatable](./equatable.md)
- [Escapable](./escapable.md)
- [ExpressibleByIntegerLiteral](./expressiblebyintegerliteral.md)
- [FixedWidthInteger](./fixedwidthinteger.md)
- [Hashable](./hashable.md)
- [IntentValueConvertible](../AppIntents/intentvalueconvertible.md)
- [IntentValueExpressing](../AppIntents/intentvalueexpressing.md)
- [LosslessStringConvertible](./losslessstringconvertible.md)
- [MLShapedArrayScalar](../CoreML/mlshapedarrayscalar.md)
- [MLTensorScalar](../CoreML/mltensorscalar.md)
- [NetworkFixedWidthInteger](../Network/networkfixedwidthinteger.md)
- [Numeric](./numeric.md)
- [Plottable](../Charts/plottable.md)
- [PrimitivePlottableProtocol](../Charts/primitiveplottableprotocol.md)
- [SIMDScalar](./simdscalar.md)
- [Sendable](./sendable.md)
- [SendableMetatype](./sendablemetatype.md)
- [SignedInteger](./signedinteger.md)
- [SignedNumeric](./signednumeric.md)
- [Strideable](./strideable.md)
- [USDValueProtocol](../USDKit/usdvalueprotocol.md)
- [vDSP_IntegerConvertable](../Accelerate/vdsp_integerconvertable.md)

## See Also

### Signed Integers
- [struct Int16](./int16.md)
  A 16-bit signed integer value type.
- [struct Int32](./int32.md)
  A 32-bit signed integer value type.
- [struct Int64](./int64.md)
  A 64-bit signed integer value type.
- [struct Int128](./int128.md)
  A 128-bit signed integer value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int8)*