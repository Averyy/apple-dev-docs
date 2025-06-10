# ulp

**Framework**: Swift  
**Kind**: property

The unit in the last place of this value.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var ulp: Float80 { get }
```

#### Discussion

This is the unit of the least significant digit in this value’s significand. For most numbers `x`, this is the difference between `x` and the next greater (in magnitude) representable number. There are some edge cases to be aware of:

- If `x` is not a finite number, then `x.ulp` is NaN.
- If `x` is very small in magnitude, then `x.ulp` may be a subnormal number. If a type does not support subnormals, `x.ulp` may be rounded to zero.
- `greatestFiniteMagnitude.ulp` is a finite number, even though the next greater representable value is `infinity`.

See also the `ulpOfOne` static property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float80/ulp)*