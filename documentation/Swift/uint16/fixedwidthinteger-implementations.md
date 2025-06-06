# FixedWidthInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func &* (Self, Self) -> Self](uint16/&*(_:_:).md)
  Returns the product of the two given values, wrapping the result in case of any overflow.
- [static func &*= (inout Self, Self)](uint16/&*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &+ (Self, Self) -> Self](uint16/&+(_:_:).md)
  Returns the sum of the two given values, wrapping the result in case of any overflow.
- [static func &+= (inout Self, Self)](uint16/&+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &- (Self, Self) -> Self](uint16/&-(_:_:).md)
  Returns the difference of the two given values, wrapping the result in case of any overflow.
- [static func &-= (inout Self, Self)](uint16/&-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.
- [static func &<< (UInt16, UInt16) -> UInt16](uint16/&__(_:_:)-1s44o.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &<< <Other>(Self, Other) -> Self](uint16/&__(_:_:)-23wlt.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &>> <Other>(Self, Other) -> Self](uint16/&__(_:_:)-4pl2m.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<< (Self, Self) -> Self](uint16/&__(_:_:)-5j3zt.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &>> (Self, Self) -> Self](uint16/&__(_:_:)-6qf3.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &>> (UInt16, UInt16) -> UInt16](uint16/&__(_:_:)-u6vr.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &>>= <Other>(inout Self, Other)](uint16/&__=(_:_:)-4eicd.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &<<= <Other>(inout Self, Other)](uint16/&__=(_:_:)-4iwdg.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
### Initializers
- [init<T>(T)](uint16/init(_:)-5nfkl.md)
- [init?(String)](uint16/init(_:)-6powq.md)
  Creates a new integer value from the given string.
- [init?<S>(S, radix: Int)](uint16/init(_:radix:).md)
  Creates a new integer value from the given string and radix.
- [init(bigEndian: Self)](uint16/init(bigendian:).md)
  Creates an integer from its big-endian representation, changing the byte order if necessary.
- [init?<T>(exactly: T)](uint16/init(exactly:)-8acu7.md)
- [init(littleEndian: Self)](uint16/init(littleendian:).md)
  Creates an integer from its little-endian representation, changing the byte order if necessary.
### Instance Properties
- [var bigEndian: Self](uint16/bigendian.md)
  The big-endian representation of this integer.
- [var littleEndian: Self](uint16/littleendian.md)
  The little-endian representation of this integer.
### Type Methods
- [static func random(in: ClosedRange<Self>) -> Self](uint16/random(in:)-512t7.md)
  Returns a random value within the specified range.
- [static func random(in: Range<Self>) -> Self](uint16/random(in:)-5jx03.md)
  Returns a random value within the specified range.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](uint16/random(in:using:)-7a3q0.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](uint16/random(in:using:)-8uepg.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint16/fixedwidthinteger-implementations)*