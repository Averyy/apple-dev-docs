# AsyncIteratorProtocol Implementations

**Framework**: Group Activities

## Topics

### Instance Methods
- [func next() async throws(Self.Failure) -> Self.Element?](groupsessionmessenger/messages/iterator/next-8kuna.md)
  Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.
- [func next(isolation: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?](groupsessionmessenger/messages/iterator/next(isolation:).md)
  Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/groupsessionmessenger/messages/iterator/asynciteratorprotocol-implementations)*