# FloatingPoint Implementations

**Framework**: Swift

## Topics

### Operators
- [static func * (Float16, Float16) -> Float16](float16/*(_:_:).md)
  Multiplies two values and produces their product, rounding to a representable value.
- [static func *= (inout Float16, Float16)](float16/*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable, rounding to a representable value.
- [static func + (Float16, Float16) -> Float16](float16/+(_:_:).md)
  Adds two values and produces their sum, rounded to a representable value.
- [static func += (inout Float16, Float16)](float16/+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable, rounded to a representable value.
- [static func - (Float16) -> Float16](float16/-(_:).md)
  Calculates the additive inverse of a value.
- [static func - (Float16, Float16) -> Float16](float16/-(_:_:).md)
  Subtracts one value from another and produces their difference, rounded to a representable value.
- [static func -= (inout Float16, Float16)](float16/-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, rounding to a representable value.
- [static func / (Float16, Float16) -> Float16](float16/_(_:_:).md)
  Returns the quotient of dividing the first value by the second, rounded to a representable value.
- [static func > (Self, Self) -> Bool](float16/_(_:_:)-9d93b.md)
- [static func /= (inout Float16, Float16)](float16/_=(_:_:).md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable, rounding to a representable value.
- [static func >= (Self, Self) -> Bool](float16/_=(_:_:)-1s8n2.md)
- [static func <= (Self, Self) -> Bool](float16/_=(_:_:)-4bq0a.md)
### Initializers
- [init(Int)](float16/init(_:)-4iaoz.md)
  Creates a new value, rounded to the closest possible representation.
- [init<Source>(Source)](float16/init(_:)-67cee.md)
  Creates a new value, rounded to the closest possible representation.
- [init?<Source>(exactly: Source)](float16/init(exactly:)-2qxl0.md)
  Creates a new value, if the given integer can be represented exactly.
- [init(sign: FloatingPointSign, exponent: Int, significand: Float16)](float16/init(sign:exponent:significand:).md)
  Creates a new value from the given sign, exponent, and significand.
- [init(signOf: Float16, magnitudeOf: Float16)](float16/init(signof:magnitudeof:).md)
  Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init(signOf: Self, magnitudeOf: Self)](float16/init(signof:magnitudeof:)-1oylh.md)
  Creates a new floating-point value using the sign of one value and the magnitude of another.
### Instance Properties
- [var exponent: Int](float16/exponent-swift.property.md)
  The exponent of the floating-point value.
- [var floatingPointClass: FloatingPointClassification](float16/floatingpointclass.md)
  The classification of this value.
- [var isCanonical: Bool](float16/iscanonical.md)
  A Boolean value indicating whether the instance’s representation is in its canonical form.
- [var isFinite: Bool](float16/isfinite.md)
  A Boolean value indicating whether this instance is finite.
- [var isInfinite: Bool](float16/isinfinite.md)
  A Boolean value indicating whether the instance is infinite.
- [var isNaN: Bool](float16/isnan.md)
  A Boolean value indicating whether the instance is NaN (“not a number”).
- [var isNormal: Bool](float16/isnormal.md)
  A Boolean value indicating whether this instance is normal.
- [var isSignalingNaN: Bool](float16/issignalingnan.md)
  A Boolean value indicating whether the instance is a signaling NaN.
- [var isSubnormal: Bool](float16/issubnormal.md)
  A Boolean value indicating whether the instance is subnormal.
- [var isZero: Bool](float16/iszero.md)
  A Boolean value indicating whether the instance is equal to zero.
- [var nextDown: Self](float16/nextdown.md)
  The greatest representable value that compares less than this value.
- [var nextUp: Float16](float16/nextup.md)
  The least representable value that compares greater than this value.
- [var sign: FloatingPointSign](float16/sign.md)
  The sign of the floating-point value.
- [var significand: Float16](float16/significand.md)
  The significand of the floating-point value.
- [var ulp: Float16](float16/ulp.md)
  The unit in the last place of this value.
### Instance Methods
- [func addProduct(Float16, Float16)](float16/addproduct(_:_:).md)
  Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [func addingProduct(Self, Self) -> Self](float16/addingproduct(_:_:).md)
  Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [func formRemainder(dividingBy: Float16)](float16/formremainder(dividingby:).md)
  Replaces this value with the remainder of itself divided by the given value.
- [func formSquareRoot()](float16/formsquareroot.md)
  Replaces this value with its square root, rounded to a representable value.
- [func formTruncatingRemainder(dividingBy: Float16)](float16/formtruncatingremainder(dividingby:).md)
  Replaces this value with the remainder of itself divided by the given value using truncating division.
- [func isEqual(to: Float16) -> Bool](float16/isequal(to:).md)
  Returns a Boolean value indicating whether this instance is equal to the given value.
- [func isLess(than: Float16) -> Bool](float16/isless(than:).md)
  Returns a Boolean value indicating whether this instance is less than the given value.
- [func isLessThanOrEqualTo(Float16) -> Bool](float16/islessthanorequalto(_:).md)
  Returns a Boolean value indicating whether this instance is less than or equal to the given value.
- [func isTotallyOrdered(belowOrEqualTo: Self) -> Bool](float16/istotallyordered(beloworequalto:).md)
  Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.
- [func negate()](float16/negate.md)
  Replaces this value with its additive inverse.
- [func remainder(dividingBy: Self) -> Self](float16/remainder(dividingby:).md)
  Returns the remainder of this value divided by the given value.
- [func round()](float16/round.md)
- [func round(FloatingPointRoundingRule)](float16/round(_:).md)
  Rounds the value to an integral value using the specified rounding rule.
- [func rounded() -> Self](float16/rounded.md)
- [func rounded(FloatingPointRoundingRule) -> Self](float16/rounded(_:).md)
  Returns this value rounded to an integral value using the specified rounding rule.
- [func squareRoot() -> Self](float16/squareroot.md)
  Returns the square root of the value, rounded to a representable value.
- [func truncatingRemainder(dividingBy: Self) -> Self](float16/truncatingremainder(dividingby:).md)
  Returns the remainder of this value divided by the given value using truncating division.
### Type Aliases
- [typealias Exponent](float16/exponent-swift.typealias.md)
  A type that can represent any written exponent.
### Type Properties
- [static var greatestFiniteMagnitude: Float16](float16/greatestfinitemagnitude.md)
  The greatest finite number representable by this type.
- [static var infinity: Float16](float16/infinity.md)
  Positive infinity.
- [static var leastNonzeroMagnitude: Float16](float16/leastnonzeromagnitude.md)
  The least positive number.
- [static var leastNormalMagnitude: Float16](float16/leastnormalmagnitude.md)
  The least positive normal number.
- [static var nan: Float16](float16/nan.md)
  A quiet NaN (“not a number”).
- [static var pi: Float16](float16/pi.md)
  The mathematical constant pi (π), approximately equal to 3.14159.
- [static var radix: Int](float16/radix.md)
  The radix, or base of exponentiation, for a floating-point type.
- [static var signalingNaN: Float16](float16/signalingnan.md)
  A signaling NaN (“not a number”).
- [static var ulpOfOne: Float16](float16/ulpofone.md)
  The unit in the last place of 1.0.
- [static var ulpOfOne: Self](float16/ulpofone-8wr95.md)
  The unit in the last place of 1.0.
### Type Methods
- [static func maximum(Self, Self) -> Self](float16/maximum(_:_:).md)
  Returns the greater of the two given values.
- [static func maximumMagnitude(Self, Self) -> Self](float16/maximummagnitude(_:_:).md)
  Returns the value with greater magnitude.
- [static func minimum(Self, Self) -> Self](float16/minimum(_:_:).md)
  Returns the lesser of the two given values.
- [static func minimumMagnitude(Self, Self) -> Self](float16/minimummagnitude(_:_:).md)
  Returns the value with lesser magnitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float16/floatingpoint-implementations)*