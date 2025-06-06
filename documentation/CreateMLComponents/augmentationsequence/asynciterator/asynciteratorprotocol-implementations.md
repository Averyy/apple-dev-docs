# AsyncIteratorProtocol Implementations

**Framework**: Create ML Components

## Topics

### Instance Methods
- [func next() async throws(Self.Failure) -> Self.Element?](augmentationsequence/asynciterator/next-7w7gn.md)
  Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.
- [func next(isolation: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?](augmentationsequence/asynciterator/next(isolation:).md)
  Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/augmentationsequence/asynciterator/asynciteratorprotocol-implementations)*