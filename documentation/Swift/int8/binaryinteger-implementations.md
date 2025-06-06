# BinaryInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func != <Other>(Self, Other) -> Bool](int8/!=(_:_:)-5cims.md)
  Returns a Boolean value indicating whether the two given values are not equal.
- [static func & (Int8, Int8) -> Int8](int8/&(_:_:).md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func & (Self, Self) -> Self](int8/&(_:_:)-6jf06.md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func * (Int8, Int8) -> Int8](int8/*(_:_:).md)
  Multiplies two values and produces their product.
- [static func + (Int8, Int8) -> Int8](int8/+(_:_:).md)
  Adds two values and produces their sum.
- [static func - (Int8, Int8) -> Int8](int8/-(_:_:).md)
  Subtracts one value from another and produces their difference.
- [static func == <Other>(Self, Other) -> Bool](int8/==(_:_:)-exky.md)
  Returns a Boolean value indicating whether the two given values are equal.
- [static func > (Self, Self) -> Bool](int8/_(_:_:)-1jlfi.md)
- [static func ^ (Int8, Int8) -> Int8](int8/_(_:_:)-346io.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func > <Other>(Self, Other) -> Bool](int8/_(_:_:)-53qq.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func | (Int8, Int8) -> Int8](int8/_(_:_:)-5p6eu.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func < <Other>(Self, Other) -> Bool](int8/_(_:_:)-615a6.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func | (Self, Self) -> Self](int8/_(_:_:)-662qp.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func % (Int8, Int8) -> Int8](int8/_(_:_:)-6tefc.md)
  Returns the remainder of dividing the first value by the second.
- [static func ^ (Self, Self) -> Self](int8/_(_:_:)-a3sx.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func / (Int8, Int8) -> Int8](int8/_(_:_:)-aic4.md)
  Returns the quotient of dividing the first value by the second.
- [static func <= <Other>(Self, Other) -> Bool](int8/_=(_:_:)-10tl1.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [static func >= (Self, Self) -> Bool](int8/_=(_:_:)-3nz2d.md)
- [static func >= <Other>(Self, Other) -> Bool](int8/_=(_:_:)-41bgc.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func <= (Self, Self) -> Bool](int8/_=(_:_:)-5bita.md)
- [static func << <Other>(Self, Other) -> Self](int8/__(_:_:)-3z21o.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >> <Other>(Self, Other) -> Self](int8/__(_:_:)-7wosz.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func << <RHS>(Self, RHS) -> Self](int8/__(_:_:)-9i518.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >> <RHS>(Self, RHS) -> Self](int8/__(_:_:)-moua.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func >>= <Other>(inout Self, Other)](int8/__=(_:_:)-40egk.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
- [static func <<= <Other>(inout Self, Other)](int8/__=(_:_:)-53mkr.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
- [static func ~ (Self) -> Self](int8/~(_:).md)
  Returns the inverse of the bits set in the argument.
### Initializers
- [init()](int8/init.md)
  Creates a new value equal to zero.
- [init<Other>(clamping: Other)](int8/init(clamping:).md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<T>(truncatingIfNeeded: T)](int8/init(truncatingifneeded:).md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
### Instance Properties
- [var bitWidth: Int](int8/bitwidth-swift.property.md)
  The number of bits in the current binary representation of this value.
- [var description: String](int8/description.md)
  A textual representation of this value.
### Instance Methods
- [func advanced(by: Int) -> Self](int8/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Self) -> Int](int8/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [func isMultiple(of: Self) -> Bool](int8/ismultiple(of:).md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](int8/quotientandremainder(dividingby:).md)
  Returns the quotient and remainder of this value divided by the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int8/binaryinteger-implementations)*