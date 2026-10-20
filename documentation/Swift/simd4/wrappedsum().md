# wrappedSum()

**Framework**: Swift  
**Kind**: method

Returns the sum of the scalars in the vector, computed with wrapping addition.

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
func wrappedSum() -> Self.Scalar
```

#### Discussion

Equivalent to `indices.reduce(into: 0) { $0 &+= self[$1] }`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd4/wrappedsum())*