# BinaryInteger Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Operators
- [static func != <Other>(Self, Other) -> Bool](./noteq%28_,_%29-6i9jj.md)
  Returns a Boolean value indicating whether the two given values are not equal.
- [static func & (UInt32, UInt32) -> UInt32](./amp%28_,_%29.md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func & (Self, Self) -> Self](./amp%28_,_%29-3g9c6.md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func * (UInt32, UInt32) -> UInt32](./star%28_,_%29.md)
  Multiplies two values and produces their product.
- [static func + (UInt32, UInt32) -> UInt32](./plus%28_,_%29.md)
  Adds two values and produces their sum.
- [static func - (UInt32, UInt32) -> UInt32](./minus%28_,_%29.md)
  Subtracts one value from another and produces their difference.
- [static func == <Other>(Self, Other) -> Bool](./eqeq%28_,_%29-6gtla.md)
  Returns a Boolean value indicating whether the two given values are equal.
- [static func | (Self, Self) -> Self](./op%28_,_%29-1zok6.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func ^ (Self, Self) -> Self](./op%28_,_%29-21za9.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func / (UInt32, UInt32) -> UInt32](./op%28_,_%29-544gh.md)
  Returns the quotient of dividing the first value by the second.
- [static func | (UInt32, UInt32) -> UInt32](./op%28_,_%29-5p6yw.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func > (Self, Self) -> Bool](./op%28_,_%29-60hif.md)
- [static func % (UInt32, UInt32) -> UInt32](./op%28_,_%29-6ovdh.md)
  Returns the remainder of dividing the first value by the second.
- [static func < <Other>(Self, Other) -> Bool](./op%28_,_%29-7gl7s.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func ^ (UInt32, UInt32) -> UInt32](./op%28_,_%29-9mox3.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func > <Other>(Self, Other) -> Bool](./op%28_,_%29-ru4w.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func <= (Self, Self) -> Bool](./opeq%28_,_%29-4zprc.md)
- [static func >= <Other>(Self, Other) -> Bool](./opeq%28_,_%29-6655v.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func >= (Self, Self) -> Bool](./opeq%28_,_%29-69qui.md)
- [static func <= <Other>(Self, Other) -> Bool](./opeq%28_,_%29-vr4i.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [static func >> <Other>(Self, Other) -> Self](./opop%28_,_%29-2fuku.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func << <Other>(Self, Other) -> Self](./opop%28_,_%29-63byq.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >> <RHS>(Self, RHS) -> Self](./opop%28_,_%29-8299k.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func << <RHS>(Self, RHS) -> Self](./opop%28_,_%29-8ecom.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >>= <Other>(inout Self, Other)](./opopeq%28_,_%29-2nln1.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the right in the left-hand-side variable.
- [static func <<= <Other>(inout Self, Other)](./opopeq%28_,_%29-9xth9.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint32/binaryinteger-implementations)*