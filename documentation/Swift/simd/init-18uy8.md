# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a vector from the given sequence.

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
init<S>(_ scalars: S) where S : Sequence, Self.Scalar == S.Element
```

#### Discussion

> **Note**: `scalars` must have the same number of elements as the vector type.

`scalars` must have the same number of elements as the vector type.

## Parameters

- `scalars`: The elements to use in the vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/simd/init(_:)-18uy8)*