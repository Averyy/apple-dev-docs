# AsyncIteratorProtocol Implementations

**Framework**: AlarmKit

## Topics

### Instance Methods
- [func next() async throws(Self.Failure) -> Self.Element?](alarmmanager/alarmupdates-swift.struct/iterator/next-4cmw1.md)
  Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.
- [func next(isolation: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?](alarmmanager/alarmupdates-swift.struct/iterator/next(isolation:).md)
  Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/alarmkit/alarmmanager/alarmupdates-swift.struct/iterator/asynciteratorprotocol-implementations)*