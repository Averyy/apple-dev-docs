# BinaryInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func != <Other>(Self, Other) -> Bool](uint32/!=(_:_:)-6i9jj.md)
  Returns a Boolean value indicating whether the two given values are not equal.
- [static func & (UInt32, UInt32) -> UInt32](uint32/&(_:_:).md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func & (Self, Self) -> Self](uint32/&(_:_:)-3g9c6.md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func * (UInt32, UInt32) -> UInt32](uint32/*(_:_:).md)
  Multiplies two values and produces their product.
- [static func + (UInt32, UInt32) -> UInt32](uint32/+(_:_:).md)
  Adds two values and produces their sum.
- [static func - (UInt32, UInt32) -> UInt32](uint32/-(_:_:).md)
  Subtracts one value from another and produces their difference.
- [static func == <Other>(Self, Other) -> Bool](uint32/==(_:_:)-6gtla.md)
  Returns a Boolean value indicating whether the two given values are equal.
- [static func | (Self, Self) -> Self](uint32/_(_:_:)-1zok6.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func ^ (Self, Self) -> Self](uint32/_(_:_:)-21za9.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func / (UInt32, UInt32) -> UInt32](uint32/_(_:_:)-544gh.md)
  Returns the quotient of dividing the first value by the second.
- [static func | (UInt32, UInt32) -> UInt32](uint32/_(_:_:)-5p6yw.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func > (Self, Self) -> Bool](uint32/_(_:_:)-60hif.md)
- [static func % (UInt32, UInt32) -> UInt32](uint32/_(_:_:)-6ovdh.md)
  Returns the remainder of dividing the first value by the second.
- [static func < <Other>(Self, Other) -> Bool](uint32/_(_:_:)-7gl7s.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func ^ (UInt32, UInt32) -> UInt32](uint32/_(_:_:)-9mox3.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func > <Other>(Self, Other) -> Bool](uint32/_(_:_:)-ru4w.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func <= (Self, Self) -> Bool](uint32/_=(_:_:)-4zprc.md)
- [static func >= <Other>(Self, Other) -> Bool](uint32/_=(_:_:)-6655v.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func >= (Self, Self) -> Bool](uint32/_=(_:_:)-69qui.md)
- [static func <= <Other>(Self, Other) -> Bool](uint32/_=(_:_:)-vr4i.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [static func >> <Other>(Self, Other) -> Self](uint32/__(_:_:)-2fuku.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func << <Other>(Self, Other) -> Self](uint32/__(_:_:)-63byq.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >> <RHS>(Self, RHS) -> Self](uint32/__(_:_:)-8299k.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func << <RHS>(Self, RHS) -> Self](uint32/__(_:_:)-8ecom.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >>= <Other>(inout Self, Other)](uint32/__=(_:_:)-2nln1.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
- [static func <<= <Other>(inout Self, Other)](uint32/__=(_:_:)-9xth9.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
- [static func ~ (Self) -> Self](uint32/~(_:).md)
  Returns the inverse of the bits set in the argument.
### Initializers
- [init()](uint32/init.md)
  Creates a new value equal to zero.
- [init<Other>(clamping: Other)](uint32/init(clamping:).md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<T>(truncatingIfNeeded: T)](uint32/init(truncatingifneeded:).md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
### Instance Properties
- [var bitWidth: Int](uint32/bitwidth-swift.property.md)
  The number of bits in the current binary representation of this value.
- [var description: String](uint32/description.md)
  A textual representation of this value.
### Instance Methods
- [func advanced(by: Int) -> Self](uint32/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Self) -> Int](uint32/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [func isMultiple(of: Self) -> Bool](uint32/ismultiple(of:).md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](uint32/quotientandremainder(dividingby:).md)
  Returns the quotient and remainder of this value divided by the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint32/binaryinteger-implementations)*