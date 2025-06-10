# binade

**Framework**: Swift  
**Kind**: property

The floating-point value with the same sign and exponent as this value, but with a significand of 1.0.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var binade: Float80 { get }
```

#### Discussion

A  is a set of binary floating-point values that all have the same sign and exponent. The `binade` property is a member of the same binade as this value, but with a unit significand.

In this example, `x` has a value of `21.5`, which is stored as `1.34375 * 2**4`, where `**` is exponentiation. Therefore, `x.binade` is equal to `1.0 * 2**4`, or `16.0`.

```swift
let x = 21.5
// x.significand == 1.34375
// x.exponent == 4

let y = x.binade
// y == 16.0
// y.significand == 1.0
// y.exponent == 4
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/binade)*