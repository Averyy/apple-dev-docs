# next(isolation:)

**Framework**: Swift  
**Kind**: method

Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.

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
mutating func next(isolation actor: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingcompactmapsequence/iterator/next(isolation:)-5p1be)*