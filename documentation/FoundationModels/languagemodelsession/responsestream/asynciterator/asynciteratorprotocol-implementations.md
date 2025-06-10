# AsyncIteratorProtocol Implementations

**Framework**: Foundation Models

## Topics

### Instance Methods
- [func next() async throws(Self.Failure) -> Self.Element?](languagemodelsession/responsestream/asynciterator/next.md)
  Default implementation of `next()` in terms of `next(isolation:)`, which is required to maintain backward compatibility with existing async iterators.
- [func next(isolation: isolated (any Actor)?) async throws(Self.Failure) -> Self.Element?](languagemodelsession/responsestream/asynciterator/next(isolation:)-9tsui.md)
  Default implementation of `next(isolation:)` in terms of `next()`, which is required to maintain backward compatibility with existing async iterators.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/responsestream/asynciterator/asynciteratorprotocol-implementations)*