# init(_:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer  
**Required**: Yes

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
init<T>(_ source: T) where T : BinaryFloatingPoint
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

## Default Implementations

### BinaryInteger Implementations
- [init?(String)](./init%28_%29-3cx61.md)
  Creates a new integer value from the given string.
- [init<T>(T)](./init%28_%29-5yrn0.md)
  Creates a new instance from the given integer.
- [init<T>(T)](./init%28_%29-62cdc.md)
- [init<T>(T)](./init%28_%29-6u4mr.md)
  Creates a new instance from the given integer.
### FixedWidthInteger Implementations
- [init?(Backtrace.Address)](../fixedwidthinteger/init%28_%29.md)
  Convert from an Backtrace.Address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/binaryinteger/init(_:)-2ln0u)*