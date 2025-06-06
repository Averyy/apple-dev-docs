# AsyncIteratorProtocol Implementations

**Framework**: Swift

## Topics

### Instance Methods
- [func next() async throws(Self.Failure) -> Self.Element?](asyncdropfirstsequence/iterator/next-9cp7j.md)
  Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.
- [func next(isolation: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?](asyncdropfirstsequence/iterator/next(isolation:)-46dp7.md)
  Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncdropfirstsequence/iterator/asynciteratorprotocol-implementations)*