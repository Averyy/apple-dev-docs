# FixedWidthInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func &* (Self, Self) -> Self](int32/&*(_:_:).md)
  Returns the product of the two given values, wrapping the result in case of any overflow.
- [static func &*= (inout Self, Self)](int32/&*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &+ (Self, Self) -> Self](int32/&+(_:_:).md)
  Returns the sum of the two given values, wrapping the result in case of any overflow.
- [static func &+= (inout Self, Self)](int32/&+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &- (Self, Self) -> Self](int32/&-(_:_:).md)
  Returns the difference of the two given values, wrapping the result in case of any overflow.
- [static func &-= (inout Self, Self)](int32/&-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.
- [static func &<< <Other>(Self, Other) -> Self](int32/&__(_:_:)-1djlp.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &>> <Other>(Self, Other) -> Self](int32/&__(_:_:)-2odv2.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &>> (Self, Self) -> Self](int32/&__(_:_:)-5dixx.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<< (Self, Self) -> Self](int32/&__(_:_:)-6cb7m.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &>> (Int32, Int32) -> Int32](int32/&__(_:_:)-7sh72.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<< (Int32, Int32) -> Int32](int32/&__(_:_:)-98mep.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &<<= <Other>(inout Self, Other)](int32/&__=(_:_:)-1642g.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &>>= <Other>(inout Self, Other)](int32/&__=(_:_:)-7weao.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
### Initializers
- [init?(String)](int32/init(_:)-6wz3b.md)
  Creates a new integer value from the given string.
- [init<T>(T)](int32/init(_:)-97yta.md)
- [init?<S>(S, radix: Int)](int32/init(_:radix:).md)
  Creates a new integer value from the given string and radix.
- [init(bigEndian: Self)](int32/init(bigendian:).md)
  Creates an integer from its big-endian representation, changing the byte order if necessary.
- [init?<T>(exactly: T)](int32/init(exactly:)-77qpt.md)
- [init(littleEndian: Self)](int32/init(littleendian:).md)
  Creates an integer from its little-endian representation, changing the byte order if necessary.
### Instance Properties
- [var bigEndian: Self](int32/bigendian.md)
  The big-endian representation of this integer.
- [var littleEndian: Self](int32/littleendian.md)
  The little-endian representation of this integer.
### Type Methods
- [static func random(in: Range<Self>) -> Self](int32/random(in:)-47fh7.md)
  Returns a random value within the specified range.
- [static func random(in: ClosedRange<Self>) -> Self](int32/random(in:)-4xbuz.md)
  Returns a random value within the specified range.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](int32/random(in:using:)-2c18d.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](int32/random(in:using:)-thxt.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int32/fixedwidthinteger-implementations)*