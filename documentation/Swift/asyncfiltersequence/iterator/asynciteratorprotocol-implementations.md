# AsyncIteratorProtocol Implementations

**Framework**: Swift

## Topics

### Instance Methods
- [func next() async throws(Self.Failure) -> Self.Element?](asyncfiltersequence/iterator/next-32s0r.md)
  Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.
- [func next(isolation: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?](asyncfiltersequence/iterator/next(isolation:)-7czxv.md)
  Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncfiltersequence/iterator/asynciteratorprotocol-implementations)*