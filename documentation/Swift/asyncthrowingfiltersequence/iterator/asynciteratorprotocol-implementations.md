# AsyncIteratorProtocol Implementations

**Framework**: Swift

## Topics

### Instance Methods
- [func next() async throws(Self.Failure) -> Self.Element?](asyncthrowingfiltersequence/iterator/next-5cr1d.md)
  Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.
- [func next(isolation: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?](asyncthrowingfiltersequence/iterator/next(isolation:)-4w94d.md)
  Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingfiltersequence/iterator/asynciteratorprotocol-implementations)*