# next(isolation:)

**Framework**: Swift  
**Kind**: method

Produces the next element in the drop-first sequence.

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
mutating func next(isolation actor: isolated (any Actor)?) async throws(AsyncDropFirstSequence<Base>.Failure) -> Base.Element?
```

#### Discussion

Until reaching the number of elements to drop, this iterator calls `next(isolation:)` on its base iterator and discards the result. If the base iterator returns `nil`, indicating the end of the sequence, this iterator returns `nil`. After reaching the number of elements to drop, this iterator passes along the result of calling `next(isolation:)` on the base iterator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncdropfirstsequence/iterator/next(isolation:))*