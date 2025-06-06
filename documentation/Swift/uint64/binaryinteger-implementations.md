# BinaryInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func != <Other>(Self, Other) -> Bool](uint64/!=(_:_:)-67tzk.md)
  Returns a Boolean value indicating whether the two given values are not equal.
- [static func & (UInt64, UInt64) -> UInt64](uint64/&(_:_:).md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func & (Self, Self) -> Self](uint64/&(_:_:)-3x1yh.md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func * (UInt64, UInt64) -> UInt64](uint64/*(_:_:).md)
  Multiplies two values and produces their product.
- [static func + (UInt64, UInt64) -> UInt64](uint64/+(_:_:).md)
  Adds two values and produces their sum.
- [static func - (UInt64, UInt64) -> UInt64](uint64/-(_:_:).md)
  Subtracts one value from another and produces their difference.
- [static func == <Other>(Self, Other) -> Bool](uint64/==(_:_:)-6ra49.md)
  Returns a Boolean value indicating whether the two given values are equal.
- [static func ^ (Self, Self) -> Self](uint64/_(_:_:)-1kwg2.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func | (Self, Self) -> Self](uint64/_(_:_:)-2girh.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func ^ (UInt64, UInt64) -> UInt64](uint64/_(_:_:)-5hgaz.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func > (Self, Self) -> Bool](uint64/_(_:_:)-5jero.md)
- [static func % (UInt64, UInt64) -> UInt64](uint64/_(_:_:)-68vrk.md)
  Returns the remainder of dividing the first value by the second.
- [static func | (UInt64, UInt64) -> UInt64](uint64/_(_:_:)-6ykmm.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func < <Other>(Self, Other) -> Bool](uint64/_(_:_:)-75vtz.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func / (UInt64, UInt64) -> UInt64](uint64/_(_:_:)-8b3l2.md)
  Returns the quotient of dividing the first value by the second.
- [static func > <Other>(Self, Other) -> Bool](uint64/_(_:_:)-9xpv.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func <= <Other>(Self, Other) -> Bool](uint64/_=(_:_:)-1clb5.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [static func <= (Self, Self) -> Bool](uint64/_=(_:_:)-4pbv7.md)
- [static func >= <Other>(Self, Other) -> Bool](uint64/_=(_:_:)-5p2f4.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func >= (Self, Self) -> Bool](uint64/_=(_:_:)-5sy3d.md)
- [static func >> <Other>(Self, Other) -> Self](uint64/__(_:_:)-25f5d.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func << <Other>(Self, Other) -> Self](uint64/__(_:_:)-5so09.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >> <RHS>(Self, RHS) -> Self](uint64/__(_:_:)-7rk6f.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func << <RHS>(Self, RHS) -> Self](uint64/__(_:_:)-83yhh.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >>= <Other>(inout Self, Other)](uint64/__=(_:_:)-25p32.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
- [static func <<= <Other>(inout Self, Other)](uint64/__=(_:_:)-7usr.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
- [static func ~ (Self) -> Self](uint64/~(_:).md)
  Returns the inverse of the bits set in the argument.
### Initializers
- [init()](uint64/init.md)
  Creates a new value equal to zero.
- [init(String, format: IntegerFormatStyle<Self>, lenient: Bool) throws](uint64/init(_:format:lenient:)-1b9ur.md)
- [init(String, format: IntegerFormatStyle<Self>.Currency, lenient: Bool) throws](uint64/init(_:format:lenient:)-1h8g6.md)
- [init(String, format: IntegerFormatStyle<Self>.Percent, lenient: Bool) throws](uint64/init(_:format:lenient:)-1x7s1.md)
- [init<S>(S.ParseInput, strategy: S) throws](uint64/init(_:strategy:)-2ggmt.md)
  Initialize an instance by parsing `value` with the given `strategy`.
- [init<S>(S.ParseInput, strategy: S) throws](uint64/init(_:strategy:)-9spow.md)
  Initialize an instance by parsing `value` with the given `strategy`.
- [init<Other>(clamping: Other)](uint64/init(clamping:).md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<T>(truncatingIfNeeded: T)](uint64/init(truncatingifneeded:).md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
### Instance Properties
- [var bitWidth: Int](uint64/bitwidth-swift.property.md)
  The number of bits in the current binary representation of this value.
- [var description: String](uint64/description.md)
  A textual representation of this value.
### Instance Methods
- [func advanced(by: Int) -> Self](uint64/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Self) -> Int](uint64/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [func formatted() -> String](uint64/formatted.md)
  Format `self` using `IntegerFormatStyle()`
- [func formatted<S>(S) -> S.FormatOutput](uint64/formatted(_:)-2wm83.md)
  Format `self` with the given format.
- [func formatted<S>(S) -> S.FormatOutput](uint64/formatted(_:)-533x0.md)
  Format `self` with the given format. `self` is first converted to `S.FormatInput` type, then format with the given format.
- [func isMultiple(of: Self) -> Bool](uint64/ismultiple(of:).md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](uint64/quotientandremainder(dividingby:).md)
  Returns the quotient and remainder of this value divided by the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint64/binaryinteger-implementations)*