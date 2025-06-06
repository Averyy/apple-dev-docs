# AsyncIteratorProtocol Implementations

**Framework**: Swift

## Topics

### Instance Methods
- [func next() async throws(Self.Failure) -> Self.Element?](asyncdropwhilesequence/iterator/next-6nmld.md)
  Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.
- [func next(isolation: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?](asyncdropwhilesequence/iterator/next(isolation:)-6b5gu.md)
  Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncdropwhilesequence/iterator/asynciteratorprotocol-implementations)*