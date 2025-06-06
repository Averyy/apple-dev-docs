# Integer Operators

**Framework**: Swift

Perform arithmetic and bitwise operations or compare values.

## Topics

### Arithmetic
- [static func + (Int, Int) -> Int](int/+(_:_:).md)
  Adds two values and produces their sum.
- [static func - (Int, Int) -> Int](int/-(_:_:).md)
  Subtracts one value from another and produces their difference.
- [static func * (Int, Int) -> Int](int/*(_:_:).md)
  Multiplies two values and produces their product.
- [static func / (Int, Int) -> Int](int/_(_:_:)-7j9bj.md)
  Returns the quotient of dividing the first value by the second.
### Arithmetic with Assignment
- [static func += (inout Int, Int)](int/+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable.
- [static func *= (inout Int, Int)](int/*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable.
- [static func /= (inout Int, Int)](int/_=(_:_:)-9lzpe.md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable.
### Masked Arithmetic
- [static func &+ (Self, Self) -> Self](int/&+(_:_:).md)
  Returns the sum of the two given values, wrapping the result in case of any overflow.
- [static func &- (Self, Self) -> Self](int/&-(_:_:).md)
  Returns the difference of the two given values, wrapping the result in case of any overflow.
- [static func &* (Self, Self) -> Self](int/&*(_:_:).md)
  Returns the product of the two given values, wrapping the result in case of any overflow.
- [static func &+= (inout Self, Self)](int/&+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &-= (inout Self, Self)](int/&-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.
- [static func &*= (inout Self, Self)](int/&*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable, wrapping any overflow.
### Bitwise Operations
- [static func & (Int, Int) -> Int](int/&(_:_:).md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func &= (inout Int, Int)](int/&=(_:_:).md)
  Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [static func ~ (Self) -> Self](int/~(_:).md)
  Returns the inverse of the bits set in the argument.
### Negation
- [static func - (Self) -> Self](int/-(_:).md)
  Returns the additive inverse of the specified value.
- [static func + (Self) -> Self](int/+(_:).md)
  Returns the given number unchanged.
### Comparison
- [static func == (Int, Int) -> Bool](int/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func == <Other>(Self, Other) -> Bool](int/==(_:_:)-1zalu.md)
  Returns a Boolean value indicating whether the two given values are equal.
- [static func != (Self, Self) -> Bool](int/!=(_:_:)-1baz3.md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func != <Other>(Self, Other) -> Bool](int/!=(_:_:)-4jphg.md)
  Returns a Boolean value indicating whether the two given values are not equal.
### Range Expressions
- [static func ... (Self, Self) -> ClosedRange<Self>](int/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.
- [static func ... (Self) -> PartialRangeFrom<Self>](int/'...(_:)-6ct66.md)
  Returns a partial range extending upward from a lower bound.
- [static func ... (Self) -> PartialRangeThrough<Self>](int/'...(_:)-4mm5u.md)
  Returns a partial range up to, and including, its upper bound.
### Deprecated
- [static func -= (inout Int, Int)](int/-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable.

## See Also

- [func negate()](int/negate.md)
  Replaces this value with its additive inverse.
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](int/quotientandremainder(dividingby:).md)
  Returns the quotient and remainder of this value divided by the given value.
- [func isMultiple(of: Self) -> Bool](int/ismultiple(of:).md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/integer-operators)*