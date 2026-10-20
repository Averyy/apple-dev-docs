# random(using:)

**Framework**: Swift  
**Kind**: method  
**Role**: Type Method

Returns a vector mask with `true` or `false` randomly assigned in each lane, using the given generator as a source for randomness.

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
static func random<T>(using generator: inout T) -> SIMDMask<Storage> where T : RandomNumberGenerator
```

Available when `Storage` conforms to `SIMD`, `Storage.Scalar` conforms to `FixedWidthInteger`, and `Storage.Scalar` conforms to `SignedInteger`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simdmask/random(using:))*