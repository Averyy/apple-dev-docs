# init(_:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates an integer from the given floating-point value, rounding toward zero.

**Availability**:
- macOS 10.10+

## Declaration

```swift
init(_ source: Float80)
```

#### Discussion

Any fractional part of the value passed as `source` is removed, rounding the value toward zero.

```swift
let x = Int(21.5)
// x == 21
let y = Int(-21.5)
// y == -21
```

If `source` is outside the bounds of this type after rounding toward zero, a runtime error may occur.

```swift
let z = UInt(-21.5)
// Error: ...the result would be less than UInt.min
```

## Parameters

- `source`: A floating-point value to convert to an integer. `source` must be representable in this type after rounding toward zero.

## See Also

### Converting Floating-Point Values
- [init<T>(T)](./init%28_%29-6gt9z.md)
- [init(Double)](./init%28_%29-8vbwo.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Float)](./init%28_%29-2oscb.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Float16)](./init%28_%29-3huv0.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(CGFloat)](./init%28_%29-5q6q5.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/init(_:)-66i0w)*