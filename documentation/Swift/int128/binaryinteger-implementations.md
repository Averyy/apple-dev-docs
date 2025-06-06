# BinaryInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func != <Other>(Self, Other) -> Bool](int128/!=(_:_:)-4l6xf.md)
  Returns a Boolean value indicating whether the two given values are not equal.
- [static func & (Self, Self) -> Self](int128/&(_:_:).md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func &= (inout Int128, Int128)](int128/&=(_:_:).md)
  Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [static func == <Other>(Self, Other) -> Bool](int128/==(_:_:)-31spp.md)
  Returns a Boolean value indicating whether the two given values are equal.
- [static func | (Self, Self) -> Self](int128/_(_:_:)-120rc.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func > <Other>(Self, Other) -> Bool](int128/_(_:_:)-3jxf8.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func / (Int128, Int128) -> Int128](int128/_(_:_:)-3u29x.md)
  Returns the quotient of dividing the first value by the second.
- [static func % (Int128, Int128) -> Int128](int128/_(_:_:)-4kr9j.md)
  Returns the remainder of dividing the first value by the second.
- [static func ^ (Self, Self) -> Self](int128/_(_:_:)-4wqvr.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func < <Other>(Self, Other) -> Bool](int128/_(_:_:)-6c38s.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func > (Self, Self) -> Bool](int128/_(_:_:)-71bfg.md)
- [static func >= (Self, Self) -> Bool](int128/_=(_:_:)-2rq25.md)
- [static func <= (Self, Self) -> Bool](int128/_=(_:_:)-3tzf9.md)
- [static func /= (inout Int128, Int128)](int128/_=(_:_:)-4hmtz.md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable.
- [static func %= (inout Int128, Int128)](int128/_=(_:_:)-58nmj.md)
  Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [static func |= (inout Int128, Int128)](int128/_=(_:_:)-791af.md)
  Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [static func >= <Other>(Self, Other) -> Bool](int128/_=(_:_:)-90wyd.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func <= <Other>(Self, Other) -> Bool](int128/_=(_:_:)-9kicv.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [static func ^= (inout Int128, Int128)](int128/_=(_:_:)-ckwk.md)
  Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [static func >> <Other>(Self, Other) -> Self](int128/__(_:_:)-10plt.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func << <Other>(Self, Other) -> Self](int128/__(_:_:)-30yed.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func << <RHS>(Self, RHS) -> Self](int128/__(_:_:)-6jhs3.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >> <RHS>(Self, RHS) -> Self](int128/__(_:_:)-80gwd.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func <<= <Other>(inout Self, Other)](int128/__=(_:_:)-195op.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
- [static func >>= <Other>(inout Self, Other)](int128/__=(_:_:)-3w1qu.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
- [static func ~ (Self) -> Self](int128/~(_:).md)
  Returns the inverse of the bits set in the argument.
### Initializers
- [init()](int128/init.md)
  Creates a new value equal to zero.
- [init<T>(T)](int128/init(_:)-7ib60.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init<T>(T)](int128/init(_:)-95d5.md)
  Creates a new instance from the given integer.
- [init<T>(clamping: T)](int128/init(clamping:).md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<Other>(clamping: Other)](int128/init(clamping:)-4ogm3.md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init?<T>(exactly: T)](int128/init(exactly:)-7ybhb.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init<T>(truncatingIfNeeded: T)](int128/init(truncatingifneeded:).md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
- [init<T>(truncatingIfNeeded: T)](int128/init(truncatingifneeded:)-9tq25.md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
### Instance Properties
- [var bitWidth: Int](int128/bitwidth-swift.property.md)
  The number of bits in the current binary representation of this value.
- [var description: String](int128/description.md)
  A textual representation of this value.
- [var trailingZeroBitCount: Int](int128/trailingzerobitcount.md)
  The number of trailing zeros in this value’s binary representation.
- [var words: UInt128.Words](int128/words-swift.property.md)
  A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
### Instance Methods
- [func advanced(by: Int) -> Self](int128/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Self) -> Int](int128/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [func isMultiple(of: Self) -> Bool](int128/ismultiple(of:).md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](int128/quotientandremainder(dividingby:).md)
  Returns the quotient and remainder of this value divided by the given value.
- [func signum() -> Self](int128/signum.md)
  Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
### Type Aliases
- [typealias Words](int128/words-swift.typealias.md)
  A type that represents the words of a binary integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int128/binaryinteger-implementations)*