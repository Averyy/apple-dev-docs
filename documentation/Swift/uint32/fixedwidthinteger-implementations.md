# FixedWidthInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func &* (Self, Self) -> Self](uint32/&*(_:_:).md)
  Returns the product of the two given values, wrapping the result in case of any overflow.
- [static func &*= (inout Self, Self)](uint32/&*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &+ (Self, Self) -> Self](uint32/&+(_:_:).md)
  Returns the sum of the two given values, wrapping the result in case of any overflow.
- [static func &+= (inout Self, Self)](uint32/&+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &- (Self, Self) -> Self](uint32/&-(_:_:).md)
  Returns the difference of the two given values, wrapping the result in case of any overflow.
- [static func &-= (inout Self, Self)](uint32/&-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.
- [static func &<< <Other>(Self, Other) -> Self](uint32/&__(_:_:)-2b50j.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &>> <Other>(Self, Other) -> Self](uint32/&__(_:_:)-4icck.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<< (Self, Self) -> Self](uint32/&__(_:_:)-5qjx7.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &<< (UInt32, UInt32) -> UInt32](uint32/&__(_:_:)-6boh2.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &>> (UInt32, UInt32) -> UInt32](uint32/&__(_:_:)-6cy2r.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &>> (Self, Self) -> Self](uint32/&__(_:_:)-bol.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &>>= <Other>(inout Self, Other)](uint32/&__=(_:_:)-477ef.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &<<= <Other>(inout Self, Other)](uint32/&__=(_:_:)-4p3qm.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
### Initializers
- [init<T>(T)](uint32/init(_:)-5tue7.md)
- [init?(String)](uint32/init(_:)-6w6ag.md)
  Creates a new integer value from the given string.
- [init?<S>(S, radix: Int)](uint32/init(_:radix:).md)
  Creates a new integer value from the given string and radix.
- [init(bigEndian: Self)](uint32/init(bigendian:).md)
  Creates an integer from its big-endian representation, changing the byte order if necessary.
- [init?<T>(exactly: T)](uint32/init(exactly:)-8348l.md)
- [init(littleEndian: Self)](uint32/init(littleendian:).md)
  Creates an integer from its little-endian representation, changing the byte order if necessary.
### Instance Properties
- [var bigEndian: Self](uint32/bigendian.md)
  The big-endian representation of this integer.
- [var littleEndian: Self](uint32/littleendian.md)
  The little-endian representation of this integer.
### Type Methods
- [static func random(in: ClosedRange<Self>) -> Self](uint32/random(in:)-58bdl.md)
  Returns a random value within the specified range.
- [static func random(in: Range<Self>) -> Self](uint32/random(in:)-5r5dt.md)
  Returns a random value within the specified range.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](uint32/random(in:using:)-7gifu.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](uint32/random(in:using:)-91wzi.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint32/fixedwidthinteger-implementations)*