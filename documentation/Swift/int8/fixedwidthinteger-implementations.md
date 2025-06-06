# FixedWidthInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func &* (Self, Self) -> Self](int8/&*(_:_:).md)
  Returns the product of the two given values, wrapping the result in case of any overflow.
- [static func &*= (inout Self, Self)](int8/&*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &+ (Self, Self) -> Self](int8/&+(_:_:).md)
  Returns the sum of the two given values, wrapping the result in case of any overflow.
- [static func &+= (inout Self, Self)](int8/&+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &- (Self, Self) -> Self](int8/&-(_:_:).md)
  Returns the difference of the two given values, wrapping the result in case of any overflow.
- [static func &-= (inout Self, Self)](int8/&-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.
- [static func &>> (Int8, Int8) -> Int8](int8/&__(_:_:)-1v821.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &>> <Other>(Self, Other) -> Self](int8/&__(_:_:)-24uqw.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<< <Other>(Self, Other) -> Self](int8/&__(_:_:)-2a90q.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &<< (Int8, Int8) -> Int8](int8/&__(_:_:)-4szuk.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &<< (Self, Self) -> Self](int8/&__(_:_:)-7028d.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &>> (Self, Self) -> Self](int8/&__(_:_:)-9x51j.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<<= <Other>(inout Self, Other)](int8/&__=(_:_:)-6g9h1.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &>>= <Other>(inout Self, Other)](int8/&__=(_:_:)-9dar0.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
### Initializers
- [init<T>(T)](int8/init(_:)-7lqol.md)
- [init?(String)](int8/init(_:)-89uu.md)
  Creates a new integer value from the given string.
- [init?<S>(S, radix: Int)](int8/init(_:radix:).md)
  Creates a new integer value from the given string and radix.
- [init(bigEndian: Self)](int8/init(bigendian:).md)
  Creates an integer from its big-endian representation, changing the byte order if necessary.
- [init?<T>(exactly: T)](int8/init(exactly:)-16mcu.md)
- [init(littleEndian: Self)](int8/init(littleendian:).md)
  Creates an integer from its little-endian representation, changing the byte order if necessary.
### Instance Properties
- [var bigEndian: Self](int8/bigendian.md)
  The big-endian representation of this integer.
- [var littleEndian: Self](int8/littleendian.md)
  The little-endian representation of this integer.
### Type Methods
- [static func random(in: Range<Self>) -> Self](int8/random(in:)-2fyvz.md)
  Returns a random value within the specified range.
- [static func random(in: ClosedRange<Self>) -> Self](int8/random(in:)-5kgo1.md)
  Returns a random value within the specified range.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](int8/random(in:using:)-1n6up.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](int8/random(in:using:)-8ennz.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int8/fixedwidthinteger-implementations)*