# Floating-Point Operators for Double

**Framework**: Swift  
**Role**: API Collection

Perform arithmetic and bitwise operations or compare values.

## Topics

### Arithmetic
- [static func + (Double, Double) -> Double](./double/plus%28_,_%29.md)
  Adds two values and produces their sum, rounded to a representable value.
- [static func - (Double, Double) -> Double](./double/minus%28_,_%29.md)
  Subtracts one value from another and produces their difference, rounded to a representable value.
- [static func * (Double, Double) -> Double](./double/star%28_,_%29.md)
  Multiplies two values and produces their product, rounding to a representable value.
- [static func / (Double, Double) -> Double](./double/op%28_,_%29.md)
  Returns the quotient of dividing the first value by the second, rounded to a representable value.
### Arithmetic with Assignment
- [static func += (inout Double, Double)](./double/pluseq%28_,_%29.md)
  Adds two values and stores the result in the left-hand-side variable, rounded to a representable value.
- [static func -= (inout Double, Double)](./double/minuseq%28_,_%29.md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, rounding to a representable value.
- [static func *= (inout Double, Double)](./double/stareq%28_,_%29.md)
  Multiplies two values and stores the result in the left-hand-side variable, rounding to a representable value.
- [static func /= (inout Double, Double)](./double/opeq%28_,_%29.md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable, rounding to a representable value.
### Comparison
- [static func == (Self, Self) -> Bool](./double/eqeq%28_,_%29-12hdv.md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (borrowing Self, borrowing Self) -> Bool](./double/noteq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are not equal.
### Negation
- [static func - (Double) -> Double](./double/minus%28_%29.md)
  Calculates the additive inverse of a value.
- [static func + (Self) -> Self](./double/plus%28_%29.md)
  Returns the given number unchanged.
### Range Expressions
- [static func ... (Self) -> PartialRangeThrough<Self>](./double/dotdotdot%28_%29-4mm67.md)
  Returns a partial range up to, and including, its upper bound.
- [static func ... (Self) -> PartialRangeFrom<Self>](./double/dotdotdot%28_%29-6ct5v.md)
  Returns a partial range extending upward from a lower bound.

## See Also

### Performing Calculations
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/floating-point-operators-for-double)*