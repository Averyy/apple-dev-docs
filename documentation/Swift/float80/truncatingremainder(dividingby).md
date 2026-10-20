# truncatingRemainder(dividingBy:)

**Framework**: Swift  
**Kind**: method

Returns the remainder of this value divided by the given value using truncating division.

**Availability**:
- macOS 10.10+

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/truncatingremainder(dividingby:))*