# FloatingPoint Implementations

**Framework**: Swift

## Topics

### Operators
- [static func * (Float, Float) -> Float](float/*(_:_:).md)
  Multiplies two values and produces their product, rounding to a representable value.
- [static func *= (inout Float, Float)](float/*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable, rounding to a representable value.
- [static func + (Float, Float) -> Float](float/+(_:_:).md)
  Adds two values and produces their sum, rounded to a representable value.
- [static func += (inout Float, Float)](float/+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable, rounded to a representable value.
- [static func - (Float) -> Float](float/-(_:).md)
  Calculates the additive inverse of a value.
- [static func - (Float, Float) -> Float](float/-(_:_:).md)
  Subtracts one value from another and produces their difference, rounded to a representable value.
- [static func -= (inout Float, Float)](float/-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, rounding to a representable value.
- [static func / (Float, Float) -> Float](float/_(_:_:).md)
  Returns the quotient of dividing the first value by the second, rounded to a representable value.
- [static func > (Self, Self) -> Bool](float/_(_:_:)-552jr.md)
- [static func /= (inout Float, Float)](float/_=(_:_:).md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable, rounding to a representable value.
- [static func <= (Self, Self) -> Bool](float/_=(_:_:)-5yoz5.md)
- [static func >= (Self, Self) -> Bool](float/_=(_:_:)-9o6ha.md)
### Initializers
- [init(Int)](float/init(_:)-6cvkq.md)
  Creates a new value, rounded to the closest possible representation.
- [init<Source>(Source)](float/init(_:)-7e965.md)
  Creates a new value, rounded to the closest possible representation.
- [init?<Source>(exactly: Source)](float/init(exactly:)-uz92.md)
  Creates a new value, if the given integer can be represented exactly.
- [init(sign: FloatingPointSign, exponent: Int, significand: Float)](float/init(sign:exponent:significand:).md)
  Creates a new value from the given sign, exponent, and significand.
- [init(signOf: Float, magnitudeOf: Float)](float/init(signof:magnitudeof:).md)
  Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init(signOf: Self, magnitudeOf: Self)](float/init(signof:magnitudeof:)-6i9uw.md)
  Creates a new floating-point value using the sign of one value and the magnitude of another.
### Instance Properties
- [var exponent: Int](float/exponent-swift.property.md)
  The exponent of the floating-point value.
- [var floatingPointClass: FloatingPointClassification](float/floatingpointclass.md)
  The classification of this value.
- [var isCanonical: Bool](float/iscanonical.md)
  A Boolean value indicating whether the instance’s representation is in its canonical form.
- [var isFinite: Bool](float/isfinite.md)
  A Boolean value indicating whether this instance is finite.
- [var isInfinite: Bool](float/isinfinite.md)
  A Boolean value indicating whether the instance is infinite.
- [var isNaN: Bool](float/isnan.md)
  A Boolean value indicating whether the instance is NaN (“not a number”).
- [var isNormal: Bool](float/isnormal.md)
  A Boolean value indicating whether this instance is normal.
- [var isSignalingNaN: Bool](float/issignalingnan.md)
  A Boolean value indicating whether the instance is a signaling NaN.
- [var isSubnormal: Bool](float/issubnormal.md)
  A Boolean value indicating whether the instance is subnormal.
- [var isZero: Bool](float/iszero.md)
  A Boolean value indicating whether the instance is equal to zero.
- [var nextDown: Self](float/nextdown.md)
  The greatest representable value that compares less than this value.
- [var nextUp: Float](float/nextup.md)
  The least representable value that compares greater than this value.
- [var sign: FloatingPointSign](float/sign.md)
  The sign of the floating-point value.
- [var significand: Float](float/significand.md)
  The significand of the floating-point value.
- [var ulp: Float](float/ulp.md)
  The unit in the last place of this value.
### Instance Methods
- [func addProduct(Float, Float)](float/addproduct(_:_:).md)
  Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [func addingProduct(Self, Self) -> Self](float/addingproduct(_:_:).md)
  Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [func formRemainder(dividingBy: Float)](float/formremainder(dividingby:).md)
  Replaces this value with the remainder of itself divided by the given value.
- [func formSquareRoot()](float/formsquareroot.md)
  Replaces this value with its square root, rounded to a representable value.
- [func formTruncatingRemainder(dividingBy: Float)](float/formtruncatingremainder(dividingby:).md)
  Replaces this value with the remainder of itself divided by the given value using truncating division.
- [func isEqual(to: Float) -> Bool](float/isequal(to:).md)
  Returns a Boolean value indicating whether this instance is equal to the given value.
- [func isLess(than: Float) -> Bool](float/isless(than:).md)
  Returns a Boolean value indicating whether this instance is less than the given value.
- [func isLessThanOrEqualTo(Float) -> Bool](float/islessthanorequalto(_:).md)
  Returns a Boolean value indicating whether this instance is less than or equal to the given value.
- [func isTotallyOrdered(belowOrEqualTo: Self) -> Bool](float/istotallyordered(beloworequalto:).md)
  Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.
- [func negate()](float/negate.md)
  Replaces this value with its additive inverse.
- [func remainder(dividingBy: Self) -> Self](float/remainder(dividingby:).md)
  Returns the remainder of this value divided by the given value.
- [func round()](float/round.md)
- [func round(FloatingPointRoundingRule)](float/round(_:).md)
  Rounds the value to an integral value using the specified rounding rule.
- [func rounded() -> Self](float/rounded.md)
- [func rounded(FloatingPointRoundingRule) -> Self](float/rounded(_:).md)
  Returns this value rounded to an integral value using the specified rounding rule.
- [func squareRoot() -> Self](float/squareroot.md)
  Returns the square root of the value, rounded to a representable value.
- [func truncatingRemainder(dividingBy: Self) -> Self](float/truncatingremainder(dividingby:).md)
  Returns the remainder of this value divided by the given value using truncating division.
### Type Aliases
- [typealias Exponent](float/exponent-swift.typealias.md)
  A type that can represent any written exponent.
### Type Properties
- [static var greatestFiniteMagnitude: Float](float/greatestfinitemagnitude.md)
  The greatest finite number representable by this type.
- [static var infinity: Float](float/infinity.md)
  Positive infinity.
- [static var leastNonzeroMagnitude: Float](float/leastnonzeromagnitude.md)
  The least positive number.
- [static var leastNormalMagnitude: Float](float/leastnormalmagnitude.md)
  The least positive normal number.
- [static var nan: Float](float/nan.md)
  A quiet NaN (“not a number”).
- [static var pi: Float](float/pi.md)
  The mathematical constant pi (π), approximately equal to 3.14159.
- [static var radix: Int](float/radix.md)
  The radix, or base of exponentiation, for a floating-point type.
- [static var signalingNaN: Float](float/signalingnan.md)
  A signaling NaN (“not a number”).
- [static var ulpOfOne: Float](float/ulpofone.md)
  The unit in the last place of 1.0.
- [static var ulpOfOne: Self](float/ulpofone-1s81z.md)
  The unit in the last place of 1.0.
### Type Methods
- [static func maximum(Self, Self) -> Self](float/maximum(_:_:).md)
  Returns the greater of the two given values.
- [static func maximumMagnitude(Self, Self) -> Self](float/maximummagnitude(_:_:).md)
  Returns the value with greater magnitude.
- [static func minimum(Self, Self) -> Self](float/minimum(_:_:).md)
  Returns the lesser of the two given values.
- [static func minimumMagnitude(Self, Self) -> Self](float/minimummagnitude(_:_:).md)
  Returns the value with lesser magnitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/floatingpoint-implementations)*