# AsyncIteratorProtocol Implementations

**Framework**: MusicKit

## Topics

### Instance Methods
- [func next() async throws(Self.Failure) -> Self.Element?](musicsubscription/updates/iterator/next-6rdhm.md)
  Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.
- [func next(isolation: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?](musicsubscription/updates/iterator/next(isolation:).md)
  Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/musicsubscription/updates/iterator/asynciteratorprotocol-implementations)*