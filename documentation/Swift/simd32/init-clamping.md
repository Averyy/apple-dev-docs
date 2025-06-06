# init(clamping:)

**Framework**: Swift  
**Kind**: init

Creates a new vector from the given vector, clamping the values of the given vector’s elements if necessary.

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
init<Other>(clamping other: SIMD32<Other>) where Other : FixedWidthInteger, Other : SIMDScalar
```

## Parameters

- `other`: The vector to convert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd32/init(clamping:))*