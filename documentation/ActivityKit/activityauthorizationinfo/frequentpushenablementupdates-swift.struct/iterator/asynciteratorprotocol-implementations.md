# AsyncIteratorProtocol Implementations

**Framework**: ActivityKit

## Topics

### Instance Methods
- [func next() async throws(Self.Failure) -> Self.Element?](activityauthorizationinfo/frequentpushenablementupdates-swift.struct/iterator/next-3kelq.md)
  Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.
- [func next(isolation: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?](activityauthorizationinfo/frequentpushenablementupdates-swift.struct/iterator/next(isolation:).md)
  Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activityauthorizationinfo/frequentpushenablementupdates-swift.struct/iterator/asynciteratorprotocol-implementations)*