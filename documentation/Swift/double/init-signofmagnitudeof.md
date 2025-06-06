# init(signOf:magnitudeOf:)

**Framework**: Swift  
**Kind**: init

Creates a new floating-point value using the sign of one value and the magnitude of another.

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
init(signOf sign: Double, magnitudeOf mag: Double)
```

#### Discussion

The following example uses this initializer to create a new `Double` instance with the sign of `a` and the magnitude of `b`:

```swift
let a = -21.5
let b = 305.15
let c = Double(signOf: a, magnitudeOf: b)
print(c)
// Prints "-305.15"
```

This initializer implements the IEEE 754 `copysign` operation.

## See Also

- [init<Source>(Source)](double/init(_:)-1488d.md)
  Creates a new instance from the given value, rounded to the closest possible representation.
- [init(Double)](double/init(_:)-o1k9.md)
  Creates a new instance initialized to the given value.
- [init(Float)](double/init(_:)-5h7qh.md)
  Creates a new instance that approximates the given value.
- [init(Float16)](double/init(_:)-aeox.md)
  Creates a new instance that approximates the given value.
- [init(Float80)](double/init(_:)-9z7ob.md)
  Creates a new instance that approximates the given value.
- [init(CGFloat)](double/init(_:)-7ag2w.md)
- [init(sign: FloatingPointSign, exponent: Int, significand: Double)](double/init(sign:exponent:significand:).md)
  Creates a new value from the given sign, exponent, and significand.
- [init<Source>(Source)](double/init(_:)-1oh9r.md)
  Creates a new value, rounded to the closest possible representation.
- [init(truncating: NSNumber)](double/init(truncating:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/init(signof:magnitudeof:))*