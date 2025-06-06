# resetBytes(in:)

**Framework**: Foundation  
**Kind**: method

Replaces the contents of the buffer at the given range with zeroes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func resetBytes<R>(in range: R) where R : RangeExpression, Self.Index == R.Bound
```

#### Discussion

A default implementation is given in terms of `replaceSubrange(_:with:)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/resetbytes(in:)-5eicw)*