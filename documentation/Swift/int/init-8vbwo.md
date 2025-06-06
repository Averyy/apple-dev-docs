# init(_:)

**Framework**: Swift  
**Kind**: init

Creates an integer from the given floating-point value, rounding toward zero.

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
init(_ source: Double)
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

- `source`: A floating-point value to convert to an integer.    must be representable in this type after rounding toward   zero.

## See Also

- [init<T>(T)](int/init(_:)-6gt9z.md)
- [init(Float)](int/init(_:)-2oscb.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Float16)](int/init(_:)-3huv0.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(Float80)](int/init(_:)-66i0w.md)
  Creates an integer from the given floating-point value, rounding toward zero.
- [init(CGFloat)](int/init(_:)-5q6q5.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int/init(_:)-8vbwo)*