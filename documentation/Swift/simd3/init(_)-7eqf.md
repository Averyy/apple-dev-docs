# init(_:)

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

Creates a new vector from the given vector of floating-point values.

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
init<Other>(_ other: SIMD3<Other>) where Other : BinaryFloatingPoint, Other : SIMDScalar
```

Available when `Scalar` conforms to `BinaryFloatingPoint` and `SIMDScalar`.

## Parameters

- `other`: The vector to convert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd3/init(_:)-7eqf)*