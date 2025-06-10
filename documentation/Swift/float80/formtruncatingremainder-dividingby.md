# formTruncatingRemainder(dividingBy:)

**Framework**: Swift  
**Kind**: method

Replaces this value with the remainder of itself divided by the given value using truncating division.

**Availability**:
- macOS 10.10+

## Declaration

```swift
mutating func formTruncatingRemainder(dividingBy other: Float80)
```

#### Discussion

Performing truncating division with floating-point values results in a truncated integer quotient and a remainder. For values `x` and `y` and their truncated integer quotient `q`, the remainder `r` satisfies `x == y * q + r`.

The following example calculates the truncating remainder of dividing 8.625 by 0.75:

```swift
var x = 8.625
print(x / 0.75)
// Prints "11.5"

let q = (x / 0.75).rounded(.towardZero)
// q == 11.0
x.formTruncatingRemainder(dividingBy: 0.75)
// x == 0.375

let x1 = 0.75 * q + x
// x1 == 8.625
```

If this value and `other` are both finite numbers, the truncating remainder has the same sign as this value and is strictly smaller in magnitude than `other`. The `formTruncatingRemainder(dividingBy:)` method is always exact.

## Parameters

- `other`: The value to use when dividing this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/formtruncatingremainder(dividingby:))*