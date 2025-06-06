# next()

**Framework**: Swift  
**Kind**: method

Produces the next element in the compact map sequence.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
mutating func next() async throws -> ElementOfResult?
```

#### Discussion

This iterator calls `next()` on its base iterator; if this call returns `nil`, `next()` returns `nil`. Otherwise, `next()` calls the transforming closure on the received element, returning it if the transform returns a non-`nil` value. If the transform returns `nil`, this method continues to wait for further elements until it gets one that transforms to a non-`nil` value. If calling the closure throws an error, the sequence ends and `next()` rethrows the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingcompactmapsequence/iterator/next())*