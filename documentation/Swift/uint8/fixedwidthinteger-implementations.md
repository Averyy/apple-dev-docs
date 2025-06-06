# FixedWidthInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func &* (Self, Self) -> Self](uint8/&*(_:_:).md)
  Returns the product of the two given values, wrapping the result in case of any overflow.
- [static func &*= (inout Self, Self)](uint8/&*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &+ (Self, Self) -> Self](uint8/&+(_:_:).md)
  Returns the sum of the two given values, wrapping the result in case of any overflow.
- [static func &+= (inout Self, Self)](uint8/&+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &- (Self, Self) -> Self](uint8/&-(_:_:).md)
  Returns the difference of the two given values, wrapping the result in case of any overflow.
- [static func &-= (inout Self, Self)](uint8/&-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.
- [static func &>> (UInt8, UInt8) -> UInt8](uint8/&__(_:_:)-1fquv.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &>> <Other>(Self, Other) -> Self](uint8/&__(_:_:)-3qwyl.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<< (Self, Self) -> Self](uint8/&__(_:_:)-5m6yb.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &<< <Other>(Self, Other) -> Self](uint8/&__(_:_:)-60i6u.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &>> (Self, Self) -> Self](uint8/&__(_:_:)-6jqbr.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<< (UInt8, UInt8) -> UInt8](uint8/&__(_:_:)-7gp0b.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &>>= <Other>(inout Self, Other)](uint8/&__=(_:_:)-16yhm.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &<<= <Other>(inout Self, Other)](uint8/&__=(_:_:)-60dw2.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
### Initializers
- [init?(String)](uint8/init(_:)-1iroc.md)
  Creates a new integer value from the given string.
- [init<T>(T)](uint8/init(_:)-5e02.md)
- [init?<S>(S, radix: Int)](uint8/init(_:radix:).md)
  Creates a new integer value from the given string and radix.
- [init(bigEndian: Self)](uint8/init(bigendian:).md)
  Creates an integer from its big-endian representation, changing the byte order if necessary.
- [init?<T>(exactly: T)](uint8/init(exactly:)-8szg6.md)
- [init(littleEndian: Self)](uint8/init(littleendian:).md)
  Creates an integer from its little-endian representation, changing the byte order if necessary.
### Instance Properties
- [var bigEndian: Self](uint8/bigendian.md)
  The big-endian representation of this integer.
- [var littleEndian: Self](uint8/littleendian.md)
  The little-endian representation of this integer.
### Type Methods
- [static func random(in: Range<Self>) -> Self](uint8/random(in:)-6wnz5.md)
  Returns a random value within the specified range.
- [static func random(in: ClosedRange<Self>) -> Self](uint8/random(in:)-85h4o.md)
  Returns a random value within the specified range.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](uint8/random(in:using:)-3zjsj.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](uint8/random(in:using:)-6l2z5.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint8/fixedwidthinteger-implementations)*