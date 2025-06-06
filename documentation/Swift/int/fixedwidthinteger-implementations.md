# FixedWidthInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func &* (Self, Self) -> Self](int/&*(_:_:).md)
  Returns the product of the two given values, wrapping the result in case of any overflow.
- [static func &*= (inout Self, Self)](int/&*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &+ (Self, Self) -> Self](int/&+(_:_:).md)
  Returns the sum of the two given values, wrapping the result in case of any overflow.
- [static func &+= (inout Self, Self)](int/&+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &- (Self, Self) -> Self](int/&-(_:_:).md)
  Returns the difference of the two given values, wrapping the result in case of any overflow.
- [static func &-= (inout Self, Self)](int/&-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.
- [static func &<< (Self, Self) -> Self](int/&__(_:_:)-2kxph.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &>> (Int, Int) -> Int](int/&__(_:_:)-35o0c.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<< (Int, Int) -> Int](int/&__(_:_:)-3euzz.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &>> (Self, Self) -> Self](int/&__(_:_:)-5zh5j.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &>> <Other>(Self, Other) -> Self](int/&__(_:_:)-76ndv.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<< <Other>(Self, Other) -> Self](int/&__(_:_:)-voti.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &<<= <Other>(inout Self, Other)](int/&__=(_:_:)-13miv.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &>>= <Other>(inout Self, Other)](int/&__=(_:_:)-704vj.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
### Initializers
- [init?(String)](int/init(_:)-2hmii.md)
  Creates a new integer value from the given string.
- [init<T>(T)](int/init(_:)-6gt9z.md)
- [init?<S>(S, radix: Int)](int/init(_:radix:).md)
  Creates a new integer value from the given string and radix.
- [init(bigEndian: Self)](int/init(bigendian:).md)
  Creates an integer from its big-endian representation, changing the byte order if necessary.
- [init?<T>(exactly: T)](int/init(exactly:)-7yhn6.md)
- [init(littleEndian: Self)](int/init(littleendian:).md)
  Creates an integer from its little-endian representation, changing the byte order if necessary.
### Instance Properties
- [var bigEndian: Self](int/bigendian.md)
  The big-endian representation of this integer.
- [var littleEndian: Self](int/littleendian.md)
  The little-endian representation of this integer.
### Type Methods
- [static func random(in: ClosedRange<Self>) -> Self](int/random(in:)-8zzqh.md)
  Returns a random value within the specified range.
- [static func random(in: Range<Self>) -> Self](int/random(in:)-9mjpw.md)
  Returns a random value within the specified range.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](int/random(in:using:)-3dwv4.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](int/random(in:using:)-4lsb5.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/fixedwidthinteger-implementations)*