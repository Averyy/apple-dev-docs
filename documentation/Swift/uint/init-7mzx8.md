# init(_:)

**Framework**: Swift  
**Kind**: init

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

- `source`: A floating-point value to convert to an integer.    must be representable in this type after rounding toward   zero.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uint/init(_:)-7mzx8)*