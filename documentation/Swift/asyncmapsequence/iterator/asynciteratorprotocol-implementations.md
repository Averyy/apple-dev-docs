# AsyncIteratorProtocol Implementations

**Framework**: Swift

## Topics

### Instance Methods
- [func next() async throws(Self.Failure) -> Self.Element?](asyncmapsequence/iterator/next-38mq7.md)
  Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.
- [func next(isolation: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?](asyncmapsequence/iterator/next(isolation:)-5gvj0.md)
  Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncmapsequence/iterator/asynciteratorprotocol-implementations)*