# BinaryInteger Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Operators
- [static func != <Other>(Self, Other) -> Bool](./noteq%28_,_%29-99bok.md)
  Returns a Boolean value indicating whether the two given values are not equal.
- [static func & (UInt8, UInt8) -> UInt8](./amp%28_,_%29.md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func & (Self, Self) -> Self](./amp%28_,_%29-4psmt.md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func * (UInt8, UInt8) -> UInt8](./star%28_,_%29.md)
  Multiplies two values and produces their product.
- [static func + (UInt8, UInt8) -> UInt8](./plus%28_,_%29.md)
  Adds two values and produces their sum.
- [static func - (UInt8, UInt8) -> UInt8](./minus%28_,_%29.md)
  Subtracts one value from another and produces their difference.
- [static func == <Other>(Self, Other) -> Bool](./eqeq%28_,_%29-156b9.md)
  Returns a Boolean value indicating whether the two given values are equal.
- [static func | (UInt8, UInt8) -> UInt8](./op%28_,_%29-17p9c.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func ^ (UInt8, UInt8) -> UInt8](./op%28_,_%29-2kgmz.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func / (UInt8, UInt8) -> UInt8](./op%28_,_%29-327b5.md)
  Returns the quotient of dividing the first value by the second.
- [static func ^ (Self, Self) -> Self](./op%28_,_%29-4eiav.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func < <Other>(Self, Other) -> Bool](./op%28_,_%29-5kmc9.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func > (Self, Self) -> Bool](./op%28_,_%29-6ieix.md)
- [static func > <Other>(Self, Other) -> Bool](./op%28_,_%29-7nbqc.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func | (Self, Self) -> Self](./op%28_,_%29-865lu.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func % (UInt8, UInt8) -> UInt8](./op%28_,_%29-9tmal.md)
  Returns the remainder of dividing the first value by the second.
- [static func <= <Other>(Self, Other) -> Bool](./opeq%28_,_%29-6b690.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [static func <= (Self, Self) -> Bool](./opeq%28_,_%29-7efxq.md)
- [static func >= (Self, Self) -> Bool](./opeq%28_,_%29-8oubr.md)
- [static func >= <Other>(Self, Other) -> Bool](./opeq%28_,_%29-9rm29.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func >> <Other>(Self, Other) -> Self](./opop%28_,_%29-2qqlb.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func >> <RHS>(Self, RHS) -> Self](./opop%28_,_%29-56eg9.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func << <Other>(Self, Other) -> Self](./opop%28_,_%29-7yxgh.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func << <RHS>(Self, RHS) -> Self](./opop%28_,_%29-jtqk.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func <<= <Other>(inout Self, Other)](./opopeq%28_,_%29-1p711.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
- [static func >>= <Other>(inout Self, Other)](./opopeq%28_,_%29-8pj4c.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
- [static func ~ (Self) -> Self](./tilde%28_%29.md)
  Returns the inverse of the bits set in the argument.
### Initializers
- [init()](./init%28%29.md)
  Creates a new value equal to zero.
- [init<Other>(clamping: Other)](./init%28clamping%29.md)
  Creates a new instance with the representable value that’s closest to the given integer.
- [init<T>(truncatingIfNeeded: T)](./init%28truncatingifneeded%29.md)
  Creates a new instance from the bit pattern of the given instance by sign-extending or truncating to fit this type.
### Instance Properties
- [var bitWidth: Int](./bitwidth-swift.property.md)
  The number of bits in the current binary representation of this value.
- [var description: String](./description.md)
  A textual representation of this value.
### Instance Methods
- [func advanced(by: Int) -> Self](./advanced%28by%29.md)
  Returns a value that is offset the specified distance from this value.
- [func distance(to: Self) -> Int](./distance%28to%29.md)
  Returns the distance from this value to the given value, expressed as a stride.
- [func isMultiple(of: Self) -> Bool](./ismultiple%28of%29.md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](./quotientandremainder%28dividingby%29.md)
  Returns the quotient and remainder of this value divided by the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint8/binaryinteger-implementations)*