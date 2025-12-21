# BinaryInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func != <Other>(Self, Other) -> Bool](int/!=(_:_:)-4jphg.md)
  Returns a Boolean value indicating whether the two given values are not equal.
- [static func & (Int, Int) -> Int](int/&(_:_:).md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func & (Self, Self) -> Self](int/&(_:_:)-1gv8r.md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func * (Int, Int) -> Int](int/*(_:_:).md)
  Multiplies two values and produces their product.
- [static func + (Int, Int) -> Int](int/+(_:_:).md)
  Adds two values and produces their sum.
- [static func - (Int, Int) -> Int](int/-(_:_:).md)
  Subtracts one value from another and produces their difference.
- [static func == <Other>(Self, Other) -> Bool](int/==(_:_:)-1zalu.md)
  Returns a Boolean value indicating whether the two given values are equal.
- [static func | (Self, Self) -> Self](int/_(_:_:)-1e0ee.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func | (Int, Int) -> Int](int/_(_:_:)-26x3w.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func ^ (Self, Self) -> Self](int/_(_:_:)-2yuui.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func < <Other>(Self, Other) -> Bool](int/_(_:_:)-3r70c.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func > (Self, Self) -> Bool](int/_(_:_:)-4e53i.md)
- [static func ^ (Int, Int) -> Int](int/_(_:_:)-591r5.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func % (Int, Int) -> Int](int/_(_:_:)-6lyj3.md)
  Returns the remainder of dividing the first value by the second.
- [static func > <Other>(Self, Other) -> Bool](int/_(_:_:)-7d57p.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func / (Int, Int) -> Int](int/_(_:_:)-7j9bj.md)
  Returns the quotient of dividing the first value by the second.
- [static func <= (Self, Self) -> Bool](int/_=(_:_:)-6cfca.md)
- [static func >= (Self, Self) -> Bool](int/_=(_:_:)-7tmrx.md)
- [static func >= <Other>(Self, Other) -> Bool](int/_=(_:_:)-7v58y.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func <= <Other>(Self, Other) -> Bool](int/_=(_:_:)-yera.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [static func << <RHS>(Self, RHS) -> Self](int/__(_:_:)-2xfjq.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func << <Other>(Self, Other) -> Self](int/__(_:_:)-60q97.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >> <Other>(Self, Other) -> Self](int/__(_:_:)-635pg.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func >> <RHS>(Self, RHS) -> Self](int/__(_:_:)-97tkh.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func <<= <Other>(inout Self, Other)](int/__=(_:_:)-66xgb.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
- [static func >>= <Other>(inout Self, Other)](int/__=(_:_:)-9p0ct.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
- [static func ~ (Self) -> Self](int/~(_:).md)
  Returns the inverse of the bits set in the argument.
### Initializers
- [init()](int/init.md)
  Creates a new value equal to zero.
- [init<Other>(clamping: Other)](int/init(clamping:).md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<T>(truncatingIfNeeded: T)](int/init(truncatingifneeded:).md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
### Instance Properties
- [var bitWidth: Int](int/bitwidth-swift.property.md)
  The number of bits in the current binary representation of this value.
- [var description: String](int/description.md)
  A textual representation of this value.
### Instance Methods
- [func isMultiple(of: Self) -> Bool](int/ismultiple(of:).md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](int/quotientandremainder(dividingby:).md)
  Returns the quotient and remainder of this value divided by the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/binaryinteger-implementations)*