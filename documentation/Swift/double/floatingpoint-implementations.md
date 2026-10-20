# FloatingPoint Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Operators
- [static func * (Double, Double) -> Double](./star%28_,_%29.md)
  Multiplies two values and produces their product, rounding to a representable value.
- [static func *= (inout Double, Double)](./stareq%28_,_%29.md)
  Multiplies two values and stores the result in the left-hand-side variable, rounding to a representable value.
- [static func + (Double, Double) -> Double](./plus%28_,_%29.md)
  Adds two values and produces their sum, rounded to a representable value.
- [static func += (inout Double, Double)](./pluseq%28_,_%29.md)
  Adds two values and stores the result in the left-hand-side variable, rounded to a representable value.
- [static func - (Double) -> Double](./minus%28_%29.md)
  Calculates the additive inverse of a value.
- [static func - (Double, Double) -> Double](./minus%28_,_%29.md)
  Subtracts one value from another and produces their difference, rounded to a representable value.
- [static func -= (inout Double, Double)](./minuseq%28_,_%29.md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, rounding to a representable value.
- [static func / (Double, Double) -> Double](./op%28_,_%29.md)
  Returns the quotient of dividing the first value by the second, rounded to a representable value.
- [static func > (Self, Self) -> Bool](./op%28_,_%29-552jp.md)
- [static func /= (inout Double, Double)](./opeq%28_,_%29.md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable, rounding to a representable value.
- [static func <= (Self, Self) -> Bool](./opeq%28_,_%29-5yoz7.md)
- [static func >= (Self, Self) -> Bool](./opeq%28_,_%29-9o6h8.md)
### Initializers
- [init<Source>(Source)](./init%28_%29-5blrp.md)
  Creates a new value, rounded to the closest possible representation.
- [init(Int)](./init%28_%29-84ohu.md)
  Creates a new value, rounded to the closest possible representation.
- [init?<Source>(exactly: Source)](./init%28exactly%29-2uexo.md)
  Creates a new value, if the given integer can be represented exactly.
- [init(sign: FloatingPointSign, exponent: Int, significand: Double)](./init%28sign,exponent,significand%29.md)
  Creates a new value from the given sign, exponent, and significand.
- [init(signOf: Double, magnitudeOf: Double)](./init%28signof,magnitudeof%29.md)
  Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init(signOf: Self, magnitudeOf: Self)](./init%28signof,magnitudeof%29-6i9uy.md)
  Creates a new floating-point value using the sign of one value and the magnitude of another.
### Instance Properties
- [var exponent: Int](./exponent-swift.property.md)
  The exponent of the floating-point value.
- [var floatingPointClass: FloatingPointClassification](./floatingpointclass.md)
  The classification of this value.
- [var isCanonical: Bool](./iscanonical.md)
  A Boolean value indicating whether the instance’s representation is in its canonical form.
- [var isFinite: Bool](./isfinite.md)
  A Boolean value indicating whether this instance is finite.
- [var isInfinite: Bool](./isinfinite.md)
  A Boolean value indicating whether the instance is infinite.
- [var isNaN: Bool](./isnan.md)
  A Boolean value indicating whether the instance is NaN (“not a number”).
- [var isNormal: Bool](./isnormal.md)
  A Boolean value indicating whether this instance is normal.
- [var isSignalingNaN: Bool](./issignalingnan.md)
  A Boolean value indicating whether the instance is a signaling NaN.
- [var isSubnormal: Bool](./issubnormal.md)
  A Boolean value indicating whether the instance is subnormal.
- [var isZero: Bool](./iszero.md)
  A Boolean value indicating whether the instance is equal to zero.
- [var nextDown: Self](./nextdown.md)
  The greatest representable value that compares less than this value.
- [var nextUp: Double](./nextup.md)
  The least representable value that compares greater than this value.
- [var sign: FloatingPointSign](./sign.md)
  The sign of the floating-point value.
- [var significand: Double](./significand.md)
  The significand of the floating-point value.
- [var ulp: Double](./ulp.md)
  The unit in the last place of this value.
### Instance Methods
- [func addProduct(Double, Double)](./addproduct%28_,_%29.md)
  Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [func addingProduct(Self, Self) -> Self](./addingproduct%28_,_%29.md)
  Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [func formRemainder(dividingBy: Double)](./formremainder%28dividingby%29.md)
  Replaces this value with the remainder of itself divided by the given value.
- [func formSquareRoot()](./formsquareroot%28%29.md)
  Replaces this value with its square root, rounded to a representable value.
- [func formTruncatingRemainder(dividingBy: Double)](./formtruncatingremainder%28dividingby%29.md)
  Replaces this value with the remainder of itself divided by the given value using truncating division.
- [func isEqual(to: Double) -> Bool](./isequal%28to%29.md)
  Returns a Boolean value indicating whether this instance is equal to the given value.
- [func isLess(than: Double) -> Bool](./isless%28than%29.md)
  Returns a Boolean value indicating whether this instance is less than the given value.
- [func isLessThanOrEqualTo(Double) -> Bool](./islessthanorequalto%28_%29.md)
  Returns a Boolean value indicating whether this instance is less than or equal to the given value.
- [func isTotallyOrdered(belowOrEqualTo: Self) -> Bool](./istotallyordered%28beloworequalto%29.md)
  Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.
- [func negate()](./negate%28%29.md)
  Replaces this value with its additive inverse.
- [func remainder(dividingBy: Self) -> Self](./remainder%28dividingby%29.md)
  Returns the remainder of this value divided by the given value.
- [func round()](./round%28%29.md)
- [func round(FloatingPointRoundingRule)](./round%28_%29.md)
  Rounds the value to an integral value using the specified rounding rule.
- [func rounded() -> Self](./rounded%28%29.md)
- [func rounded(FloatingPointRoundingRule) -> Self](./rounded%28_%29.md)
  Returns this value rounded to an integral value using the specified rounding rule.
- [func squareRoot() -> Self](./squareroot%28%29.md)
  Returns the square root of the value, rounded to a representable value.
- [func truncatingRemainder(dividingBy: Self) -> Self](./truncatingremainder%28dividingby%29.md)
  Returns the remainder of this value divided by the given value using truncating division.
### Type Aliases
- [typealias Exponent](./exponent-swift.typealias.md)
  A type that can represent any written exponent.
### Type Properties
- [static var greatestFiniteMagnitude: Double](./greatestfinitemagnitude.md)
  The greatest finite number representable by this type.
- [static var infinity: Double](./infinity.md)
  Positive infinity.
- [static var leastNonzeroMagnitude: Double](./leastnonzeromagnitude.md)
  The least positive number.
- [static var leastNormalMagnitude: Double](./leastnormalmagnitude.md)
  The least positive normal number.
- [static var nan: Double](./nan.md)
  A quiet NaN (“not a number”).
- [static var pi: Double](./pi.md)
  The mathematical constant pi (π), approximately equal to 3.14159.
- [static var radix: Int](./radix.md)
  The radix, or base of exponentiation, for a floating-point type.
- [static var signalingNaN: Double](./signalingnan.md)
  A signaling NaN (“not a number”).
- [static var ulpOfOne: Double](./ulpofone.md)
  The unit in the last place of 1.0.
- [static var ulpOfOne: Self](./ulpofone-1s81x.md)
  The unit in the last place of 1.0.
### Type Methods
- [static func maximum(Self, Self) -> Self](./maximum%28_,_%29.md)
  Returns the greater of the two given values.
- [static func maximumMagnitude(Self, Self) -> Self](./maximummagnitude%28_,_%29.md)
  Returns the value with greater magnitude.
- [static func minimum(Self, Self) -> Self](./minimum%28_,_%29.md)
  Returns the lesser of the two given values.
- [static func minimumMagnitude(Self, Self) -> Self](./minimummagnitude%28_,_%29.md)
  Returns the value with lesser magnitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/floatingpoint-implementations)*