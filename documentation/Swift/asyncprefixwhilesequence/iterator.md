# AsyncPrefixWhileSequence.Iterator

**Framework**: Swift  
**Kind**: struct

The iterator that produces elements of the prefix-while sequence.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct Iterator
```

## Topics

### Instance Methods
- [func next() async rethrows -> Base.Element?](asyncprefixwhilesequence/iterator/next.md)
  Produces the next element in the prefix-while sequence.
- [func next(isolation: isolated (any Actor)?) async throws(AsyncPrefixWhileSequence<Base>.Failure) -> Base.Element?](asyncprefixwhilesequence/iterator/next(isolation:).md)
  Produces the next element in the prefix-while sequence.
### Type Aliases
- [AsyncPrefixWhileSequence.Iterator.Element](asyncprefixwhilesequence/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](asyncprefixwhilesequence/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](asynciteratorprotocol.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncprefixwhilesequence/iterator)*