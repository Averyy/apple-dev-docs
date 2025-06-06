# BinaryInteger Implementations

**Framework**: Swift

## Topics

### Operators
- [static func != <Other>(Self, Other) -> Bool](int16/!=(_:_:)-35jaq.md)
  Returns a Boolean value indicating whether the two given values are not equal.
- [static func & (Int16, Int16) -> Int16](int16/&(_:_:).md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func & (Self, Self) -> Self](int16/&(_:_:)-11qqq.md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func * (Int16, Int16) -> Int16](int16/*(_:_:).md)
  Multiplies two values and produces their product.
- [static func + (Int16, Int16) -> Int16](int16/+(_:_:).md)
  Adds two values and produces their sum.
- [static func - (Int16, Int16) -> Int16](int16/-(_:_:).md)
  Subtracts one value from another and produces their difference.
- [static func == <Other>(Self, Other) -> Bool](int16/==(_:_:)-1ntek.md)
  Returns a Boolean value indicating whether the two given values are equal.
- [static func ^ (Self, Self) -> Self](int16/_(_:_:)-2n4zk.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func % (Int16, Int16) -> Int16](int16/_(_:_:)-412im.md)
  Returns the remainder of dividing the first value by the second.
- [static func > <Other>(Self, Other) -> Bool](int16/_(_:_:)-4d8dd.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func | (Self, Self) -> Self](int16/_(_:_:)-5s4nw.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func ^ (Int16, Int16) -> Int16](int16/_(_:_:)-5yszf.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func < <Other>(Self, Other) -> Bool](int16/_(_:_:)-6e2wc.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func | (Int16, Int16) -> Int16](int16/_(_:_:)-6tyn.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func > (Self, Self) -> Bool](int16/_(_:_:)-93553.md)
- [static func / (Int16, Int16) -> Int16](int16/_(_:_:)-kd81.md)
  Returns the quotient of dividing the first value by the second.
- [static func <= <Other>(Self, Other) -> Bool](int16/_=(_:_:)-1hfy3.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [static func >= (Self, Self) -> Bool](int16/_=(_:_:)-3c0fc.md)
- [static func <= (Self, Self) -> Bool](int16/_=(_:_:)-4hrh6.md)
- [static func >= <Other>(Self, Other) -> Bool](int16/_=(_:_:)-808tq.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func << <Other>(Self, Other) -> Self](int16/__(_:_:)-1zwhf.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >> <RHS>(Self, RHS) -> Self](int16/__(_:_:)-2ve4s.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func >> <Other>(Self, Other) -> Self](int16/__(_:_:)-64bg6.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func << <RHS>(Self, RHS) -> Self](int16/__(_:_:)-70yoj.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >>= <Other>(inout Self, Other)](int16/__=(_:_:)-1hmwr.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
- [static func <<= <Other>(inout Self, Other)](int16/__=(_:_:)-88k9n.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
- [static func ~ (Self) -> Self](int16/~(_:).md)
  Returns the inverse of the bits set in the argument.
### Initializers
- [init()](int16/init.md)
  Creates a new value equal to zero.
- [init<Other>(clamping: Other)](int16/init(clamping:).md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<T>(truncatingIfNeeded: T)](int16/init(truncatingifneeded:).md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
### Instance Properties
- [var bitWidth: Int](int16/bitwidth-swift.property.md)
  The number of bits in the current binary representation of this value.
- [var description: String](int16/description.md)
  A textual representation of this value.
### Instance Methods
- [func advanced(by: Int) -> Self](int16/advanced(by:).md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Self) -> Int](int16/distance(to:).md)
  Returns the distance from this value to the given value, expressed as a stride.
- [func isMultiple(of: Self) -> Bool](int16/ismultiple(of:).md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](int16/quotientandremainder(dividingby:).md)
  Returns the quotient and remainder of this value divided by the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int16/binaryinteger-implementations)*