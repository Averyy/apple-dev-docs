# BinaryInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func != <Other>(Self, Other) -> Bool](uint8/!=(_:_:)-99bok.md)
  Returns a Boolean value indicating whether the two given values are not equal.
- [static func & (UInt8, UInt8) -> UInt8](uint8/&(_:_:).md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func & (Self, Self) -> Self](uint8/&(_:_:)-4psmt.md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func * (UInt8, UInt8) -> UInt8](uint8/*(_:_:).md)
  Multiplies two values and produces their product.
- [static func + (UInt8, UInt8) -> UInt8](uint8/+(_:_:).md)
  Adds two values and produces their sum.
- [static func - (UInt8, UInt8) -> UInt8](uint8/-(_:_:).md)
  Subtracts one value from another and produces their difference.
- [static func == <Other>(Self, Other) -> Bool](uint8/==(_:_:)-156b9.md)
  Returns a Boolean value indicating whether the two given values are equal.
- [static func | (UInt8, UInt8) -> UInt8](uint8/_(_:_:)-17p9c.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func ^ (UInt8, UInt8) -> UInt8](uint8/_(_:_:)-2kgmz.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func / (UInt8, UInt8) -> UInt8](uint8/_(_:_:)-327b5.md)
  Returns the quotient of dividing the first value by the second.
- [static func ^ (Self, Self) -> Self](uint8/_(_:_:)-4eiav.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func < <Other>(Self, Other) -> Bool](uint8/_(_:_:)-5kmc9.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func > (Self, Self) -> Bool](uint8/_(_:_:)-6ieix.md)
- [static func > <Other>(Self, Other) -> Bool](uint8/_(_:_:)-7nbqc.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func | (Self, Self) -> Self](uint8/_(_:_:)-865lu.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func % (UInt8, UInt8) -> UInt8](uint8/_(_:_:)-9tmal.md)
  Returns the remainder of dividing the first value by the second.
- [static func <= <Other>(Self, Other) -> Bool](uint8/_=(_:_:)-6b690.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [static func <= (Self, Self) -> Bool](uint8/_=(_:_:)-7efxq.md)
- [static func >= (Self, Self) -> Bool](uint8/_=(_:_:)-8oubr.md)
- [static func >= <Other>(Self, Other) -> Bool](uint8/_=(_:_:)-9rm29.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func >> <Other>(Self, Other) -> Self](uint8/__(_:_:)-2qqlb.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func >> <RHS>(Self, RHS) -> Self](uint8/__(_:_:)-56eg9.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func << <Other>(Self, Other) -> Self](uint8/__(_:_:)-7yxgh.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func << <RHS>(Self, RHS) -> Self](uint8/__(_:_:)-jtqk.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func <<= <Other>(inout Self, Other)](uint8/__=(_:_:)-1p711.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
- [static func >>= <Other>(inout Self, Other)](uint8/__=(_:_:)-8pj4c.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
- [static func ~ (Self) -> Self](uint8/~(_:).md)
  Returns the inverse of the bits set in the argument.
### Initializers
- [init()](uint8/init.md)
  Creates a new value equal to zero.
- [init<Other>(clamping: Other)](uint8/init(clamping:).md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<T>(truncatingIfNeeded: T)](uint8/init(truncatingifneeded:).md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
### Instance Properties
- [var bitWidth: Int](uint8/bitwidth-swift.property.md)
  The number of bits in the current binary representation of this value.
- [var description: String](uint8/description.md)
  A textual representation of this value.
### Instance Methods
- [func advanced(by: Int) -> Self](uint8/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Self) -> Int](uint8/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [func isMultiple(of: Self) -> Bool](uint8/ismultiple(of:).md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](uint8/quotientandremainder(dividingby:).md)
  Returns the quotient and remainder of this value divided by the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint8/binaryinteger-implementations)*