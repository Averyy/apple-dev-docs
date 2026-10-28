# init(_:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates a new instance that approximates the given value.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init(_ other: Float80)
```

## Discussion

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

### Converting Floating-Point Values
- [init<Source>(Source)](./init%28_%29-1488f.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init<Source>(Source)](./init%28_%29-1oh9p.md)
  Creates a new value, rounded to the closest possible representation.
- [init(Double)](./init%28_%29-1kp2p.md)
  Creates a new instance that approximates the given value.
- [init(Float)](./init%28_%29-975tv.md)
  Creates a new instance initialized to the given value.
- [init(CGFloat)](./init%28_%29-5soww.md)
- [init(Float16)](./init%28_%29-ussz.md)
  Creates a new instance that approximates the given value.
- [init(signOf: Float, magnitudeOf: Float)](./init%28signof,magnitudeof%29.md)
  Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init(sign: FloatingPointSign, exponent: Int, significand: Float)](./init%28sign,exponent,significand%29.md)
  Creates a new value from the given sign, exponent, and significand.
- [init(truncating: NSNumber)](./init%28truncating%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/float/init(_:)-11orc)*