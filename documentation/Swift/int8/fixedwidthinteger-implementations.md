# FixedWidthInteger Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Operators
- [static func &* (Self, Self) -> Self](./ampstar%28_,_%29.md)
  Returns the product of the two given values, wrapping the result in case of any overflow.
- [static func &*= (inout Self, Self)](./ampstareq%28_,_%29.md)
  Multiplies two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &+ (Self, Self) -> Self](./ampplus%28_,_%29.md)
  Returns the sum of the two given values, wrapping the result in case of any overflow.
- [static func &+= (inout Self, Self)](./amppluseq%28_,_%29.md)
  Adds two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &- (Self, Self) -> Self](./ampminus%28_,_%29.md)
  Returns the difference of the two given values, wrapping the result in case of any overflow.
- [static func &-= (inout Self, Self)](./ampminuseq%28_,_%29.md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.
- [static func &>> (Int8, Int8) -> Int8](./ampopop%28_,_%29-1v821.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &>> <Other>(Self, Other) -> Self](./ampopop%28_,_%29-24uqw.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<< <Other>(Self, Other) -> Self](./ampopop%28_,_%29-2a90q.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &<< (Int8, Int8) -> Int8](./ampopop%28_,_%29-4szuk.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &<< (Self, Self) -> Self](./ampopop%28_,_%29-7028d.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &>> (Self, Self) -> Self](./ampopop%28_,_%29-9x51j.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<<= <Other>(inout Self, Other)](./ampopopeq%28_,_%29-6g9h1.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &>>= <Other>(inout Self, Other)](./ampopopeq%28_,_%29-9dar0.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
### Initializers
- [init<T>(T)](./init%28_%29-7lqol.md)
- [init?(String)](./init%28_%29-89uu.md)
  Creates a new integer value from the given string.
- [init?<S>(S, radix: Int)](./init%28_,radix%29.md)
  Creates a new integer value from the given string and radix.
- [init(bigEndian: Self)](./init%28bigendian%29.md)
  Creates an integer from its big-endian representation, changing the byte order if necessary.
- [init?<T>(exactly: T)](./init%28exactly%29-16mcu.md)
- [init(littleEndian: Self)](./init%28littleendian%29.md)
  Creates an integer from its little-endian representation, changing the byte order if necessary.
### Instance Properties
- [var bigEndian: Self](./bigendian.md)
  The big-endian representation of this integer.
- [var littleEndian: Self](./littleendian.md)
  The little-endian representation of this integer.
### Type Methods
- [static func random(in: Range<Self>) -> Self](./random%28in%29-2fyvz.md)
  Returns a random value within the specified range.
- [static func random(in: ClosedRange<Self>) -> Self](./random%28in%29-5kgo1.md)
  Returns a random value within the specified range.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](./random%28in,using%29-1n6up.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](./random%28in,using%29-8ennz.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int8/fixedwidthinteger-implementations)*