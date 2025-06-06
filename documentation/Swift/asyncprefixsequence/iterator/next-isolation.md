# next(isolation:)

**Framework**: Swift  
**Kind**: method

Produces the next element in the prefix sequence.

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
mutating func next(isolation actor: isolated (any Actor)?) async throws(AsyncPrefixSequence<Base>.Failure) -> Base.Element?
```

#### Discussion

Until reaching the number of elements to include, this iterator calls `next(isolation:)` on its base iterator and passes through the result. After reaching the maximum number of elements, subsequent calls to `next(isolation:)` return `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncprefixsequence/iterator/next(isolation:))*