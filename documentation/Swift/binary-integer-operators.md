# Binary Integer Operators

**Framework**: Swift  
**Role**: API Collection

Perform arithmetic and bitwise operations or compare values.

## Topics

### Arithmetic
- [static func + (Self, Self) -> Self](./binaryinteger/plus%28_,_%29.md)
  Adds two values and produces their sum.
- [static func - (Self, Self) -> Self](./binaryinteger/minus%28_,_%29.md)
  Subtracts one value from another and produces their difference.
- [static func * (Self, Self) -> Self](./binaryinteger/star%28_,_%29.md)
  Multiplies two values and produces their product.
- [static func / (Self, Self) -> Self](./binaryinteger/op%28_,_%29-8zc6l.md)
  Returns the quotient of dividing the first value by the second.
### Arithmetic with Assignment
- [static func += (inout Self, Self)](./binaryinteger/pluseq%28_,_%29.md)
  Adds two values and stores the result in the left-hand-side variable.
- [static func -= (inout Self, Self)](./binaryinteger/minuseq%28_,_%29.md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable.
- [static func *= (inout Self, Self)](./binaryinteger/stareq%28_,_%29.md)
  Multiplies two values and stores the result in the left-hand-side variable.
- [static func /= (inout Self, Self)](./binaryinteger/opeq%28_,_%29-20xv1.md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable.
### Bitwise Operations
- [static func & (Self, Self) -> Self](./binaryinteger/amp%28_,_%29.md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func &= (inout Self, Self)](./binaryinteger/ampeq%28_,_%29.md)
  Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [static func ~ (Self) -> Self](./binaryinteger/tilde%28_%29.md)
  Returns the inverse of the bits set in the argument.
### Comparison
- [static func != <Other>(Self, Other) -> Bool](./binaryinteger/noteq%28_,_%29-9ooa7.md)
  Returns a Boolean value indicating whether the two given values are not equal.
- [static func != (Self, Self) -> Bool](./binaryinteger/noteq%28_,_%29-4ljme.md)
  Returns a Boolean value indicating whether two values are not equal.

## See Also

### Performing Calculations
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](./binaryinteger/quotientandremainder%28dividingby%29.md)
  Returns the quotient and remainder of this value divided by the given value.
- [func isMultiple(of: Self) -> Bool](./binaryinteger/ismultiple%28of%29.md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binary-integer-operators)*