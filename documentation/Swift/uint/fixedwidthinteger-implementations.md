# FixedWidthInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func &* (Self, Self) -> Self](uint/&*(_:_:).md)
  Returns the product of the two given values, wrapping the result in case of any overflow.
- [static func &*= (inout Self, Self)](uint/&*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &+ (Self, Self) -> Self](uint/&+(_:_:).md)
  Returns the sum of the two given values, wrapping the result in case of any overflow.
- [static func &+= (inout Self, Self)](uint/&+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &- (Self, Self) -> Self](uint/&-(_:_:).md)
  Returns the difference of the two given values, wrapping the result in case of any overflow.
- [static func &-= (inout Self, Self)](uint/&-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.
- [static func &<< (Self, Self) -> Self](uint/&__(_:_:)-2kxq1.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &<< (UInt, UInt) -> UInt](uint/&__(_:_:)-4xvpf.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &>> (Self, Self) -> Self](uint/&__(_:_:)-5zh57.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &>> <Other>(Self, Other) -> Self](uint/&__(_:_:)-76nen.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &>> (UInt, UInt) -> UInt](uint/&__(_:_:)-83cmc.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<< <Other>(Self, Other) -> Self](uint/&__(_:_:)-vou2.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &<<= <Other>(inout Self, Other)](uint/&__=(_:_:)-13mjf.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &>>= <Other>(inout Self, Other)](uint/&__=(_:_:)-704vn.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
### Initializers
- [init?(String)](uint/init(_:)-2hmhy.md)
  Creates a new integer value from the given string.
- [init<T>(T)](uint/init(_:)-6gt9n.md)
- [init?<S>(S, radix: Int)](uint/init(_:radix:).md)
  Creates a new integer value from the given string and radix.
- [init(bigEndian: Self)](uint/init(bigendian:).md)
  Creates an integer from its big-endian representation, changing the byte order if necessary.
- [init?<T>(exactly: T)](uint/init(exactly:)-7yhn2.md)
- [init(littleEndian: Self)](uint/init(littleendian:).md)
  Creates an integer from its little-endian representation, changing the byte order if necessary.
### Instance Properties
- [var bigEndian: Self](uint/bigendian.md)
  The big-endian representation of this integer.
- [var littleEndian: Self](uint/littleendian.md)
  The little-endian representation of this integer.
### Type Methods
- [static func random(in: ClosedRange<Self>) -> Self](uint/random(in:)-8zzqt.md)
  Returns a random value within the specified range.
- [static func random(in: Range<Self>) -> Self](uint/random(in:)-9mjpk.md)
  Returns a random value within the specified range.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](uint/random(in:using:)-3dwvw.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](uint/random(in:using:)-4lsb1.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint/fixedwidthinteger-implementations)*