# sign

**Framework**: Swift  
**Kind**: property

The sign of the floating-point value.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var sign: FloatingPointSign { get }
```

#### Discussion

The `sign` property is `.minus` if the value’s signbit is set, and `.plus` otherwise. For example:

```swift
let x = -33.375
// x.sign == .minus
```

Don’t use this property to check whether a floating point value is negative. For a value `x`, the comparison `x.sign == .minus` is not necessarily the same as `x < 0`. In particular, `x.sign == .minus` if `x` is -0, and while `x < 0` is always `false` if `x` is NaN, `x.sign` could be either `.plus` or `.minus`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/sign)*