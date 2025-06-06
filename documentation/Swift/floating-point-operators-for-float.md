# Floating-Point Operators for Float

**Framework**: Swift

Perform arithmetic and bitwise operations or compare values.

## Topics

### Arithmetic
- [static func + (Float, Float) -> Float](float/+(_:_:).md)
  Adds two values and produces their sum, rounded to a representable value.
- [static func - (Float, Float) -> Float](float/-(_:_:).md)
  Subtracts one value from another and produces their difference, rounded to a representable value.
- [static func * (Float, Float) -> Float](float/*(_:_:).md)
  Multiplies two values and produces their product, rounding to a representable value.
- [static func / (Float, Float) -> Float](float/_(_:_:).md)
  Returns the quotient of dividing the first value by the second, rounded to a representable value.
### Arithmetic with Assignment
- [static func += (inout Float, Float)](float/+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable, rounded to a representable value.
- [static func -= (inout Float, Float)](float/-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, rounding to a representable value.
- [static func *= (inout Float, Float)](float/*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable, rounding to a representable value.
- [static func /= (inout Float, Float)](float/_=(_:_:).md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable, rounding to a representable value.
### Comparison
- [static func == (Self, Self) -> Bool](float/==(_:_:)-12hdt.md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](float/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func < (Self, Self) -> Bool](float/_(_:_:)-7lwp7.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func <= (Self, Self) -> Bool](float/_=(_:_:)-5yoz5.md)
- [static func > (Self, Self) -> Bool](float/_(_:_:)-552jr.md)
- [static func >= (Self, Self) -> Bool](float/_=(_:_:)-9o6ha.md)
### Negation
- [static func - (Float) -> Float](float/-(_:).md)
  Calculates the additive inverse of a value.
- [static func + (Self) -> Self](float/+(_:).md)
  Returns the given number unchanged.
### Range Expressions
- [static func ..< (Self) -> PartialRangeUpTo<Self>](float/'.._(_:).md)
  Returns a partial range up to, but not including, its upper bound.
- [static func ... (Self) -> PartialRangeThrough<Self>](float/'...(_:)-4mm65.md)
  Returns a partial range up to, and including, its upper bound.
- [static func ... (Self) -> PartialRangeFrom<Self>](float/'...(_:)-6ct5t.md)
  Returns a partial range extending upward from a lower bound.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/floating-point-operators-for-float)*