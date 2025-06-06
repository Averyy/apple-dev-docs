# FixedWidthInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func &* (Self, Self) -> Self](uint128/&*(_:_:).md)
  Returns the product of the two given values, wrapping the result in case of any overflow.
- [static func &*= (inout Self, Self)](uint128/&*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &+ (Self, Self) -> Self](uint128/&+(_:_:).md)
  Returns the sum of the two given values, wrapping the result in case of any overflow.
- [static func &+= (inout Self, Self)](uint128/&+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &- (Self, Self) -> Self](uint128/&-(_:_:).md)
  Returns the difference of the two given values, wrapping the result in case of any overflow.
- [static func &-= (inout Self, Self)](uint128/&-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.
- [static func &<< <Other>(Self, Other) -> Self](uint128/&__(_:_:)-6im7h.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &<< (Self, Self) -> Self](uint128/&__(_:_:)-6vbmo.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &>> <Other>(Self, Other) -> Self](uint128/&__(_:_:)-7vshb.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &>> (Self, Self) -> Self](uint128/&__(_:_:)-t1dt.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &>>= (inout UInt128, UInt128)](uint128/&__=(_:_:)-2trlh.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &>>= <Other>(inout Self, Other)](uint128/&__=(_:_:)-7h6z1.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &<<= <Other>(inout Self, Other)](uint128/&__=(_:_:)-c0o3.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &<<= (inout UInt128, UInt128)](uint128/&__=(_:_:)-l1y8.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
### Initializers
- [init<T>(T)](uint128/init(_:)-7l4pg.md)
- [init?(String)](uint128/init(_:)-7reec.md)
  Creates a new integer value from the given string.
- [init?<S>(S, radix: Int)](uint128/init(_:radix:).md)
  Creates a new integer value from the given string and radix.
- [init(bigEndian: Self)](uint128/init(bigendian:).md)
  Creates an integer from its big-endian representation, changing the byte order if necessary.
- [init?<T>(exactly: T)](uint128/init(exactly:)-4u158.md)
- [init(littleEndian: Self)](uint128/init(littleendian:).md)
  Creates an integer from its little-endian representation, changing the byte order if necessary.
### Instance Properties
- [var bigEndian: Self](uint128/bigendian.md)
  The big-endian representation of this integer.
- [var byteSwapped: UInt128](uint128/byteswapped.md)
  A representation of this integer with the byte order swapped.
- [var leadingZeroBitCount: Int](uint128/leadingzerobitcount.md)
  The number of leading zeros in this value’s binary representation.
- [var littleEndian: Self](uint128/littleendian.md)
  The little-endian representation of this integer.
- [var nonzeroBitCount: Int](uint128/nonzerobitcount.md)
  The number of bits equal to 1 in this value’s binary representation.
### Instance Methods
- [func addingReportingOverflow(UInt128) -> (partialValue: UInt128, overflow: Bool)](uint128/addingreportingoverflow(_:).md)
  Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividedReportingOverflow(by: UInt128) -> (partialValue: UInt128, overflow: Bool)](uint128/dividedreportingoverflow(by:).md)
  Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func multipliedFullWidth(by: Self) -> (high: Self, low: Self.Magnitude)](uint128/multipliedfullwidth(by:).md)
  Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [func multipliedReportingOverflow(by: UInt128) -> (partialValue: UInt128, overflow: Bool)](uint128/multipliedreportingoverflow(by:).md)
  Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func remainderReportingOverflow(dividingBy: UInt128) -> (partialValue: UInt128, overflow: Bool)](uint128/remainderreportingoverflow(dividingby:).md)
  Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [func subtractingReportingOverflow(UInt128) -> (partialValue: UInt128, overflow: Bool)](uint128/subtractingreportingoverflow(_:).md)
  Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.
### Type Properties
- [static var bitWidth: Int](uint128/bitwidth.md)
  The number of bits used for the underlying binary representation of values of this type.
- [static var max: UInt128](uint128/max.md)
  The maximum representable integer in this type.
- [static var min: UInt128](uint128/min.md)
  The minimum representable integer in this type.
### Type Methods
- [static func random(in: ClosedRange<Self>) -> Self](uint128/random(in:)-1tk4g.md)
  Returns a random value within the specified range.
- [static func random(in: Range<Self>) -> Self](uint128/random(in:)-6h05w.md)
  Returns a random value within the specified range.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](uint128/random(in:using:)-1acx9.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](uint128/random(in:using:)-535e1.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint128/fixedwidthinteger-implementations)*