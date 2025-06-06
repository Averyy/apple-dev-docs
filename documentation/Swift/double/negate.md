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

The result is always exact. This example uses the `negate()` method to negate the value of the variable `x`:

```swift
var x = 21.5
x.negate()
// x == -21.5
```

## See Also

- [Floating-Point Operators for Double](floating-point-operators-for-double.md)
  Perform arithmetic and bitwise operations or compare values.
- [func addingProduct(Self, Self) -> Self](double/addingproduct(_:_:).md)
  Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [func addProduct(Double, Double)](double/addproduct(_:_:).md)
  Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [func squareRoot() -> Self](double/squareroot.md)
  Returns the square root of the value, rounded to a representable value.
- [func formSquareRoot()](double/formsquareroot.md)
  Replaces this value with its square root, rounded to a representable value.
- [func remainder(dividingBy: Self) -> Self](double/remainder(dividingby:).md)
  Returns the remainder of this value divided by the given value.
- [func formRemainder(dividingBy: Double)](double/formremainder(dividingby:).md)
  Replaces this value with the remainder of itself divided by the given value.
- [func truncatingRemainder(dividingBy: Self) -> Self](double/truncatingremainder(dividingby:).md)
  Returns the remainder of this value divided by the given value using truncating division.
- [func formTruncatingRemainder(dividingBy: Double)](double/formtruncatingremainder(dividingby:).md)
  Replaces this value with the remainder of itself divided by the given value using truncating division.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/negate())*