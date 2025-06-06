# BinaryInteger Implementations

**Framework**: Swift

## Topics

### Structures
- [UInt128.Words](uint128/words-swift.struct.md)
  A type that represents the words of a binary integer.
### Operators
- [static func != <Other>(Self, Other) -> Bool](uint128/!=(_:_:)-9eyev.md)
  Returns a Boolean value indicating whether the two given values are not equal.
- [static func & (Self, Self) -> Self](uint128/&(_:_:).md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func &= (inout UInt128, UInt128)](uint128/&=(_:_:).md)
  Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [static func == <Other>(Self, Other) -> Bool](uint128/==(_:_:)-4hd8l.md)
  Returns a Boolean value indicating whether the two given values are equal.
- [static func ^ (Self, Self) -> Self](uint128/_(_:_:)-1bfdp.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func < <Other>(Self, Other) -> Bool](uint128/_(_:_:)-3fwln.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func % (UInt128, UInt128) -> UInt128](uint128/_(_:_:)-3t4ck.md)
  Returns the remainder of dividing the first value by the second.
- [static func > (Self, Self) -> Bool](uint128/_(_:_:)-41n11.md)
- [static func / (UInt128, UInt128) -> UInt128](uint128/_(_:_:)-4hvzy.md)
  Returns the quotient of dividing the first value by the second.
- [static func > <Other>(Self, Other) -> Bool](uint128/_(_:_:)-8enxk.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func | (Self, Self) -> Self](uint128/_(_:_:)-k8pw.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func >= <Other>(Self, Other) -> Bool](uint128/_=(_:_:)-1t601.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func >= (Self, Self) -> Bool](uint128/_=(_:_:)-36npw.md)
- [static func <= <Other>(Self, Other) -> Bool](uint128/_=(_:_:)-3wmkz.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [static func ^= (inout UInt128, UInt128)](uint128/_=(_:_:)-4j7m1.md)
  Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [static func /= (inout UInt128, UInt128)](uint128/_=(_:_:)-6xh2i.md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable.
- [static func %= (inout UInt128, UInt128)](uint128/_=(_:_:)-75khj.md)
  Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [static func |= (inout UInt128, UInt128)](uint128/_=(_:_:)-8ko9m.md)
  Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [static func <= (Self, Self) -> Bool](uint128/_=(_:_:)-906fm.md)
- [static func << <Other>(Self, Other) -> Self](uint128/__(_:_:)-3yi94.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func << <RHS>(Self, RHS) -> Self](uint128/__(_:_:)-70lq0.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >> <Other>(Self, Other) -> Self](uint128/__(_:_:)-9qcxu.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func >> <RHS>(Self, RHS) -> Self](uint128/__(_:_:)-9tjzy.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func <<= <Other>(inout Self, Other)](uint128/__=(_:_:)-22e6u.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
- [static func >>= <Other>(inout Self, Other)](uint128/__=(_:_:)-6t3cz.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
- [static func ~ (Self) -> Self](uint128/~(_:).md)
  Returns the inverse of the bits set in the argument.
### Initializers
- [init()](uint128/init.md)
  Creates a new value equal to zero.
- [init<T>(T)](uint128/init(_:)-2b08e.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init<T>(T)](uint128/init(_:)-luvl.md)
  Creates a new instance from the given integer.
- [init<T>(clamping: T)](uint128/init(clamping:).md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<Other>(clamping: Other)](uint128/init(clamping:)-7tt6l.md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init?<T>(exactly: T)](uint128/init(exactly:)-13dy3.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init<T>(truncatingIfNeeded: T)](uint128/init(truncatingifneeded:).md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
- [init<T>(truncatingIfNeeded: T)](uint128/init(truncatingifneeded:)-1xc1t.md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
### Instance Properties
- [var bitWidth: Int](uint128/bitwidth-swift.property.md)
  The number of bits in the current binary representation of this value.
- [var description: String](uint128/description.md)
  A textual representation of this value.
- [var trailingZeroBitCount: Int](uint128/trailingzerobitcount.md)
  The number of trailing zeros in this value’s binary representation.
- [var words: UInt128.Words](uint128/words-swift.property.md)
  A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
### Instance Methods
- [func advanced(by: Int) -> Self](uint128/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Self) -> Int](uint128/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [func isMultiple(of: Self) -> Bool](uint128/ismultiple(of:).md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](uint128/quotientandremainder(dividingby:).md)
  Returns the quotient and remainder of this value divided by the given value.
- [func signum() -> Self](uint128/signum.md)
  Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint128/binaryinteger-implementations)*