# next(isolation:)

**Framework**: Swift  
**Kind**: method

Produces the next element in the map sequence.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func next(isolation actor: isolated (any Actor)?) async throws -> Transformed?
```

#### Discussion

This iterator calls `next(isolation:)` on its base iterator; if this call returns `nil`, `next(isolation:)` returns nil. Otherwise, `next(isolation:)` returns the result of calling the transforming closure on the received element. If calling the closure throws an error, the sequence ends and `next(isolation:)` rethrows the error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingmapsequence/iterator/next(isolation:))*