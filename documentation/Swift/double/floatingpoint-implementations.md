# FloatingPoint Implementations

**Framework**: Swift

## Topics

### Operators
- [static func * (Double, Double) -> Double](double/*(_:_:).md)
  Multiplies two values and produces their product, rounding to a representable value.
- [static func *= (inout Double, Double)](double/*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable, rounding to a representable value.
- [static func + (Double, Double) -> Double](double/+(_:_:).md)
  Adds two values and produces their sum, rounded to a representable value.
- [static func += (inout Double, Double)](double/+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable, rounded to a representable value.
- [static func - (Double) -> Double](double/-(_:).md)
  Calculates the additive inverse of a value.
- [static func - (Double, Double) -> Double](double/-(_:_:).md)
  Subtracts one value from another and produces their difference, rounded to a representable value.
- [static func -= (inout Double, Double)](double/-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, rounding to a representable value.
- [static func / (Double, Double) -> Double](double/_(_:_:).md)
  Returns the quotient of dividing the first value by the second, rounded to a representable value.
- [static func > (Self, Self) -> Bool](double/_(_:_:)-552jp.md)
- [static func /= (inout Double, Double)](double/_=(_:_:).md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable, rounding to a representable value.
- [static func <= (Self, Self) -> Bool](double/_=(_:_:)-5yoz7.md)
- [static func >= (Self, Self) -> Bool](double/_=(_:_:)-9o6h8.md)
### Initializers
- [init<Source>(Source)](double/init(_:)-5blrp.md)
  Creates a new value, rounded to the closest possible representation.
- [init(Int)](double/init(_:)-84ohu.md)
  Creates a new value, rounded to the closest possible representation.
- [init?<Source>(exactly: Source)](double/init(exactly:)-2uexo.md)
  Creates a new value, if the given integer can be represented exactly.
- [init(sign: FloatingPointSign, exponent: Int, significand: Double)](double/init(sign:exponent:significand:).md)
  Creates a new value from the given sign, exponent, and significand.
- [init(signOf: Double, magnitudeOf: Double)](double/init(signof:magnitudeof:).md)
  Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init(signOf: Self, magnitudeOf: Self)](double/init(signof:magnitudeof:)-6i9uy.md)
  Creates a new floating-point value using the sign of one value and the magnitude of another.
### Instance Properties
- [var exponent: Int](double/exponent-swift.property.md)
  The exponent of the floating-point value.
- [var floatingPointClass: FloatingPointClassification](double/floatingpointclass.md)
  The classification of this value.
- [var isCanonical: Bool](double/iscanonical.md)
  A Boolean value indicating whether the instance’s representation is in its canonical form.
- [var isFinite: Bool](double/isfinite.md)
  A Boolean value indicating whether this instance is finite.
- [var isInfinite: Bool](double/isinfinite.md)
  A Boolean value indicating whether the instance is infinite.
- [var isNaN: Bool](double/isnan.md)
  A Boolean value indicating whether the instance is NaN (“not a number”).
- [var isNormal: Bool](double/isnormal.md)
  A Boolean value indicating whether this instance is normal.
- [var isSignalingNaN: Bool](double/issignalingnan.md)
  A Boolean value indicating whether the instance is a signaling NaN.
- [var isSubnormal: Bool](double/issubnormal.md)
  A Boolean value indicating whether the instance is subnormal.
- [var isZero: Bool](double/iszero.md)
  A Boolean value indicating whether the instance is equal to zero.
- [var nextDown: Self](double/nextdown.md)
  The greatest representable value that compares less than this value.
- [var nextUp: Double](double/nextup.md)
  The least representable value that compares greater than this value.
- [var sign: FloatingPointSign](double/sign.md)
  The sign of the floating-point value.
- [var significand: Double](double/significand.md)
  The significand of the floating-point value.
- [var ulp: Double](double/ulp.md)
  The unit in the last place of this value.
### Instance Methods
- [func addProduct(Double, Double)](double/addproduct(_:_:).md)
  Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [func addingProduct(Self, Self) -> Self](double/addingproduct(_:_:).md)
  Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [func formRemainder(dividingBy: Double)](double/formremainder(dividingby:).md)
  Replaces this value with the remainder of itself divided by the given value.
- [func formSquareRoot()](double/formsquareroot.md)
  Replaces this value with its square root, rounded to a representable value.
- [func formTruncatingRemainder(dividingBy: Double)](double/formtruncatingremainder(dividingby:).md)
  Replaces this value with the remainder of itself divided by the given value using truncating division.
- [func isEqual(to: Double) -> Bool](double/isequal(to:).md)
  Returns a Boolean value indicating whether this instance is equal to the given value.
- [func isLess(than: Double) -> Bool](double/isless(than:).md)
  Returns a Boolean value indicating whether this instance is less than the given value.
- [func isLessThanOrEqualTo(Double) -> Bool](double/islessthanorequalto(_:).md)
  Returns a Boolean value indicating whether this instance is less than or equal to the given value.
- [func isTotallyOrdered(belowOrEqualTo: Self) -> Bool](double/istotallyordered(beloworequalto:).md)
  Returns a Boolean value indicating whether this instance should precede or tie positions with the given value in an ascending sort.
- [func negate()](double/negate.md)
  Replaces this value with its additive inverse.
- [func remainder(dividingBy: Self) -> Self](double/remainder(dividingby:).md)
  Returns the remainder of this value divided by the given value.
- [func round()](double/round.md)
- [func round(FloatingPointRoundingRule)](double/round(_:).md)
  Rounds the value to an integral value using the specified rounding rule.
- [func rounded() -> Self](double/rounded.md)
- [func rounded(FloatingPointRoundingRule) -> Self](double/rounded(_:).md)
  Returns this value rounded to an integral value using the specified rounding rule.
- [func squareRoot() -> Self](double/squareroot.md)
  Returns the square root of the value, rounded to a representable value.
- [func truncatingRemainder(dividingBy: Self) -> Self](double/truncatingremainder(dividingby:).md)
  Returns the remainder of this value divided by the given value using truncating division.
### Type Aliases
- [typealias Exponent](double/exponent-swift.typealias.md)
  A type that can represent any written exponent.
### Type Properties
- [static var greatestFiniteMagnitude: Double](double/greatestfinitemagnitude.md)
  The greatest finite number representable by this type.
- [static var infinity: Double](double/infinity.md)
  Positive infinity.
- [static var leastNonzeroMagnitude: Double](double/leastnonzeromagnitude.md)
  The least positive number.
- [static var leastNormalMagnitude: Double](double/leastnormalmagnitude.md)
  The least positive normal number.
- [static var nan: Double](double/nan.md)
  A quiet NaN (“not a number”).
- [static var pi: Double](double/pi.md)
  The mathematical constant pi (π), approximately equal to 3.14159.
- [static var radix: Int](double/radix.md)
  The radix, or base of exponentiation, for a floating-point type.
- [static var signalingNaN: Double](double/signalingnan.md)
  A signaling NaN (“not a number”).
- [static var ulpOfOne: Double](double/ulpofone.md)
  The unit in the last place of 1.0.
- [static var ulpOfOne: Self](double/ulpofone-1s81x.md)
  The unit in the last place of 1.0.
### Type Methods
- [static func maximum(Self, Self) -> Self](double/maximum(_:_:).md)
  Returns the greater of the two given values.
- [static func maximumMagnitude(Self, Self) -> Self](double/maximummagnitude(_:_:).md)
  Returns the value with greater magnitude.
- [static func minimum(Self, Self) -> Self](double/minimum(_:_:).md)
  Returns the lesser of the two given values.
- [static func minimumMagnitude(Self, Self) -> Self](double/minimummagnitude(_:_:).md)
  Returns the value with lesser magnitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/floatingpoint-implementations)*