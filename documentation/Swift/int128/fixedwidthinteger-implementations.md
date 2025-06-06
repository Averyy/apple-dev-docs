# FixedWidthInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func &* (Int128, Int128) -> Int128](int128/&*(_:_:).md)
  Returns the product of the two given values, wrapping the result in case of any overflow.
- [static func &* (Self, Self) -> Self](int128/&*(_:_:)-ctty.md)
  Returns the product of the two given values, wrapping the result in case of any overflow.
- [static func &*= (inout Self, Self)](int128/&*=(_:_:).md)
  Multiplies two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &+ (Self, Self) -> Self](int128/&+(_:_:).md)
  Returns the sum of the two given values, wrapping the result in case of any overflow.
- [static func &+= (inout Self, Self)](int128/&+=(_:_:).md)
  Adds two values and stores the result in the left-hand-side variable, wrapping any overflow.
- [static func &- (Self, Self) -> Self](int128/&-(_:_:).md)
  Returns the difference of the two given values, wrapping the result in case of any overflow.
- [static func &-= (inout Self, Self)](int128/&-=(_:_:).md)
  Subtracts the second value from the first and stores the difference in the left-hand-side variable, wrapping any overflow.
- [static func &>> <Other>(Self, Other) -> Self](int128/&__(_:_:)-227qu.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &>> (Self, Self) -> Self](int128/&__(_:_:)-71ih1.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width.
- [static func &<< <Other>(Self, Other) -> Self](int128/&__(_:_:)-9gig.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &<< (Self, Self) -> Self](int128/&__(_:_:)-lkqj.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width.
- [static func &<<= <Other>(inout Self, Other)](int128/&__=(_:_:)-1pdlg.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &<<= (inout Int128, Int128)](int128/&__=(_:_:)-2vr5o.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &>>= <Other>(inout Self, Other)](int128/&__=(_:_:)-5pnjk.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
- [static func &>>= (inout Int128, Int128)](int128/&__=(_:_:)-69tya.md)
  Calculates the result of shifting a value’s binary representation the specified number of digits to the right, masking the shift amount to the type’s bit width, and stores the result in the left-hand-side variable.
### Initializers
- [init<T>(T)](int128/init(_:)-3gl5w.md)
- [init?(String)](int128/init(_:)-9xe9j.md)
  Creates a new integer value from the given string.
- [init?<S>(S, radix: Int)](int128/init(_:radix:).md)
  Creates a new integer value from the given string and radix.
- [init(bigEndian: Self)](int128/init(bigendian:).md)
  Creates an integer from its big-endian representation, changing the byte order if necessary.
- [init?<T>(exactly: T)](int128/init(exactly:)-yans.md)
- [init(littleEndian: Self)](int128/init(littleendian:).md)
  Creates an integer from its little-endian representation, changing the byte order if necessary.
### Instance Properties
- [var bigEndian: Self](int128/bigendian.md)
  The big-endian representation of this integer.
- [var byteSwapped: Int128](int128/byteswapped.md)
  A representation of this integer with the byte order swapped.
- [var leadingZeroBitCount: Int](int128/leadingzerobitcount.md)
  The number of leading zeros in this value’s binary representation.
- [var littleEndian: Self](int128/littleendian.md)
  The little-endian representation of this integer.
- [var nonzeroBitCount: Int](int128/nonzerobitcount.md)
  The number of bits equal to 1 in this value’s binary representation.
### Instance Methods
- [func addingReportingOverflow(Int128) -> (partialValue: Int128, overflow: Bool)](int128/addingreportingoverflow(_:).md)
  Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func dividedReportingOverflow(by: Int128) -> (partialValue: Int128, overflow: Bool)](int128/dividedreportingoverflow(by:).md)
  Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func multipliedFullWidth(by: Self) -> (high: Self, low: Self.Magnitude)](int128/multipliedfullwidth(by:).md)
  Returns a tuple containing the high and low parts of the result of multiplying this value by the given value.
- [func multipliedReportingOverflow(by: Int128) -> (partialValue: Int128, overflow: Bool)](int128/multipliedreportingoverflow(by:).md)
  Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [func remainderReportingOverflow(dividingBy: Int128) -> (partialValue: Int128, overflow: Bool)](int128/remainderreportingoverflow(dividingby:).md)
  Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.
- [func subtractingReportingOverflow(Int128) -> (partialValue: Int128, overflow: Bool)](int128/subtractingreportingoverflow(_:).md)
  Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.
### Type Properties
- [static var bitWidth: Int](int128/bitwidth.md)
  The number of bits used for the underlying binary representation of values of this type.
- [static var max: Int128](int128/max.md)
  The maximum representable integer in this type.
- [static var min: Int128](int128/min.md)
  The minimum representable integer in this type.
### Type Methods
- [static func random(in: Range<Self>) -> Self](int128/random(in:)-4lf3w.md)
  Returns a random value within the specified range.
- [static func random(in: ClosedRange<Self>) -> Self](int128/random(in:)-55a79.md)
  Returns a random value within the specified range.
- [static func random<T>(in: ClosedRange<Self>, using: inout T) -> Self](int128/random(in:using:)-4e4vx.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.
- [static func random<T>(in: Range<Self>, using: inout T) -> Self](int128/random(in:using:)-7t428.md)
  Returns a random value within the specified range, using the given generator as a source for randomness.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int128/fixedwidthinteger-implementations)*