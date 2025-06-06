# AsyncThrowingStream.Iterator

**Framework**: Swift  
**Kind**: struct

The asynchronous iterator for iterating an asynchronous stream.

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

#### Overview

This type is not `Sendable`. Don’t use it from multiple concurrent contexts. It is a programmer error to invoke `next()` from a concurrent context that contends with another such call, which results in a call to `fatalError()`.

## Topics

### Iterating over Elements
- [func next() async throws -> Element?](asyncthrowingstream/iterator/next.md)
  The next value from the asynchronous stream.
### Instance Methods
- [func next(isolation: isolated (any Actor)?) async throws(Failure) -> Element?](asyncthrowingstream/iterator/next(isolation:).md)
  The next value from the asynchronous stream.
### Default Implementations
- [AsyncIteratorProtocol Implementations](asyncthrowingstream/iterator/asynciteratorprotocol-implementations.md)

## Relationships

### Conforms To
- [AsyncIteratorProtocol](asynciteratorprotocol.md)

## See Also

- [func makeAsyncIterator() -> AsyncThrowingStream<Element, Failure>.Iterator](asyncthrowingstream/makeasynciterator.md)
  Creates the asynchronous iterator that produces elements of this asynchronous sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingstream/iterator)*