# negate()

**Framework**: Swift  
**Kind**: method

Replaces this value with its additive inverse.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func negate()
```

#### Discussion

The following example uses the `negate()` method to negate the value of an integer `x`:

```swift
var x = 21
x.negate()
// x == -21
```

The resulting value must be representable within the value’s type. In particular, negating a signed, fixed-width integer type’s minimum results in a value that cannot be represented.

```swift
var y = Int8.min
y.negate()
// Overflow error
```

## See Also

- [Integer Operators](integer-operators.md)
  Perform arithmetic and bitwise operations or compare values.
- [func quotientAndRemainder(dividingBy: Self) -> (quotient: Self, remainder: Self)](int/quotientandremainder(dividingby:).md)
  Returns the quotient and remainder of this value divided by the given value.
- [func isMultiple(of: Self) -> Bool](int/ismultiple(of:).md)
  Returns `true` if this value is a multiple of the given value, and `false` otherwise.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/negate())*