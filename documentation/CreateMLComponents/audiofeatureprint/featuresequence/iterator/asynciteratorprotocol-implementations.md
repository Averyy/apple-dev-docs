# AsyncIteratorProtocol Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func next() async throws(Self.Failure) -> Self.Element?](audiofeatureprint/featuresequence/iterator/next-s06a.md)
  Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.
- [func next(isolation: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?](audiofeatureprint/featuresequence/iterator/next(isolation:).md)
  Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/audiofeatureprint/featuresequence/iterator/asynciteratorprotocol-implementations)*