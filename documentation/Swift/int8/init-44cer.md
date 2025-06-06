# init(_:)

**Framework**: Swift  
**Kind**: init

Creates an integer from the given floating-point value, rounding toward zero.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
init(_ source: Float16)
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/int8/init(_:)-44cer)*