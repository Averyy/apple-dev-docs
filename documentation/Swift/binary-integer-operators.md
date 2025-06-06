# Binary Integer Operators

**Framework**: Swift

Perform arithmetic and bitwise operations or compare values.

## Topics

### Arithmetic
- [static func + (Self, Self) -> Self](binaryinteger/+(_:_:).md)
  Adds two values and produces their sum.
- [static func - (Self, Self) -> Self](binaryinteger/-(_:_:).md)
  Subtracts one value from another and produces their difference.
- [static func * (Self, Self) -> Self](binaryinteger/*(_:_:).md)
  Multiplies two values and produces their product.
- [static func / (Self, Self) -> Self](binaryinteger/_(_:_:)-8zc6l.md)
  Returns the quotient of dividing the first value by the second.
### Arithmetic with Assignment
- [static func += (inout Self, Self)](binaryinteger/+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable.
- [static func -= (inout Self, Self)](binaryinteger/-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable.
- [static func *= (inout Self, Self)](binaryinteger/*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable.
- [static func /= (inout Self, Self)](binaryinteger/_=(_:_:)-20xv1.md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable.
### Bitwise Operations
- [static func & (Self, Self) -> Self](binaryinteger/&(_:_:).md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func &= (inout Self, Self)](binaryinteger/&=(_:_:).md)
  Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [static func ~ (Self) -> Self](binaryinteger/~(_:).md)
  Returns the inverse of the bits set in the argument.
### Comparison
- [static func != <Other>(Self, Other) -> Bool](binaryinteger/!=(_:_:)-9ooa7.md)
  Returns a Boolean value indicating whether the two given values are not equal.
- [static func != (Self, Self) -> Bool](binaryinteger/!=(_:_:)-4ljme.md)
  Returns a Boolean value indicating whether two values are not equal.

## See Also

- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](binaryinteger/quotientandremainder(dividingby:).md)
  Returns the quotient and remainder of this value divided by the given value.
- [func isMultiple(of: Self) -> Bool](binaryinteger/ismultiple(of:).md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binary-integer-operators)*