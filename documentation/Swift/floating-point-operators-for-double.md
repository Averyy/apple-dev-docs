# Floating-Point Operators for Double

**Framework**: Swift

Perform arithmetic and bitwise operations or compare values.

## Topics

### Arithmetic
- [static func + (Double, Double) -> Double](double/+(_:_:).md)
  Adds two values and produces their sum, rounded to a representable value.
- [static func - (Double, Double) -> Double](double/-(_:_:).md)
  Subtracts one value from another and produces their difference, rounded to a representable value.
- [static func * (Double, Double) -> Double](double/*(_:_:).md)
  Multiplies two values and produces their product, rounding to a representable value.
- [static func / (Double, Double) -> Double](double/_(_:_:).md)
  Returns the quotient of dividing the first value by the second, rounded to a representable value.
### Arithmetic with Assignment
- [static func += (inout Double, Double)](double/+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable, rounded to a representable value.
- [static func -= (inout Double, Double)](double/-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, rounding to a representable value.
- [static func *= (inout Double, Double)](double/*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable, rounding to a representable value.
- [static func /= (inout Double, Double)](double/_=(_:_:).md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable, rounding to a representable value.
### Comparison
- [static func == (Self, Self) -> Bool](double/==(_:_:)-12hdv.md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](double/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Negation
- [static func - (Double) -> Double](double/-(_:).md)
  Calculates the additive inverse of a value.
- [static func + (Self) -> Self](double/+(_:).md)
  Returns the given number unchanged.
### Range Expressions
- [static func ... (Self) -> PartialRangeThrough<Self>](double/'...(_:)-4mm67.md)
  Returns a partial range up to, and including, its upper bound.
- [static func ... (Self) -> PartialRangeFrom<Self>](double/'...(_:)-6ct5v.md)
  Returns a partial range extending upward from a lower bound.

## See Also

- [func addingProduct(Self, Self) -> Self](double/addingproduct(_:_:).md)
  Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [func addProduct(Double, Double)](double/addproduct(_:_:).md)
  Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [func squareRoot() -> Self](double/squareroot.md)
  Returns the square root of the value, rounded to a representable value.
- [func formSquareRoot()](double/formsquareroot.md)
  Replaces this value with its square root, rounded to a representable value.
- [func remainder(dividingBy: Self) -> Self](double/remainder(dividingby:).md)
  Returns the remainder of this value divided by the given value.
- [func formRemainder(dividingBy: Double)](double/formremainder(dividingby:).md)
  Replaces this value with the remainder of itself divided by the given value.
- [func truncatingRemainder(dividingBy: Self) -> Self](double/truncatingremainder(dividingby:).md)
  Returns the remainder of this value divided by the given value using truncating division.
- [func formTruncatingRemainder(dividingBy: Double)](double/formtruncatingremainder(dividingby:).md)
  Replaces this value with the remainder of itself divided by the given value using truncating division.
- [func negate()](double/negate.md)
  Replaces this value with its additive inverse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/floating-point-operators-for-double)*