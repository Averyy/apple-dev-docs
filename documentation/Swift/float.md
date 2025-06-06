# Float

**Framework**: Swift  
**Kind**: struct

A single-precision, floating-point value type.

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
struct Float
```

## Topics

### Converting Integers
- [init<Source>(Source)](float/init(_:)-7e965.md)
  Creates a new value, rounded to the closest possible representation.
- [init(Int)](float/init(_:)-6cvkq.md)
  Creates a new value, rounded to the closest possible representation.
### Converting Strings
- [init?<S>(S)](float/init(_:)-h2f4.md)
  Creates a new instance from the given string.
- [init?(Substring)](float/init(_:)-4xsj6.md)
### Converting Floating-Point Values
- [init<Source>(Source)](float/init(_:)-1488f.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init<Source>(Source)](float/init(_:)-1oh9p.md)
  Creates a new value, rounded to the closest possible representation.
- [init(Double)](float/init(_:)-1kp2p.md)
  Creates a new instance that approximates the given value.
- [init(Float)](float/init(_:)-975tv.md)
  Creates a new instance initialized to the given value.
- [init(Float80)](float/init(_:)-11orc.md)
  Creates a new instance that approximates the given value.
- [init(CGFloat)](float/init(_:)-5soww.md)
- [init(Float16)](float/init(_:)-ussz.md)
  Creates a new instance that approximates the given value.
- [init(signOf: Float, magnitudeOf: Float)](float/init(signof:magnitudeof:).md)
  Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init(sign: FloatingPointSign, exponent: Int, significand: Float)](float/init(sign:exponent:significand:).md)
  Creates a new value from the given sign, exponent, and significand.
- [init(truncating: NSNumber)](float/init(truncating:).md)
### Converting with No Loss of Precision
- [init?<Source>(exactly: Source)](float/init(exactly:)-8esr8.md)
  Creates a new instance from the given value, if it can be represented exactly.
- [init?(exactly: Double)](float/init(exactly:)-89na7.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float)](float/init(exactly:)-89pn7.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float80)](float/init(exactly:)-6l5fa.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: NSNumber)](float/init(exactly:)-zknq.md)
- [init?<Source>(exactly: Source)](float/init(exactly:)-1h1oe.md)
  Creates a new value, if the given integer can be represented exactly.
- [init?(exactly: Float16)](float/init(exactly:)-8ho5q.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
### Creating a Random Value
- [static func random(in: Range<Self>) -> Self](float/random(in:)-6ided.md)
  Returns a random value within the specified range.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](float/random(in:using:)-1m6gf.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random(in: ClosedRange<Self>) -> Self](float/random(in:)-5o5h8.md)
  Returns a random value within the specified range.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](float/random(in:using:)-613hx.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
### Performing Calculations
- [Floating-Point Operators for Float](floating-point-operators-for-float.md)
  Perform arithmetic and bitwise operations or compare values.
- [func addingProduct(Self, Self) -> Self](float/addingproduct(_:_:).md)
  Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [func addProduct(Float, Float)](float/addproduct(_:_:).md)
  Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [func squareRoot() -> Self](float/squareroot.md)
  Returns the square root of the value, rounded to a representable value.
- [func formSquareRoot()](float/formsquareroot.md)
  Replaces this value with its square root, rounded to a representable value.
- [func remainder(dividingBy: Self) -> Self](float/remainder(dividingby:).md)
  Returns the remainder of this value divided by the given value.
- [func formRemainder(dividingBy: Float)](float/formremainder(dividingby:).md)
  Replaces this value with the remainder of itself divided by the given value.
- [func truncatingRemainder(dividingBy: Self) -> Self](float/truncatingremainder(dividingby:).md)
  Returns the remainder of this value divided by the given value using truncating division.
- [func formTruncatingRemainder(dividingBy: Float)](float/formtruncatingremainder(dividingby:).md)
  Replaces this value with the remainder of itself divided by the given value using truncating division.
- [func negate()](float/negate.md)
  Replaces this value with its additive inverse.
### Rounding Values
- [func rounded() -> Self](float/rounded.md)
- [func rounded(FloatingPointRoundingRule) -> Self](float/rounded(_:).md)
  Returns this value rounded to an integral value using the specified rounding rule.
- [func round()](float/round.md)
- [func round(FloatingPointRoundingRule)](float/round(_:).md)
  Rounds the value to an integral value using the specified rounding rule.
### Comparing Values
- [Floating-Point Operators for Float](floating-point-operators-for-float.md)
  Perform arithmetic and bitwise operations or compare values.
- [func isEqual(to: Float) -> Bool](float/isequal(to:).md)
  Returns a Boolean value indicating whether this instance is equal to the given value.
- [func isLess(than: Float) -> Bool](float/isless(than:).md)
  Returns a Boolean value indicating whether this instance is less than the given value.
- [func isLessThanOrEqualTo(Float) -> Bool](float/islessthanorequalto(_:).md)
  Returns a Boolean value indicating whether this instance is less than or equal to the given value.
- [func isTotallyOrdered(belowOrEqualTo: Self) -> Bool](float/istotallyordered(beloworequalto:).md)
  Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.
- [static func maximum(Self, Self) -> Self](float/maximum(_:_:).md)
  Returns the greater of the two given values.
- [static func maximumMagnitude(Self, Self) -> Self](float/maximummagnitude(_:_:).md)
  Returns the value with greater magnitude.
- [static func minimum(Self, Self) -> Self](float/minimum(_:_:).md)
  Returns the lesser of the two given values.
- [static func minimumMagnitude(Self, Self) -> Self](float/minimummagnitude(_:_:).md)
  Returns the value with lesser magnitude.
### Finding the Sign and Magnitude
- [var magnitude: Float](float/magnitude-swift.property.md)
  The magnitude of this value.
- [var sign: FloatingPointSign](float/sign.md)
  The sign of the floating-point value.
- [typealias Magnitude](float/magnitude-swift.typealias.md)
  A type that can represent the absolute value of any possible value of the conforming type.
### Querying a Float
- [var ulp: Float](float/ulp.md)
  The unit in the last place of this value.
- [var significand: Float](float/significand.md)
  The significand of the floating-point value.
- [var exponent: Int](float/exponent-swift.property.md)
  The exponent of the floating-point value.
- [var nextUp: Float](float/nextup.md)
  The least representable value that compares greater than this value.
- [var nextDown: Self](float/nextdown.md)
  The greatest representable value that compares less than this value.
- [var binade: Float](float/binade.md)
  The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.
### Accessing Numeric Constants
- [static var pi: Float](float/pi.md)
  The mathematical constant pi (π), approximately equal to 3.14159.
- [static var infinity: Float](float/infinity.md)
  Positive infinity.
- [static var greatestFiniteMagnitude: Float](float/greatestfinitemagnitude.md)
  The greatest finite number representable by this type.
- [static var nan: Float](float/nan.md)
  A quiet NaN (“not a number”).
- [static var signalingNaN: Float](float/signalingnan.md)
  A signaling NaN (“not a number”).
- [static var ulpOfOne: Float](float/ulpofone.md)
  The unit in the last place of 1.0.
- [static var leastNormalMagnitude: Float](float/leastnormalmagnitude.md)
  The least positive normal number.
- [static var leastNonzeroMagnitude: Float](float/leastnonzeromagnitude.md)
  The least positive number.
- [static var zero: Self](float/zero.md)
  The zero value.
### Working with Binary Representation
- [var bitPattern: UInt32](float/bitpattern.md)
  The bit pattern of the value’s encoding.
- [var significandBitPattern: UInt32](float/significandbitpattern.md)
  The raw encoding of the value’s significand field.
- [var significandWidth: Int](float/significandwidth.md)
  The number of bits required to represent the value’s significand.
- [var exponentBitPattern: UInt](float/exponentbitpattern.md)
  The raw encoding of the value’s exponent field.
- [static var significandBitCount: Int](float/significandbitcount.md)
  The available number of fractional significand bits.
- [static var exponentBitCount: Int](float/exponentbitcount.md)
  The number of bits used to represent the type’s exponent.
- [static var radix: Int](float/radix.md)
  The radix, or base of exponentiation, for a floating-point type.
- [init(bitPattern: UInt32)](float/init(bitpattern:).md)
  Creates a new value with the given bit pattern.
- [init(sign: FloatingPointSign, exponentBitPattern: UInt, significandBitPattern: UInt32)](float/init(sign:exponentbitpattern:significandbitpattern:).md)
  Creates a new instance from the specified sign and bit patterns.
- [init(nan: Float.RawSignificand, signaling: Bool)](float/init(nan:signaling:).md)
  Creates a NaN (“not a number”) value with the specified payload.
- [typealias Exponent](float/exponent-swift.typealias.md)
  A type that can represent any written exponent.
- [typealias RawSignificand](float/rawsignificand.md)
  A type that represents the encoded significand of a value.
### Querying a Float’s State
- [var isZero: Bool](float/iszero.md)
  A Boolean value indicating whether the instance is equal to zero.
- [var isFinite: Bool](float/isfinite.md)
  A Boolean value indicating whether this instance is finite.
- [var isInfinite: Bool](float/isinfinite.md)
  A Boolean value indicating whether the instance is infinite.
- [var isNaN: Bool](float/isnan.md)
  A Boolean value indicating whether the instance is NaN (“not a number”).
- [var isSignalingNaN: Bool](float/issignalingnan.md)
  A Boolean value indicating whether the instance is a signaling NaN.
- [var isNormal: Bool](float/isnormal.md)
  A Boolean value indicating whether this instance is normal.
- [var isSubnormal: Bool](float/issubnormal.md)
  A Boolean value indicating whether the instance is subnormal.
- [var isCanonical: Bool](float/iscanonical.md)
  A Boolean value indicating whether the instance’s representation is in its canonical form.
- [var floatingPointClass: FloatingPointClassification](float/floatingpointclass.md)
  The classification of this value.
### Encoding and Decoding Values
- [func encode(to: any Encoder) throws](float/encode(to:).md)
  Encodes this value into the given encoder.
- [init(from: any Decoder) throws](float/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Creating a Range
- [static func ... (Self, Self) -> ClosedRange<Self>](float/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.
### Describing a Float
- [func hash(into: inout Hasher)](float/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var description: String](float/description.md)
  A textual representation of the value.
- [var debugDescription: String](float/debugdescription.md)
  A textual representation of the value, suitable for debugging.
- [var customMirror: Mirror](float/custommirror.md)
  A mirror that reflects the `Float` instance.
- [var hashValue: Int](float/hashvalue.md)
  The hash value.
### SIMD-Supporting Types
- [typealias SIMDMaskScalar](float/simdmaskscalar.md)
- [struct SIMD2Storage](float/simd2storage.md)
  Storage for a vector of two floating-point values.
- [struct SIMD4Storage](float/simd4storage.md)
  Storage for a vector of four floating-point values.
- [struct SIMD8Storage](float/simd8storage.md)
  Storage for a vector of eight floating-point values.
- [struct SIMD16Storage](float/simd16storage.md)
  Storage for a vector of 16 floating-point values.
- [struct SIMD32Storage](float/simd32storage.md)
  Storage for a vector of 32 floating-point values.
- [struct SIMD64Storage](float/simd64storage.md)
  Storage for a vector of 64 floating-point values.
### Infrequently Used Functionality
- [init()](float/init.md)
- [init(integerLiteral: Int64)](float/init(integerliteral:).md)
  Creates an instance initialized to the specified integer value.
- [init(floatLiteral: Float)](float/init(floatliteral:).md)
  Creates an instance initialized to the specified floating-point value.
- [init(integerLiteral: Self)](float/init(integerliteral:)-6hc7h.md)
- [func advanced(by: Float) -> Float](float/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Float) -> Float](float/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [func write<Target>(to: inout Target)](float/write(to:).md)
  Writes a textual representation of this instance into the given output stream.
### Deprecated
- [init(NSNumber)](float/init(_:)-7dbrz.md)
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](float/customplaygroundquicklook.md)
  A custom playground Quick Look for the `Float` instance.
### Type Properties
- [static var mlMultiArrayDataType: MLMultiArrayDataType](float/mlmultiarraydatatype.md)
### Default Implementations
- [AdditiveArithmetic Implementations](float/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](float/atomicrepresentable-implementations.md)
- [BinaryFloatingPoint Implementations](float/binaryfloatingpoint-implementations.md)
- [Comparable Implementations](float/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](float/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](float/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](float/customstringconvertible-implementations.md)
- [Decodable Implementations](float/decodable-implementations.md)
- [Encodable Implementations](float/encodable-implementations.md)
- [EntityIdentifierConvertible Implementations](float/entityidentifierconvertible-implementations.md)
- [Equatable Implementations](float/equatable-implementations.md)
- [ExpressibleByFloatLiteral Implementations](float/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](float/expressiblebyintegerliteral-implementations.md)
- [FloatingPoint Implementations](float/floatingpoint-implementations.md)
- [Hashable Implementations](float/hashable-implementations.md)
- [LosslessStringConvertible Implementations](float/losslessstringconvertible-implementations.md)
- [Numeric Implementations](float/numeric-implementations.md)
- [SIMDScalar Implementations](float/simdscalar-implementations.md)
- [SignedNumeric Implementations](float/signednumeric-implementations.md)
- [Strideable Implementations](float/strideable-implementations.md)
- [TextOutputStreamable Implementations](float/textoutputstreamable-implementations.md)

## Relationships

### Conforms To
- [AdditiveArithmetic](additivearithmetic.md)
- [AnimatableData](../RealityKit/AnimatableData.md)
- [AtomicRepresentable](../synchronization/atomicrepresentable.md)
- [BNNSScalar](../Accelerate/BNNSScalar.md)
- [BinaryFloatingPoint](binaryfloatingpoint.md)
- [BindableData](../RealityKit/BindableData.md)
- [BitwiseCopyable](bitwisecopyable.md)
- [CKRecordValueProtocol](../CloudKit/CKRecordValueProtocol.md)
- [CVarArg](cvararg.md)
- [Comparable](comparable.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomReflectable](customreflectable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [EntityIdentifierConvertible](../AppIntents/EntityIdentifierConvertible.md)
- [Equatable](equatable.md)
- [ExpressibleByFloatLiteral](expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](expressiblebyintegerliteral.md)
- [FloatingPoint](floatingpoint.md)
- [Hashable](hashable.md)
- [LosslessStringConvertible](losslessstringconvertible.md)
- [MLShapedArrayScalar](../CoreML/MLShapedArrayScalar.md)
- [MLTensorScalar](../CoreML/MLTensorScalar.md)
- [Numeric](numeric.md)
- [Plottable](../Charts/Plottable.md)
- [PrimitivePlottableProtocol](../Charts/PrimitivePlottableProtocol.md)
- [SIMDScalar](simdscalar.md)
- [Sendable](sendable.md)
- [SignedNumeric](signednumeric.md)
- [Strideable](strideable.md)
- [TextOutputStreamable](textoutputstreamable.md)
- [VectorArithmetic](../SwiftUI/VectorArithmetic.md)
- [vDSP_DiscreteFourierTransformable](../Accelerate/vDSP_DiscreteFourierTransformable.md)
- [vDSP_FloatingPointBiquadFilterable](../Accelerate/vDSP_FloatingPointBiquadFilterable.md)
- [vDSP_FloatingPointConvertable](../Accelerate/vDSP_FloatingPointConvertable.md)
- [vDSP_FloatingPointDiscreteFourierTransformable](../Accelerate/vDSP_FloatingPointDiscreteFourierTransformable.md)
- [vDSP_FloatingPointGeneratable](../Accelerate/vDSP_FloatingPointGeneratable.md)

## See Also

- [struct Int](int.md)
  A signed integer value type.
- [struct Double](double.md)
  A double-precision, floating-point value type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float)*