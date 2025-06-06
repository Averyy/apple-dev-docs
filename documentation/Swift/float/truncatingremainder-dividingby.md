# truncatingRemainder(dividingBy:)

**Framework**: Swift  
**Kind**: method

Returns the remainder of this value divided by the given value using truncating division.

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
func truncatingRemainder(dividingBy other: Self) -> Self
```

#### Return Value

The remainder of this value divided by `other` using truncating division.

#### Discussion

Performing truncating division with floating-point values results in a truncated integer quotient and a remainder. For values `x` and `y` and their truncated integer quotient `q`, the remainder `r` satisfies `x == y * q + r`.

The following example calculates the truncating remainder of dividing 8.625 by 0.75:

```swift
let x = 8.625
print(x / 0.75)
// Prints "11.5"

let q = (x / 0.75).rounded(.towardZero)
// q == 11.0
let r = x.truncatingRemainder(dividingBy: 0.75)
// r == 0.375

let x1 = 0.75 * q + r
// x1 == 8.625
```

If this value and `other` are both finite numbers, the truncating remainder has the same sign as this value and is strictly smaller in magnitude than `other`. The `truncatingRemainder(dividingBy:)` method is always exact.

## Parameters

- `other`: The value to use when dividing this value.

## See Also

- [Floating-Point Operators for Float](floating-point-operators-for-float.md)
  Perform arithmetic and bitwise operations or compare values.
- [func addingProduct(Self, Self) -> Self](float/addingproduct(_:_:).md)
  Returns the result of adding the product of the two given values to this value, computed without intermediate rounding.
- [func addProduct(Float, Float)](float/addproduct(_:_:).md)
  Adds the product of the two given values to this value in place, computed without intermediate rounding.
- [func squareRoot() -> Self](float/squareroot.md)
  Returns the square root of the value, rounded to a representable value.
- [func formSquareRoot()](float/formsquareroot.md)
  Replaces this value with its square root, rounded to a representable value.
- [func remainder(dividingBy: Self) -> Self](float/remainder(dividingby:).md)
  Returns the remainder of this value divided by the given value.
- [func formRemainder(dividingBy: Float)](float/formremainder(dividingby:).md)
  Replaces this value with the remainder of itself divided by the given value.
- [func formTruncatingRemainder(dividingBy: Float)](float/formtruncatingremainder(dividingby:).md)
  Replaces this value with the remainder of itself divided by the given value using truncating division.
- [func negate()](float/negate.md)
  Replaces this value with its additive inverse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/truncatingremainder(dividingby:))*