# remainder(dividingBy:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Returns the remainder of this value divided by the given value.

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
func remainder(dividingBy other: Self) -> Self
```

#### Return Value

The remainder of this value divided by `other`.

#### Discussion

For two finite values `x` and `y`, the remainder `r` of dividing `x` by `y` satisfies `x == y * q + r`, where `q` is the integer nearest to `x / y`. If `x / y` is exactly halfway between two integers, `q` is chosen to be even. Note that `q` is  `x / y` computed in floating-point arithmetic, and that `q` may not be representable in any available integer type.

The following example calculates the remainder of dividing 8.625 by 0.75:

```swift
let x = 8.625
print(x / 0.75)
// Prints "11.5"

let q = (x / 0.75).rounded(.toNearestOrEven)
// q == 12.0
let r = x.remainder(dividingBy: 0.75)
// r == -0.375

let x1 = 0.75 * q + r
// x1 == 8.625
```

If this value and `other` are finite numbers, the remainder is in the closed range `-abs(other / 2)...abs(other / 2)`. The `remainder(dividingBy:)` method is always exact. This method implements the remainder operation defined by the [`IEEE 754 specification`](https://developer.apple.comhttp://ieeexplore.ieee.org/servlet/opac?punumber=4610933).

## Parameters

- `other`: The value to use when dividing this value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/floatingpoint/remainder(dividingby:))*