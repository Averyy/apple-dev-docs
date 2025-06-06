# BinaryInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func != <Other>(Self, Other) -> Bool](uint16/!=(_:_:)-6oo9x.md)
  Returns a Boolean value indicating whether the two given values are not equal.
- [static func & (UInt16, UInt16) -> UInt16](uint16/&(_:_:).md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func & (Self, Self) -> Self](uint16/&(_:_:)-3mlmk.md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func * (UInt16, UInt16) -> UInt16](uint16/*(_:_:).md)
  Multiplies two values and produces their product.
- [static func + (UInt16, UInt16) -> UInt16](uint16/+(_:_:).md)
  Adds two values and produces their sum.
- [static func - (UInt16, UInt16) -> UInt16](uint16/-(_:_:).md)
  Subtracts one value from another and produces their difference.
- [static func == <Other>(Self, Other) -> Bool](uint16/==(_:_:)-69b04.md)
  Returns a Boolean value indicating whether the two given values are equal.
- [static func / (UInt16, UInt16) -> UInt16](uint16/_(_:_:)-1a3d4.md)
  Returns the quotient of dividing the first value by the second.
- [static func | (Self, Self) -> Self](uint16/_(_:_:)-1s8m4.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func ^ (Self, Self) -> Self](uint16/_(_:_:)-297tf.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func | (UInt16, UInt16) -> UInt16](uint16/_(_:_:)-50tep.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func > (Self, Self) -> Bool](uint16/_(_:_:)-67pzh.md)
- [static func % (UInt16, UInt16) -> UInt16](uint16/_(_:_:)-6nw45.md)
  Returns the remainder of dividing the first value by the second.
- [static func < <Other>(Self, Other) -> Bool](uint16/_(_:_:)-7mpvu.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func ^ (UInt16, UInt16) -> UInt16](uint16/_(_:_:)-drxc.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func > <Other>(Self, Other) -> Bool](uint16/_(_:_:)-y91e.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func <= (Self, Self) -> Bool](uint16/_=(_:_:)-4shca.md)
- [static func >= <Other>(Self, Other) -> Bool](uint16/_=(_:_:)-6ddld.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func >= (Self, Self) -> Bool](uint16/_=(_:_:)-6h9fs.md)
- [static func <= <Other>(Self, Other) -> Bool](uint16/_=(_:_:)-ob5s.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [static func >> <Other>(Self, Other) -> Self](uint16/__(_:_:)-2m9b8.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func << <Other>(Self, Other) -> Self](uint16/__(_:_:)-5wx7k.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func << <RHS>(Self, RHS) -> Self](uint16/__(_:_:)-8745o.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >> <RHS>(Self, RHS) -> Self](uint16/__(_:_:)-89hsa.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func >>= <Other>(inout Self, Other)](uint16/__=(_:_:)-2u0d3.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
- [static func <<= <Other>(inout Self, Other)](uint16/__=(_:_:)-9qkzb.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
- [static func ~ (Self) -> Self](uint16/~(_:).md)
  Returns the inverse of the bits set in the argument.
### Initializers
- [init()](uint16/init.md)
  Creates a new value equal to zero.
- [init<Other>(clamping: Other)](uint16/init(clamping:).md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<T>(truncatingIfNeeded: T)](uint16/init(truncatingifneeded:).md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
### Instance Properties
- [var bitWidth: Int](uint16/bitwidth-swift.property.md)
  The number of bits in the current binary representation of this value.
- [var description: String](uint16/description.md)
  A textual representation of this value.
### Instance Methods
- [func advanced(by: Int) -> Self](uint16/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Self) -> Int](uint16/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [func isMultiple(of: Self) -> Bool](uint16/ismultiple(of:).md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](uint16/quotientandremainder(dividingby:).md)
  Returns the quotient and remainder of this value divided by the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint16/binaryinteger-implementations)*