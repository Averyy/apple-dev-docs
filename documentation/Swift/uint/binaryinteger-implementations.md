# BinaryInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func != <Other>(Self, Other) -> Bool](uint/!=(_:_:)-4jpi0.md)
  Returns a Boolean value indicating whether the two given values are not equal.
- [static func & (UInt, UInt) -> UInt](uint/&(_:_:).md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func & (Self, Self) -> Self](uint/&(_:_:)-1gv93.md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func * (UInt, UInt) -> UInt](uint/*(_:_:).md)
  Multiplies two values and produces their product.
- [static func + (UInt, UInt) -> UInt](uint/+(_:_:).md)
  Adds two values and produces their sum.
- [static func - (UInt, UInt) -> UInt](uint/-(_:_:).md)
  Subtracts one value from another and produces their difference.
- [static func == <Other>(Self, Other) -> Bool](uint/==(_:_:)-1zalq.md)
  Returns a Boolean value indicating whether the two given values are equal.
- [static func | (Self, Self) -> Self](uint/_(_:_:)-1e0ey.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func / (UInt, UInt) -> UInt](uint/_(_:_:)-1w9sv.md)
  Returns the quotient of dividing the first value by the second.
- [static func ^ (Self, Self) -> Self](uint/_(_:_:)-2yuuu.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func < <Other>(Self, Other) -> Bool](uint/_(_:_:)-3r6zk.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func > (Self, Self) -> Bool](uint/_(_:_:)-4e53m.md)
- [static func % (UInt, UInt) -> UInt](uint/_(_:_:)-5hyxb.md)
  Returns the remainder of dividing the first value by the second.
- [static func | (UInt, UInt) -> UInt](uint/_(_:_:)-70g4r.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func > <Other>(Self, Other) -> Bool](uint/_(_:_:)-7d589.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func ^ (UInt, UInt) -> UInt](uint/_(_:_:)-e9z4.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func <= (Self, Self) -> Bool](uint/_=(_:_:)-6cfcm.md)
- [static func >= (Self, Self) -> Bool](uint/_=(_:_:)-7tms1.md)
- [static func >= <Other>(Self, Other) -> Bool](uint/_=(_:_:)-7v58u.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func <= <Other>(Self, Other) -> Bool](uint/_=(_:_:)-yeqy.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [static func << <RHS>(Self, RHS) -> Self](uint/__(_:_:)-2xfje.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func << <Other>(Self, Other) -> Self](uint/__(_:_:)-60q9j.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >> <Other>(Self, Other) -> Self](uint/__(_:_:)-635q0.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func >> <RHS>(Self, RHS) -> Self](uint/__(_:_:)-97tkd.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func <<= <Other>(inout Self, Other)](uint/__=(_:_:)-66xfr.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
- [static func >>= <Other>(inout Self, Other)](uint/__=(_:_:)-9p0cx.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
- [static func ~ (Self) -> Self](uint/~(_:).md)
  Returns the inverse of the bits set in the argument.
### Initializers
- [init()](uint/init.md)
  Creates a new value equal to zero.
- [init<Other>(clamping: Other)](uint/init(clamping:).md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<T>(truncatingIfNeeded: T)](uint/init(truncatingifneeded:).md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
### Instance Properties
- [var bitWidth: Int](uint/bitwidth-swift.property.md)
  The number of bits in the current binary representation of this value.
- [var description: String](uint/description.md)
  A textual representation of this value.
### Instance Methods
- [func advanced(by: Int) -> Self](uint/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Self) -> Int](uint/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [func isMultiple(of: Self) -> Bool](uint/ismultiple(of:).md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](uint/quotientandremainder(dividingby:).md)
  Returns the quotient and remainder of this value divided by the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint/binaryinteger-implementations)*