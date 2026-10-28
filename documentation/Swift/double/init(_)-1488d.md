# init(_:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates a new instance from the given value, rounded to the closest possible representation.

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
init<Source>(_ value: Source) where Source : BinaryFloatingPoint
```

## Discussion

If two representable values are equally close, the result is the value with more trailing zeros in its significand bit pattern.

## Parameters

- `value`: A floating-point value to be converted.

## See Also

### Converting Floating-Point Values
- [init(Double)](./init%28_%29-o1k9.md)
  Creates a new instance initialized to the given value.
- [init(Float)](./init%28_%29-5h7qh.md)
  Creates a new instance that approximates the given value.
- [init(Float16)](./init%28_%29-aeox.md)
  Creates a new instance that approximates the given value.
- [init(Float80)](./init%28_%29-9z7ob.md)
  Creates a new instance that approximates the given value.
- [init(CGFloat)](./init%28_%29-7ag2w.md)
- [init(sign: FloatingPointSign, exponent: Int, significand: Double)](./init%28sign,exponent,significand%29.md)
  Creates a new value from the given sign, exponent, and significand.
- [init(signOf: Double, magnitudeOf: Double)](./init%28signof,magnitudeof%29.md)
  Creates a new floating-point value using the sign of one value and the magnitude of another.
- [init<Source>(Source)](./init%28_%29-1oh9r.md)
  Creates a new value, rounded to the closest possible representation.
- [init(truncating: NSNumber)](./init%28truncating%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/double/init(_:)-1488d)*