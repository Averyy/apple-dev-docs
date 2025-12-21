# BinaryInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func != <Other>(Self, Other) -> Bool](int64/!=(_:_:)-3fzrz.md)
  Returns a Boolean value indicating whether the two given values are not equal.
- [static func & (Int64, Int64) -> Int64](int64/&(_:_:).md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func & (Self, Self) -> Self](int64/&(_:_:)-jsun.md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func * (Int64, Int64) -> Int64](int64/*(_:_:).md)
  Multiplies two values and produces their product.
- [static func + (Int64, Int64) -> Int64](int64/+(_:_:).md)
  Adds two values and produces their sum.
- [static func - (Int64, Int64) -> Int64](int64/-(_:_:).md)
  Subtracts one value from another and produces their difference.
- [static func == <Other>(Self, Other) -> Bool](int64/==(_:_:)-1qxpp.md)
  Returns a Boolean value indicating whether the two given values are equal.
- [static func ^ (Int64, Int64) -> Int64](int64/_(_:_:)-1pc7e.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func % (Int64, Int64) -> Int64](int64/_(_:_:)-2xs3w.md)
  Returns the remainder of dividing the first value by the second.
- [static func ^ (Self, Self) -> Self](int64/_(_:_:)-340al.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func > <Other>(Self, Other) -> Bool](int64/_(_:_:)-4u3sc.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func / (Int64, Int64) -> Int64](int64/_(_:_:)-52g64.md)
  Returns the quotient of dividing the first value by the second.
- [static func | (Self, Self) -> Self](int64/_(_:_:)-5oz05.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func | (Int64, Int64) -> Int64](int64/_(_:_:)-65vvy.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func < <Other>(Self, Other) -> Bool](int64/_(_:_:)-6otcp.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func > (Self, Self) -> Bool](int64/_(_:_:)-9l49m.md)
- [static func <= <Other>(Self, Other) -> Bool](int64/_=(_:_:)-1d6gy.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [static func >= (Self, Self) -> Bool](int64/_=(_:_:)-3tzj9.md)
- [static func <= (Self, Self) -> Bool](int64/_=(_:_:)-561mj.md)
- [static func >= <Other>(Self, Other) -> Bool](int64/_=(_:_:)-8h42b.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func << <Other>(Self, Other) -> Self](int64/__(_:_:)-2o6oi.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >> <RHS>(Self, RHS) -> Self](int64/__(_:_:)-364qh.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func >> <Other>(Self, Other) -> Self](int64/__(_:_:)-6es2r.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func << <RHS>(Self, RHS) -> Self](int64/__(_:_:)-7p8tu.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >>= <Other>(inout Self, Other)](int64/__=(_:_:)-1yiba.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
- [static func <<= <Other>(inout Self, Other)](int64/__=(_:_:)-8bomq.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
- [static func ~ (Self) -> Self](int64/~(_:).md)
  Returns the inverse of the bits set in the argument.
### Initializers
- [init()](int64/init.md)
  Creates a new value equal to zero.
- [init<Other>(clamping: Other)](int64/init(clamping:).md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<T>(truncatingIfNeeded: T)](int64/init(truncatingifneeded:).md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
### Instance Properties
- [var bitWidth: Int](int64/bitwidth-swift.property.md)
  The number of bits in the current binary representation of this value.
- [var description: String](int64/description.md)
  A textual representation of this value.
### Instance Methods
- [func advanced(by: Int) -> Self](int64/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Self) -> Int](int64/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [func isMultiple(of: Self) -> Bool](int64/ismultiple(of:).md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](int64/quotientandremainder(dividingby:).md)
  Returns the quotient and remainder of this value divided by the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int64/binaryinteger-implementations)*