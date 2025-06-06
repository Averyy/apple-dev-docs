# addingProduct(_:_:)

**Framework**: Swift  
**Kind**: method

Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.

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
func addingProduct(_ lhs: Self, _ rhs: Self) -> Self
```

#### Return Value

The product of `lhs` and `rhs`, added to this value.

#### Discussion

This method is equivalent to the C `fma` function and implements the `fusedMultiplyAdd` operation defined by the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `lhs`: One of the values to multiply before adding to this value.
- `rhs`: The other value to multiply.

## See Also

- [Floating-Point Operators for Double](floating-point-operators-for-double.md)
  Perform arithmetic and bitwise operations or compare values.
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
- [func negate()](double/negate.md)
  Replaces this value with its additive inverse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/addingproduct(_:_:))*