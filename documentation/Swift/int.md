# Int

**Framework**: Swift  
**Kind**: struct

A signed integer value type.

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
struct Int
```

#### Overview

On 32-bit platforms, `Int` is the same size as `Int32`, and on 64-bit platforms, `Int` is the same size as `Int64`.

## Topics

### Converting Integers
- [init<T>(T)](int/init(_:)-4ekvl.md)
  Creates a new instance from the given integer.
- [init?<T>(exactly: T)](int/init(exactly:)-b1dy.md)
- [init<Other>(clamping: Other)](int/init(clamping:).md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<T>(truncatingIfNeeded: T)](int/init(truncatingifneeded:).md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
- [init(bitPattern: UInt)](int/init(bitpattern:)-72037.md)
  Creates a new instance with the same memory representation as the given value.
- [init?(exactly: NSNumber)](int/init(exactly:)-177ax.md)
- [init(truncating: NSNumber)](int/init(truncating:).md)
### Converting Floating-Point Values
- [init<T>(T)](int/init(_:)-6gt9z.md)
- [init(Double)](int/init(_:)-8vbwo.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Float)](int/init(_:)-2oscb.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Float16)](int/init(_:)-3huv0.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Float80)](int/init(_:)-66i0w.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(CGFloat)](int/init(_:)-5q6q5.md)
### Converting with No Loss of Precision
- [init?<T>(exactly: T)](int/init(exactly:)-7yhn6.md)
- [init?(exactly: Double)](int/init(exactly:)-77kq8.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float)](int/init(exactly:)-7qdwf.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float16)](int/init(exactly:)-5xh2s.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init?(exactly: Float80)](int/init(exactly:)-5kot1.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
### Converting Strings
- [init?(String)](int/init(_:)-2hmii.md)
  Creates a new integer value from the given string.
- [init?<S>(S, radix: Int)](int/init(_:radix:).md)
  Creates a new integer value from the given string and radix.
### Creating a Random Integer
- [static func random(in: Range<Self>) -> Self](int/random(in:)-9mjpw.md)
  Returns a random value within the specified range.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](int/random(in:using:)-4lsb5.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random(in: ClosedRange<Self>) -> Self](int/random(in:)-8zzqh.md)
  Returns a random value within the specified range.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](int/random(in:using:)-3dwv4.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
### Performing Calculations
- [Integer Operators](integer-operators.md)
  Perform arithmetic and bitwise operations or compare values.
- [func negate()](int/negate.md)
  Replaces this value with its additive inverse.
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](int/quotientandremainder(dividingby:).md)
  Returns the quotient and remainder of this value divided by the given value.
- [func isMultiple(of: Self) -> Bool](int/ismultiple(of:).md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.
### Performing Calculations with Overflow
- [func addingReportingOverflow(Int) -> (partialValue: Int, overflow: Bool)](int/addingreportingoverflow(_:).md)
  Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func subtractingReportingOverflow(Int) -> (partialValue: Int, overflow: Bool)](int/subtractingreportingoverflow(_:).md)
  Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func multipliedReportingOverflow(by: Int) -> (partialValue: Int, overflow: Bool)](int/multipliedreportingoverflow(by:).md)
  Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividedReportingOverflow(by: Int) -> (partialValue: Int, overflow: Bool)](int/dividedreportingoverflow(by:).md)
  Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func remainderReportingOverflow(dividingBy: Int) -> (partialValue: Int, overflow: Bool)](int/remainderreportingoverflow(dividingby:).md)
  Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
### Performing Double-Width Calculations
- [func multipliedFullWidth(by: Int) -> (high: Int, low: Int.Magnitude)](int/multipliedfullwidth(by:).md)
  Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [func dividingFullWidth((high: Int, low: Int.Magnitude)) -> (quotient: Int, remainder: Int)](int/dividingfullwidth(_:).md)
  Returns a tuple containing the quotient and remainder of dividing the given value by this value.
### Finding the Sign and Magnitude
- [var magnitude: UInt](int/magnitude-swift.property.md)
  The magnitude of this value.
- [typealias Magnitude](int/magnitude-swift.typealias.md)
  A type that can represent the absolute value of any possible value of this type.
- [func abs<T>(T) -> T](abs(_:).md)
  Returns the absolute value of the given number.
- [func signum() -> Int](int/signum.md)
  Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
### Accessing Numeric Constants
- [static var zero: Self](int/zero.md)
  The zero value.
- [static var min: Self](int/min.md)
  The minimum representable integer in this type.
- [static var max: Self](int/max.md)
  The maximum representable integer in this type.
- [static var isSigned: Bool](int/issigned.md)
  A Boolean value indicating whether this type is a signed integer type.
### Working with Byte Order
- [var byteSwapped: Int](int/byteswapped.md)
  A representation of this integer with the byte order swapped.
- [var littleEndian: Self](int/littleendian.md)
  The little-endian representation of this integer.
- [var bigEndian: Self](int/bigendian.md)
  The big-endian representation of this integer.
- [init(littleEndian: Self)](int/init(littleendian:).md)
  Creates an integer from its little-endian representation, changing the byte order if necessary.
- [init(bigEndian: Self)](int/init(bigendian:).md)
  Creates an integer from its big-endian representation, changing the byte order if necessary.
### Working with Binary Representation
- [static var bitWidth: Int](int/bitwidth.md)
  The number of bits used for the underlying binary representation of values of this type.
- [var bitWidth: Int](int/bitwidth-swift.property.md)
  The number of bits in the current binary representation of this value.
- [var nonzeroBitCount: Int](int/nonzerobitcount.md)
  The number of bits equal to 1 in this value’s binary representation.
- [var leadingZeroBitCount: Int](int/leadingzerobitcount.md)
  The number of leading zeros in this value’s binary representation.
- [var trailingZeroBitCount: Int](int/trailingzerobitcount.md)
  The number of trailing zeros in this value’s binary representation.
- [var words: Int.Words](int/words-swift.property.md)
  A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
- [struct Words](int/words-swift.struct.md)
  A type that represents the words of this integer.
### Working with Memory Addresses
- [init<P>(bitPattern: P?)](int/init(bitpattern:)-2i0qy.md)
  Creates a new value with the bit pattern of the given pointer.
- [init(bitPattern: ObjectIdentifier)](int/init(bitpattern:)-2o9co.md)
  Creates an integer that captures the full value of the given object identifier.
- [init(bitPattern: OpaquePointer?)](int/init(bitpattern:)-5qm7a.md)
  Creates a new value with the bit pattern of the given pointer.
### Encoding and Decoding Values
- [func encode(to: any Encoder) throws](int/encode(to:).md)
  Encodes this value into the given encoder.
- [init(from: any Decoder) throws](int/init(from:)-5ru5.md)
  Creates a new instance by decoding from the given decoder.
### Describing an Integer
- [var description: String](int/description.md)
  A textual representation of this value.
- [func hash(into: inout Hasher)](int/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var customMirror: Mirror](int/custommirror.md)
  A mirror that reflects the `Int` instance.
### Using an Integer as a Data Value
- [init?(from: MLDataValue)](int/init(from:)-kl1p.md)
  Creates an instance of the conforming type from a data value.
- [var dataValue: MLDataValue](int/datavalue.md)
  The value of the conforming type’s instance wrapped in a data value.
- [var identifierValue: MLDataValue](int/identifiervalue.md)
  The value of the unique identifier wrapped in a data value.
- [static var dataValueType: MLDataValue.ValueType](int/datavaluetype.md)
  The underlying type the conforming type uses when it wraps itself in a data value.
### Infrequently Used Functionality
- [init()](int/init.md)
  Creates a new value equal to zero.
- [init(integerLiteral: Self)](int/init(integerliteral:).md)
- [typealias IntegerLiteralType](int/integerliteraltype.md)
  A type that represents an integer literal.
- [func distance(to: Int) -> Int](int/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [func advanced(by: Int) -> Int](int/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [typealias Stride](int/stride.md)
  A type that represents the distance between two values.
- [var hashValue: Int](int/hashvalue.md)
  The hash value.
### Deprecated
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](int/customplaygroundquicklook.md)
  A custom playground Quick Look for the `Int` instance.
- [init(NSNumber)](int/init(_:)-3mb3q.md)
### SIMD-Supporting Types
- [typealias SIMDMaskScalar](int/simdmaskscalar.md)
- [struct SIMD2Storage](int/simd2storage.md)
  Storage for a vector of two integers.
- [struct SIMD4Storage](int/simd4storage.md)
  Storage for a vector of four integers.
- [struct SIMD8Storage](int/simd8storage.md)
  Storage for a vector of eight integers.
- [struct SIMD16Storage](int/simd16storage.md)
  Storage for a vector of 16 integers.
- [struct SIMD32Storage](int/simd32storage.md)
  Storage for a vector of 32 integers.
- [struct SIMD64Storage](int/simd64storage.md)
  Storage for a vector of 64 integers.
### Operators
- [static func != (Int, Int) -> Bool](int/!=(_:_:).md)
- [static func &>>= (inout Int, Int)](int/&__=(_:_:)-2i06i.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &<<= (inout Int, Int)](int/&__=(_:_:)-58orm.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func < (Int, Int) -> Bool](int/_(_:_:)-3wpum.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func ^= (inout Int, Int)](int/_=(_:_:)-1ypi9.md)
  Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [static func %= (inout Int, Int)](int/_=(_:_:)-30t77.md)
  Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [static func |= (inout Int, Int)](int/_=(_:_:)-4b29i.md)
  Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
### Type Aliases
- [typealias Specification](int/specification.md)
- [typealias UnwrappedType](int/unwrappedtype.md)
- [typealias ValueType](int/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](int/defaultresolverspecification.md)
### Default Implementations
- [AdditiveArithmetic Implementations](int/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](int/atomicrepresentable-implementations.md)
- [BinaryInteger Implementations](int/binaryinteger-implementations.md)
- [CodingKeyRepresentable Implementations](int/codingkeyrepresentable-implementations.md)
- [Comparable Implementations](int/comparable-implementations.md)
- [CustomReflectable Implementations](int/customreflectable-implementations.md)
- [CustomURLRepresentationParameterConvertible Implementations](int/customurlrepresentationparameterconvertible-implementations.md)
- [Decodable Implementations](int/decodable-implementations.md)
- [Encodable Implementations](int/encodable-implementations.md)
- [EntityIdentifierConvertible Implementations](int/entityidentifierconvertible-implementations.md)
- [Equatable Implementations](int/equatable-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](int/expressiblebyintegerliteral-implementations.md)
- [FixedWidthInteger Implementations](int/fixedwidthinteger-implementations.md)
- [Hashable Implementations](int/hashable-implementations.md)
- [MLDataValueConvertible Implementations](int/mldatavalueconvertible-implementations.md)
- [MLIdentifier Implementations](int/mlidentifier-implementations.md)
- [SIMDScalar Implementations](int/simdscalar-implementations.md)
- [SignedInteger Implementations](int/signedinteger-implementations.md)
- [SignedNumeric Implementations](int/signednumeric-implementations.md)
- [Strideable Implementations](int/strideable-implementations.md)

## Relationships

### Conforms To
- [AdditiveArithmetic](additivearithmetic.md)
- [AtomicRepresentable](../synchronization/atomicrepresentable.md)
- [BinaryInteger](binaryinteger.md)
- [BindableData](../RealityKit/BindableData.md)
- [BitwiseCopyable](bitwisecopyable.md)
- [CKRecordValueProtocol](../CloudKit/CKRecordValueProtocol.md)
- [CVarArg](cvararg.md)
- [CodingKeyRepresentable](codingkeyrepresentable.md)
- [Comparable](comparable.md)
- [Copyable](copyable.md)
- [CustomReflectable](customreflectable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [CustomURLRepresentationParameterConvertible](../AppIntents/CustomURLRepresentationParameterConvertible.md)
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [EntityIdentifierConvertible](../AppIntents/EntityIdentifierConvertible.md)
- [Equatable](equatable.md)
- [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md)
- [FixedWidthInteger](fixedwidthinteger.md)
- [Hashable](hashable.md)
- [LosslessStringConvertible](losslessstringconvertible.md)
- [MLDataValueConvertible](../CreateML/MLDataValueConvertible.md)
- [MLIdentifier](../CreateML/MLIdentifier.md)
- [MLTensorRangeExpression](../CoreML/MLTensorRangeExpression.md)
- [MirrorPath](mirrorpath.md)
- [Numeric](numeric.md)
- [Plottable](../Charts/Plottable.md)
- [PrimitivePlottableProtocol](../Charts/PrimitivePlottableProtocol.md)
- [RangeComparableProperty](../AppIntents/RangeComparableProperty.md)
- [SIMDScalar](simdscalar.md)
- [Sendable](sendable.md)
- [SignedInteger](signedinteger.md)
- [SignedNumeric](signednumeric.md)
- [Strideable](strideable.md)

## See Also

- [struct Double](double.md)
  A double-precision, floating-point value type.
- [struct String](string.md)
  A Unicode string value that is a collection of characters.
- [struct Array](array.md)
  An ordered, random-access collection.
- [struct Dictionary](dictionary.md)
  A collection whose elements are key-value pairs.
- [Swift Standard Library](swift-standard-library.md)
  Solve complex problems and write high-performance, readable code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int)*