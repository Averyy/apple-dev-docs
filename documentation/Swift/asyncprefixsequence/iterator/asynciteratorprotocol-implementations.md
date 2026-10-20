# AsyncIteratorProtocol Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Methods
- [func next() async throws(Self.Failure) -> Self.Element?](./next%28%29-4oocd.md)
  Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.
- [func next(isolation: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?](./next%28isolation%29-96z8m.md)
  Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncprefixsequence/iterator/asynciteratorprotocol-implementations)*