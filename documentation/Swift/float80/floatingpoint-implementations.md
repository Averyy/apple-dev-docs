# FloatingPoint Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Operators
- [static func * (Float80, Float80) -> Float80](./star%28_,_%29.md)
  Multiplies two values and produces their product, rounding to a representable value.
- [static func *= (inout Float80, Float80)](./stareq%28_,_%29.md)
  Multiplies two values and stores the result in the left-hand-side variable, rounding to a representable value.
- [static func + (Float80, Float80) -> Float80](./plus%28_,_%29.md)
  Adds two values and produces their sum, rounded to a representable value.
- [static func += (inout Float80, Float80)](./pluseq%28_,_%29.md)
  Adds two values and stores the result in the left-hand-side variable, rounded to a representable value.
- [static func - (Float80) -> Float80](./minus%28_%29.md)
  Calculates the additive inverse of a value.
- [static func - (Float80, Float80) -> Float80](./minus%28_,_%29.md)
  Subtracts one value from another and produces their difference, rounded to a representable value.
- [static func -= (inout Float80, Float80)](./minuseq%28_,_%29.md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, rounding to a representable value.
- [static func / (Float80, Float80) -> Float80](./op%28_,_%29.md)
  Returns the quotient of dividing the first value by the second, rounded to a representable value.
- [static func > (Self, Self) -> Bool](./op%28_,_%29-8otyc.md)
- [static func /= (inout Float80, Float80)](./opeq%28_,_%29.md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable, rounding to a representable value.
- [static func >= (Self, Self) -> Bool](./opeq%28_,_%29-2myj1.md)
- [static func <= (Self, Self) -> Bool](./opeq%28_,_%29-502lh.md)
### Initializers
- [init<Source>(Source)](./init%28_%29-33oy4.md)
  Creates a new value, rounded to the closest possible representation.
- [init(Int)](./init%28_%29-42n91.md)
  Creates a new value, rounded to the closest possible representation.
- [init?<Source>(exactly: Source)](./init%28exactly%29-2t92j.md)
  Creates a new value, if the given integer can be represented exactly.
- [init(sign: FloatingPointSign, exponent: Int, significand: Float80)](./init%28sign,exponent,significand%29.md)
  Creates a new value from the given sign, exponent, and significand.
- [init(signOf: Float80, magnitudeOf: Float80)](./init%28signof,magnitudeof%29.md)
  Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init(signOf: Self, magnitudeOf: Self)](./init%28signof,magnitudeof%29-t3cu.md)
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
- [var nextUp: Float80](./nextup.md)
  The least representable value that compares greater than this value.
- [var sign: FloatingPointSign](./sign.md)
  The sign of the floating-point value.
- [var significand: Float80](./significand.md)
  The significand of the floating-point value.
- [var ulp: Float80](./ulp.md)
  The unit in the last place of this value.
### Instance Methods
- [func addProduct(Float80, Float80)](./addproduct%28_,_%29.md)
  Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [func addingProduct(Self, Self) -> Self](./addingproduct%28_,_%29.md)
  Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [func formRemainder(dividingBy: Float80)](./formremainder%28dividingby%29.md)
  Replaces this value with the remainder of itself divided by the given value.
- [func formSquareRoot()](./formsquareroot%28%29.md)
  Replaces this value with its square root, rounded to a representable value.
- [func formTruncatingRemainder(dividingBy: Float80)](./formtruncatingremainder%28dividingby%29.md)
  Replaces this value with the remainder of itself divided by the given value using truncating division.
- [func isEqual(to: Float80) -> Bool](./isequal%28to%29.md)
  Returns a Boolean value indicating whether this instance is equal to the given value.
- [func isLess(than: Float80) -> Bool](./isless%28than%29.md)
  Returns a Boolean value indicating whether this instance is less than the given value.
- [func isLessThanOrEqualTo(Float80) -> Bool](./islessthanorequalto%28_%29.md)
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
- [static var greatestFiniteMagnitude: Float80](./greatestfinitemagnitude.md)
  The greatest finite number representable by this type.
- [static var infinity: Float80](./infinity.md)
  Positive infinity.
- [static var leastNonzeroMagnitude: Float80](./leastnonzeromagnitude.md)
  The least positive number.
- [static var leastNormalMagnitude: Float80](./leastnormalmagnitude.md)
  The least positive normal number.
- [static var nan: Float80](./nan.md)
  A quiet NaN (“not a number”).
- [static var pi: Float80](./pi.md)
  The mathematical constant pi (π), approximately equal to 3.14159.
- [static var radix: Int](./radix.md)
  The radix, or base of exponentiation, for a floating-point type.
- [static var signalingNaN: Float80](./signalingnan.md)
  A signaling NaN (“not a number”).
- [static var ulpOfOne: Float80](./ulpofone.md)
  The unit in the last place of 1.0.
- [static var ulpOfOne: Self](./ulpofone-817da.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/floatingpoint-implementations)*