# AsyncIteratorProtocol Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func next() async throws(Self.Failure) -> Self.Element?](humanbodyactioncounter/cumulativesumsequence/iterator/next-9v11f.md)
  Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.
- [func next(isolation: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?](humanbodyactioncounter/cumulativesumsequence/iterator/next(isolation:).md)
  Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/humanbodyactioncounter/cumulativesumsequence/iterator/asynciteratorprotocol-implementations)*