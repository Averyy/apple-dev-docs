# FixedWidthInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func &* (Self, Self) -> Self](int16/&*(_:_:).md)
  Returns the product of the two given values, wrapping the result in case of any overflow.
- [static func &*= (inout Self, Self)](int16/&*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &+ (Self, Self) -> Self](int16/&+(_:_:).md)
  Returns the sum of the two given values, wrapping the result in case of any overflow.
- [static func &+= (inout Self, Self)](int16/&+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &- (Self, Self) -> Self](int16/&-(_:_:).md)
  Returns the difference of the two given values, wrapping the result in case of any overflow.
- [static func &-= (inout Self, Self)](int16/&-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.
- [static func &<< (Int16, Int16) -> Int16](int16/&__(_:_:)-11whl.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &<< <Other>(Self, Other) -> Self](int16/&__(_:_:)-177cn.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &>> <Other>(Self, Other) -> Self](int16/&__(_:_:)-2vu0k.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &>> (Self, Self) -> Self](int16/&__(_:_:)-5kz3z.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<< (Self, Self) -> Self](int16/&__(_:_:)-6669c.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &>> (Int16, Int16) -> Int16](int16/&__(_:_:)-8zhel.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<<= <Other>(inout Self, Other)](int16/&__=(_:_:)-1cj5m.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &>>= <Other>(inout Self, Other)](int16/&__=(_:_:)-7px1u.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
### Initializers
- [init?(String)](int16/init(_:)-733m5.md)
  Creates a new integer value from the given string.
- [init<T>(T)](int16/init(_:)-90imc.md)
- [init?<S>(S, radix: Int)](int16/init(_:radix:).md)
  Creates a new integer value from the given string and radix.
- [init(bigEndian: Self)](int16/init(bigendian:).md)
  Creates an integer from its big-endian representation, changing the byte order if necessary.
- [init?<T>(exactly: T)](int16/init(exactly:)-71m8j.md)
- [init(littleEndian: Self)](int16/init(littleendian:).md)
  Creates an integer from its little-endian representation, changing the byte order if necessary.
### Instance Properties
- [var bigEndian: Self](int16/bigendian.md)
  The big-endian representation of this integer.
- [var littleEndian: Self](int16/littleendian.md)
  The little-endian representation of this integer.
### Type Methods
- [static func random(in: Range<Self>) -> Self](int16/random(in:)-3zzix.md)
  Returns a random value within the specified range.
- [static func random(in: ClosedRange<Self>) -> Self](int16/random(in:)-4qzm1.md)
  Returns a random value within the specified range.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](int16/random(in:using:)-25p6v.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](int16/random(in:using:)-m203.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int16/fixedwidthinteger-implementations)*