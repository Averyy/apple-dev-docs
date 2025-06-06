# AsyncThrowingDropWhileSequence.Iterator

**Framework**: Swift  
**Kind**: struct

The iterator that produces elements of the drop-while sequence.

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
- [func next() async throws -> Base.Element?](asyncthrowingdropwhilesequence/iterator/next.md)
  Produces the next element in the drop-while sequence.
- [func next(isolation: isolated (any Actor)?) async throws -> Base.Element?](asyncthrowingdropwhilesequence/iterator/next(isolation:).md)
  Produces the next element in the drop-while sequence.
### Type Aliases
- [AsyncThrowingDropWhileSequence.Iterator.Element](asyncthrowingdropwhilesequence/iterator/element.md)
### Default Implementations
- [AsyncIteratorProtocol Implementations](asyncthrowingdropwhilesequence/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](asynciteratorprotocol.md)
- [Sendable](sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingdropwhilesequence/iterator)*