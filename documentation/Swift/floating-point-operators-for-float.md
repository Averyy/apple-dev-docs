# Floating-Point Operators for Float

**Framework**: Swift  
**Role**: API Collection

Perform arithmetic and bitwise operations or compare values.

## Topics

### Arithmetic
- [static func + (Float, Float) -> Float](./float/plus%28_,_%29.md)
  Adds two values and produces their sum, rounded to a representable value.
- [static func - (Float, Float) -> Float](./float/minus%28_,_%29.md)
  Subtracts one value from another and produces their difference, rounded to a representable value.
- [static func * (Float, Float) -> Float](./float/star%28_,_%29.md)
  Multiplies two values and produces their product, rounding to a representable value.
- [static func / (Float, Float) -> Float](./float/op%28_,_%29.md)
  Returns the quotient of dividing the first value by the second, rounded to a representable value.
### Arithmetic with Assignment
- [static func += (inout Float, Float)](./float/pluseq%28_,_%29.md)
  Adds two values and stores the result in the left-hand-side variable, rounded to a representable value.
- [static func -= (inout Float, Float)](./float/minuseq%28_,_%29.md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, rounding to a representable value.
- [static func *= (inout Float, Float)](./float/stareq%28_,_%29.md)
  Multiplies two values and stores the result in the left-hand-side variable, rounding to a representable value.
- [static func /= (inout Float, Float)](./float/opeq%28_,_%29.md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable, rounding to a representable value.
### Comparison
- [static func == (Self, Self) -> Bool](./float/eqeq%28_,_%29-12hdt.md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (borrowing Self, borrowing Self) -> Bool](./float/noteq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func < (Self, Self) -> Bool](./float/op%28_,_%29-7lwp7.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func <= (Self, Self) -> Bool](./float/opeq%28_,_%29-5yoz5.md)
- [static func > (Self, Self) -> Bool](./float/op%28_,_%29-552jr.md)
- [static func >= (Self, Self) -> Bool](./float/opeq%28_,_%29-9o6ha.md)
### Negation
- [static func - (Float) -> Float](./float/minus%28_%29.md)
  Calculates the additive inverse of a value.
- [static func + (Self) -> Self](./float/plus%28_%29.md)
  Returns the given number unchanged.
### Range Expressions
- [static func ..< (Self) -> PartialRangeUpTo<Self>](./float/dotdotop%28_%29.md)
  Returns a partial range up to, but not including, its upper bound.
- [static func ... (Self) -> PartialRangeThrough<Self>](./float/dotdotdot%28_%29-4mm65.md)
  Returns a partial range up to, and including, its upper bound.
- [static func ... (Self) -> PartialRangeFrom<Self>](./float/dotdotdot%28_%29-6ct5t.md)
  Returns a partial range extending upward from a lower bound.

## See Also

### Performing Calculations
- [func addingProduct(Self, Self) -> Self](./float/addingproduct%28_,_%29.md)
  Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [func addProduct(Float, Float)](./float/addproduct%28_,_%29.md)
  Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [func squareRoot() -> Self](./float/squareroot%28%29.md)
  Returns the square root of the value, rounded to a representable value.
- [func formSquareRoot()](./float/formsquareroot%28%29.md)
  Replaces this value with its square root, rounded to a representable value.
- [func remainder(dividingBy: Self) -> Self](./float/remainder%28dividingby%29.md)
  Returns the remainder of this value divided by the given value.
- [func formRemainder(dividingBy: Float)](./float/formremainder%28dividingby%29.md)
  Replaces this value with the remainder of itself divided by the given value.
- [func truncatingRemainder(dividingBy: Self) -> Self](./float/truncatingremainder%28dividingby%29.md)
  Returns the remainder of this value divided by the given value using truncating division.
- [func formTruncatingRemainder(dividingBy: Float)](./float/formtruncatingremainder%28dividingby%29.md)
  Replaces this value with the remainder of itself divided by the given value using truncating division.
- [func negate()](./float/negate%28%29.md)
  Replaces this value with its additive inverse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/floating-point-operators-for-float)*