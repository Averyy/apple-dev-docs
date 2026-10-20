# BinaryInteger Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Operators
- [static func != <Other>(Self, Other) -> Bool](./noteq%28_,_%29-4l6xf.md)
  Returns a Boolean value indicating whether the two given values are not equal.
- [static func & (Self, Self) -> Self](./amp%28_,_%29.md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func &= (inout Int128, Int128)](./ampeq%28_,_%29.md)
  Stores the result of performing a bitwise AND operation on the two given values in the left-hand-side variable.
- [static func == <Other>(Self, Other) -> Bool](./eqeq%28_,_%29-31spp.md)
  Returns a Boolean value indicating whether the two given values are equal.
- [static func | (Self, Self) -> Self](./op%28_,_%29-120rc.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func > <Other>(Self, Other) -> Bool](./op%28_,_%29-3jxf8.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func / (Int128, Int128) -> Int128](./op%28_,_%29-3u29x.md)
  Returns the quotient of dividing the first value by the second.
- [static func % (Int128, Int128) -> Int128](./op%28_,_%29-4kr9j.md)
  Returns the remainder of dividing the first value by the second.
- [static func ^ (Self, Self) -> Self](./op%28_,_%29-4wqvr.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func < <Other>(Self, Other) -> Bool](./op%28_,_%29-6c38s.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func > (Self, Self) -> Bool](./op%28_,_%29-71bfg.md)
- [static func >= (Self, Self) -> Bool](./opeq%28_,_%29-2rq25.md)
- [static func <= (Self, Self) -> Bool](./opeq%28_,_%29-3tzf9.md)
- [static func /= (inout Int128, Int128)](./opeq%28_,_%29-4hmtz.md)
  Divides the first value by the second and stores the quotient in the left-hand-side variable.
- [static func %= (inout Int128, Int128)](./opeq%28_,_%29-58nmj.md)
  Divides the first value by the second and stores the remainder in the left-hand-side variable.
- [static func |= (inout Int128, Int128)](./opeq%28_,_%29-791af.md)
  Stores the result of performing a bitwise OR operation on the two given values in the left-hand-side variable.
- [static func >= <Other>(Self, Other) -> Bool](./opeq%28_,_%29-90wyd.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func <= <Other>(Self, Other) -> Bool](./opeq%28_,_%29-9kicv.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [static func ^= (inout Int128, Int128)](./opeq%28_,_%29-ckwk.md)
  Stores the result of performing a bitwise XOR operation on the two given values in the left-hand-side variable.
- [static func >> <Other>(Self, Other) -> Self](./opop%28_,_%29-10plt.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func << <Other>(Self, Other) -> Self](./opop%28_,_%29-30yed.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func << <RHS>(Self, RHS) -> Self](./opop%28_,_%29-6jhs3.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >> <RHS>(Self, RHS) -> Self](./opop%28_,_%29-80gwd.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func <<= <Other>(inout Self, Other)](./opopeq%28_,_%29-195op.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
- [static func >>= <Other>(inout Self, Other)](./opopeq%28_,_%29-3w1qu.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
- [static func ~ (Self) -> Self](./tilde%28_%29.md)
  Returns the inverse of the bits set in the argument.
### Initializers
- [init()](./init%28%29.md)
  Creates a new value equal to zero.
- [init<T>(T)](./init%28_%29-7ib60.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init<T>(T)](./init%28_%29-95d5.md)
  Creates a new instance from the given integer.
- [init<T>(clamping: T)](./init%28clamping%29.md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<Other>(clamping: Other)](./init%28clamping%29-4ogm3.md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init?<T>(exactly: T)](./init%28exactly%29-7ybhb.md)
  Creates an integer from the given floating-point value, if it can be represented exactly.
- [init<T>(truncatingIfNeeded: T)](./init%28truncatingifneeded%29.md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
- [init<T>(truncatingIfNeeded: T)](./init%28truncatingifneeded%29-9tq25.md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
### Instance Properties
- [var bitWidth: Int](./bitwidth-swift.property.md)
  The number of bits in the current binary representation of this value.
- [var description: String](./description.md)
  A textual representation of this value.
- [var trailingZeroBitCount: Int](./trailingzerobitcount.md)
  The number of trailing zeros in this value’s binary representation.
- [var words: UInt128.Words](./words-swift.property.md)
  A collection containing the words of this value’s binary representation, in order from the least significant to most significant.
### Instance Methods
- [func advanced(by: Int) -> Self](./advanced%28by%29.md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Self) -> Int](./distance%28to%29.md)
  Returns the distance from this value to the given value, expressed as a stride.
- [func isMultiple(of: Self) -> Bool](./ismultiple%28of%29.md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](./quotientandremainder%28dividingby%29.md)
  Returns the quotient and remainder of this value divided by the given value.
- [func signum() -> Self](./signum%28%29.md)
  Returns `-1` if this value is negative and `1` if it’s positive; otherwise, `0`.
### Type Aliases
- [typealias Words](./words-swift.typealias.md)
  A type that represents the words of a binary integer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int128/binaryinteger-implementations)*