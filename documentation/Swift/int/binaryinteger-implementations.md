# BinaryInteger Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Operators
- [static func != <Other>(Self, Other) -> Bool](./noteq%28_,_%29-4jphg.md)
  Returns a Boolean value indicating whether the two given values are not equal.
- [static func & (Int, Int) -> Int](./amp%28_,_%29.md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func & (Self, Self) -> Self](./amp%28_,_%29-1gv8r.md)
  Returns the result of performing a bitwise AND operation on the two given values.
- [static func * (Int, Int) -> Int](./star%28_,_%29.md)
  Multiplies two values and produces their product.
- [static func + (Int, Int) -> Int](./plus%28_,_%29.md)
  Adds two values and produces their sum.
- [static func - (Int, Int) -> Int](./minus%28_,_%29.md)
  Subtracts one value from another and produces their difference.
- [static func == <Other>(Self, Other) -> Bool](./eqeq%28_,_%29-1zalu.md)
  Returns a Boolean value indicating whether the two given values are equal.
- [static func | (Self, Self) -> Self](./op%28_,_%29-1e0ee.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func | (Int, Int) -> Int](./op%28_,_%29-26x3w.md)
  Returns the result of performing a bitwise OR operation on the two given values.
- [static func ^ (Self, Self) -> Self](./op%28_,_%29-2yuui.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func < <Other>(Self, Other) -> Bool](./op%28_,_%29-3r70c.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func > (Self, Self) -> Bool](./op%28_,_%29-4e53i.md)
- [static func ^ (Int, Int) -> Int](./op%28_,_%29-591r5.md)
  Returns the result of performing a bitwise XOR operation on the two given values.
- [static func % (Int, Int) -> Int](./op%28_,_%29-6lyj3.md)
  Returns the remainder of dividing the first value by the second.
- [static func > <Other>(Self, Other) -> Bool](./op%28_,_%29-7d57p.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func / (Int, Int) -> Int](./op%28_,_%29-7j9bj.md)
  Returns the quotient of dividing the first value by the second.
- [static func <= (Self, Self) -> Bool](./opeq%28_,_%29-6cfca.md)
- [static func >= (Self, Self) -> Bool](./opeq%28_,_%29-7tmrx.md)
- [static func >= <Other>(Self, Other) -> Bool](./opeq%28_,_%29-7v58y.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
- [static func <= <Other>(Self, Other) -> Bool](./opeq%28_,_%29-yera.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [static func << <RHS>(Self, RHS) -> Self](./opop%28_,_%29-2xfjq.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func << <Other>(Self, Other) -> Self](./opop%28_,_%29-60q97.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the left.
- [static func >> <Other>(Self, Other) -> Self](./opop%28_,_%29-635pg.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func >> <RHS>(Self, RHS) -> Self](./opop%28_,_%29-97tkh.md)
  Returns the result of shifting a value’s binary representation the specified number of digits to the right.
- [static func <<= <Other>(inout Self, Other)](./opopeq%28_,_%29-66xgb.md)
  Stores the result of shifting a value’s binary representation the specified number of digits to the left in the left-hand-side variable.
- [static func >>= <Other>(inout Self, Other)](./opopeq%28_,_%29-9p0ct.md)
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
- [func isMultiple(of: Self) -> Bool](./ismultiple%28of%29.md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](./quotientandremainder%28dividingby%29.md)
  Returns the quotient and remainder of this value divided by the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/binaryinteger-implementations)*