# BinaryInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func != <Other>(Self, Other) -> Bool](int32/!=(_:_:)-2y35c.md)
  Returns a Boolean value indicating whether the two given values are not equal.
- [static func & (Int32, Int32) -> Int32](int32/&(_:_:).md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func & (Self, Self) -> Self](int32/&(_:_:)-ui0w.md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func * (Int32, Int32) -> Int32](int32/*(_:_:).md)
  Multiplies two values and produces their product.
- [static func + (Int32, Int32) -> Int32](int32/+(_:_:).md)
  Adds two values and produces their sum.
- [static func - (Int32, Int32) -> Int32](int32/-(_:_:).md)
  Subtracts one value from another and produces their difference.
- [static func == <Other>(Self, Other) -> Bool](int32/==(_:_:)-1giba.md)
  Returns a Boolean value indicating whether the two given values are equal.
- [static func ^ (Int32, Int32) -> Int32](int32/_(_:_:)-1xb80.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func ^ (Self, Self) -> Self](int32/_(_:_:)-2t9oy.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func % (Int32, Int32) -> Int32](int32/_(_:_:)-41rsu.md)
  Returns the remainder of dividing the first value by the second.
- [static func > <Other>(Self, Other) -> Bool](int32/_(_:_:)-4jn4j.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func | (Int32, Int32) -> Int32](int32/_(_:_:)-5i6yu.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func | (Self, Self) -> Self](int32/_(_:_:)-5zn2u.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func < <Other>(Self, Other) -> Bool](int32/_(_:_:)-67qna.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func / (Int32, Int32) -> Int32](int32/_(_:_:)-6fvom.md)
  Returns the quotient of dividing the first value by the second.
- [static func > (Self, Self) -> Bool](int32/_(_:_:)-9adkd.md)
- [static func <= <Other>(Self, Other) -> Bool](int32/_=(_:_:)-1nkpl.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [static func >= (Self, Self) -> Bool](int32/_=(_:_:)-3jitm.md)
- [static func <= (Self, Self) -> Bool](int32/_=(_:_:)-4p7mg.md)
- [static func >= <Other>(Self, Other) -> Bool](int32/_=(_:_:)-86dc4.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func << <Other>(Self, Other) -> Self](int32/__(_:_:)-27cld.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >> <RHS>(Self, RHS) -> Self](int32/__(_:_:)-2ny6e.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func >> <Other>(Self, Other) -> Self](int32/__(_:_:)-5xz7g.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func << <RHS>(Self, RHS) -> Self](int32/__(_:_:)-78esh.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >>= <Other>(inout Self, Other)](int32/__=(_:_:)-1o1y1.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
- [static func <<= <Other>(inout Self, Other)](int32/__=(_:_:)-80z6h.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
- [static func ~ (Self) -> Self](int32/~(_:).md)
  Returns the inverse of the bits set in the argument.
### Initializers
- [init()](int32/init.md)
  Creates a new value equal to zero.
- [init<Other>(clamping: Other)](int32/init(clamping:).md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<T>(truncatingIfNeeded: T)](int32/init(truncatingifneeded:).md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
### Instance Properties
- [var bitWidth: Int](int32/bitwidth-swift.property.md)
  The number of bits in the current binary representation of this value.
- [var description: String](int32/description.md)
  A textual representation of this value.
### Instance Methods
- [func advanced(by: Int) -> Self](int32/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Self) -> Int](int32/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [func isMultiple(of: Self) -> Bool](int32/ismultiple(of:).md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](int32/quotientandremainder(dividingby:).md)
  Returns the quotient and remainder of this value divided by the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int32/binaryinteger-implementations)*