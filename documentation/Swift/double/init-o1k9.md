# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a new instance initialized to the given value.

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
init(_ other: Double)
```

#### Discussion

The value of `other` is represented exactly by the new instance. A NaN passed as `other` results in another NaN, with a signaling NaN value converted to quiet NaN.

```swift
let x: Double = 21.25
let y = Double(x)
// y == 21.25

let z = Double(Double.nan)
// z.isNaN == true
```

## Parameters

- `other`: The value to use for the new instance.

## See Also

- [init<Source>(Source)](double/init(_:)-1488d.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init(Float)](double/init(_:)-5h7qh.md)
  Creates a new instance that approximates the given value.
- [init(Float16)](double/init(_:)-aeox.md)
  Creates a new instance that approximates the given value.
- [init(Float80)](double/init(_:)-9z7ob.md)
  Creates a new instance that approximates the given value.
- [init(CGFloat)](double/init(_:)-7ag2w.md)
- [init(sign: FloatingPointSign, exponent: Int, significand: Double)](double/init(sign:exponent:significand:).md)
  Creates a new value from the given sign, exponent, and significand.
- [init(signOf: Double, magnitudeOf: Double)](double/init(signof:magnitudeof:).md)
  Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init<Source>(Source)](double/init(_:)-1oh9r.md)
  Creates a new value, rounded to the closest possible representation.
- [init(truncating: NSNumber)](double/init(truncating:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/init(_:)-o1k9)*