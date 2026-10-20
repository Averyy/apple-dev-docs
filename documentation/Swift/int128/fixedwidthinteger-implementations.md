# FixedWidthInteger Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Operators
- [static func &* (Int128, Int128) -> Int128](./ampstar%28_,_%29.md)
  Returns the product of the two given values, wrapping the result in case of any overflow.
- [static func &* (Self, Self) -> Self](./ampstar%28_,_%29-ctty.md)
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
- [static func &>> <Other>(Self, Other) -> Self](./ampopop%28_,_%29-227qu.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &>> (Self, Self) -> Self](./ampopop%28_,_%29-71ih1.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<< <Other>(Self, Other) -> Self](./ampopop%28_,_%29-9gig.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &<< (Self, Self) -> Self](./ampopop%28_,_%29-lkqj.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &<<= <Other>(inout Self, Other)](./ampopopeq%28_,_%29-1pdlg.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &<<= (inout Int128, Int128)](./ampopopeq%28_,_%29-2vr5o.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &>>= <Other>(inout Self, Other)](./ampopopeq%28_,_%29-5pnjk.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &>>= (inout Int128, Int128)](./ampopopeq%28_,_%29-69tya.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
### Initializers
- [init<T>(T)](./init%28_%29-3gl5w.md)
- [init?(String)](./init%28_%29-9xe9j.md)
  Creates a new integer value from the given string.
- [init?<S>(S, radix: Int)](./init%28_,radix%29.md)
  Creates a new integer value from the given string and radix.
- [init(bigEndian: Self)](./init%28bigendian%29.md)
  Creates an integer from its big-endian representation, changing the byte order if necessary.
- [init?<T>(exactly: T)](./init%28exactly%29-yans.md)
- [init(littleEndian: Self)](./init%28littleendian%29.md)
  Creates an integer from its little-endian representation, changing the byte order if necessary.
### Instance Properties
- [var bigEndian: Self](./bigendian.md)
  The big-endian representation of this integer.
- [var byteSwapped: Int128](./byteswapped.md)
  A representation of this integer with the byte order swapped.
- [var leadingZeroBitCount: Int](./leadingzerobitcount.md)
  The number of leading zeros in this value’s binary representation.
- [var littleEndian: Self](./littleendian.md)
  The little-endian representation of this integer.
- [var nonzeroBitCount: Int](./nonzerobitcount.md)
  The number of bits equal to 1 in this value’s binary representation.
### Instance Methods
- [func addingReportingOverflow(Int128) -> (partialValue: Int128, overflow: Bool)](./addingreportingoverflow%28_%29.md)
  Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividedReportingOverflow(by: Int128) -> (partialValue: Int128, overflow: Bool)](./dividedreportingoverflow%28by%29.md)
  Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func multipliedFullWidth(by: Self) -> (high: Self, low: Self.Magnitude)](./multipliedfullwidth%28by%29.md)
  Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [func multipliedReportingOverflow(by: Int128) -> (partialValue: Int128, overflow: Bool)](./multipliedreportingoverflow%28by%29.md)
  Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func remainderReportingOverflow(dividingBy: Int128) -> (partialValue: Int128, overflow: Bool)](./remainderreportingoverflow%28dividingby%29.md)
  Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [func subtractingReportingOverflow(Int128) -> (partialValue: Int128, overflow: Bool)](./subtractingreportingoverflow%28_%29.md)
  Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.
### Type Properties
- [static var bitWidth: Int](./bitwidth.md)
  The number of bits used for the underlying binary representation of values of this type.
- [static var max: Int128](./max.md)
  The maximum representable integer in this type.
- [static var min: Int128](./min.md)
  The minimum representable integer in this type.
### Type Methods
- [static func random(in: Range<Self>) -> Self](./random%28in%29-4lf3w.md)
  Returns a random value within the specified range.
- [static func random(in: ClosedRange<Self>) -> Self](./random%28in%29-55a79.md)
  Returns a random value within the specified range.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](./random%28in,using%29-4e4vx.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](./random%28in,using%29-7t428.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int128/fixedwidthinteger-implementations)*