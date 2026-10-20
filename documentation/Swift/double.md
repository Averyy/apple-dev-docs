# Double

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

A double-precision (64-bit), floating-point value type.

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
struct Double
```

## Topics

### Converting Integers
- [init<Source>(Source)](./double/init%28_%29-5blrp.md)
  Creates a new value, rounded to the closest possible representation.
- [init(Int)](./double/init%28_%29-84ohu.md)
  Creates a new value, rounded to the closest possible representation.
### Converting Strings
- [init?<S>(S)](./double/init%28_%29-5wmm8.md)
  Creates a new instance from the given string.
- [init?(Substring)](./double/init%28_%29-15kej.md)
### Converting Floating-Point Values
- [init<Source>(Source)](./double/init%28_%29-1488d.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init(Double)](./double/init%28_%29-o1k9.md)
  Creates a new instance initialized to the given value.
- [init(Float)](./double/init%28_%29-5h7qh.md)
  Creates a new instance that approximates the given value.
- [init(Float16)](./double/init%28_%29-aeox.md)
  Creates a new instance that approximates the given value.
- [init(Float80)](./double/init%28_%29-9z7ob.md)
  Creates a new instance that approximates the given value.
- [init(CGFloat)](./double/init%28_%29-7ag2w.md)
- [init(sign: FloatingPointSign, exponent: Int, significand: Double)](./double/init%28sign,exponent,significand%29.md)
  Creates a new value from the given sign, exponent, and significand.
- [init(signOf: Double, magnitudeOf: Double)](./double/init%28signof,magnitudeof%29.md)
  Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init<Source>(Source)](./double/init%28_%29-1oh9r.md)
  Creates a new value, rounded to the closest possible representation.
- [init(truncating: NSNumber)](./double/init%28truncating%29.md)
### Converting with No Loss of Precision
- [init?<Source>(exactly: Source)](./double/init%28exactly%29-8esra.md)
  Creates a new instance from the given value, if it can be represented exactly.
- [init?<Source>(exactly: Source)](./double/init%28exactly%29-1h1oc.md)
  Creates a new value, if the given integer can be represented exactly.
- [init?<Source>(exactly: Source)](./double/init%28exactly%29-2uexo.md)
  Creates a new value, if the given integer can be represented exactly.
- [init?(exactly: Double)](./double/init%28exactly%29-2l6p1.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float)](./double/init%28exactly%29-7cl0t.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float16)](./double/init%28exactly%29-50ofc.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: Float80)](./double/init%28exactly%29-63925.md)
  Creates a new instance initialized to the given value, if it can be represented without rounding.
- [init?(exactly: NSNumber)](./double/init%28exactly%29-8e00y.md)
### Creating a Random Value
- [static func random(in: Range<Self>) -> Self](./double/random%28in%29-6idef.md)
  Returns a random value within the specified range.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](./double/random%28in,using%29-1m6gd.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random(in: ClosedRange<Self>) -> Self](./double/random%28in%29-5o5ha.md)
  Returns a random value within the specified range.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](./double/random%28in,using%29-613hz.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
### Performing Calculations
- [Floating-Point Operators for Double](./floating-point-operators-for-double.md)
  Perform arithmetic and bitwise operations or compare values.
- [func addingProduct(Self, Self) -> Self](./double/addingproduct%28_,_%29.md)
  Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [func addProduct(Double, Double)](./double/addproduct%28_,_%29.md)
  Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [func squareRoot() -> Self](./double/squareroot%28%29.md)
  Returns the square root of the value, rounded to a representable value.
- [func formSquareRoot()](./double/formsquareroot%28%29.md)
  Replaces this value with its square root, rounded to a representable value.
- [func remainder(dividingBy: Self) -> Self](./double/remainder%28dividingby%29.md)
  Returns the remainder of this value divided by the given value.
- [func formRemainder(dividingBy: Double)](./double/formremainder%28dividingby%29.md)
  Replaces this value with the remainder of itself divided by the given value.
- [func truncatingRemainder(dividingBy: Self) -> Self](./double/truncatingremainder%28dividingby%29.md)
  Returns the remainder of this value divided by the given value using truncating division.
- [func formTruncatingRemainder(dividingBy: Double)](./double/formtruncatingremainder%28dividingby%29.md)
  Replaces this value with the remainder of itself divided by the given value using truncating division.
- [func negate()](./double/negate%28%29.md)
  Replaces this value with its additive inverse.
### Rounding Values
- [func rounded() -> Self](./double/rounded%28%29.md)
- [func rounded(FloatingPointRoundingRule) -> Self](./double/rounded%28_%29.md)
  Returns this value rounded to an integral value using the specified rounding rule.
- [func round()](./double/round%28%29.md)
- [func round(FloatingPointRoundingRule)](./double/round%28_%29.md)
  Rounds the value to an integral value using the specified rounding rule.
### Comparing Values
- [Floating-Point Operators for Double](./floating-point-operators-for-double.md)
  Perform arithmetic and bitwise operations or compare values.
- [func isEqual(to: Double) -> Bool](./double/isequal%28to%29.md)
  Returns a Boolean value indicating whether this instance is equal to the given value.
- [func isLess(than: Double) -> Bool](./double/isless%28than%29.md)
  Returns a Boolean value indicating whether this instance is less than the given value.
- [func isLessThanOrEqualTo(Double) -> Bool](./double/islessthanorequalto%28_%29.md)
  Returns a Boolean value indicating whether this instance is less than or equal to the given value.
- [func isTotallyOrdered(belowOrEqualTo: Self) -> Bool](./double/istotallyordered%28beloworequalto%29.md)
  Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.
- [static func minimum(Self, Self) -> Self](./double/minimum%28_,_%29.md)
  Returns the lesser of the two given values.
- [static func minimumMagnitude(Self, Self) -> Self](./double/minimummagnitude%28_,_%29.md)
  Returns the value with lesser magnitude.
- [static func maximum(Self, Self) -> Self](./double/maximum%28_,_%29.md)
  Returns the greater of the two given values.
- [static func maximumMagnitude(Self, Self) -> Self](./double/maximummagnitude%28_,_%29.md)
  Returns the value with greater magnitude.
### Finding the Sign and Magnitude
- [var magnitude: Double](./double/magnitude-swift.property.md)
  The magnitude of this value.
- [var sign: FloatingPointSign](./double/sign.md)
  The sign of the floating-point value.
- [typealias Magnitude](./double/magnitude-swift.typealias.md)
  A type that can represent the absolute value of any possible value of the conforming type.
### Querying a Double
- [var ulp: Double](./double/ulp.md)
  The unit in the last place of this value.
- [var significand: Double](./double/significand.md)
  The significand of the floating-point value.
- [var exponent: Int](./double/exponent-swift.property.md)
  The exponent of the floating-point value.
- [var nextUp: Double](./double/nextup.md)
  The least representable value that compares greater than this value.
- [var nextDown: Self](./double/nextdown.md)
  The greatest representable value that compares less than this value.
- [var binade: Double](./double/binade.md)
  The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.
### Accessing Numeric Constants
- [static var pi: Double](./double/pi.md)
  The mathematical constant pi (π), approximately equal to 3.14159.
- [static var infinity: Double](./double/infinity.md)
  Positive infinity.
- [static var greatestFiniteMagnitude: Double](./double/greatestfinitemagnitude.md)
  The greatest finite number representable by this type.
- [static var nan: Double](./double/nan.md)
  A quiet NaN (“not a number”).
- [static var signalingNaN: Double](./double/signalingnan.md)
  A signaling NaN (“not a number”).
- [static var ulpOfOne: Double](./double/ulpofone.md)
  The unit in the last place of 1.0.
- [static var leastNonzeroMagnitude: Double](./double/leastnonzeromagnitude.md)
  The least positive number.
- [static var leastNormalMagnitude: Double](./double/leastnormalmagnitude.md)
  The least positive normal number.
- [static var zero: Self](./double/zero.md)
  The zero value.
### Working with Binary Representation
- [var bitPattern: UInt64](./double/bitpattern.md)
  The bit pattern of the value’s encoding.
- [var significandBitPattern: UInt64](./double/significandbitpattern.md)
  The raw encoding of the value’s significand field.
- [var significandWidth: Int](./double/significandwidth.md)
  The number of bits required to represent the value’s significand.
- [var exponentBitPattern: UInt](./double/exponentbitpattern.md)
  The raw encoding of the value’s exponent field.
- [static var significandBitCount: Int](./double/significandbitcount.md)
  The available number of fractional significand bits.
- [static var exponentBitCount: Int](./double/exponentbitcount.md)
  The number of bits used to represent the type’s exponent.
- [static var radix: Int](./double/radix.md)
  The radix, or base of exponentiation, for a floating-point type.
- [init(bitPattern: UInt64)](./double/init%28bitpattern%29.md)
  Creates a new value with the given bit pattern.
- [init(sign: FloatingPointSign, exponentBitPattern: UInt, significandBitPattern: UInt64)](./double/init%28sign,exponentbitpattern,significandbitpattern%29.md)
  Creates a new instance from the specified sign and bit patterns.
- [init(nan: Double.RawSignificand, signaling: Bool)](./double/init%28nan,signaling%29.md)
  Creates a NaN (“not a number”) value with the specified payload.
- [typealias Exponent](./double/exponent-swift.typealias.md)
  A type that can represent any written exponent.
- [typealias RawSignificand](./double/rawsignificand.md)
  A type that represents the encoded significand of a value.
- [typealias RawExponent](./double/rawexponent.md)
  A type that represents the encoded exponent of a value.
### Querying a Double’s State
- [var isZero: Bool](./double/iszero.md)
  A Boolean value indicating whether the instance is equal to zero.
- [var isFinite: Bool](./double/isfinite.md)
  A Boolean value indicating whether this instance is finite.
- [var isInfinite: Bool](./double/isinfinite.md)
  A Boolean value indicating whether the instance is infinite.
- [var isNaN: Bool](./double/isnan.md)
  A Boolean value indicating whether the instance is NaN (“not a number”).
- [var isSignalingNaN: Bool](./double/issignalingnan.md)
  A Boolean value indicating whether the instance is a signaling NaN.
- [var isNormal: Bool](./double/isnormal.md)
  A Boolean value indicating whether this instance is normal.
- [var isSubnormal: Bool](./double/issubnormal.md)
  A Boolean value indicating whether the instance is subnormal.
- [var isCanonical: Bool](./double/iscanonical.md)
  A Boolean value indicating whether the instance’s representation is in its canonical form.
- [var floatingPointClass: FloatingPointClassification](./double/floatingpointclass.md)
  The classification of this value.
### Encoding and Decoding Values
- [func encode(to: any Encoder) throws](./double/encode%28to%29.md)
  Encodes this value into the given encoder.
- [init(from: any Decoder) throws](./double/init%28from%29.md)
  Creates a new instance by decoding from the given decoder.
### Creating a Range
- [static func ... (Self, Self) -> ClosedRange<Self>](./double/dotdotdot%28_,_%29.md)
  Returns a closed range that contains both of its bounds.
### Describing a Double
- [var description: String](./double/description.md)
  A textual representation of the value.
- [var debugDescription: String](./double/debugdescription.md)
  A textual representation of the value, suitable for debugging.
- [var customMirror: Mirror](./double/custommirror.md)
  A mirror that reflects the `Double` instance.
- [func hash(into: inout Hasher)](./double/hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Infrequently Used Functionality
- [init()](./double/init%28%29.md)
- [init(floatLiteral: Double)](./double/init%28floatliteral%29.md)
  Creates an instance initialized to the specified floating-point value.
- [init(integerLiteral: Int64)](./double/init%28integerliteral%29.md)
  Creates an instance initialized to the specified integer value.
- [init(integerLiteral: Self)](./double/init%28integerliteral%29-6hc7j.md)
- [typealias FloatLiteralType](./double/floatliteraltype.md)
  A type that represents a floating-point literal.
- [typealias IntegerLiteralType](./double/integerliteraltype.md)
  A type that represents an integer literal.
- [func advanced(by: Double) -> Double](./double/advanced%28by%29.md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Double) -> Double](./double/distance%28to%29.md)
  Returns the distance from this value to the given value, expressed as a stride.
- [typealias Stride](./double/stride.md)
  A type that represents the distance between two values.
- [func write<Target>(to: inout Target)](./double/write%28to%29.md)
  Writes a textual representation of this instance into the given output stream.
- [var hashValue: Int](./double/hashvalue.md)
  The hash value.
### SIMD-Supporting Types
- [typealias SIMDMaskScalar](./double/simdmaskscalar.md)
- [Double.SIMD2Storage](./double/simd2storage.md)
  Storage for a vector of two floating-point values.
- [Double.SIMD4Storage](./double/simd4storage.md)
  Storage for a vector of four floating-point values.
- [Double.SIMD8Storage](./double/simd8storage.md)
  Storage for a vector of eight floating-point values.
- [Double.SIMD16Storage](./double/simd16storage.md)
  Storage for a vector of 16 floating-point values.
- [Double.SIMD32Storage](./double/simd32storage.md)
  Storage for a vector of 32 floating-point values.
- [Double.SIMD64Storage](./double/simd64storage.md)
  Storage for a vector of 64 floating-point values.
### Deprecated
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](./double/customplaygroundquicklook.md)
  A custom playground Quick Look for the `Double` instance.
- [init(NSNumber)](./double/init%28_%29-8kme5.md)
### Type Aliases
- [typealias Specification](./double/specification.md)
- [typealias UnwrappedType](./double/unwrappedtype.md)
- [typealias ValueType](./double/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](./double/defaultresolverspecification.md)
- [static var mlMultiArrayDataType: MLMultiArrayDataType](./double/mlmultiarraydatatype.md)
### Default Implementations
- [AdditiveArithmetic Implementations](./double/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](./double/atomicrepresentable-implementations.md)
- [BinaryFloatingPoint Implementations](./double/binaryfloatingpoint-implementations.md)
- [Comparable Implementations](./double/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](./double/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](./double/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](./double/customstringconvertible-implementations.md)
- [Decodable Implementations](./double/decodable-implementations.md)
- [Encodable Implementations](./double/encodable-implementations.md)
- [Equatable Implementations](./double/equatable-implementations.md)
- [ExpressibleByFloatLiteral Implementations](./double/expressiblebyfloatliteral-implementations.md)
- [ExpressibleByIntegerLiteral Implementations](./double/expressiblebyintegerliteral-implementations.md)
- [FloatingPoint Implementations](./double/floatingpoint-implementations.md)
- [Hashable Implementations](./double/hashable-implementations.md)
- [LosslessStringConvertible Implementations](./double/losslessstringconvertible-implementations.md)
- [Numeric Implementations](./double/numeric-implementations.md)
- [SIMDScalar Implementations](./double/simdscalar-implementations.md)
- [SignedNumeric Implementations](./double/signednumeric-implementations.md)
- [Strideable Implementations](./double/strideable-implementations.md)
- [TextOutputStreamable Implementations](./double/textoutputstreamable-implementations.md)

## Relationships

### Conforms To
- [AdditiveArithmetic](./additivearithmetic.md)
- [Animatable](../SwiftUI/animatable.md)
- [AnimatableData](../RealityKit/animatabledata.md)
- [AtomicRepresentable](../Synchronization/atomicrepresentable.md)
- [BinaryFloatingPoint](./binaryfloatingpoint.md)
- [BindableData](../RealityKit/bindabledata.md)
- [BitwiseCopyable](./bitwisecopyable.md)
- [CKRecordValueProtocol](../CloudKit/ckrecordvalueprotocol.md)
- [CVAttachmentValueRepresentable](../CoreVideo/cvattachmentvaluerepresentable.md)
- [CVarArg](./cvararg.md)
- [Comparable](./comparable.md)
- [ConvertibleFromBytes](./convertiblefrombytes.md)
- [ConvertibleFromGeneratedContent](../FoundationModels/convertiblefromgeneratedcontent.md)
- [ConvertibleToBytes](./convertibletobytes.md)
- [ConvertibleToGeneratedContent](../FoundationModels/convertibletogeneratedcontent.md)
- [Copyable](./copyable.md)
- [CustomDebugStringConvertible](./customdebugstringconvertible.md)
- [CustomReflectable](./customreflectable.md)
- [CustomStringConvertible](./customstringconvertible.md)
- [Decodable](./decodable.md)
- [Encodable](./encodable.md)
- [Equatable](./equatable.md)
- [Escapable](./escapable.md)
- [ExpressibleByFloatLiteral](./expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](./expressiblebyintegerliteral.md)
- [FloatingPoint](./floatingpoint.md)
- [Generable](../FoundationModels/generable.md)
- [Hashable](./hashable.md)
- [InstructionsRepresentable](../FoundationModels/instructionsrepresentable.md)
- [IntentValueConvertible](../AppIntents/intentvalueconvertible.md)
- [IntentValueExpressing](../AppIntents/intentvalueexpressing.md)
- [LosslessStringConvertible](./losslessstringconvertible.md)
- [MLDataValueConvertible](../CreateML/mldatavalueconvertible.md)
- [MLShapedArrayScalar](../CoreML/mlshapedarrayscalar.md)
- [Numeric](./numeric.md)
- [Plottable](../Charts/plottable.md)
- [PrimitivePlottableProtocol](../Charts/primitiveplottableprotocol.md)
- [PromptRepresentable](../FoundationModels/promptrepresentable.md)
- [RangeComparableProperty](../AppIntents/rangecomparableproperty.md)
- [SIMDScalar](./simdscalar.md)
- [Sendable](./sendable.md)
- [SendableMetatype](./sendablemetatype.md)
- [SignedNumeric](./signednumeric.md)
- [Strideable](./strideable.md)
- [TextOutputStreamable](./textoutputstreamable.md)
- [USDPrim.Attribute.Value](../USDKit/usdprim/attribute/value.md)
- [USDStage.Object.MetadataValue](../USDKit/usdstage/object/metadatavalue.md)
- [USDValueProtocol](../USDKit/usdvalueprotocol.md)
- [VectorArithmetic](../SwiftUI/vectorarithmetic.md)
- [vDSP_DiscreteFourierTransformable](../Accelerate/vdsp_discretefouriertransformable.md)
- [vDSP_FloatingPointBiquadFilterable](../Accelerate/vdsp_floatingpointbiquadfilterable.md)
- [vDSP_FloatingPointConvertable](../Accelerate/vdsp_floatingpointconvertable.md)
- [vDSP_FloatingPointDiscreteFourierTransformable](../Accelerate/vdsp_floatingpointdiscretefouriertransformable.md)
- [vDSP_FloatingPointGeneratable](../Accelerate/vdsp_floatingpointgeneratable.md)

## See Also

### Standard Library
- [struct Int](./int.md)
  A signed integer value type.
- [struct String](./string.md)
  A Unicode string value that is a collection of characters.
- [struct Array](./array.md)
  An ordered, random-access collection.
- [struct Dictionary](./dictionary.md)
  A collection whose elements are key-value pairs.
- [Swift Standard Library](./swift-standard-library.md)
  Solve complex problems and write high-performance, readable code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double)*