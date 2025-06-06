# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new instance that approximates the given value.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init(_ other: Float80)
```

#### Discussion

The value of `other` is rounded to a representable value, if necessary. A NaN passed as `other` results in another NaN, with a signaling NaN value converted to quiet NaN.

```swift
let x: Float80 = 21.25
let y = Float(x)
// y == 21.25

let z = Float(Float80.nan)
// z.isNaN == true
```

## Parameters

- `other`: The value to use for the new instance.

## See Also

- [init<Source>(Source)](float/init(_:)-1488f.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init<Source>(Source)](float/init(_:)-1oh9p.md)
  Creates a new value, rounded to the closest possible representation.
- [init(Double)](float/init(_:)-1kp2p.md)
  Creates a new instance that approximates the given value.
- [init(Float)](float/init(_:)-975tv.md)
  Creates a new instance initialized to the given value.
- [init(CGFloat)](float/init(_:)-5soww.md)
- [init(Float16)](float/init(_:)-ussz.md)
  Creates a new instance that approximates the given value.
- [init(signOf: Float, magnitudeOf: Float)](float/init(signof:magnitudeof:).md)
  Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init(sign: FloatingPointSign, exponent: Int, significand: Float)](float/init(sign:exponent:significand:).md)
  Creates a new value from the given sign, exponent, and significand.
- [init(truncating: NSNumber)](float/init(truncating:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/init(_:)-11orc)*