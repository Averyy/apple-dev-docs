# *(_:_:)

**Framework**: Swift  
**Kind**: op  
**Role**: Operator

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

> **Deprecated**: integer vector types do not support checked arithmetic; use the wrapping operator '&*' instead

## Declaration

```swift
static func * (a: Self, b: Self.Scalar) -> Self
```

Available when `Scalar` conforms to `FixedWidthInteger`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd3/*(_:_:)-50fba)*