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
- [static func &>> (UInt8, UInt8) -> UInt8](./ampopop%28_,_%29-1fquv.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &>> <Other>(Self, Other) -> Self](./ampopop%28_,_%29-3qwyl.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<< (Self, Self) -> Self](./ampopop%28_,_%29-5m6yb.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &<< <Other>(Self, Other) -> Self](./ampopop%28_,_%29-60i6u.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &>> (Self, Self) -> Self](./ampopop%28_,_%29-6jqbr.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<< (UInt8, UInt8) -> UInt8](./ampopop%28_,_%29-7gp0b.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &>>= <Other>(inout Self, Other)](./ampopopeq%28_,_%29-16yhm.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &<<= <Other>(inout Self, Other)](./ampopopeq%28_,_%29-60dw2.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
### Initializers
- [init?(String)](./init%28_%29-1iroc.md)
  Creates a new integer value from the given string.
- [init<T>(T)](./init%28_%29-5e02.md)
- [init?<S>(S, radix: Int)](./init%28_,radix%29.md)
  Creates a new integer value from the given string and radix.
- [init(bigEndian: Self)](./init%28bigendian%29.md)
  Creates an integer from its big-endian representation, changing the byte order if necessary.
- [init?<T>(exactly: T)](./init%28exactly%29-8szg6.md)
- [init(littleEndian: Self)](./init%28littleendian%29.md)
  Creates an integer from its little-endian representation, changing the byte order if necessary.
### Instance Properties
- [var bigEndian: Self](./bigendian.md)
  The big-endian representation of this integer.
- [var littleEndian: Self](./littleendian.md)
  The little-endian representation of this integer.
### Type Methods
- [static func random(in: Range<Self>) -> Self](./random%28in%29-6wnz5.md)
  Returns a random value within the specified range.
- [static func random(in: ClosedRange<Self>) -> Self](./random%28in%29-85h4o.md)
  Returns a random value within the specified range.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](./random%28in,using%29-3zjsj.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](./random%28in,using%29-6l2z5.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint8/fixedwidthinteger-implementations)*