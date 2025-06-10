# isZero

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether the instance is equal to zero.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var isZero: Bool { get }
```

#### Discussion

The `isZero` property of a value `x` is `true` when `x` represents either `-0.0` or `+0.0`. `x.isZero` is equivalent to the following comparison: `x == 0.0`.

```swift
let x = -0.0
x.isZero        // true
x == 0.0        // true
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/iszero)*