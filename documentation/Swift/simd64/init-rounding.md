# init(_:rounding:)

**Framework**: Swift  
**Kind**: init

Creates a new vector from the given vector, rounding the given vector’s of elements using the specified rounding rule.

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
init<Other>(_ other: SIMD64<Other>, rounding rule: FloatingPointRoundingRule = .towardZero) where Other : BinaryFloatingPoint, Other : SIMDScalar
```

## Parameters

- `other`: The vector to convert.
- `rule`: The round rule to use when converting elements of   The   default is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd64/init(_:rounding:))*