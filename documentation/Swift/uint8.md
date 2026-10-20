# UInt8

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

An 8-bit unsigned integer value type.

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
struct UInt8
```

## Topics

### Structures
- [struct Words](./uint8/words-swift.struct.md)
  A type that represents the words of this integer.
### Operators
- [static func != (UInt8, UInt8) -> Bool](./uint8/noteq%28_,_%29.md)
- [static func &= (inout UInt8, UInt8)](./uint8/ampeq%28_,_%29.md)
  Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [static func &>>= (inout UInt8, UInt8)](./uint8/ampopopeq%28_,_%29-172l7.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &<<= (inout UInt8, UInt8)](./uint8/ampopopeq%28_,_%29-5wuaw.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func *= (inout UInt8, UInt8)](./uint8/stareq%28_,_%29.md)
  Multiplies two values and stores the result in the left-hand-side variable.
- [static func += (inout UInt8, UInt8)](./uint8/pluseq%28_,_%29.md)
  Adds two values and stores the result in the left-hand-side variable.
- [static func -= (inout UInt8, UInt8)](./uint8/minuseq%28_,_%29.md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable.
- [static func == (UInt8, UInt8) -> Bool](./uint8/eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are equal.
- [static func < (UInt8, UInt8) -> Bool](./uint8/op%28_,_%29-140g8.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func %= (inout UInt8, UInt8)](./uint8/opeq%28_,_%29-12hmo.md)
  Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [static func ^= (inout UInt8, UInt8)](./uint8/opeq%28_,_%29-23lmz.md)
  Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [static func |= (inout UInt8, UInt8)](./uint8/opeq%28_,_%29-56yu9.md)
  Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [static func /= (inout UInt8, UInt8)](./uint8/opeq%28_,_%29-7a5f0.md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable.
### Initializers
- [init(Float16)](./uint8/init%28_%29-4e13y.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Float80)](./uint8/init%28_%29-535b5.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(CGFloat)](./uint8/init%28_%29-8f7wu.md)
- [init(Double)](./uint8/init%28_%29-8hqkq.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(NSNumber)](./uint8/init%28_%29-ey6q.md)
- [init(Float)](./uint8/init%28_%29-qdzq.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(ascii: Unicode.Scalar)](./uint8/init%28ascii%29.md)
  Construct with value `v.value`.
- [init(bitPattern: Int8)](./uint8/init%28bitpattern%29.md)
  Creates a new instance with the same memory representation as the given value.
- [init?(exactly: Double)](./uint8/init%28exactly%29-1ljfr.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: NSNumber)](./uint8/init%28exactly%29-3la4a.md)
- [init?(exactly: Float)](./uint8/init%28exactly%29-4mc0a.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float16)](./uint8/init%28exactly%29-7wsjq.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float80)](./uint8/init%28exactly%29-8rr3e.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init(truncating: NSNumber)](./uint8/init%28truncating%29.md)
### Instance Properties
- [var byteSwapped: UInt8](./uint8/byteswapped.md)
  A representation of this integer with the byte order swapped.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](./uint8/customplaygroundquicklook.md)
  A custom playground Quick Look for the `UInt8` instance.
- [var leadingZeroBitCount: Int](./uint8/leadingzerobitcount.md)
  The number of leading zeros in this value’s binary representation.
- [var nonzeroBitCount: Int](./uint8/nonzerobitcount.md)
  The number of bits equal to 1 in this value’s binary representation.
- [var trailingZeroBitCount: Int](./uint8/trailingzerobitcount.md)
  The number of trailing zeros in this value’s binary representation.
- [var words: UInt8.Words](./uint8/words-swift.property.md)
  A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
### Instance Methods
- [func addingReportingOverflow(UInt8) -> (partialValue: UInt8, overflow: Bool)](./uint8/addingreportingoverflow%28_%29.md)
  Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividedReportingOverflow(by: UInt8) -> (partialValue: UInt8, overflow: Bool)](./uint8/dividedreportingoverflow%28by%29.md)
  Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividingFullWidth((high: UInt8, low: UInt8.Magnitude)) -> (quotient: UInt8, remainder: UInt8)](./uint8/dividingfullwidth%28_%29.md)
  Returns a tuple containing the quotient and remainder of dividing the given value by this value.
- [func multipliedFullWidth(by: UInt8) -> (high: UInt8, low: UInt8.Magnitude)](./uint8/multipliedfullwidth%28by%29.md)
  Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [func multipliedReportingOverflow(by: UInt8) -> (partialValue: UInt8, overflow: Bool)](./uint8/multipliedreportingoverflow%28by%29.md)
  Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func remainderReportingOverflow(dividingBy: UInt8) -> (partialValue: UInt8, overflow: Bool)](./uint8/remainderreportingoverflow%28dividingby%29.md)
  Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [func signum() -> UInt8](./uint8/signum%28%29.md)
  Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
- [func subtractingReportingOverflow(UInt8) -> (partialValue: UInt8, overflow: Bool)](./uint8/subtractingreportingoverflow%28_%29.md)
  Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.
### Type Aliases
- [typealias IntegerLiteralType](./uint8/integerliteraltype.md)
  A type that represents an integer literal.
- [typealias Magnitude](./uint8/magnitude.md)
  A type that can represent the absolute value of any possible value of this type.
- [typealias Stride](./uint8/stride.md)
  A type that represents the distance between two values.
### Type Properties
- [static var bitWidth: Int](./uint8/bitwidth.md)
  The number of bits used for the underlying binary representation of values of this type.
### Default Implementations
- [AdditiveArithmetic Implementations](./uint8/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](./uint8/atomicrepresentable-implementations.md)
- [BinaryInteger Implementations](./uint8/binaryinteger-implementations.md)
- [Comparable Implementations](./uint8/comparable-implementations.md)
- [CustomReflectable Implementations](./uint8/customreflectable-implementations.md)
- [Decodable Implementations](./uint8/decodable-implementations.md)
- [Encodable Implementations](./uint8/encodable-implementations.md)
- [Equatable Implementations](./uint8/equatable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](./uint8/expressiblebyintegerliteral-implementations.md)
- [FixedWidthInteger Implementations](./uint8/fixedwidthinteger-implementations.md)
- [Hashable Implementations](./uint8/hashable-implementations.md)
- [SIMDScalar Implementations](./uint8/simdscalar-implementations.md)
- [UnsignedInteger Implementations](./uint8/unsignedinteger-implementations.md)

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
- [LosslessStringConvertible](./losslessstringconvertible.md)
- [MLTensorScalar](../CoreML/mltensorscalar.md)
- [NetworkFixedWidthInteger](../Network/networkfixedwidthinteger.md)
- [Numeric](./numeric.md)
- [Plottable](../Charts/plottable.md)
- [PrimitivePlottableProtocol](../Charts/primitiveplottableprotocol.md)
- [SIMDScalar](./simdscalar.md)
- [Sendable](./sendable.md)
- [SendableMetatype](./sendablemetatype.md)
- [Strideable](./strideable.md)
- [USDPrim.Attribute.Value](../USDKit/usdprim/attribute/value.md)
- [USDStage.Object.MetadataValue](../USDKit/usdstage/object/metadatavalue.md)
- [USDValueProtocol](../USDKit/usdvalueprotocol.md)
- [UnsignedInteger](./unsignedinteger.md)
- [vDSP_IntegerConvertable](../Accelerate/vdsp_integerconvertable.md)

## See Also

### Unsigned Integers
- [struct UInt](./uint.md)
  An unsigned integer value type.
- [struct UInt16](./uint16.md)
  A 16-bit unsigned integer value type.
- [struct UInt32](./uint32.md)
  A 32-bit unsigned integer value type.
- [struct UInt64](./uint64.md)
  A 64-bit unsigned integer value type.
- [struct UInt128](./uint128.md)
  A 128-bit unsigned integer value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint8)*