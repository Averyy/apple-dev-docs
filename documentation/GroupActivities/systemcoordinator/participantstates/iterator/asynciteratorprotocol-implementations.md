# AsyncIteratorProtocol Implementations

**Framework**: Group Activities

## Topics

### Instance Methods
- [func next() async throws(Self.Failure) -> Self.Element?](systemcoordinator/participantstates/iterator/next-dyvb.md)
  Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.
- [func next(isolation: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?](systemcoordinator/participantstates/iterator/next(isolation:).md)
  Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/systemcoordinator/participantstates/iterator/asynciteratorprotocol-implementations)*